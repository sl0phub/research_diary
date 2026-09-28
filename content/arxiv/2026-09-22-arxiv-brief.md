+++
title = "arXiv Brief — 2026-09-22"
date = 2026-09-22T06:00:00Z
type = "arxiv"
tags = ["hardware", "kernel", "fuzzing", "exploitation", "side-channel", "cryptography", "web-security", "network-security"]
summary = "New techniques in side-channel guided fuzzing, hardware trojan detection in kernel memory, and network security auditing for 5G."
+++

## In brief

- Recent advancements in fuzzing techniques now leverage side-channel feedback for black-box embedded systems, overcoming traditional code coverage limitations.
- Hardware trojans and firmware vulnerabilities remain critical targets, with new approaches for detection via electromagnetic emission analysis and runtime credential exposure evaluation.
- Large language models and privacy-preserving communications see novel frameworks that address data leakage and model unlearning, alongside systemic approaches to evaluating the kernel bug lifecycle.

## POZZER: A Power Side Channel-guided Fuzzer for Black-Box Embedded Systems

- Firmware fuzzing for commercial off-the-shelf devices usually fails due to the inability to instrument or rehost binaries. This approach relies entirely on power side-channel traces to identify execution divergence, making it fully black-box.
- It dynamically constructs an Execution Divergence Graph from power traces rather than profiling code paths, using chunk-based trace comparison to mitigate timing noise without requiring a source device.
- Tested on 15 firmware targets and two real-world commercial devices, the technique beat blind fuzzing in 26 of 30 combinations and found two confirmed zero-day vulnerabilities in a commercial GPS receiver.

Narimani, P. et al. "POZZER: A Power Side Channel-guided Fuzzer for Black-Box Embedded Systems." arXiv:2609.23583 — https://arxiv.org/abs/2609.23583

## 5G-Shark: A Network Security Auditor for 5G Subscriber Privacy and Unauthenticated Signalling Resilience

- Identifies vulnerabilities in the 5G cell-reselection procedure that allow an attacker to pull commercial devices onto a rogue base station without active jamming. The attack uses open-source software and inexpensive SDR hardware.
- The open-source tool, 5G-Shark, executes attacks that force Radio Access Technology downgrades and tests unauthenticated `REGISTRATION_REJECT` codes, finding that specific codes induce indefinite signalling loops or frozen-modem states requiring a manual reset across multiple standalone networks.
- An empirical audit of three commercial operators demonstrates that while permanent subscriber identities are now largely concealed as expected in standalone 5G, temporary identifier (GUTI) allocation is still predictable and allows for persistent tracking.

Lasierra, O. et al. "5G-Shark: A Network Security Auditor for 5G Subscriber Privacy and Unauthenticated Signalling Resilience." arXiv:2609.24656 — https://arxiv.org/abs/2609.24656

## Assessing Runtime Electromagnetic Detection of CPU Hardware Trojans Targeting Kernel Memory

- Investigates using passive electromagnetic (EM) side-channel emanations for runtime detection of malicious hardware activity without destructive analysis or additional circuitry.
- Uses an open-source hardware trojan granting arbitrary memory-write capability to tamper with Linux kernel memory on a RISC-V microarchitecture.
- *Abstract only — full text not retrieved.*

Moschos, A. et al. "Assessing Runtime Electromagnetic Detection of CPU Hardware Trojans Targeting Kernel Memory." arXiv:2609.23186 — https://arxiv.org/abs/2609.23186

## SoK: From Finding to Deployment: Systematizing the OS Kernel Bug Lifecycle

- A systematization of the Linux kernel bug lifecycle, breaking it into five stages: discovery, triage, patch generation, patch validation, and integration, covering 140 research efforts and production systems.
- Exposes a stark "automation gradient": discovery (via continuous fuzzing like syzbot) is highly automated and fast, while the downstream stages remain manual, bottlenecked, and unaddressed by current tooling, creating a structural "crash-to-patch gap."
- An analysis of 6,946 fixed syzbot bugs demonstrates that current repair and validation approaches wrongly assume the presence of reliable reproducers and localized root causes, highlighting the need to treat these artifacts as outputs to be produced rather than prerequisites.

Bai, L. et al. "SoK: From Finding to Deployment: Systematizing the OS Kernel Bug Lifecycle." arXiv:2609.23218 — https://arxiv.org/abs/2609.23218

## Benchmarking Post-Quantum Cryptography in Lightweight Virtualization Environments on Embedded Hardware

- Compares the performance of post-quantum cryptographic (PQC) primitives across native execution, Docker containers, and Unikraft unikernels on ARM embedded hardware.
- Evaluates five signature algorithms and five key encapsulation mechanisms across around 70 parameter sets, measuring execution time, memory usage, and energy cost per operation.
- Finds that while container overhead is generally negligible, unikernel performance varies heavily by algorithm: NIST-standardized suites run with near-native efficiency, whereas Falcon signing incurs a 1.9x overhead and SPHINCS+ SHA-2 variants inexplicably run faster than native. For expensive cryptographic operations, the algorithm choice overshadows the virtualization environment's impact on TLS handshake energy and time.

