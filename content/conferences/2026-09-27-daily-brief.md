+++
title = "Conference Brief — 2026-09-27"
date = 2026-09-27T06:00:00Z
type = "conferences"
tags = ["ndss", "side-channel", "network-security"]
summary = "DNS cache timing attacks for continuous user behavior monitoring, SMTP timeout manipulation for amplification attacks, co-training for dynamic password guessing, and performance-counter side channels on AMD SEV-SNP VMs."
+++

## In brief

## CounterSEVeillance: Performance-Counter Attacks on AMD SEV-SNP

- Gast et al. "CounterSEVeillance: Performance-Counter Attacks on AMD SEV-SNP." NDSS 2026 — [https://www.ndss-symposium.org/ndss-paper/counterseveillance-performance-counter-attacks-on-amd-sev-snp/](https://www.ndss-symposium.org/ndss-paper/counterseveillance-performance-counter-attacks-on-amd-sev-snp/)
- Demonstrates a side-channel attack that extracts secret-dependent control flow and operand properties from performance counter data inside AMD SEV-SNP VMs, achieving single-instruction resolution.
- Abuses 228 performance counter events exposed to the hypervisor, allowing an attacker to single-step the victim VM using APIC interrupts and page faults.
- Extracted a full RSA-4096 key from an Mbed TLS signature process in under 8 minutes, and recovered a 6-digit TOTP with an average of 31.1 guesses.

## Continuous User Behavior Monitoring using DNS Cache Timing Attacks

- Weissteiner et al. "Continuous User Behavior Monitoring using DNS Cache Timing Attacks." NDSS 2026 — [https://www.ndss-symposium.org/ndss-paper/continuous-user-behavior-monitoring-using-dns-cache-timing-attacks/](https://www.ndss-symposium.org/ndss-paper/continuous-user-behavior-monitoring-using-dns-cache-timing-attacks/)
- Introduces a DNS cache timing attack that enables continuous monitoring of user behavior without requiring any code execution on the victim's machine.
- Exploits differences in response times from the DNS server to infer whether a specific domain has been cached, indicating recent access by the victim.
- Evaluates the attack against real-world scenarios, demonstrating its ability to accurately track user access to targeted websites over time.

## CoordMail: Exploiting SMTP Timeout and Command Interaction to Coordinate Email Middleware for Convergence Amplification Attack

- Li et al. "CoordMail: Exploiting SMTP Timeout and Command Interaction to Coordinate Email Middleware for Convergence Amplification Attack." NDSS 2026 — [https://www.ndss-symposium.org/ndss-paper/coordmail-exploiting-smtp-timeout-and-command-interaction-to-coordinate-email-middleware-for-convergence-amplification-attack/](https://www.ndss-symposium.org/ndss-paper/coordmail-exploiting-smtp-timeout-and-command-interaction-to-coordinate-email-middleware-for-convergence-amplification-attack/)
- Identifies a denial-of-service vector against email servers by leveraging SMTP's delay-tolerant nature and long session timeouts.
- Uses coordinated SMTP connections to interact with email middleware, generating massive amplification traffic that exhausts available bandwidth and clogs task queues.
- Shows that an attacker can disrupt email services and potentially compromise authentication mechanisms by reflecting amplified traffic against centralized email servers.

## CoT-DPG: A Co-Training based Dynamic Password Guessing Method

- Wang et al. "CoT-DPG: A Co-Training based Dynamic Password Guessing Method." NDSS 2026 — [https://www.ndss-symposium.org/ndss-paper/cot-dpg-a-co-training-based-dynamic-password-guessing-method/](https://www.ndss-symposium.org/ndss-paper/cot-dpg-a-co-training-based-dynamic-password-guessing-method/)
- Proposes a dynamic password guessing framework that uses co-training to combine multiple guessing models and fit the target distribution incrementally at both the feature and character levels.
- Employs policy distribution optimization and iterative training to fuse multidimensional information, dynamically generating password guesses.
- Reports an absolute improvement in cracking rate between 6.4% and 26.7% over existing state-of-the-art methods when evaluated on eight real-world password datasets.
