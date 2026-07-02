# Zero Day Pulse

> **Generated:** 2026-07-02 19:08 UTC &nbsp;|&nbsp; **Total:** 34 &nbsp;|&nbsp; 🔴 KEV: 0 &nbsp;|&nbsp; 🟠 Zero-Day: 13 &nbsp;|&nbsp; 🟡 High: 21 &nbsp;|&nbsp; ✨ Enriched: 10

---

## 1. 🟠 Zero-Day — Ransomware Actors Exploit Unpatched SimpleHelp Remote Monitoring and Management to Compromise Utility Billing Software Provider

**CVE:** `CVE-2024-57727` &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Thu, 12 Ju
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-163a>

> Summary The Cybersecurity and Infrastructure Security Agency (CISA) is releasing this advisory in response to ransomware actors leveraging unpatched instances of a vulnerability in SimpleHelp Remote Monitoring and Management (RMM) to compromise customers of a utility billing software provider. This incident reflects a broader pattern of ransomware actors targeting organizations through unpatched v…

**Parallel AI Enrichment:**

- **Technical Details:** Multiple path traversal (directory traversal) vulnerabilities in SimpleHelp (v5.5.7 and earlier) that allow unauthenticated attackers to read sensitive files via path traversal.
- **Affected Products:** SimpleHelp remote support / Remote Monitoring and Management (RMM) software — version 5.5.7 and earlier
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Weaponized exploit observed in the wild: CISA reports ransomware actors leveraged CVE-2024-57727 against unpatched SimpleHelp RMM. No public proof-of-concept (PoC) URL is present in the provided corpus.
- **Patch Available:** Yes — vendor reports the vulnerabilities in SimpleHelp 5.5.7 and earlier were patched (see vendor advisory above).
- **Active Exploitation:** Yes — CISA reports confirmed exploitation in the wild by ransomware actors (including an incident that compromised a utility billing software provider) using unpatched SimpleHelp instances.
- **Threat Actors:** Ransomware actors (unnamed) — CISA attributes exploitation to ransomware actors but does not name a specific group in the cited advisory.
- **Mitigation:** Apply the vendor-supplied updates per the SimpleHelp advisory (upgrade patched versions). If immediate patching is not possible, limit network exposure of SimpleHelp instances (remove public/Internet access, restrict access to management interfaces) and follow the vendor guidance in the SimpleHelp KB until patched.
- **Vendor Advisory:** https://simple-help.com/blogs/security-vulnerabilities-in-simplehelp-5-5-7-and-earlier-what-you-need-to-know

---

## 2. 🟠 Zero-Day — CISA: Microsoft SharePoint RCE flaw now actively exploited

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Bleeping Computer &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://www.bleepingcomputer.com/news/security/cisa-microsoft-sharepoint-rce-flaw-now-actively-exploited/>

> CISA warned on Wednesday that attackers have begun exploiting a high-severity Microsoft SharePoint remote code execution vulnerability patched in May. [...]

**Parallel AI Enrichment:**

- **Technical Details:** CVE-2023-29357 is an elevation-of-privilege vulnerability in Microsoft SharePoint Server that can be chained with CVE-2023-24955 (a pre-auth code-injection / RCE) to achieve unauthenticated remote code execution on vulnerable SharePoint Server instances.
- **Affected Products:** Microsoft SharePoint Server (see MSRC advisory for exact affected builds/versions)
- **CVSS Score:** 9.8
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Yes — public proof-of-concept code has been published (public repositories/community writeups).
- **Patch Available:** Yes — Microsoft has released security updates for the affected SharePoint vulnerabilities (see Microsoft Security Update Guide / MSRC advisory above).
- **Active Exploitation:** Confirmed — multiple vendors/alerts report active exploitation in the wild and CISA urged patching.
- **Threat Actors:** None known
- **Mitigation:** Apply Microsoft’s security updates (MSRC/KBs) immediately; until patched, restrict or block external exposure of SharePoint management endpoints, apply network-level controls or WAF rules, and follow Microsoft/CISA remediation guidance.
- **Vendor Advisory:** https://msrc.microsoft.com/update-guide/vulnerability/CVE-2023-29357

---

## 3. 🟠 Zero-Day — Rancher Fleet vulnerable to cross namespace secret disclosure via unvalidated `valuesFrom` references in Helm Deployer

**CVE:** `CVE-2026-44935` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-xr65-5cpm-g36x>

> ### Impact
A vulnerability in Fleet for Rancher Manager affects multi-tenancy environments where different tenants share the same downstream clusters (e.g., different privileged or untrusted teams inside the same organization). 

On unpatched versions, tenants could bypass restrictions to access any config map or secret across all namespaces on the downstream cluster. They can create cluster-wide …

**Parallel AI Enrichment:**

