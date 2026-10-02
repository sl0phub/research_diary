+++
title = "arXiv Brief — 2026-10-02"
date = 2026-10-02T06:00:00Z
type = "arxiv"
tags = ["cs.CR", "llm-security", "vulnerability-discovery", "hardware"]
summary = "New frameworks for testing multimodal synergy, bounding execution claims with receipts, and identity-bound governance mechanisms for agents."
+++

## In brief

- Execution trust surfaces in multiple layers, from receipt-bound LLM tool usage to cryptographic proof blocks for governing agent halts.
- Synergistic generation risks exploit multimodal alignment, showing that safe unimodal behavior does not guarantee safe coordinated output.
- Structural techniques to limit data leakage include tokenized adapter routing for LLMs and representation alignment for transferring RL policies across cyber environments.

## UnifiedAttack: Evaluating the Safety of Large Multimodal Models in Synergistic Harmful Image-Text Generation

- Identifies "synergistic risks" in large multimodal models (LMMs) where coordinated text and image outputs amplify harm beyond isolated unimodal attacks.
- Proposes a synergistic hijacking framework using In-Context Reskinning (wrapping intent in benign virtual shells) and Cognitive Planning Injection (forcing a plan-then-execute path) to exploit the model's drive for logical consistency.
- Evaluation across five models (e.g., Gemini 2.5, GPT-4o, BAGEL) shows the attack increases the synergistic attack success rate on GPT-4.1 from 24.65% to 66.26% and on Gemini-2.0 from 24.20% to 89.90%.

Luo, B., Guo, J., Wang, T., Li, S. "UnifiedAttack: Evaluating the Safety of Large Multimodal Models in Synergistic Harmful Image-Text Generation." arXiv, 2026.
arXiv:2610.00341 — https://arxiv.org/abs/2610.00341

## Actions with Receipts: Jointly Binding Claims, Evidence, and Execution for Replayable Tool-Agent Auditing

- Introduces a claim-anchored execution contract that deterministically binds an LLM agent's emitted claim to its exact source span, ordered execution prefix, and observed source version.
- Separates structural integrity verification from semantic entailment evaluation, ensuring valid citations cannot be transplanted across different claims or runs undetected.
- Across 1,280 cross-object substitution attacks, the joint contract successfully detects 1,275 tampering attempts (0.9961 rate).

Hu, M., Hu, S., Guo, X., Wang, X., Wang, B., Sa, Y., Zha, D., Xiao, J. "Actions with Receipts: Jointly Binding Claims, Evidence, and Execution for Replayable Tool-Agent Auditing." arXiv, 2026.
arXiv:2610.00327 — https://arxiv.org/abs/2610.00327

## Tokenized Key-Gated Adapter Routing: A Secure Access Control Mechanism Against Private Data Leakage in LLMs

- Locket embeds policy-driven access control directly into generation using sequence-level hard routing, mapping a specific input token to a corresponding LoRA adapter.
- Authorized requests carrying the correct token are routed to a revealing adapter, while unauthorized requests trigger a privacy-preserving adapter that redacts PII or applies differential privacy.
- Evaluated on Llama-3.2-1B, unauthorized access drops membership inference AUC from 0.689 to 0.503 (with a DP adapter), while the gating module achieves 100% adapter-selection accuracy across all key conditions.

Shaaban, M., Elmahallawy, M. "Tokenized Key-Gated Adapter Routing: A Secure Access Control Mechanism Against Private Data Leakage in LLMs." arXiv, 2026.
arXiv:2610.00309 — https://arxiv.org/abs/2610.00309

## Intrusion Detection for Agentic Processes: Evidence-Based Runtime Monitoring

- Proposes an evidence-aware security interpretation layer (A-IDS) that monitors agentic processes by comparing observations against a governed expectation baseline for workflow state and authorization.
- Emphasizes that process deviations must be supported by bounded evidence claims, explicitly representing unresolved states rather than inferring malicious intent from anomalies.
- Identifies adversarial observation content (e.g., prompt injection) as a distinct monitoring-plane attack surface that can manipulate semantic evidence producers.

