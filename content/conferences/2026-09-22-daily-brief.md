+++
title = "Conference Brief — 2026-09-22"
date = 2026-09-22T06:00:00Z
type = "conferences"
tags = ["ndss", "fuzzing", "protocol-analysis", "exploitation"]
summary = "New findings on diffusion model membership inference, distributed system fuzzing, LLM safety alignment limitations, BLE re-pairing flaws, and hypervisor cross-domain exploitation."
+++

## In brief

- Recent attacks emphasize vulnerabilities in large-scale machine learning systems, from extracting training membership in diffusion models to breaking safety alignment in language models during text generation.
- Traditional software systems also surface new vectors, with network messages serving as fuzzing feedback for distributed applications, undocumented flaws in BLE re-pairing logic, and guest-to-host memory reuse in hypervisors.

## Black-box Membership Inference Attacks against Fine-tuned Diffusion Models

- Diffusion models fine-tuned for downstream tasks present privacy leakage risks, as adversaries can infer whether specific images were used during the fine-tuning process.
- The framework proposes a scores-based membership inference attack operating in a stringent black-box access setting, meaning it does not require access to the model's parameters or gradients.
- It is capable of targeting conditional generator models, achieving a high Area Under the Curve (AUC) of 0.95 across distinct attack scenarios.

Pang, Y., Wang, T., University of Virginia. "Black-box Membership Inference Attacks against Fine-tuned Diffusion Models." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/black-box-membership-inference-attacks-against-fine-tuned-diffusion-models/

## Blackbox Fuzzing of Distributed Systems with Multi-Dimensional Inputs and Symmetry-Based Feedback Pruning

- DistFuzz is a feedback-guided blackbox fuzzing framework designed specifically for distributed systems, where traditional code coverage metrics are difficult to obtain or ineffective.
- The input space is defined by incorporating regular events and relative timing among events, rather than just systematically mutating faults, to accommodate the request-driven and timing-dependent nature of distributed software.
- It utilizes the sequences of network messages with symmetry-based pruning as program feedback, avoiding the need for code instrumentation, and found 52 real bugs in ten popular distributed systems.

Zou, Y., Bai, J.-J., Beihang University; Jiang, Z.-M., ETH Zurich; Zhao, M., Arizona State University; Zhou, D., Peking University. "Blackbox Fuzzing of Distributed Systems with Multi-Dimensional Inputs and Symmetry-Based Feedback Pruning." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/blackbox-fuzzing-of-distributed-systems-with-multi-dimensional-inputs-and-symmetry-based-feedback-pruning/

## Bleeding Pathways: Vanishing Discriminability in LLM Hidden States Fuels Jailbreak Attacks

- Current safety fine-tuning in Large Language Models (LLMs) often fails because the model's capacity to differentiate harmful from safe outputs deteriorates as generation progresses.
- This vanishing discriminability forces the model to make compliance judgments earlier in the generation process, restricting its ability to recognize developing harmful intent concealed within seemingly benign tasks.
- A proposed inherent defense framework, DEEPALIGN, applies contrastive hidden-state steering at the midpoint of response generation to amplify the separation between harmful and benign hidden states.

Zhang, Y. et al. "Bleeding Pathways: Vanishing Discriminability in LLM Hidden States Fuels Jailbreak Attacks." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/bleeding-pathways-vanishing-discriminability-in-llm-hidden-states-fuels-jailbreak-attacks/

## BLERP: BLE Re-Pairing Attacks and Defenses

- The Bluetooth Core Specification v6.1 permits paired devices to re-pair to negotiate a new security level, but this mechanism contains six design vulnerabilities, including unauthenticated re-pairing and security level downgrade.
- These flaws affect any standard-compliant BLE device that uses pairing, and can be exploited to perform impersonation and Machine-in-the-Middle (MitM) attacks with minimal or no user interaction.
- The attacks exploit the interplay between BLE pairing and session establishment, specifically abusing the Security Manager Protocol (SMP) security request message.

Sacchetti, T., Antonioli, D., EURECOM. "BLERP: BLE Re-Pairing Attacks and Defenses." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/blerp-ble-re-pairing-attacks-and-defenses/

## Breaking Isolation: A New Perspective on Hypervisor Exploitation via Cross-Domain Attacks

- Modern virtualization environments exhibit weak memory isolation, where guest memory is fully attacker-controlled yet accessible from the host, providing a reliable primitive for hypervisor exploitation.
- This approach bypasses traditional mitigation techniques like Address Space Layout Randomization (ASLR) that complicate the exploitation of memory safety vulnerabilities (e.g., pointer corruption) within the hypervisor itself.
- A developed system can identify cross-domain gadgets, match them with corrupted pointers, synthesize triggering inputs, and assemble complete exploit chains, demonstrated against vulnerabilities in QEMU and VirtualBox.

Pan, G. et al. "Breaking Isolation: A New Perspective on Hypervisor Exploitation via Cross-Domain Attacks." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/breaking-isolation-a-new-perspective-on-hypervisor-exploitation-via-cross-domain-attacks/