- **Technical Details:** An Incorrect Authorization vulnerability (CWE-863) in Rancher Fleet's Helm Deployer affects multi-tenant environments where different tenants share the same downstream Kubernetes cluster. Fleet failed to validate the namespace/identity of references made via the `valuesFrom` field in `fleet.yaml` (through a `GitRepo` resource) or via a `HelmOp` resource. Consequently, the fleet-agent used its cluster-admin credentials to read the targeted Secret or ConfigMap across all namespaces regardless of the tenant's actual authorization, allowing cross-namespace secret/configmap disclosure. Additionally, `HelmOp` and `Bundle` resources could be deployed without being restricted to a designated service account, enabling creation of cluster-wide resources without authorization. Attack vector: Network; Complexity: Low; Privileges required: Low; User interaction: None; Scope: Changed; Impact: High on confidentiality, integrity, and availability.
- **Affected Products:** rancher/fleet (Go module) >= 0.15.0, < 0.15.2; >= 0.14.0, < 0.14.6; >= 0.13.0, < 0.13.11; >= 0.12.0, < 0.12.15
- **CVSS Score:** 9.9
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Exploit Available:** No public proof-of-concept or weaponized exploit was identified in publicly available sources. The rancher/fleet security page references a 'valid proof of concept' (https://github.com/rancher/fleet/security) that may be held privately with the reporter (NATO/NCSC) and SUSE Rancher security team, but no public PoC URL is available.
- **Patch Available:** Yes. Official vendor patches have been released by SUSE/Rancher in Fleet versions v0.15.2, v0.14.6, v0.13.11, and v0.12.15. Advisory/patch URL: https://github.com/advisories/GHSA-xr65-5cpm-g36x
- **Active Exploitation:** No confirmed active exploitation in the wild has been publicly reported for CVE-2026-44935. The vulnerability was published to the GitHub Advisory Database on July 1, 2026, and is not listed in the CISA Known Exploited Vulnerabilities (KEV) catalog. No EPSS score was available on the GitHub advisory at the time of research.
- **Threat Actors:** None known
- **Mitigation:** 1. Upgrade Fleet to a patched release: v0.15.2, v0.14.6, v0.13.11, or v0.12.15. The patch introduces a new Policy resource that allows configuring `GitRepos`, `HelmOps`, and `Bundles` to require a specific service account on downstream clusters and to restrict `HelmOp` repository/chart URLs via a regular expression. 2. Workaround if you cannot upgrade immediately: ensure that tenants do not have shared access to the same downstream clusters. 3. Review cluster and Fleet deployment logs for indicators of unauthorized cross-tenant namespace access, and rotate any service accounts and credentials that may have been exposed. 4. Before applying a new Policy, ensure the required service account exists on downstream clusters with least-privilege permissions.
- **Vendor Advisory:** https://github.com/advisories/GHSA-xr65-5cpm-g36x

---

## 4. 🟠 Zero-Day — Unpatched Argo CD Repo-Server Flaw Could Let Attackers Take Over Kubernetes Clusters

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://thehackernews.com/2026/07/unpatched-argo-cd-repo-server-flaw.html>

> Argo CD, a widely used tool for deploying software to Kubernetes, has an unpatched flaw in its repo-server component that lets an unauthenticated attacker run code, provided they can reach the component&#x27;s internal network port.

Synacktiv, which found the bug, says it can lead to a full cluster takeover. There is no fix and no CVE. The firm says it reported the flaw to Argo CD&#x27;s maintain…

**Parallel AI Enrichment:**

- **Technical Details:** The Argo CD repo-server component exposes an internal gRPC service (port 8081) that lacks authentication. An attacker who can reach this port can make an unauthenticated call to the /repository.RepoServerService/GenerateManifest endpoint. By crafting a ManifestRequest with a malicious KustomizeOptions struct, the attacker injects arguments into the kustomize build command. Using --enable-helm and --helm-command, the attacker can point helm-command at an executable in an attacker-controlled Git repository. When kustomize runs, it executes the attacker's script as the repo-server process, yielding unauthenticated RCE. With default Argo CD Helm chart installations (networkPolicy.create=false), any compromised pod in the cluster can reach the repo-server, enabling lateral movement to theft of REDIS_PASSWORD and Redis cache poisoning, ultimately leading to full Kubernetes cluster takeover. Synacktiv reported the flaw to Argo CD maintainers in January 2025.
- **Affected Products:** Argo CD repo-server component (demonstrated against Argo CD v2.13.3; complete list of affected versions not yet published). The unauthenticated internal gRPC service on port 8081 is the attack surface.
- **CVSS Score:** 7.5
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** A proof-of-concept tool named 'argo-cdown' was developed by Synacktiv but its release was temporarily delayed at the time of public disclosure (2026-07-01). The Synacktiv write-up includes a sample Go ManifestRequest payload demonstrating the attack. No public PoC repository URL is currently available. Source: https://www.synacktiv.com/en/publications/caught-in-the-octopus-trap-unauthenticated-rce-in-argo-cd-with-codeql
- **Patch Available:** No official vendor patch has been released for this specific vulnerability at the time of disclosure. Synacktiv publicly disclosed the bug on 2026-07-01 after reporting it to Argo CD maintainers in January 2025; the Argo CD project had not issued a CVE or fix as of that date. Argo CD 3.5 (release candidate) introduces internal mTLS but is not a targeted patch for this issue. Patch URL unavailable.
- **Active Exploitation:** No confirmed active exploitation in the wild has been reported. The vulnerability was demonstrated by Synacktiv researchers in a controlled setting; as of the 2026-07-01 public disclosure, no in-the-wild exploitation or associated threat actor activity has been documented by Synacktiv, The Hacker News, or Mallory threat intelligence.
- **Threat Actors:** None known.
- **Mitigation:** Because no patch is currently available, apply strict Kubernetes NetworkPolicies to restrict network access to the repo-server (gRPC port 8081) and Redis so that only Argo CD's own components (argocd-server, argocd-application-controller) can reach them. Note: the Argo CD Helm chart ships with networkPolicy.create=false by default, which leaves these internal ports exposed cluster-wide — operators must explicitly enable NetworkPolicies. Verify with: kubectl get networkpolicy -A. Defense-in-depth measures include avoiding deployment of untrusted workloads in the same cluster as Argo CD and monitoring for unexpected GenerateManifest calls to the repo-server. Argo CD 3.5 (release candidate, June 2026) adds mutual TLS (mTLS) enforcement between internal components, which would also mitigate this class of attack once adopted.
- **Vendor Advisory:** Vendor advisory URL unavailable.

---

## 5. 🟠 Zero-Day — AI threats in the wild: The current state of prompt injections on the web

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-23
**Reference:** <http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html>

> Posted by Thomas Brunner, Yu-Han Liu, Moni Pande At Google, our Threat Intelligence teams are dedicated to staying ahead of real-world adversarial activity, proactively monitoring emerging threats before they can impact users. Right now, Indirect Prompt Injection (IPI) is a top priority for the security community, anticipating it as a primary attack vector for adversaries to target and compromise …

**Parallel AI Enrichment:**

- **Technical Details:** Indirect Prompt Injection (IPI) occurs when an AI/LLM system processes external, attacker-controlled content (websites, emails, documents, image/PDF metadata) and silently follows the attacker's embedded instructions instead of the user's original intent. Attack vector techniques observed in the wild: shrinking text to a single pixel, setting font color to near-transparent white, exploiting accessibility/CSS classes ('visually-hidden', 'aria-hidden'), HTML comment and <meta> tag namespace injection, 'persuasion amplifier' keywords (e.g., 'ultrathink'), Unicode tag characters and zero-width joiners, image alt-text abuse, malicious font files remapping glyphs (font-mapping attacks), and targeting AI agent frameworks (Semantic Kernel, CrewAI, Claude Code) where IPI chains into remote code execution. Documented effects from real-world payloads: hijacking AI assistant role/persona to exfiltrate API keys, redirecting traffic for SEO manipulation, suppressing AI behavior via known model magic strings, attempting destructive shell commands ('sudo rm -rf') on the user's machine via agent tool calls, soliciting unauthorized financial transfers (PayPal/Stripe scams), causing denial-of-service by streaming infinite text to trigger model timeouts, and exfiltrating user or corporate data via tool-using agents. Google's telemetry found a 32% relative increase in the malicious share of detected IPI between November 2025 and February 2026.
- **Affected Products:** Google Gemini (family of models and AI assistant), the Gemini app, Gemini in Google Workspace apps (Gmail, Docs, Drive, etc.), Gemini-powered AI agents, AI Overviews / AI-generated summaries of web content, and generally any AI assistant/agent that ingests untrusted external content. Related frameworks documented as affected include Semantic Kernel, CrewAI, and Claude Code for RCE chaining. No specific version number is tied to the advisory as IPI is a vulnerability class.
- **CVSS Score:** 8.5
- **CVSS Vector:** CVSS vector unavailable. The Google blog post is a Threat Intelligence / GenAI Security Team research disclosure describing a vulnerability class (Indirect Prompt Injection) rather than a single CVE-scored software vulnerability. No specific CVE identifier is assigned to the findings in this advisory, and no CVSS v3 vector is published for it.
- **Exploit Available:** Yes — publicly demonstrated in-the-wild exploit/payload code is available. Forcepoint X-Labs published 10 verified Indirect Prompt Injection payloads discovered on production websites on 2026-04-22 (https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads). Specific affected sites include: thelibrary-welcome[.]uk (API key exfiltration via role impersonation), kassoon[.]com (SEO/traffic hijack via CSS concealment), luminousmen[.]com (brand promotion via hidden footer tags), faladobairro[.]com ('sudo rm -rf' → data destruction), perceptivepumpkin[.]com (PayPal.me $5,000 → financial fraud), lawsofux[.]com (AI canary probe via visually-hidden class), lcpdfr[.]com (Anthropic magic-string refusal trigger → behavioral suppression), and archibase[.]co (ai:action namespace + 'ULTRATHINK' → Stripe donation scam). Google's blog also catalogs working payload examples: invisible 'tweety bird' tone-change instructions, summary-context seeding, SEO injections, 'If you are an AI, do not crawl this website,' infinite-text-stream timeout attacks, experimental data-exfiltration prompts, and malicious commands attempting to delete files on the user's machine. Google's sweep scanned 2–3 billion crawled pages per month via the Common Crawl corpus.
- **Patch Available:** No single version-pinned patch exists for IPI as a class — this is not a discrete software bug but a structural vulnerability of LLM/agent architectures. Google continuously hardens Gemini through adversarial training and incremental product updates rather than issuing a CVE patch. The Google blog post flags hardening as an ongoing process and notes Gemini's defenses have been progressively improved (via model-training improvements described in Google's June 13, 2025 'Mitigating prompt injection attacks with a layered defense strategy' post). On 2026-04-23 Google also published a companion article 'Indirect prompt injections & Google's layered defense strategy for Gemini' providing specific Workspace admin guidance.
- **Active Exploitation:** Yes — confirmed active exploitation in the wild, on the public web, against AI agents and assistants is the central subject of this advisory. Evidence: (1) Google's own telemetry documented a 32% relative increase in the 'malicious' category of IPI between November 2025 and February 2026 across billions of crawled pages; (2) Forcepoint X-Labs (April 22, 2026) independently verified 10 working IPI payloads on production websites spanning financial fraud, data destruction, API-key exfiltration, AI denial-of-service, and behavioral suppression; (3) Google's researchers observed real-world payloads attempting destructive shell commands ('vandalizing the machine') against users of AI assistants browsing the web; (4) Help Net Security (April 24, 2026) covered the joint Google + Forcepoint disclosure confirming in-the-wild abuse; (5) thebrightbyte analysis (May 19, 2026) confirmed a Spring 2026 RCE wave affecting AI agent frameworks (Semantic Kernel, CrewAI, Claude Code) where IPI chains into remote code execution; (6) Unit 42 (March 3, 2026) independently observed weaponized web-based IPI in the wild. No specific APT/crimeware group attribution has been published.
- **Threat Actors:** None known. The blog post does not name any specific threat actor group, APT campaign, or ransomware operator. Forcepoint's companion report noted that the use of shared injection templates 'suggests the use of organized tooling,' but did not attribute the activity to any tracked group.
- **Mitigation:** Google's published mitigation framework (layered defense) includes: (1) continuous adversarial model hardening/training with adversarial data against IPI (notably in Gemini 2.5 family); (2) dedicated red-team pressure testing of Gemini products; (3) the AI Vulnerability Reward Program to crowdsource external research; (4) strict data-instruction boundary enforcement — AI agents must not treat untrusted external content as instructions to execute, only as data; (5) real-time monitoring via large-scale crawling (Common Crawl) plus LLM-based classification with human validation; (6) the Secure AI Framework (SAIF) for ecosystem-wide defense; (7) Microsoft's 'Lethal Trifecta' community rule — only allow two of three powers (read untrusted content, hold private data, take outward actions); and supplemental defenses such as input pattern sanitization, instruction hierarchy/system-prompt override, least-privilege tool access with human-in-the-loop approval for high-risk actions, output validation, and behavioral anomaly monitoring on tool-call logs. Specific defensive recommendations: strip Unicode tag characters, zero-width joiners, HTML comments, and hidden CSS; treat AI agent outputs as untrusted before downstream execution.
- **Vendor Advisory:** http://security.googleblog.com/2026/04/ai-threats-in-wild-current-state-of.html