Brömme, A. "Intrusion Detection for Agentic Processes: Evidence-Based Runtime Monitoring." arXiv, 2026.
arXiv:2610.00151 — https://arxiv.org/abs/2610.00151

## Evasion Attacks: How Adversarial Noise Bypasses ML Classifiers

- Evaluates evasion attacks across modalities, demonstrating that adversarial vulnerability is strongly modality-dependent.
- In image classification (MNIST), a PGD attack reduces a compact convolutional network's accuracy from 98.63% to 32.47% at ε = 0.15.
- In text classification (SMS Spam Collection), controlled perturbations against a DistilBERT model produce modest probability shifts but fail to flip predictions from spam to ham.

Hummel, P., Skabo, R., Abusaqer, M. "Evasion Attacks: How Adversarial Noise Bypasses ML Classifiers." arXiv, 2026.
arXiv:2610.00136 — https://arxiv.org/abs/2610.00136

## Identity-Bound Governance Under Execution Uncertainty: An Accountability Proof Block for LLM Agent Persistent Halts, with Cryptographic Implementation and Cross-Model Calibration

- Introduces the Accountability Proof Block (APB), a mechanism binding system-constructed evidence of a persistent agent halt to a human decision block using an ed25519 signature.
- Provides a formal non-repudiability guarantee, ensuring the system cannot forge the signature and the principal cannot alter the evidence undetected, implemented using the RFC 8785 JSON Canonicalization Scheme.
- Evaluated over 3,812 halt events with zero unresolved cases, detecting 100% of 1,800 tampering attacks across nine adversarial vectors.

Fernandez, M. "Identity-Bound Governance Under Execution Uncertainty: An Accountability Proof Block for LLM Agent Persistent Halts, with Cryptographic Implementation and Cross-Model Calibration." arXiv, 2026.
arXiv:2610.00787 — https://arxiv.org/abs/2610.00787

## Made to Measure: Designing Image Watermarks to Specification

- Introduces TAILOR, a request-conditioned framework that jointly optimizes the selection, embedding order, and strengths of complementary watermark fragments (e.g., VINE, TrustMark, VideoSeal).
- Uses an SMT-based solver over offline characterization curves followed by live calibration to satisfy specific robustness, false-positive rate, image quality, and latency constraints.
- Across 7,321 distinct requests and 20 attack settings, TAILOR achieves 96.21% request satisfaction with a mean PSNR of 41.02 dB.

Li, M., Peng, Y., Xia, K., Jeyakumar, P., Famularo, R. L., Ma, S. "Made to Measure: Designing Image Watermarks to Specification." arXiv, 2026.
arXiv:2610.00780 — https://arxiv.org/abs/2610.00780

## Crossing the Cyber Divide: Sim-to-Sim and Sim-to-Real Transfer for RL Agents

- Casts cross-simulator and sim-to-real transfer for offensive cyber policies as a representation alignment problem, separating state understanding from action translation.
- Uses a domain-adversarial (DAPN) encoder to map structurally mismatched observations (e.g., from CyberWheel and NetSecGame) into a shared latent space.
- Zero-shot transfer with DAPN achieves a 45.2% win rate on NetSecGame using a source policy whose native performance is 60.5%, overcoming the total failure of feature-engineering alone on mismatched schemas.

Saika, S., Du, Y., Piplai, A. "Crossing the Cyber Divide: Sim-to-Sim and Sim-to-Real Transfer for RL Agents." arXiv, 2026.
arXiv:2610.00759 — https://arxiv.org/abs/2610.00759

## Also published

- Liu, S. et al. "Do Defenses Against LLM Extraction Work Across Attacks? A Lifecycle Benchmark of Black-Box Model Extraction." arXiv:2610.00839 — https://arxiv.org/abs/2610.00839
- Li, N., Harris, I. G. "SafeDepth: Safety-Aware Token-Level Adaptive Computation." arXiv:2610.00815 — https://arxiv.org/abs/2610.00815
- Wang, D. et al. "AuraForge: Scaling Security Supervision for Training Coding Agents." arXiv:2610.00850 — https://arxiv.org/abs/2610.00850
