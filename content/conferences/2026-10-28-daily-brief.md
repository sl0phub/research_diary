+++
title = "Conference Brief — 2026-10-28"
date = 2026-10-28T07:24:28Z
type = "conferences"
tags = ["ndss", "llm-security", "privacy", "protocol-analysis", "memory-safety"]
summary = "New papers on differential privacy for code generation, LLM tool selection attacks, and protocol compliance."
+++

## In brief

- Novel approaches to differential privacy in offline reinforcement learning and code generation.
- LLM agents continue to be targeted via prompt injection on their tool selection mechanisms.
- LLMs are also increasingly leveraged for formal verification of smart contracts and protocol compliance.

## PrivCode: When Code Generation Meets Differential Privacy

- Fine-tuning Large Language Models (LLMs) on private code repositories risks leaking sensitive or proprietary data.
- The authors propose PrivCode, a differentially private synthesizer for code datasets with strict syntactic dependencies.
- It employs a two-stage approach: "privacy-sanitizing" with DP-SGD that includes syntactic information, followed by "utility-boosting" where a pre-trained LLM is fine-tuned on the synthetic code to recover utility.
- Tested across four LLMs, the framework reportedly generates higher-utility code for various tasks under four benchmarks while maintaining privacy bounds.

Zheng Liu, Chen Gong, Terry Yue Zhuo, Kecen Li, Weichen Yu, Matt Fredrikson, Tianhao Wang. "PrivCode: When Code Generation Meets Differential Privacy." NDSS — https://www.ndss-symposium.org/ndss-paper/privcode-when-code-generation-meets-differential-privacy/

## Prompt Injection Attack to Tool Selection in LLM Agents

- LLM agents frequently use a retrieval-and-selection pipeline to choose appropriate tools for a given task.
- ToolHijacker is a prompt injection attack targeting this selection step in no-box scenarios.
- The attack injects a malicious document into the tool library designed to consistently compel the LLM agent to select the attacker's tool for a target task.
- The authors formulated the malicious document creation as an optimization problem, bypassing both prevention-based (StruQ, SecAlign) and detection-based defenses.

Jiawen Shi, Zenghui Yuan, Guiyao Tie, Pan Zhou, Neil Zhenqiang Gong, Lichao Sun. "Prompt Injection Attack to Tool Selection in LLM Agents." NDSS — https://www.ndss-symposium.org/ndss-paper/prompt-injection-attack-to-tool-selection-in-llm-agents/

## ProtocolGuard: Detecting Protocol Non-compliance Bugs via LLM-guided Static Analysis and Dynamic Verification

- Natural-language protocol specifications are ambiguous, often leading to non-compliance bugs in network implementations.
- ProtocolGuard combines LLM-guided static analysis with dynamic verification to identify these bugs.
- It extracts normative rules, performs program slicing, and detects semantic inconsistencies. It then automatically generates assertions and test cases for dynamic verification.
- Evaluated on 11 protocol implementations, the framework discovered 158 non-compliance bugs, 70 of which were confirmed.

Xiangpu Song, Longjia Pei, Jianliang Wu, Yingpei Zeng, Gaoshuo He, Chaoshun Zuo, Xiaofeng Liu, Qingchuan Zhao, Shanqing Guo. "ProtocolGuard: Detecting Protocol Non-compliance Bugs via LLM-guided Static Analysis and Dynamic Verification." NDSS — https://www.ndss-symposium.org/ndss-paper/protocolguard-detecting-protocol-non-compliance-bugs-via-llm-guided-static-analysis-and-dynamic-verification/

## Also published

- Chen Gong, Zheng Liu, Kecen Li, Tianhao Wang. "PrivORL: Differentially Private Synthetic Dataset for Offline Reinforcement Learning." NDSS — https://www.ndss-symposium.org/ndss-paper/privorl-differentially-private-synthetic-dataset-for-offline-reinforcement-learning/
- Ruyi Ding, Tong Zhou, Lili Su, Aidong Adam Ding, Xiaolin Xu, Yunsi Fei. "Probe-Me-Not: Protecting Pre-trained Encoders from Malicious Probing." NDSS — https://www.ndss-symposium.org/ndss-paper/probe-me-not-protecting-pre-trained-encoders-from-malicious-probing/
- Ye Liu, Yue Xue, Daoyuan Wu, Yuqiang Sun, Yi Li, Miaolei Shi, Yang Liu. "PropertyGPT: LLM-driven Formal Verification of Smart Contracts through Retrieval-Augmented Property Generation." NDSS — https://www.ndss-symposium.org/ndss-paper/propertygpt-llm-driven-formal-verification-of-smart-contracts-through-retrieval-augmented-property-generation/
- Derui Wang, Minhui Xue, Bo Li, Seyit Camtepe, Liming Zhu. "Provably Unlearnable Data Examples." NDSS — https://www.ndss-symposium.org/ndss-paper/provably-unlearnable-data-examples/
- Ziwen Liu, Jian Mao, Jun Zeng, Jiawei Li, Qixiao Lin, Jiahao Liu, Jianwei Zhuge, Zhenkai Liang. "ProvGuard: Detecting SDN Control Policy Manipulation via Contextual Semantics of Provenance Graphs." NDSS — https://www.ndss-symposium.org/ndss-paper/provguard-detecting-sdn-control-policy-manipulation-via-contextual-semantics-of-provenance-graphs/