---

## 6. 🟠 Zero-Day — Google Workspace’s continuous approach to mitigating indirect prompt injections

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-02
**Reference:** <http://security.googleblog.com/2026/04/google-workspaces-continuous-approach.html>

> Posted by Adam Gavish, Google GenAI Security Team Indirect prompt injection (IPI) is an evolving threat vector targeting users of complex AI applications with multiple data sources, such as Workspace with Gemini. This technique enables the attacker to influence the behavior of an LLM by injecting malicious instructions into the data or tools used by the LLM as it completes the user’s query. This m…

**Parallel AI Enrichment:**

- **Technical Details:** Indirect prompt injection (IPI) attacks inject malicious instructions into data or tools consumed by an LLM so the model is influenced while completing a user query; this can occur even without direct user input and is a concern for multi‑source/agentic AI applications (e.g., Workspace with Gemini).
- **Affected Products:** Google Workspace (with Gemini)
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public reports describe IPI payloads observed in the wild (e.g., Forcepoint: "10 Indirect Prompt Injection Payloads Caught in the Wild"). The vendor advisory itself does not publish a PoC exploit.
- **Patch Available:** No official vendor patch released. The Google advisory describes ongoing hardening and "ever‑improving defenses" but does not announce a discrete patch or patch URL (see vendor advisory).
- **Active Exploitation:** Yes — third‑party reporting indicates payloads were observed "in the wild" (Forcepoint); Google’s advisory warns IPI is an evolving threat but does not enumerate confirmed, attributed incidents.
- **Threat Actors:** None known
- **Mitigation:** Mitigation steps unavailable.
- **Vendor Advisory:** https://blog.google/security/google-workspaces-continuous-approach-to-mitigating-indirect-prompt-injections/

