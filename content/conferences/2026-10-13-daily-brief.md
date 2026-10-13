+++
title = "Conference Brief — 2026-10-13"
date = 2026-10-13T06:00:00Z
type = "conferences"
tags = ["exploitation", "vulnerability-discovery", "llm-security", "ndss"]
summary = "New approaches to bug bisection using LLMs, hardware IP piracy, and Windows file system link following protection."
+++

## In brief

- Applications of LLMs are a focal point, demonstrating both defensive capabilities in bug bisection and offensive capabilities in hardware IP piracy.
- A newly introduced lightweight defense mechanism for Windows targets Link Following attacks effectively with minimal overhead.

## LinkGuard: A Lightweight State-Aware Runtime Guard Against Link Following Attacks in Windows File System

- Link Following attacks in Windows exploit symbolic links to redirect file operations, a technique not fully addressed by existing mitigations due to poor compatibility or limited applicability.
- LinkGuard introduces a lightweight state-aware runtime guard targeting Windows systems.
- LinkGuard introduces an average of 1% overhead in microbenchmarks and 3.4% overhead in real-world application workloads, adding a negligible 5 ms latency on benign file operations.

- Bocheng Xiang, Yuan Zhang, Hao Huang, Fengyu Liu, Youkun Shi. "LinkGuard: A Lightweight State-Aware Runtime Guard Against Link Following Attacks in Windows File System." NDSS — https://www.ndss-symposium.org/ndss-paper/linkguard-a-lightweight-state-aware-runtime-guard-against-link-following-attacks-in-windows-file-system/

## LLMBisect: Breaking Barriers in Bug Bisection with A Comparative Analysis Pipeline

- Traditional bug bisection struggles when the bug-inducing commit does not modify the same functions as the patch or when heuristics fail to capture vulnerability logic.
- The proposed LLM-based multi-stage pipeline uses patch information and compares multiple candidate commits to identify the bug-inducing commit.
- This approach yields an accuracy improvement of 60% compared to a baseline LLM-based solution.

- Zheng Zhang, Haonan Li, Xingyu Li, Hang Zhang, Zhiyun Qian. "LLMBisect: Breaking Barriers in Bug Bisection with A Comparative Analysis Pipeline." NDSS — https://www.ndss-symposium.org/ndss-paper/llmbisect-breaking-barriers-in-bug-bisection-with-a-comparative-analysis-pipeline/

## LLMPirate: LLMs for Black-box Hardware IP Piracy

- The use of LLMs in hardware design introduces the risk of hardware IP piracy, where designs are rewritten to evade piracy detection tools.
- LLMPirate is an automated technique leveraging LLMs to generate pirated circuit designs that successfully evade detection from state-of-the-art tools.
- The generated pirated netlists incur an average gate count overhead of approximately 50%, showing evasion is feasible at a reasonable cost.

- Vasudev Gohil, Matthew DeLorenzo, Veera Vishwa Achuta Sai Venkat Nallam, Joey See, Jeyavijayan Rajendran. "LLMPirate: LLMs for Black-box Hardware IP Piracy." NDSS — https://www.ndss-symposium.org/ndss-paper/llmpirate-llms-for-black-box-hardware-ip-piracy/
