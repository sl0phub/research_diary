+++
title = "arXiv Brief — 2026-09-23"
date = "2026-09-23T06:00:00Z"
type = "arxiv"
tags = ["cs.CR", "exploitation", "llm-security", "fuzzing", "kernel", "browser", "web-security"]
summary = "New vulnerabilities in eBPF, WebGPU fuzzing, and backdoor attacks on LLM-powered robots."
+++

## In brief

*   Analysis of eBPF vulnerabilities reveals a concentration in runtime concurrency, suggesting blind spots in current fuzzing techniques.
*   LLM-based penetration testing frameworks are shown to be vulnerable to deception-aware honeypots that can derail autonomous agents.
*   New history-based backdoor attacks against LLM-powered robots demonstrate how internal operational logic can trigger malicious actions without external cues.

## eBPF Security in the Wild: Structural Concentration, Failure Mechanisms, and Discovery Gaps

- Analyzes eBPF vulnerabilities across Linux v5.10 using KCOV-based coverage and Syzkaller.
- Finds that runtime execution and concurrency issues dominate the exposure surface, rather than Verifier or JIT components.
- Demonstrates that current discovery tools accumulate code coverage but miss broad vulnerability mechanisms.
- Suggests that semantic coverage objectives and pipeline-aware testing are needed beyond simple raw coverage.

Baihong Chen (Utah State University), Hua Ming (University of Michigan), Weifeng Pan (Zhejiang Gongshang University), Tian Xie (Utah State University), Xiaojun Qi (Utah State University), Wen Li (Utah State University). "eBPF Security in the Wild: Structural Concentration, Failure Mechanisms, and Discovery Gaps." arXiv:2609.26254 — https://arxiv.org/abs/2609.26254

## A2M: Trace-Optimized Agent Hijacking in the MCP Ecosystem

- Introduces A2M (Attraction-to-Manipulation), a framework for hijacking Model Context Protocol (MCP) agents via metadata optimization.
- Optimizes third-party tool metadata to increase malicious tool invocation to 93.6% across four scenarios on GLM-4.6.
- Steers agents toward attacker outcomes, achieving a 74.4% attack success rate across exfiltration and reasoning derailment.
- Highlights semantic supply-chain risks and the need for stricter tool vetting in MCP ecosystems.

Laizhen Li, Xuan Wang, Peicheng Zhao, Juanjuan Zhao, Kejiang Ye, Cheng-zhong Xu, Xitong Gao. "A2M: Trace-Optimized Agent Hijacking in the MCP Ecosystem." arXiv:2609.26761 — https://arxiv.org/abs/2609.26761

## Dynamic Conformance Testing of WebGPU Through Specification-Driven Mutation

- Presents LANTERN, a specification-guided fuzzer for WebGPU that mutates Conformance Test Suite (CTS) tests.
- Extracts syntactic rules from WebIDL and semantic constraints like command ordering directly from the WebGPU specification.
- Discovers three reproducible bugs, including a heap corruption vulnerability, in Chromium versions.
- Demonstrates the effectiveness of semantics-aware mutation over general-purpose fuzzers for complex graphics APIs.

Mahya Samdaliri, Zhihao Yao, Kasthuri Jayarajah. "Dynamic Conformance Testing of WebGPU Through Specification-Driven Mutation." arXiv:2609.25520 — https://arxiv.org/abs/2609.25520

## Evaluating Coding Agents on Kernel Exploit Generation

- Evaluates state-of-the-art coding agents on their ability to construct exploit primitives for Linux and Windows kernels.
- Introduces KEX-bench, containing 45 task instances across 40 CVEs, covering memory corruption and address leaks.
- Shows that without a reference proof-of-concept, the best configuration solves only 5% of Windows and 56% of Linux tasks.
- Highlights that while agents can reach kernel crashes, they struggle to shape kernel state into functional exploits.