---

## 7. 🟠 Zero-Day — Architecting Security for Agentic Capabilities in Chrome

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-12-08
**Reference:** <http://security.googleblog.com/2025/12/architecting-security-for-agentic.html>

> Posted by Nathan Parker, Chrome security team Chrome has been advancing the web’s security for well over 15 years, and we’re committed to meeting new challenges and opportunities with AI. Billions of people trust Chrome to keep them safe by default, and this is a responsibility we take seriously. Following the recent launch of Gemini in Chrome and the preview of agentic capabilities , we want to s…

**Parallel AI Enrichment:**

- **Technical Details:** Primarily: indirect prompt injection against agentic browsers — a malicious page (or UGC such as a review, or third-party iframe content) embeds hidden instructions that the Gemini-in-Chrome agent reads and acts on, leading to data exfiltration or unwanted transactions. For the related CVE-2026-0628: insufficient policy enforcement in Chrome's WebView tag lets a basic-permissions extension (using declarativeNetRequests) intercept and inject arbitrary JS/HTML into the privileged gemini.google.com/app page rendered inside the Gemini side-panel, enabling local file access, screenshot capture, and camera/microphone hijack without user consent.
- **Affected Products:** Google Chrome for Desktop prior to 143.0.7499.192 (Windows/Mac 143.0.7499.192 and .193; Linux 143.0.7499.192); Gemini in Chrome (agentic preview side-panel WebView)
- **CVSS Score:** 8.8
- **CVSS Vector:** CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Exploit Available:** No public PoC or weaponized exploit published. A documented attack chain was described by Palo Alto Unit 42 (responsible disclosure, March 2026) but the underlying PoC code was not made public.
- **Patch Available:** Yes. Google Chrome 143.0.7499.192 (Desktop) shipped January 6, 2026 fixes the related WebView-tag/CVE-2026-0628. For the broader indirect-prompt-injection defenses described in the Dec 8, 2025 blog, layered runtime mitigations (User Alignment Critic, Agent Origin Sets, Spotlighting/prompt-injection classifier, automated red-teaming) are being rolled out as part of the Gemini-in-Chrome agentic preview.
- **Active Exploitation:** No confirmed in-the-wild exploitation reported. The related WebView-tag/CVE-2026-0628 issue was found via proactive research by Palo Alto Networks Unit 42 and responsibly disclosed to Google before public release. NVD, OffSeq Threat Radar, and Unit 42 all state no known in-the-wild exploits.
- **Threat Actors:** None known
- **Mitigation:** Apply layered hardening for Gemini-in-Chrome agentic browsing: (1) User Alignment Critic isolates a high-trust model to veto misaligned agent actions; (2) Agent Origin Sets restrict agent web activity to task-relevant origins, partitioned read-only vs read-writable, with a trusted gating function for additions; (3) deterministic + model-based User Confirmations pause sensitive actions (banking, medical, purchases); (4) a real-time prompt-injection classifier runs on every page the agent sees, plus Spotlighting that biases the model toward system/user instructions over page content; (5) automated red-teaming generates malicious sites and LLM-driven attacks to continuously test defenses. For the related CVE-2026-0628, upgrade Google Chrome for Desktop to >= 143.0.7499.192 (also available via the Chrome Releases advisory).
- **Vendor Advisory:** http://security.googleblog.com/2025/12/architecting-security-for-agentic.html

