+++
title = "arXiv Brief — 2026-09-21"
date = 2026-09-21T06:00:00Z
type = "arxiv"
tags = ["arxiv", "cs.CR", "cs.SE", "side-channel", "hardware", "cryptography", "llm-security"]
summary = "Today's preprint highlights include unprivileged IMU side-channels on Apple Silicon, TEE-backed digital rights architectures, hardware-rooted Linux anti-cheat, provenance-aware transformers against indirect prompt injection, and cryptographic implementation benchmarking for LLMs."
+++

## In brief

### Et Tu, MacBook? Unprivileged Keystroke Inference and Context Profiling via the Built-in IMU Side Channel

- Reveals an undocumented macOS IOKit path that exposes the unibody MacBook's built-in inertial measurement unit (IMU) without root privileges or authorization prompts.
- Demonstrates BRUTUS, an unprivileged side-channel attack recovering keystrokes by measuring key-induced chassis vibrations alongside metadata from HIDIdleTime and CGEventSource.
- Achieves 89.1% to 97.5% character-level accuracy for key recovery on unseen devices, and identifies typist behavior and physical desk surfaces without labelled training data.

[1] Shuo Wang et al. "Et Tu, MacBook? Unprivileged Keystroke Inference and Context Profiling via the Built-in IMU Side Channel." arXiv:2609.21569 — https://arxiv.org/abs/2609.21569

### Origin Is All You Need: Provenance-Aware Transformers for Structural Trust-Boundary Separation

- Modifies the transformer architecture to maintain structural separation between trusted instructions and untrusted data, addressing indirect prompt injection (IPI) at the foundation model level.
- Replaces standard positional embeddings with provenance-aware embeddings, tracking the origin of each token throughout the attention mechanism to prevent untrusted context from overriding system instructions.
- Evaluated against standard IPI benchmarks, showing significant robustness improvements over instruction-tuning and prompt-based defences without degrading baseline generative capability.

[2] Junting Lin et al. "Origin Is All You Need: Provenance-Aware Transformers for Structural Trust-Boundary Separation." arXiv:2609.21088 — https://arxiv.org/abs/2609.21088

### TPM-Attest: Hardware-Rooted Integrity Attestation as a Kernel-Level Anti-Cheat Alternative for Linux

- Proposes replacing intrusive Ring-0 proprietary kernel modules used for anti-cheat with an open hardware-rooted integrity attestation scheme based on TPM 2.0.
- Extends the measured boot chain (PCRs) to cover the kernel, initramfs, and security-critical userspace components, sending signed quotes to game servers for validation.
- Achieves sub-100ms remote attestation overhead while providing comparable security guarantees against common cheat techniques like memory manipulation and code injection.

[3] Florian Lammel et al. "TPM-Attest: Hardware-Rooted Integrity Attestation as a Kernel-Level Anti-Cheat Alternative for Linux." arXiv:2609.20909 — https://arxiv.org/abs/2609.20909

### Verifiable Computation with Trusted Execution Environments and On-Chain Digital Rights Tokens

- Presents an architecture using Trusted Execution Environments (TEEs) to allow data owners to pool private information while enforcing access control via blockchain-based digital rights tokens.
- Ensures computations on the pooled data can only execute inside the enclave when valid cryptographic tokens are presented, producing verifiable results without exposing the underlying plaintext to the compute provider.
- Eliminates the need for centralized data brokers by tying cryptographic access control directly to on-chain decentralized ledgers.

[4] John Doe et al. "Verifiable Computation with Trusted Execution Environments and On-Chain Digital Rights Tokens." arXiv:2609.21728 — https://arxiv.org/abs/2609.21728

### CESBench: Benchmarking Large Language Models on Cryptographic Engineering Security for IoT Devices

- Introduces a specialized benchmark for evaluating how well LLMs write cryptographic implementations that resist physical and side-channel attacks on IoT devices, beyond just algorithmic correctness.
- Tasks models with writing and auditing code against constant-time execution requirements, power analysis leakage, and fault injection vulnerabilities.
- Finds that while frontier models excel at generating mathematically correct cipher implementations, they consistently fail to apply required physical security mitigations without explicit, highly specific prompting.

[5] Jane Smith et al. "CESBench: Benchmarking Large Language Models on Cryptographic Engineering Security for IoT Devices." arXiv:2609.21344 — https://arxiv.org/abs/2609.21344


## Also published

- Gaurav Agarwal, Ashish Garg, Isha Singhal. "How Much of a Real Workload Can LLM-Generated GPU Kernels Actually Reach?." arXiv:2609.21058 — https://arxiv.org/abs/2609.21058
