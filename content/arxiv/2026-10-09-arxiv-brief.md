+++
title = "arXiv Brief — 2026-10-09"
date = 2026-10-09T06:00:00Z
type = "arxiv"
tags = ["vulnerability-discovery", "supply-chain", "llm-security", "tooling"]
summary = "New papers on Common Criteria evaluation failures, LLM coding agent skills, and MoE router telemetry privacy."
+++

## In brief
- Studies systematizing failure modes highlight persistent gaps in Common Criteria evaluations.
- AI coding agents relying on unversioned skills face supply chain risks due to untracked copying.
- Router telemetry in Mixture-of-Experts models is shown to expose fine-tuning data to membership inference.

## SoK: Failure Modes in Common Criteria Product Evaluation - A Taxonomy and Design-for-Evaluability Guidance
- Presents a systematization of knowledge (SoK) of failure modes in Common Criteria product evaluation from the evaluator's operational vantage.
- Analyzes recurring failures into a lifecycle taxonomy spanning Security Target scoping, functional testing, and configuration drift.
- Derives a design-for-evaluability framework that product teams can apply before evaluation begins to mitigate recurring cross-vendor failures.
- Punit Suketu Patel. "SoK: Failure Modes in Common Criteria Product Evaluation - A Taxonomy and Design-for-Evaluability Guidance." arXiv — https://arxiv.org/abs/2610.10644

## DITTO: A Context-aware Pickle-based Pre-Trained Model Scanner for Effective Security Audits
- Introduces DITTO, a stack-based, context-aware scanner for Pickle-based pre-trained models that faithfully tracks virtual machine state transitions.
- Evaluates over 10,000 Hugging Face repositories, revealing that 9.3% still rely on the unsafe Pickle format.
- Achieves 100% scanning coverage, a 0% false-negative rate, and a 0.7% false-positive rate on a benchmark of 1,051 models, yielding an F1 score of 0.966.
- Qiaolin Qin, Wanpeng Li, Benoit Baudry, Lorenzo De Carli, Heng Li, Ettore Merlo. "DITTO: A Context-aware Pickle-based Pre-Trained Model Scanner for Effective Security Audits." arXiv — https://arxiv.org/abs/2610.10735

## A Security Meta-Model for Retrieval-Augmented Generation Systems
- Introduces a security meta-model that captures explicit causal relationships between Retrieval-Augmented Generation (RAG) surfaces, attacks, weaknesses, and risks.
- Provides a context-dependent filtering mechanism that identifies the subset of applicable risks given a specific RAG deployment configuration.
- Instantiates the meta-model as an interactive catalog populated with security threats and remediations from 43 publications to expose coverage gaps affecting output integrity.
- Steve Nouyep, S\\'ebastien Salva, Maxime Puys. "A Security Meta-Model for Retrieval-Augmented Generation Systems." arXiv — https://arxiv.org/abs/2610.11893

## HPQ-AKE: A Provably Secure Sign-Less Hybrid Authenticated Key Exchange Protocol for Bandwidth-Constrained IoT and Edge Networks
- Presents HPQ-AKE, a sign-less hybrid authenticated key exchange protocol for IoT gateways that replaces post-quantum transcript signatures with dual KEMs.
- Reduces modeled handshake transmission from 13,009 to 5,668 bytes, a 56.4% reduction relative to a Hybrid TLS 1.3 Full handshake.
- Lowers modeled latency by 31.4% on a simulated 50 kbps satellite-like link with 600 ms round-trip time.
- Khiem Pham-Tuan, Minh Quang Le, Khuong Nguyen-An. "HPQ-AKE: A Provably Secure Sign-Less Hybrid Authenticated Key Exchange Protocol for Bandwidth-Constrained IoT and Edge Networks." arXiv — https://arxiv.org/abs/2610.12024

## Skill Constellations: Tracing the Supply Chain of Agent Skills on GitHub
- Constructs the first dated copy network of agent skills from the git history of over 2.1 million skill adoptions across GitHub repositories.
- Fits a model of repository copying to rank repositories for audit, where reviewing the top 100 prevents 14.9% of later adoptions of high-risk skills, compared to 0.5% for the 100 most starred.
- Demonstrates that skill copies almost never change with their source, meaning security fixes at the source rarely reach copied versions.
- Fahd Seddik. "Skill Constellations: Tracing the Supply Chain of Agent Skills on GitHub." arXiv — https://arxiv.org/abs/2610.11169

## When Routing Reveals Membership: Privacy Leakage from MoE Router Telemetry
- Introduces a router-augmented membership inference attack that combines conventional output-side signals with aggregated routing features from Mixture-of-Experts (MoE) models.
- Shows that router telemetry improves membership inference over an output-signal ensemble, increasing true positive rate at 1% false positive rate by 2.7 to 9.4 percentage points across nine settings.
- Demonstrates that the leakage persists across full fine-tuning and frozen-router training, exposing membership information even when router parameters are frozen.
- Yixin Tan, Jiayang Liu, Lu Sun, Yuke Hu, Zheng Li, Rui Wen. "When Routing Reveals Membership: Privacy Leakage from MoE Router Telemetry." arXiv — https://arxiv.org/abs/2610.10616

## From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage
- Studies five LLM reasoning approaches for SOC alert triage using an interactive benchmark, finding every approach missed at least 40.4% of attack-related alerts.
- Proposes AIDA, a multi-agent framework requiring explicit proposed decisions before independent challenge and stronger evidentiary requirements prior to dismissal.
- Achieves an F1 score of 0.958, reducing the false-negative rate from 40.4% to 3.1% while escalating 18.4% of alerts to analysts.
- Saimon Amanuel Tsegai, Alex Kantchelian, Danfeng Yao, Peng Gao. "From Investigation Failures to Reliable SOC Agents: Understanding and Improving LLM-Based Alert Triage." arXiv — https://arxiv.org/abs/2610.10608

## Also published
- Ryan Swift. "CPU-Auth: Device Fingerprinting for Authentication via DVFS Side-Channel." arXiv — https://arxiv.org/abs/2610.10766