---

## 8. 🟠 Zero-Day — Rust in Android: move fast and fix things

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-11-13
**Reference:** <http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html>

> Posted by Jeff Vander Stoep, Android Last year, we wrote about why a memory safety strategy that focuses on vulnerability prevention in new code quickly yields durable and compounding gains. This year we look at how this approach isn’t just fixing things, but helping us move faster . The 2025 data continues to validate the approach, with memory safety vulnerabilities falling below 20% of total vul…

**Parallel AI Enrichment:**

- **Technical Details:** High-level: the blog documents that Android’s 2025 data shows a large reduction in memory-safety vulnerability density coincident with Rust adoption; memory-safety issues addressed include classic classes such as use-after-free, buffer overflows and race conditions, and mitigation centers on adopting Rust and memory-safety tooling.
- **Affected Products:** Android platform (first-party and third-party open-source components) — code across C, C++, Java, Kotlin, and Rust (no single product+version list provided).
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** The blog post itself does not publish any PoC or weaponized exploit. Independent searches found unrelated CVE analyses (for example CVE-2025-68260) but no authoritative PoC linked from the blog post.
- **Patch Available:** No single patch is described in the blog post; Android Security Bulletins publish individual vulnerability patches (see vendor bulletins for per-CVE patches).
- **Active Exploitation:** No confirmed active exploitation tied to the blog-post’s aggregated findings is reported in the collected evidence; individual CVEs (outside the blog post) should be checked in vendor bulletins/NVD for exploitation status.
- **Threat Actors:** None known
- **Mitigation:** Adopt memory-safe languages (Rust) for new platform code, use Android memory-safety tooling and testing, and apply vendor security bulletins' patches for specific CVEs (no per-vulnerability workaround described in the blog post).
- **Vendor Advisory:** http://security.googleblog.com/2025/11/rust-in-android-move-fast-fix-things.html

---

## 9. 🟠 Zero-Day — Mitigating prompt injection attacks with a layered defense strategy

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2025-06-13
**Reference:** <http://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html>

> Posted by Adam Gavish, Google GenAI Security Team With the rapid adoption of generative AI, a new wave of threats is emerging across the industry with the aim of manipulating the AI systems themselves. One such emerging attack vector is indirect prompt injections. Unlike direct prompt injections, where an attacker directly inputs malicious commands into a prompt, indirect prompt injections involve…

**Parallel AI Enrichment:**

- **Technical Details:** Attackers embed hidden instructions or payloads inside content that an LLM will later ingest (email footers, document metadata, calendar invites, HTML/SVG comments, images, or vector‑DB chunks). When the model or an agent consumes that content it can treat the hidden text as part of its prompt or as tool input, producing data exfiltration, unauthorized actions (e.g., sending emails, calling tools), or manipulation of downstream automation.
- **Affected Products:** Google Gemini (Gemini 2.5), Google Workspace integrations (Gemini in Workspace), browser-based AI agents, LLM‑integrated workflows and RAG/vector DB pipelines
- **CVSS Score:** 0.0
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** Public proof‑of‑concepts and red‑team payloads have been demonstrated in research and industry tests (crafted hidden prompts, SVG/markdown tricks, metadata injections). There is no single vendor-supplied weaponized exploit kit — PoCs appear in academic/industry research and red-team reports.
- **Patch Available:** No single vendor "patch" (this is a threat class). Google describes product-level mitigations implemented in Gemini (Gemini 2.5 hardening) and Workspace (see vendor advisory).
- **Active Exploitation:** Yes — vendor telemetry and industry researchers have observed indirect prompt injection payloads and patterns in the wild; Google and independent researchers (e.g., Forcepoint) reported findings during web and threat-hunting sweeps.
- **Threat Actors:** None known
- **Mitigation:** Layered defenses: model hardening/adversarial training (e.g., Gemini 2.5), ML detectors to flag malicious instructions, input sanitization (markdown/image sanitization), suspicious-URL redaction and Safe‑Browsing checks, strict data-vs-instruction boundaries for RAG/pipelines, deterministic output-format validation and tool confirmation, and end‑user notifications/confirmations for high‑impact actions.
- **Vendor Advisory:** https://blog.google/security/mitigating-prompt-injection-attacks/

