+++
title = "Conference Brief — 2026-09-15"
date = 2026-09-15T06:00:00Z
type = "conferences"
tags = ["ndss", "llm-security", "memory-safety", "binary-analysis", "network-security", "privacy"]
summary = "Recent NDSS research covering LLM jailbreak causality, bootloader fuzzing, the impact of compiler inlining on binary analysis, enclave privilege scaling, adversarial evasion of traffic detection, and identity-preserving facial anonymization."
+++

## In brief

- Today's selection spans system security and applied machine learning, highlighting vulnerabilities that emerge when components interact in unexpected ways—from compiler optimizations degrading binary analysis models to adversarial modifications evading traffic classification.
- A recurring theme is the necessity of structural understanding over surface-level patching: effective defenses require causal modeling of LLM jailbreaks, formal verification of enclave privilege layers, and comprehensive fuzzing across all bootloader input surfaces.
- We also see practical advancements in privacy-preserving technologies, with a new framework for generating anonymous yet recognizable virtual faces, and the identification of a severe code poisoning vector that can silently leak training data membership.

## A Causal Perspective for Enhancing Jailbreak Attack and Defense

- Introduces Causal Analyst, a framework combining Large Language Model (LLM) prompt encoding with Graph Neural Networks (GNNs) to map the causal pathways between human-readable prompt features and successful jailbreaks.
- Identifies specific features, such as "Positive Character" and "Number of Task Steps", as direct causal drivers of jailbreaks across seven tested LLMs.
- Demonstrates that these causal insights can be weaponised to boost attack success rates on public benchmarks (e.g., StrongReject), but also leveraged defensively to build a Guardrail Advisor that accurately extracts malicious intent from obfuscated queries.

Pan, L., Lu, Y., Liu, J., Tao, J., Feng, H., Xue, H., Chu, Z., Ren, K. "A Causal Perspective for Enhancing Jailbreak Attack and Defense." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/a-causal-perspective-for-enhancing-jailbreak-attack-and-defense/

## A Comprehensive Memory Safety Analysis of Bootloaders

- Presents the first systematic memory safety analysis of modern desktop and server bootloaders, identifying storage, network, and console inputs as the primary attack surfaces.
- Introduces a custom bootloader fuzzing framework that intercepts peripheral access at the source-code level to efficiently feed mutated inputs.
- Discovered 39 vulnerabilities (38 novel) across nine bootloaders, including 14 within the widely used GRUB, some of which could be exploited to bypass secure boot protections entirely.

Wang, J., Wang, M., Wang, Q., Langius, N., Shi, L., Abbasi, A., Holz, T. "A Comprehensive Memory Safety Analysis of Bootloaders." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/a-comprehensive-memory-safety-analysis-of-bootloaders/

## A Deep Dive into Function Inlining and its Security Implications for ML-based Binary Analysis

- Investigates the often-overlooked impact of function inlining on static binary features—such as instruction frequencies and control flow graphs—and its downstream effects on Machine Learning (ML) models used for binary reverse engineering.
- Dissects the LLVM compiler's cost model and identifies specific combinations of compiler options that trigger "extreme inlining," aggressively replacing call sites with callee bodies beyond standard optimization levels.
- Reveals through systematic evaluation of 20 ML models that extreme inlining can drastically alter model behaviour, providing a mechanism for adversaries to deliberately craft evasive binary variants that bypass both generative and discriminative analysis tools.

Abusabha, O., Uhm, J., Abuhmed, T., Koo, H. "A Deep Dive into Function Inlining and its Security Implications for ML-based Binary Analysis." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/a-deep-dive-into-function-inlining-and-its-security-implications-for-ml-based-binary-analysis/

## A Formal Approach to Multi-Layered Privileges for Enclaves

