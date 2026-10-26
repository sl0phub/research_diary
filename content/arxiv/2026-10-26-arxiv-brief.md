+++
title = "arXiv Brief — 2026-10-26"
date = 2026-10-26T06:00:00Z
type = "arxiv"
tags = ["cs.CR", "protocol-analysis", "reverse-engineering", "llm-security"]
summary = "Automated protocol reverse engineering via tree-of-thought search, incomparable minima in tool authorization for agents, and decode-time provenance binding to stop MCP indirect injection."
+++

## In brief

- Protocol reverse engineering tools often fail on nested sub-protocols. SEMPRE solves this using an LLM-driven tree-of-thought search guided by taint-flow and loop traces, reaching an F1 score of 0.76 for field detection.
- When an agent is authorized to use a tool, deciding which grant is smaller is non-trivial. For roughly 30% of Microsoft Graph tasks and 3% of Google resource tasks, the minimal sufficient grants form an antichain, meaning no grant is a subset of another.
- Untrusted tool outputs can cause indirect prompt injections in MCP. Decode-time provenance binding stops this by enforcing trust labels based on layer-held lineage rather than agent-presented labels.

## SEMPRE: Semantic-Aware Protocol Reverse Engineering via Consistency-Driven Joint Optimization

- Protocol reverse engineering typically relies on hand-written rules that under-model contextual dependencies and fail on nested sub-protocols. SEMPRE replaces these heuristics with a recursive LLM reasoning process grounded in dynamic program analysis.
- It uses taint-flow and loop traces to guide an LLM-driven tree-of-thought search that slices messages into fields and detects nested sub-payloads. It iteratively refines boundaries by freezing high-confidence segments until structure and semantics converge.
- Evaluated against six baseline approaches on eight mainstream protocols, SEMPRE achieves an F1 score of 0.76 for field detection (over twice the prior best) and 0.72 for semantic inference.

- Yihua Xu, Weijie Huang, Xiaofeng Wang, Hang Zhang, Binghui Wang, Yue Duan. "SEMPRE: Semantic-Aware Protocol Reverse Engineering via Consistency-Driven Joint Optimization." arXiv — https://arxiv.org/abs/2610.31844

## Incomparable Minima in Agent Tool Authorization

- Over-privilege benchmarks assume one grant is clearly smaller than another. This paper tests that assumption against Microsoft Graph and Google API authorization tables.
- For 29.8-33.3% of Microsoft Graph tasks and 3.2% of Google resource tasks, the minimal sufficient authority forms an antichain: a set of grants where none authorizes a subset of what another does.
- In its two main authorization modes, Microsoft's shipped privilegeLevel rates 67.4-74.4% of these incomparable pairs equal. Google's reconstructed FORTIS privilege ladder rates 90.7-98.7% of them equal.
- Four risk measures (operations, writes, services reached, administrative surface) order up to 28.7% of incomparable Google pairs and 23.4% of Graph pairs in opposite directions, showing that for those pairs, the ranking has no measure-independent answer.

- Xin Xu. "Incomparable Minima in Agent Tool Authorization." arXiv — https://arxiv.org/abs/2610.31914

## Agentic AI Defense: Decode-Time Provenance Binding for MCP

- Agentic AI systems using the Model Context Protocol (MCP) are vulnerable to indirect prompt injection through untrusted tool outputs. An attacker can conceal instructions inside an image (via LSB, DCT, or metadata steganography) to bypass text scanners.
- The proposed defense uses decode-time provenance binding, combining HMAC-authenticated trust labels with an MCP-maintained provenance ledger and context-taint tracking. It blocks critical tool calls influenced by untrusted decoded content, resisting label substitution because trust is decided on layer-held lineage.
- On a real MCP testbed of three carriers and 24 adaptive payloads, the undefended pipeline leaks on 100% of attacks, and a keyword scanner and a regex parser leak on 62.5% each. The proposed mechanism reduces attack success to 0%.

- Eric Yocam, Varghese Vaidyan, Paris Kalathas, Patrick Tague, Bruce DeBruhl, Yong Wang. "Agentic AI Defense: Decode-Time Provenance Binding for MCP." arXiv — https://arxiv.org/abs/2610.31974

## Also published

- Utkarsh Kanwat. "Fooling LLM Safety Guards into Judging the Wrong Text." arXiv — https://arxiv.org/abs/2610.31695
- Junhao Wang, Yidou Chen, Li Lu, Hongwei Yao, Xiaodan Li, Mengjie Wu, Yuefeng Chen, Zhan Qin, Kui Ren. "Omni-UBench: Benchmarking Omni-Modal LLM-based Guardrails Across Safety, Utility, and Reliability." arXiv — https://arxiv.org/abs/2610.31713
- Khadijeh Bagheri, Hassan Khodaiemehr, Chen Feng. "SILMARILS-MV: Information-Theoretically Secure Multi-Verifier Signatures with Dealer-Free Key Issuance and Linear Aggregation for Permissioned Blockchains." arXiv — https://arxiv.org/abs/2610.31814
- Aditya Oke, Andr'e Vicente Duarte, Rui Melo, Shubham Gandhi, Nachiket Kotalwar, Charmi Khandor, Danqing Wang, Carolyn Ros'e, Lei Li. "Ulysses: A Security Harness For Synthesizing Verifiable Web Exploits." arXiv — https://arxiv.org/abs/2610.31831
- Tiffany Bao, Shangtao Li, Yifan Sun, Mengwen He, Bowei Li, Alden Wang, Changliu Liu, Ruoyu Wang, David Brumley. "Not an Accident: Exploiting Safety Filter Inadequacy in Humanoid Robots." arXiv — https://arxiv.org/abs/2610.31923