---

## 10. 🟠 Zero-Day — Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System

**CVE:** _No CVE_ &nbsp;|&nbsp; **Source:** CISA US-CERT Alerts &nbsp;|&nbsp; **Published:** Mon, 25 Au
**Reference:** <https://www.cisa.gov/news-events/cybersecurity-advisories/aa25-239a>

> Executive summary People’s Republic of China (PRC) state-sponsored cyber threat actors are targeting networks globally, including, but not limited to, telecommunications, government, transportation, lodging, and military infrastructure networks. While these actors focus on large backbone routers of major telecommunications providers, as well as provider edge (PE) and customer edge (CE) routers, th…

**Parallel AI Enrichment:**

- **Technical Details:** PRC state-sponsored actors target large backbone, provider-edge (PE) and customer-edge (CE) routers (and sometimes compromised devices/trusted connections), modify router configurations (including ACLs) to maintain persistent access, capture sensitive authentication traffic (e.g., RADIUS and TACACS+) and pivot to other networks.
- **Affected Products:** Cisco, Palo Alto, Ivanti, Fortinet, Juniper, Microsoft Exchange, and other backbone/PE/CE router products (vendor-level details dispersed across vendor CVE advisories).
- **CVSS Score:** 6.4
- **CVSS Vector:** CVSS vector unavailable.
- **Exploit Available:** No public PoC or weaponized exploit tied to the AA25-239A advisory has been reported; CISA stated exploitation of zero-day vulnerabilities has not been observed.
- **Patch Available:** No — multiple analyst summaries and CISA reporting indicate vendors have not published a consolidated patch or remediation guidance tied to AA25-239A.
- **Active Exploitation:** No confirmed active exploitation of the specific zero-day vulnerabilities described by AA25-239A has been reported (per CISA and industry reporting).
- **Threat Actors:** Salt Typhoon, OPERATOR PANDA, RedMike, UNC5807, GhostEmperor
- **Mitigation:** Harden and restrict router management interfaces (use MFA where available), rotate and strengthen credentials, increase logging/monitoring (including RADIUS/TACACS+), detect anomalous ACL/configuration changes, network segmentation/isolation of critical routing infrastructure, apply vendor updates when they become available, and deploy detection rules/visibility for the indicators CISA and industry provided.
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

## 14. 🟡 High Severity — Craft CMS: Authorization bypass in `entries/move-to-section` via missing target-section save check

**CVE:** `CVE-2026-50280` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-43cq-c2gq-pfpw>

> ### Summary

The `EntriesController::actionMoveToSection()` endpoint checks only whether the current user can view the destination section, but it does not require permission to save entries into that section. A low-privileged authenticated control-panel user who can move an entry out of its current section can therefore move that entry into a different section where they have read access but no w…

---

## 15. 🟡 High Severity — Langroid: Path traversal in the file tools allows read/write outside configured current directory

**CVE:** `CVE-2026-50181` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-fg23-3346-88f5>

> ### Summary

Langroid&#x27;s `ReadFileTool` and `WriteFileTool` appear to treat `curr_dir` as the intended working-directory boundary for file operations. However, the tools only change the process working directory to `curr_dir` and then operate on the user-supplied `file_path` without resolving and enforcing that the final path remains inside `curr_dir`.

As a result, a tool caller can supply pa…

---

## 16. 🟡 High Severity — Kerberos Hub private key (X-Kerberos-Hub-PrivateKey) leaked to cross-host redirect target due to redirect-following HTTP client without CheckRedirect

**CVE:** `CVE-2026-50192` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-h5gx-45rj-2h5j>

> ### Summary

The Kerberos Hub upload path sends the agent&#x27;s Hub credentials in the custom `X-Kerberos-Hub-PrivateKey` and `X-Kerberos-Hub-PublicKey` request headers to the operator-configured Hub URL (`config.HubURI`). The HTTP client used (`&amp;http.Client{}` in `UploadKerberosHub`) is constructed without a `CheckRedirect` policy, so it follows HTTP redirects automatically. Go&#x27;s `net/h…

---

## 17. 🟡 High Severity — OpenClaw: Hook-triggered CLI runs could receive owner MCP tool authority

**CVE:** `CVE-2026-53814` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-6fvr-66p3-3qj4>

> ### Summary

OpenClaw hook ingress can start automated agent runs using a configured hook token. In affected releases, a hook-triggered run could select a bundled CLI backend that received owner-scoped MCP loopback authority instead of a scope appropriate for hook ingress.

This issue affects the boundary between hook-token automation and owner-only MCP tools. It does not affect deployments with h…