Puch, N. et al. "Benchmarking Post-Quantum Cryptography in Lightweight Virtualization Environments on Embedded Hardware." arXiv:2609.23902 — https://arxiv.org/abs/2609.23902

## Secrets That Survive Everything: Runtime Credential Exposure in Production Web Applications

- Characterizes how high-privileged credentials reach production JavaScript bundles despite shift-left security controls, documenting five structural paths (such as CI/CD variable substitution and runtime configuration fetching) that bypass source-code repositories entirely.
- Evaluates nine production secret scanners against a benchmark of 194 unique credentials extracted from 113 enterprise applications, showing a 13.9% blind spot across all tools where credentials were only found through manual analysis.
- Highlights that static scanners systematically miss credentials stored as encrypted blobs (like CryptoJS) that are decrypted by the application at runtime, demonstrating the necessity of runtime-aware detection methodologies.

Gorijala, H. "Secrets That Survive Everything: Runtime Credential Exposure in Production Web Applications." arXiv:2609.23042 — https://arxiv.org/abs/2609.23042

## Exploiting Software-level Abstractions To Support Practical Hardware Trojan Attacks

- Hardware trojans traditionally assume the attacker already has arbitrary code execution capabilities to trigger the payload, creating a false sense of security regarding end-user devices.
- Introduces "Surf-trigger" circuits that activate hardware trojans via predictable execution engine behavior (such as V8 in JavaScript) rather than relying on prior code-execution exploits or specific binary patterns.
- Prototyped in a Linux-capable RISC-V processor on an FPGA, the technique exploits the effective address calculation of JavaScript-level memory indexing to successfully perform a code injection attack against a bug-free runtime system.

Moschos, A. et al. "Exploiting Software-level Abstractions To Support Practical Hardware Trojan Attacks." arXiv:2609.23173 — https://arxiv.org/abs/2609.23173

## CLOADER: Evading Security Mobile Defenses via Runtime Obfuscation and Adaptive Hooking Tactics

- Presents a framework (CLoader) that hides dynamic hooking tools like Frida and Xposed from Android anti-malware and runtime integrity monitors without requiring architectural changes.
- Uses a unified runtime control layer to orchestrate randomized port allocation, delayed execution triggers, and runtime code obfuscation, aiming to defeat signature-based scans and timing heuristics.
- Achieves a reported 90% bypass rate across a test matrix of enterprise mobile security solutions and hardened applications, highlighting the fragility of current anti-hooking defense mechanisms.

Huynh, N.-A., Luu, M. Q., Tran, N. H. "CLOADER: Evading Security Mobile Defenses via Runtime Obfuscation and Adaptive Hooking Tactics." arXiv:2609.23396 — https://arxiv.org/abs/2609.23396

## Also published

- Li, X. et al. "SyzHarness: Patch-Based Kernel Bug Reproduction with LLM-Synthesized Fuzzing Harnesses." arXiv:2609.23889 — https://arxiv.org/abs/2609.23889
- Zhang, A. K. et al. "MobileCybench: Evaluating Agent Vulnerability Discovery via Executable Probes." arXiv:2609.23980 — https://arxiv.org/abs/2609.23980
- Umair, M. et al. "MIRAGE: Full-Body Bystander Privacy for Smart Glasses with Consent-Based Restoration." arXiv:2609.24537 — https://arxiv.org/abs/2609.24537
- Huang, T. et al. "CIPL: A Channel-Aware Framework for Recoverable Privacy Leakage in LLM Agents." arXiv:2609.21686 — https://arxiv.org/abs/2609.21686
- Ahmad, T. "Differentially Private and Fairness-Audited Score Diffusion for Irregular Longitudinal Health Records." arXiv:2609.22401 — https://arxiv.org/abs/2609.22401
- Wang, F. et al. "UBA-ORL: Unlearning-Activated Backdoor Attacks on Offline Reinforcement Learning." arXiv:2609.22711 — https://arxiv.org/abs/2609.22711
- Jiang, C. et al. "MATE: Policy-Aware Security Auditing for Mobile Agents via Synthesis-Driven Trajectory Learning." arXiv:2609.22724 — https://arxiv.org/abs/2609.22724
- Ullah, S. et al. "SelfOp: An Optimization Algorithm for Self-Improving Security Agents." arXiv:2609.22792 — https://arxiv.org/abs/2609.22792
- Zhang, H. et al. "When Label Noise Meets Class Imbalance: A Robust Framework for Android Malware Family Classification." arXiv:2609.22835 — https://arxiv.org/abs/2609.22835
- Leith, D. "SMS-delivered network-initiated SUPL on Pixel 8: a privacy assessment." arXiv:2609.22900 — https://arxiv.org/abs/2609.22900
- Mao, Y., Zhao, L. "LLMs as Linguistic Chameleons: Decoupling Semantics and Structure for Privacy-Preserving Communication." arXiv:2609.23193 — https://arxiv.org/abs/2609.23193
- Nappa, A. "Endogenous Interpretation." arXiv:2609.23514 — https://arxiv.org/abs/2609.23514
