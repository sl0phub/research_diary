+++
title = "Conference Brief — 2026-09-26"
date = 2026-09-26T06:00:00Z
type = "conferences"
tags = ["llm-security", "fuzzing", "memory-safety", "ndss"]
summary = "A batch of new research from NDSS exploring pitfalls in LLM security evaluations, automated insider threat simulation, distributed SNARKs, and more."
+++

## In brief

- Several papers highlight the fragility of current machine learning security evaluations, showing that LLM security benchmarks are often flawed and backdoor detection mechanisms struggle with dynamic triggers.
- Other work advances system design, offering performant distributed SNARK architectures and new collaborative frameworks for network intrusion detection.

## Chasing Shadows: Pitfalls in LLM Security Research

- Identifies 9 common experimental pitfalls in LLM security research spanning data collection, pre-training, fine-tuning, prompting, and evaluation.
- Evaluates 72 peer-reviewed papers from leading security venues (2023-2024) and finds that every single paper contains at least one pitfall, while only 15.7% explicitly acknowledge them.
- Demonstrates through four case studies how specific flaws, such as evaluating on synthetic data or ignoring context truncation, can artificially inflate model performance or completely invalidate reproducibility.

Evertz, J. et al. "Chasing Shadows: Pitfalls in LLM Security Research." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/chasing-shadows-pitfalls-in-llm-security-research/

## Chimera: Harnessing Multi-Agent LLMs for Automatic Insider Threat Simulation

- Introduces an LLM-based multi-agent framework to simulate both benign and malicious insider activities across enterprise environments to generate realistic system logs.
- Constructs ChimeraLog, a new dataset based on 15 abstracted insider attack types, resolving the lack of accessible, high-quality, and semantically rich training data for insider threat detection (ITD).
- Benchmarking existing ITD methods on ChimeraLog yields substantially lower detection rates compared to prior datasets, confirming it as a more rigorous and realistic evaluation target.

Yu, J. et al. "Chimera: Harnessing Multi-Agent LLMs for Automatic Insider Threat Simulation." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/chimera-harnessing-multi-agent-llms-for-automatic-insider-threat-simulation/

## Cirrus: Performant and Accountable Distributed SNARK

- *Abstract only — full text not retrieved.*

Wang, W. et al. "Cirrus: Performant and Accountable Distributed SNARK." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/cirrus-performant-and-accountable-distributed-snark/

## CLIBE: Detecting Dynamic Backdoors in Transformer-based NLP Models

- Injects a "few-shot perturbation" into suspect Transformer models, optimizing weight perturbation in attention layers to classify limited reference samples as a target label.
- Leverages the generalization of this perturbation to determine whether the original model contains a dynamic backdoor.
- Scrutinizes 49 popular Transformer models on Hugging Face, discovering one model exhibiting a high probability of containing a dynamic backdoor.

Zeng, R. et al. "CLIBE: Detecting Dynamic Backdoors in Transformer-based NLP Models." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/clibe-detecting-dynamic-backdoors-in-transformer-based-nlp-models/

## CoLD: Collaborative Label Denoising Framework for Network Intrusion Detection

- Attributes performance degradation in network intrusion detection to the local consistency of features across categories in network traffic when learning from noisy labels.
- Partitions the feature set and employs Local Joint Learning to disrupt local consistency, compelling the encoder to learn fine-grained and robust representations.
- Applies Causal Collaborative Denoising to filter noisy labels by analyzing causal divergences between representations, yielding a purified dataset for training.

Yang, S. et al. "CoLD: Collaborative Label Denoising Framework for Network Intrusion Detection." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/cold-collaborative-label-denoising-framework-for-network-intrusion-detection/

## Compiled Models, Built-In Exploits: Uncovering Pervasive Bit-Flip Attack Surfaces in DNN Executables

- Reveals that bit-flip attacks on DNN executables can exploit model structures stored in the executable code, circumventing the need to know confidential model weights.
- Shows that structure-based attacks are transferable and severe, enabling single-bit flips to successfully manipulate the model and slip past existing defenses.
- Assumes a weak attacker without knowledge of victim weights, demonstrating automated identification of vulnerable bits in victim executables.

Chen, Y. et al. "Compiled Models, Built-In Exploits: Uncovering Pervasive Bit-Flip Attack Surfaces in DNN Executables." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/compiled-models-built-in-exploits-uncovering-pervasive-bit-flip-attack-surfaces-in-dnn-executables/

## Connecting the Dots: An Investigative Study on Linking Private User Data Across Messaging Apps

- Demonstrates concrete attacks exploiting contact discovery, SSO-based account linking, and nearby user search across messaging apps like KakaoTalk, Telegram, and WhatsApp.
- Chains these attacks to conduct a cross-platform linking attack that deanonymizes user names and infers physical locations with an average error margin of 324 meters.
- Highlights that permissive contact discovery policies allow phone numbers and profile images to be used as linking keys across platforms.

Kang, J. et al. "Connecting the Dots: An Investigative Study on Linking Private User Data Across Messaging Apps." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/connecting-the-dots-an-investigative-study-on-linking-private-user-data-across-messaging-apps/

## Consensus in the Known Participation Model with Byzantine Failures and Sleepy Replicas

- Explores consensus protocols in a known participation model where the minimum number of awake honest replicas is known.
- Distinguishes from the sleepy model with recovery (which matches the crash-recovery model) by focusing on unknown participation of sleepy replicas alongside Byzantine failures.
- Shows that protocols tolerating both Byzantine failures and sleepy replicas in the known participation model provide independent properties from asynchronous network models.

Wang, C. et al. "Consensus in the Known Participation Model with Byzantine Failures and Sleepy Replicas." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/consensus-in-the-known-participation-model-with-byzantine-faults-and-sleepy-replicas/
