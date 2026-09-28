+++
title = "Conference Brief — 2026-09-28"
date = "2026-09-28T06:00:00Z"
type = "conferences"
tags = ["mobile", "privacy", "kernel", "exploitation", "web-security", "ndss"]
summary = "New insights into WebView privacy leaks, kernel cache exploitation, and HTTP/2 cross-origin attacks."
+++

## In brief

- **Cross-Boundary Mobile Tracking:** Demonstrates how Android apps can interfere with WebViews by injecting JavaScript at runtime, leading to the diffusion of context-restricted information from Java to JavaScript environments. The study highlights privacy violations caused by these dynamic injections across various apps.
Datta, S. et al. "Cross-Boundary Mobile Tracking: Exploring Java-to-JavaScript Information Diffusion in WebViews." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/cross-boundary-mobile-tracking-exploring-java-to-javascript-information-diffusion-in-webviews/

- **Cross-Cache Attacks for the Linux Kernel via PCP Massaging:** Introduces PCPLOST, a novel cross-cache memory massaging technique that reliably exploits the Linux kernel allocator despite modern mitigations like `SLAB_VIRTUAL`. It leverages a side channel involving system call timings to detect object and page allocations, achieving over 90% reliability for out-of-bounds, use-after-free, and double-free vulnerabilities across generic caches.
Migliorelli, C. et al. "Cross-Cache Attacks for the Linux Kernel via PCP Massaging." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/cross-cache-attacks-for-the-linux-kernel-via-pcp-massaging/

- **Cross-Origin Web Attacks via HTTP/2 Server Push and Signed HTTP Exchange:** Identifies a fundamental flaw in how HTTP/2 features weaken the Same-Origin Policy (SOP). By exploiting the SubjectAlternativeName (SAN) list in TLS certificates, attackers can bypass URI-based origin constraints. The research details two novel vectors—CrossPUSH and CrossSXG—allowing for cross-origin attacks on unrelated domains sharing a certificate.
Chen, P. et al. "Cross-Origin Web Attacks via HTTP/2 Server Push and Signed HTTP Exchange." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/cross-origin-web-attacks-via-http-2-server-push-and-signed-http-exchange/