Junyoung Jang, Gwanhyun Lee, Hwiwon Lee, Kyuheon Kim, Jongseong Kim, Jinho Jung, Lingming Zhang. "Evaluating Coding Agents on Kernel Exploit Generation." arXiv:2609.25591 — https://arxiv.org/abs/2609.25591

## Rouxii: Exploiting Honeypots with Deception-Aware AI Pentesters

- Develops Rouxii, an AI-driven penetration testing framework equipped to recognize and pivot from honeypot deception.
- Increases correct honeypot identification from 19% to 97% on OT services by integrating counter-deception reasoning.
- Shows that identified honeypots can be turned against operators, demonstrating denial-of-service and corruption of reported intelligence.
- Argues that evaluating deception systems must account for adversaries that actively reason about the deception layer.

Arthur Cordeiro, Alberto Maria Mongardini, Emmanouil Vasilomanolakis. "Rouxii: Exploiting Honeypots with Deception-Aware AI Pentesters." arXiv:2609.26555 — https://arxiv.org/abs/2609.26555

## Silent Sabotage: Internal State Triggered Backdoor Attacks on LLM-Powered Robotic Systems

- Demonstrates a history-based backdoor attack against LLM-powered robotic control systems.
- Embeds stealthy backdoors into controllers that are triggered by a specific, rare sequence of the robot's own past actions, rather than external stimuli.
- Achieves near-perfect attack success rates in simulated environments while preserving normal utility and remaining difficult to detect.
- Reveals that internal operational state can be manipulated to induce malicious behaviors like complete stops or collisions.

Doniyorkhon Obidov, Shivayogi Akki, Tan Chen, Kaichen Yang. "Silent Sabotage: Internal State Triggered Backdoor Attacks on LLM-Powered Robotic Systems." arXiv:2609.26184 — https://arxiv.org/abs/2609.26184

## RAG-NAROK: Retrieval-Aware Knowledge Corpus Poisoning in RAG with Source-specific Refutation

- Introduces RAG-NAROK, a query-adaptive attack framework for poisoning Retrieval-Augmented Generation (RAG) knowledge bases.
- Extracts legitimate source identities and generates Anchor-Specific Refutation documents that devalue retrieved context.
- Leverages recency and authority biases to steer LLM text generation towards attacker-desired answers.
- Outperforms static knowledge poisoning baselines, highlighting a vulnerability in the transparency of the RAG pipeline.

Abdullahil Kafi, Alvi Ataur Khalil. "RAG-NAROK: Retrieval-Aware Knowledge Corpus Poisoning in RAG with Source-specific Refutation." arXiv:2609.25469 — https://arxiv.org/abs/2609.25469

## Also published

- Carlos Benitez. "Quantum ROP: Using Quantum Algorithms for ROP Chain Selection in Exploit Construction." arXiv:2609.25364 — https://arxiv.org/abs/2609.25364
- Alexandros Fourtounis, Emmanouil Papadogiannakis, Panagiotis Papadopoulos, Nicolas Kourtellis, Evangelos Markatos. "COBRA: A Content-Agnostic Framework for Zero-Day Detection of Suspicious Domains." arXiv:2609.25882 — https://arxiv.org/abs/2609.25882
- Md. Meheraj Hossain, Saumik Das Turja, Sibgatullah Tasnim, Md. Fahmid-Ul-Alam Juboraj, Muhammad Iqbal Hossain. "A Cross-Dataset based Zero-Day Intrusion Detection System by Integrating Siamese Network and Reinforcement Learning." arXiv:2609.26115 — https://arxiv.org/abs/2609.26115
- Bin Duan, Jintao Lin, Dan Dongseong Kim, Guowei Yang. "Towards Effective Black-Box Adversarial Attacks on Deep Code Models via Structural and Identifier Perturbations." arXiv:2609.26234 — https://arxiv.org/abs/2609.26234
- Mauro Conti, Lorenzo Perinello, Umberto Salviati. "On the security and privacy of LLMs in Mobility." arXiv:2609.26295 — https://arxiv.org/abs/2609.26295