---

## 18. 🟡 High Severity — OpenClaw's browser act interactions could bypass private-network navigation checks

**CVE:** `CVE-2026-53812` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-2hfg-4fh4-qp7f>

> ### Summary

OpenClaw&#x27;s browser control SSRF checks blocked direct navigation to private or loopback URLs, but some Playwright `act` interactions could trigger navigation after the initial check. A later browser evaluation could then read from the page reached by that action-triggered navigation.

This issue is specific to browser control actions and private-network navigation policy. Browser…

---

## 19. 🟡 High Severity — mcp-memory-service: Missing Authentication on Document API Endpoints Allows Unauthenticated Memory Read/Write/Delete

**CVE:** `CVE-2026-50027` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://github.com/advisories/GHSA-84hp-mqvj-3p8h>

> ## Missing Authentication on Document API Endpoints Allows Unauthenticated Memory Read/Write/Delete

### Summary

All HTTP routes under `/api/documents/*` in `mcp-memory-service` are served without any authentication dependency, even when the server is configured with an API key (`MCP_API_KEY`) or OAuth. An unauthenticated remote attacker can upload arbitrary content into the memory store (write),…

---

## 20. 🟡 High Severity — SharePoint RCE CVE-2026-45659 Added to CISA KEV After Active Exploitation

**CVE:** `CVE-2026-45659` &nbsp;|&nbsp; **Source:** The Hacker News Security &nbsp;|&nbsp; **Published:** 2026-07-02
**Reference:** <https://thehackernews.com/2026/07/sharepoint-rce-cve-2026-45659-added-to.html>

> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday added a high-severity flaw impacting Microsoft SharePoint Server to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

The vulnerability, tracked as CVE-2026-45659 (CVSS score: 8.8), is a case of remote code execution arising from the deserialization of untrusted data. The issue

---

## 21. 🟡 High Severity — Apify Model Context Protocol (MCP) server: Actor MCP path authority injection leaks Apify token

**CVE:** `CVE-2026-50143` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-6gr2-qh89-hxwm>

> ## Actor MCP path authority injection leaks Apify token

### Summary

