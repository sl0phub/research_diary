+++
title = "Conference Brief — 2026-10-21"
date = 2026-10-21T06:00:00Z
type = "conferences"
tags = ["hardware", "cs.CR", "ndss"]
summary = "New findings at NDSS cover cross-modality IEMI attacks against LiDAR, split learning inference risks, and an uncertainty-aware adversarial defense for edge IoT devices."
+++

## In brief

- Defenses and attacks alike are adapting to constrained or distributed environments: PANDORA tailors adversarial network defense for edge IoT, while SDAR exposes inference vulnerabilities in split learning.
- The PhantomLiDAR attack expands the threat model for autonomous vehicle sensors by proving that electromagnetic interference can successfully manipulate LiDAR systems regardless of their optical security.

## PANDORA: Lightweight Adversarial Defense for Edge IoT using Uncertainty-Aware Metric Learning

- Introduces PANDORA (Probabilistic Adversarial Network Defense Over Resource-constrained Architectures), an end-to-end framework for detecting zero-day attacks on edge devices.
- It learns uncertainty-aware probabilistic embeddings for robust representations, introduces a Probabilistic Manifold Structuring and Distance (PMSD) Loss for zero-shot generalization, and uses an efficient Mamba-Mixture of Experts (MoE) architecture.
- In evaluations, PANDORA achieves an F1-score of 0.971 with 10-shot adaptation on CICIDS2017 and up to 99% accuracy in zero-shot detection under domain shift. When deployed on a Raspberry Pi, it maintains a low memory footprint of 24 MB and a throughput of up to 4.26 flows/sec.
- Avinash Awasthi, Pritam Vediya, Hemant Miranka, Ramesh Babu Battula, Manoj Singh Gaur. "PANDORA: Lightweight Adversarial Defense for Edge IoT using Uncertainty-Aware Metric Learning." NDSS — https://www.ndss-symposium.org/ndss-paper/pandora-lightweight-adversarial-defense-for-edge-iot-using-uncertainty-aware-metric-learning/

## Passive Inference Attacks on Split Learning via Adversarial Regularization

- Introduces SDAR, an attack framework against split learning with an honest-but-curious server, leveraging auxiliary data and adversarial regularization to learn a decodable simulator of the client's private model.
- The framework effectively infers the client's private features in vanilla split learning, and both features and labels under U-shaped split learning configurations.
- On CIFAR-10 at a deep split level of 7, SDAR achieves private feature reconstruction with less than 0.025 mean squared error in both vanilla and U-shaped settings, and attains a label inference accuracy of over 98% in the U-shaped setting.
- Xiaochen Zhu, Xinjian Luo, Yuncheng Wu, Yangfan Jiang, Xiaokui Xiao, Beng Chin Ooi. "Passive Inference Attacks on Split Learning via Adversarial Regularization." NDSS — https://www.ndss-symposium.org/ndss-paper/passive-inference-attacks-on-split-learning-via-adversarial-regularization/

## PhantomLiDAR: Cross-modality Signal Injection Attacks against LiDAR

- Proposes a cross-modality signal injection attack that uses intentional electromagnetic interference (IEMI) to manipulate LiDAR output, rather than exploiting laser signals directly.
- The attack exploits the finding that internal LiDAR modules, such as the laser receiving circuit, monitoring sensors, and beam-steering modules, can still couple with IEMI attack signals despite electromagnetic compatibility testing.
- The PhantomLiDAR attack manipulates output through Points Interference, Points Injection, Points Removal, and LiDAR Power-Off, demonstrated successfully on five COTS LiDAR systems in both simulated and real-world moving scenarios.
- Zizhi Jin, Qinhong Jiang, Xuancun Lu, Chen Yan, Xiaoyu Ji, Wenyuan Xu. "PhantomLiDAR: Cross-modality Signal Injection Attacks against LiDAR." NDSS — https://www.ndss-symposium.org/ndss-paper/phantomlidar-cross-modality-signal-injection-attacks-against-lidar/
