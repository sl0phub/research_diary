+++
title = "Conference Brief — 2026-09-18"
date = 2026-09-18T00:00:00Z
type = "conferences"
tags = ["ndss", "web-security", "fuzzing", "vulnerability-discovery"]
summary = "New approaches for finding business logic flaws via annotation-based sanitisation and detecting site isolation bypasses in modern browsers."
+++

## In brief

- Today's highlights feature advancements in automated vulnerability discovery for web applications and browser architecture.
- We cover a new approach that combines developer annotations with dynamic analysis to find business logic flaws, and an automated framework for uncovering site isolation bypasses in modern browsers.

## Anota: Identifying Business Logic Vulnerabilities via Annotation-Based Sanitization

- Introduces Anota, a framework that leverages lightweight developer annotations combined with dynamic fuzzing to uncover business logic vulnerabilities that evade traditional scanners.
- Extends the memory-safety sanitizer model to application logic, allowing developers to define custom sources, sinks, and access rules directly in the code, which Anota then tracks at runtime using an instrumented interpreter.
- Evaluated against standard vulnerable benchmarks and out-performed existing static and dynamic scanners, reporting all 35 in-scope vulnerabilities with zero false positives during a 24-hour fuzzing trial.

Wang, M., Görz, P., Schilling, J., Hassler, K., Guo, L., Holz, T., Abbasi, A. "Anota: Identifying Business Logic Vulnerabilities via Annotation-Based Sanitization." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/anota-identifying-business-logic-vulnerabilities-via-annotation-based-sanitization/

## Are your Sites Truly Isolated? Automatically Detecting Logic Bugs in Site Isolation Implementations

- Examines the implementation flaws in browser Site Isolation mechanisms, which aim to confine separate web origins to distinct renderer processes.
- Proposes an automated fuzzing framework specifically targeting the Inter-Process Communication (IPC) boundary between the compromised renderer and the privileged browser process to detect logic bugs that allow origins to bypass isolation.
- Discovered multiple logic bugs in Chrome and Firefox that enable an attacker to spoof origins, access cross-site data, or interact with privileged APIs, demonstrating the fragility of current Site Isolation implementations.

| Browser | Bug Class | Example Attack Surface |
|---|---|---|
| Chrome | Origin Confusion | Spoofing origin during filesystem URL creation |
| Chrome | Missing Checks | Accessing IndexedDB or Blob URLs across origins |
| Firefox | Checks Bypassed | Forging notifications or setting arbitrary document URIs |

Drescher, J., Klein, D., Johns, M. "Are your Sites Truly Isolated? Automatically Detecting Logic Bugs in Site Isolation Implementations." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/are-your-sites-truly-isolated-automatically-detecting-logic-bugs-in-site-isolation-implementations/