`@apify/actors-mcp-server` version `0.10.7` builds Actor standby URLs by directly concatenating a trusted base URL with an attacker-controlled `webServerMcpPath` value taken from an Actor definition returned by the Apify API. An attacker who publishes a malicious Actor with a crafted `webServerMcpPath` (e.g., `@attacker.example/…

---

## 22. 🟡 High Severity — goshs: Share-link ?token=… redemption races past download limit

**CVE:** `CVE-2026-50139` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-j48m-h7xq-2xpj>

> # Share-link `?token=…` redemption races past download limit

**Ecosystem:** Go
**Package:** `goshs.de/goshs/v2` (`github.com/patrickhener/goshs`)
**Affected:** `&lt;= v2.0.9` (every release that shipped the share-link feature)

## Summary

`ShareHandler` reads the share token&#x27;s `DownloadLimit` under `RLock`, releases the lock, serves the file, then re-acquires the lock to increment the count…

---

## 23. 🟡 High Severity — goshs: WebDAV listener ignores --read-only, --upload-only, and --no-delete mode flags

**CVE:** `CVE-2026-50138` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-3whc-qvhv-xqjp>

> # WebDAV listener ignores `--read-only`, `--upload-only`, and `--no-delete` mode flags

**Ecosystem:** Go
**Package:** `goshs.de/goshs/v2` (`github.com/patrickhener/goshs`)
**Affected:** `&lt;= v2.0.9` (every release that ships the WebDAV handler)

## Summary

When `goshs` is launched with WebDAV enabled (`-w`), the mode-restriction flags `--read-only`, `--upload-only`, and `--no-delete` are enfor…

---

## 24. 🟡 High Severity — `oras-go` tar extraction: Hardlink entry with relative Linkname escapes extract dir via process CWD resolution

**CVE:** `CVE-2026-50163` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-fxhp-mv3v-67qp>

> ### Root cause

The tar-extraction helper `ensureLinkPath` at [`content/file/utils.go:262-275`](https://github.com/oras-project/oras-go/blob/main/content/file/utils.go#L262-L275) validates that a hardlink&#x27;s target resolves inside the extract base, but then returns the original unresolved `target` string back to the caller:

```go
func ensureLinkPath(baseAbs, baseRel, link, target string) (str…

---

## 25. 🟡 High Severity — oras-go blob upload vulnerable to credential forwarding via unvalidated Location header

**CVE:** `CVE-2026-50151` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-jxpm-75mh-9fp7>

> ## Summary

oras-go follows a registry-controlled `Location` header during the monolithic blob upload flow and reuses the `Authorization` header from the initial `POST` request for the subsequent `PUT` request. If a malicious registry returns a cross-host `Location`, oras-go can send the caller&#x27;s credentials to an attacker-controlled endpoint.

## Affected Versions

tested: v2.6.0 (commit 032…

---

## 26. 🟡 High Severity — Keycloak has privilege escalation via improper scope mapping enforcement

**CVE:** `CVE-2026-9795` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-32h4-44jj-c5vx>

> ### Description
A flaw was found in Keycloak&#x27;s Fine-Grained Admin Permissions (FGAPv2) feature. An administrator with limited client management permissions can exploit this vulnerability to assign any realm role, including highly privileged roles, to a client&#x27;s scope mapping. This bypasses intended security controls, allowing the injected role to be projected into a user&#x27;s authentic…

---

## 27. 🟡 High Severity — oras-go: Malicious registry can hijack Bearer token realm to exfiltrate credentials and refresh tokens

**CVE:** `CVE-2026-48978` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-xf85-363p-868w>

> ## Summary

oras-go&#x27;s `auth.Client` follows the `realm` URL from a registry&#x27;s `WWW-Authenticate: Bearer` challenge without validating its scheme or host. The `realm` field is server-controlled by design in the OCI/distribution spec — registries legitimately point token requests at a separate auth endpoint (e.g. Docker Hub&#x27;s `registry-1.docker.io` -&gt; `auth.docker.io`), so cross-ho…

---

## 28. 🟡 High Severity — Rancher has Privilege Escalation from Project Owner to Host

**CVE:** `CVE-2026-41052` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-vx8h-4prv-g744>

> ### Impact

A vulnerability has been identified in Rancher Manager that allows users assigned the Project Owner role to modify Pod Security Admission (PSA) labels on namespaces within their projects. Under the default role configuration, an attacker with the following access pattern can exploit this issue:
1. **Cluster Access:** The user is granted Cluster Member access.
2. **Project Ownership:** …

---

## 29. 🟡 High Severity — Mailpit: Sibling-endpoint memory-exhaustion DoS via unbounded JSON body on /api/v1/messages, /api/v1/tags, and /api/v1/message/{id}/release (incomplete fix of GHSA-fpxj-m5q8-fphw)

**CVE:** `CVE-2026-48824` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-28pq-6qxg-wg5r>

> ### Summary

The fix for GHSA-fpxj-m5q8-fphw (CVE-2026-45710, &quot;Mailpit: Set a default 50MB p/m limit to prevent DoS via unlimited SMTP DATA and /api/v1/send body sizes&quot;) wrapped only `POST /api/v1/send` with `http.MaxBytesReader`. The four other Mailpit JSON-body API endpoints  `PUT /api/v1/messages` (SetReadStatus), `DELETE /api/v1/messages` (DeleteMessages), `PUT /api/v1/tags` (SetMess…

---

## 30. 🟡 High Severity — Rancher Fleet has SSRF in Bundle Reader via Unvalidated Helm Repository URL in fleet.yaml

**CVE:** `CVE-2026-44936` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-hx4v-cxpf-vh8m>

> ### Impact
A vulnerability has been identified in Fleet when the `helmRepoURLRegex` field isn&#x27;t set on a `GitRepo` resource. Fleet&#x27;s bundle reader forwards Helm authentication credentials (`BasicAuth`) to any URL specified in the `helm.repo` field of a `fleet.yaml` file.

An attacker with git push access to a Fleet-monitored repository can exploit this behavior by specifying a malicious …

---

## 31. 🟡 High Severity — Rancher vulnerable to command injection through unsanitized YAML parameter

**CVE:** `CVE-2026-44939` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-mhc6-2gfq-xx62>

> ### Impact
A critical command injection vulnerability has been identified in the Rancher Manager cluster import endpoint  `/v3/import/{token}_{clusterId}.yaml` through unsanitized YAML parameters. This endpoint accepts an `authImage` query parameter that is rendered without sanitization into a generated Kubernetes manifest template. By including URL-encoded newlines in the parameter value, an atta…

---

## 32. 🟡 High Severity — Rancher Fleet has Unauthenticated Webhook: Regex Injection via Unsanitized Repository URL Components

**CVE:** `CVE-2026-44937` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-jmf4-m7j9-g72r>

> ### Impact
A vulnerability has been identified in Fleet when the webhook endpoint is configured without a secret; an attacker can forge webhook requests. The attacker doesn&#x27;t need to know the specific repository or path configured in the GitRepo resource to make Fleet process these requests.

An attacker can exploit this vulnerability to cause the following impacts:
1. Trigger continuous repo…

---

## 33. 🟡 High Severity — Fleet has PSS Bypass through addLabelsFromOptions in Fleet Agent

**CVE:** `CVE-2026-44938` &nbsp;|&nbsp; **Source:** GitHub Security Advisories &nbsp;|&nbsp; **Published:** 2026-07-01
**Reference:** <https://github.com/advisories/GHSA-864g-863m-vcvq>

> ### Impact
A vulnerability has been identified in Fleet&#x27;s agent-side deployer, which did not filter security-sensitive keys from `namespaceLabels` in `fleet.yaml` (or `BundleDeployment.spec.options.namespaceLabels`) when applying them to the target namespace. 

An attacker with `git push` access to a Fleet-monitored repository could overwrite Pod Security Standards (PSS) enforcement labels on…

---

## 34. 🟡 High Severity — Bringing Rust to the Pixel Baseband

**CVE:** `CVE-2024-27227` &nbsp;|&nbsp; **Source:** Google Security Blog &nbsp;|&nbsp; **Published:** 2026-04-10
**Reference:** <http://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html>

> Posted by Jiacheng Lu, Software Engineer, Google Pixel Team Google is continuously advancing the security of Pixel devices. We have been focusing on hardening the cellular baseband modem against exploitation. Recognizing the risks associated within the complex modem firmware, Pixel 9 shipped with mitigations against a range of memory-safety vulnerabilities. For Pixel 10, Google is advancing its pr…

---
