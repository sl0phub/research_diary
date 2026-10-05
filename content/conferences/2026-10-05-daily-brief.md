+++
title = "Conference Brief — 2026-10-05"
date = 2026-10-05T06:00:00Z
type = "conferences"
tags = ["mitigations", "reverse-engineering", "llm-security", "firmware", "ndss"]
summary = "A new fast pointer nullification defense against UAF, resolving decompilation distortions with FidelityGPT, FirmAgent applying fuzzing to assist LLM vulnerability discovery, and FirmCross analyzing C-Lua hybrid firmware."
+++

## In brief

- Memory safety mitigation focuses on optimizing use-after-free prevention by moving metadata organization to the region level.
- Firmware security improvements tackle hybrid environments directly, with new techniques addressing C-Lua cross-language flows and combining fuzzing with LLM agents.

- Existing Pointer Nullification (PN) techniques for mitigating Use-After-Free (UAF) vulnerabilities incur high performance overhead and excessive memory usage due to metadata lookups for each pointer.
- Fast Pointer Nullification (FPN) organizes metadata at the region level to eliminate costly search operations and uses block-based registration to efficiently capture pointer locality.
- Evaluated on SPEC CPU benchmarks and real-world applications, FPN provides strong security guarantees while significantly reducing performance and memory overhead compared to prior PN techniques.
- Yubo Du (University of Pittsburgh), Youtao Zhang (University of Pittsburgh), Jun Yang (University of Pittsburgh). "Fast Pointer Nullification for Use-After-Free Prevention." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/fast-pointer-nullification-for-use-after-free-prevention/

- Decompilation processes often suffer from fidelity issues, producing output with impaired readability and accuracy that existing tools fail to fully correct.
- FidelityGPT is a novel framework that improves decompiled code accuracy by systematically detecting and correcting discrepancies using Retrieval-Augmented Generation (RAG) and a dynamic semantic intensity algorithm.
- A variable dependency algorithm is designed to overcome long-context limitations, and evaluation shows the framework successfully mitigates semantic drift.
- Zhiping Zhou (Tianjin University), Xiaohong Li (Tianjin University), Ruitao Feng (Southern Cross University), Yao Zhang (Tianjin University), Yuekang Li (University of New South Wales), Wenbu Feng (Tianjin University), Yunqian Wang (Tianjin University), Yuqing Li (Tianjin University). "FidelityGPT: Correcting Decompilation Distortions with Retrieval Augmented Generation." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/fidelitygpt-correcting-decompilation-distortions-with-retrieval-augmented-generation/

- Static analysis for vulnerability discovery in IoT firmware often yields high false positives, while dynamic analysis like fuzzing suffers from high false negatives.
- FirmAgent is a hybrid solution that uses fuzzing to collect runtime input points and reconstruct potential vulnerability paths, then applies an LLM agent for context-aware taint analysis.
- Evaluated on 14 real-world IoT firmware images, FirmAgent identified 182 vulnerabilities with a precision of 91%, including 140 zero-days (17 assigned CVEs).
- Jiangan Ji (Information Engineering University,Tsinghua University), Chao Zhang (Tsinghua University), Shuitao Gan (Labortory for Advanced Computing and Intelligence Engineering), Lin Jian (Information Engineering University), Hangtian Liu (Information Engineering University), Tieming Liu (Information Engineering University), Lei Zheng (Tsinghua university), Zhipeng Jia (Information Engineering University). "FirmAgent: Leveraging Fuzzing to Assist LLM Agents with IoT Firmware Vulnerability Discovery." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/firmagent-leveraging-fuzzing-to-assist-llm-agents-with-iot-firmware-vulnerability-discovery/

- Modern firmware increasingly combines Lua scripts and C binaries for web services, making traditional C-binary-oriented static taint analysis techniques inadequate.
- FirmCross is an automated taint-style vulnerability detector that deobfuscates Lua bytecode, identifies Lua-specific taint sources, and captures C-Lua cross-language taint flows.
- In an evaluation across 73 firmware images from 11 vendors, FirmCross detected up to 14.5X more vulnerabilities than state-of-the-art approaches, identifying 610 zero-days.
- Runhao Liu (National University of Defense Technology), Jiarun Dai (Fudan University), Haoyu Xiao (Fudan University), Yuan Zhang (Fudan University), Yeqi Mou (National University of Defense Technology), Lukai Xu (National University of Defense Technology), Bo Yu (National University of Defense Technology), Baosheng Wang (National University of Defense Technology), Min Yang (Fudan University). "FirmCross: Detecting Taint-style Vulnerabilities in Modern C-Lua Hybrid Web Services of Linux-based Firmware." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/firmcross-detecting-taint-style-vulnerabilities-in-modern-c-lua-hybrid-web-services-of-linux-based-firmware/