- Proposes PALANTÍR, a verifiable multi-layered privilege model for Trusted Execution Environments (TEEs) that allows feature extensions without compromising the principle of least privilege.
- Introduces a parent-children inter-enclave relationship, granting the parent specific execution and spatial controls over its children to facilitate secure feature provisioning.
- Formally verifies the security of the model using TAP∞, proving that the introduction of multi-layered privileges does not weaken the fundamental integrity, confidentiality, or secure measurement guarantees of the underlying enclave architecture.

Yang, G., Liu, C., Huang, Z., Chen, G., Fu, H., Zhang, Y., Zhu, H. "A Formal Approach to Multi-Layered Privileges for Enclaves." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/a-formal-approach-to-multi-layered-privileges-for-enclaves/

## A Hard-Label Black-Box Evasion Attack against ML-based Malicious Traffic Detection Systems

- Introduces NetMasquerade, a protocol- and task-agnostic evasion attack against ML-based traffic detection systems that requires only binary (blocked or allowed) feedback from the target.
- Develops Traffic-BERT, a pre-trained model utilizing a network-specific tokenizer and attention mechanism to capture the complex statistical distributions of benign internet traffic.
- Employs deep reinforcement learning to manipulate malicious packet sequences based on Traffic-BERT's patterns, successfully evading six state-of-the-art detection systems with over a 96% success rate while applying modifications in ten steps or fewer.

Liu, Z., Zhao, Y., Liu, Z., Li, Q., Fu, C., Zhou, G., Xu, K. "A Hard-Label Black-Box Evasion Attack against ML-based Malicious Traffic Detection Systems." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/a-hard-label-black-box-evasion-attack-against-ml-based-malicious-traffic-detection-systems/

## A Key-Driven Framework for Identity-Preserving Face Anonymization

- Proposes a framework that generates high-quality, anonymized virtual faces while retaining the ability to cryptographically recover the original identity for authorized authentication.
- Implements a head posture-preserving virtual face generation (HPVFG) module that uses a specific user key to project the original facial latent vector into an anonymized form, explicitly maintaining the original head pose and expression.
- Introduces a key-controllable virtual face authentication (KVFA) module that can extract the original identity directly from the anonymized image, eliminating the need to ever expose or process the original face image during the authentication phase.

Wang, M., Hua, G., Li, S., Feng, G. "A Key-Driven Framework for Identity-Preserving Face Anonymization." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/a-key-driven-framework-for-identity-preserving-face-anonymization/

## A Large-Scale Measurement Study of the PROXY Protocol and its Security Implications

- Conducts the first internet-wide measurement study of the HAProxy PROXY protocol (Layer 4 client IP forwarding) across the entire IPv4 space.
- Reveals that hundreds of thousands of hosts accept PROXY headers from arbitrary sources across HTTP, SMTP, and SSH, allowing adversaries to spoof their source IP addresses to backend infrastructure.
- Demonstrates that spoofed PROXY headers can bypass access controls on over 10,000 HTTP servers, granting unauthorized access to internal dashboards, home automation systems, and IoT monitoring platforms, as well as turning over 350 SMTP servers into open relays.

Pletinckx, S., Kruegel, C., Vigna, G. "A Large-Scale Measurement Study of the PROXY Protocol and its Security Implications." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/a-large-scale-measurement-study-of-the-proxy-protocol-and-its-security-implications/

## A Method to Facilitate Membership Inference Attacks in Deep Learning Models

- Demonstrates a severe code poisoning attack where an adversary provides malicious model-training code to a data holder, amplifying membership privacy leakage without requiring access to the training data or process.
- Shows that by manipulating the loss-value computation and model structure, the resulting poisoned model can leak the training set membership of over 99% of samples (at a 0.1% false positive rate) to a black-box adversary.
- Highlights that this massive privacy leakage incurs less than a 1% drop in model accuracy and remains completely undetectable by standard membership privacy auditing methods, which do not inspect the underlying training code.

Chen, Z., Pattabiraman, K. "A Method to Facilitate Membership Inference Attacks in Deep Learning Models." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/a-method-to-facilitate-membership-inference-attacks-in-deep-learning-models/
