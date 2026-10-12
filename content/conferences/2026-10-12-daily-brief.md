+++
title = "Conference Brief — 2026-10-12"
date = 2026-10-12T06:00:00Z
type = "conferences"
tags = ["ndss", "vulnerability-discovery", "side-channel", "llm-security", "cryptography"]
summary = "New findings from NDSS include an evolutionary backdoor attack on CNNs, a side-channel attack on WiFi beamforming, vulnerabilities in multi-tool LLM agents, and database reconstruction from range queries."
+++

## In brief

- **ML Backdoors**: The LADDER attack formulates a multi-objective optimization problem in dual domains to insert robust backdoors into CNNs, achieving a high attack success rate in the low-frequency spectral region.
- **WiFi Side-Channels**: LeakyBeam exploits plaintext beamforming feedback in WiFi to accurately detect human occupancy at a distance.
- **Agent Vulnerabilities**: Cross-Tool Harvesting and Polluting (XTHP) reveals a novel class of control flow hijacking in LLM agents, successfully compromising real-world agent frameworks.
- **Database Reconstruction**: A new attack leverages multidimensional range queries to reconstruct databases efficiently, heavily reducing the mean squared error over previous approaches.

## LADDER: Multi-Objective Backdoor Attack via Evolutionary Algorithm

- This work proposes a multi-objective black-box backdoor attack in dual domains via an evolutionary algorithm, optimizing triggers without requiring prior knowledge about the victim model.
- The attack demonstrates effectiveness against convolutional neural networks, achieving an average Attack Success Rate (ASR) of 90.23% when utilizing a low-frequency trigger design.
- The low-frequency triggers outperform five other backdoor attacks and three LADDER variants in the low-frequency spectral region by 50.09% on average.

- Dazhuang Liu, Yanqi Qiao, Rui Wang, Kaitai Liang, Georgios Smaragdakis. "LADDER: Multi-Objective Backdoor Attack via Evolutionary Algorithm." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/ladder-multi-objective-backdoor-attack-via-evolutionary-algorithm/

## Lend Me Your Beam: Privacy Implications of Plaintext Beamforming Feedback in WiFi

- LeakyBeam is a novel side-channel occupancy detection attack that leverages plaintext Beamforming Feedback (BFI) packets from WiFi devices.
- The attack fuses dynamic components attributable to human motion across subcarriers to identify occupancy despite interference.
- Real-world evaluations show LeakyBeam attains an average accuracy of 89.7% across different environments, with a 82.7% true positive rate at 20 meters.

- Rui Xiao, Xiankai Chen, Yinghui He, Jun Han, Jinsong Han. "Lend Me Your Beam: Privacy Implications of Plaintext Beamforming Feedback in WiFi." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/lend-me-your-beam-privacy-implications-of-plaintext-beamforming-feedback-in-wifi/

## Les Dissonances: Cross-Tool Harvesting and Polluting in Pool-of-Tools Empowered LLM Agents

- The authors identify Cross-Tool Harvesting and Polluting (XTHP), a novel vulnerability where adversarial tools hijack the control flow of LLM agents by semantic or syntax format hooking.
- XTHP enables cross-tool data harvesting to exfiltrate sensitive data and cross-tool information polluting to influence subsequent tool behaviors within task workflows.
- An evaluation across 66 real-world tools from frameworks like LangChain and Llama-Index revealed that 75% are vulnerable to XTHP attacks.

- Zichuan Li, Jian Cui, Xiaojing Liao, Luyi Xing. "Les Dissonances: Cross-Tool Harvesting and Polluting in Pool-of-Tools Empowered LLM Agents." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/les-dissonances-cross-tool-harvesting-and-polluting-in-pool-of-tools-empowered-llm-agents/

## Learning from Leakage: Database Reconstruction from Just a Few Multidimensional Range Queries

- The paper introduces a highly efficient database reconstruction attack against Searchable Encryption (SE) that operates from multidimensional range queries.
- The method uses a co-occurrence-based dimensionality reduction pipeline using t-SNE to preserve local spatial relationships without needing access to all possible responses.
- The attack reduces the mean squared error by up to 50% compared to state-of-the-art baselines, and requires only 1% uniform query coverage to achieve stable reconstruction with over 72% neighbor accuracy.

- Peijie Li, Huanhuan Chen, Evangelia Anna Markatou, Kaitai Liang. "Learning from Leakage: Database Reconstruction from Just a Few Multidimensional Range Queries." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/learning-from-leakage-database-reconstruction-from-just-a-few-multidimensional-range-queries/

## Also published

- Mahdi Rahimi, Piyush Kumar Sharma, Claudia Diaz. "LAMP: Lightweight Approaches for Latency Minimization in Mixnets with Practical Deployment Considerations." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/lamp-lightweight-approaches-for-latency-minimization-in-mixnets-with-practical-deployment-considerations/
- Feng Luo, Zihao Li, Wenxuan Luo, Zheyuan He, Xiapu Luo, Zuchao Ma, Shuwei Song, Ting Chen. "Light into Darkness: Demystifying Profit Strategies Throughout the MEV Bot Lifecycle." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/light-into-darkness-demystifying-profit-strategies-throughout-the-mev-bot-lifecycle/
