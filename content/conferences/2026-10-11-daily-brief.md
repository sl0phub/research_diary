+++
title = "Conference Brief — 2026-10-11"
date = 2026-10-11T00:00:00Z
type = "conferences"
tags = ["ndss", "kernel", "side-channel", "mobile", "cryptography"]
summary = "New findings from NDSS include side-channel attacks on kernel data structures, a smartwatch continuous authentication system, and an optimized sharding blockchain consensus."
+++

## In brief
- **Kernel-level attacks**: KernelSnitch highlights how unprivileged attackers can exploit variable-size kernel data structures like hash tables and trees to leak sensitive information via side-channel timing differences.
- **Wearable authentication**: Researchers introduced a smartwatch continuous authentication system utilizing low-frequency multi-channel PPG signals, showing practicality through significant power consumption reductions while retaining high accuracy.
- **Blockchain efficiency**: A new generic sharding blockchain consensus pattern, Kronos, was proposed to achieve scaling and optimized overhead, showcasing substantial improvements in throughput and latency.
## KernelSnitch: Side Channel-Attacks on Kernel Data Structures
- The authors introduce KernelSnitch, a novel software side-channel attack targeting variable-size kernel data structures like hash tables and trees.
- By exploiting the timing differences caused by varying occupancy levels of these data structures, an unprivileged attacker can leak sensitive information.
- The paper demonstrates a website fingerprinting attack with an F1 score of 89.5% and a covert channel achieving a capacity of 580 kbit/s at an error rate of 2.8%.
- Lukas Maar, Jonas Juffinger, Thomas Steinbauer, Daniel Gruss, Stefan Mangard. "KernelSnitch: Side Channel-Attacks on Kernel Data Structures." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/kernelsnitch-side-channel-attacks-on-kernel-data-structures/
## Know Me by My Pulse: Toward Practical Continuous Authentication on Wearable Devices via Wrist-Worn PPG
- This work presents a continuous authentication system for smartwatches using low-frequency (25 Hz) multi-channel Photoplethysmography (PPG) signals to reduce power consumption.
- The system employs a Bi-LSTM model with an attention mechanism to extract features from short 4-second windows of PPG data.
- The real-world implementation achieved an 88.11% accuracy, a 0.48% False Acceptance Rate (FAR), and an 11.77% False Rejection Rate (FRR) while reducing sensor power consumption by 53% compared to a 512 Hz setup.
- Wei Shao, Zequan Liang, Ruoyu Zhang, Ruijie Fang, Ning Miao, Ehsan Kourkchi, Setareh Rafatirad, Houman Homayoun, Chongzhou Fang. "Know Me by My Pulse: Toward Practical Continuous Authentication on Wearable Devices via Wrist-Worn PPG." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/know-me-by-my-pulse-toward-practical-continuous-authentication-on-wearable-devices-via-wrist-worn-ppg/
## Kronos: A Secure and Generic Sharding Blockchain Consensus with Optimized Overhead
- The paper proposes Kronos, a secure sharding blockchain consensus pattern designed to optimize overhead for cross-shard transactions.
- Kronos utilizes a shared buffer managed by shard members to handle transactions, requiring no Byzantine fault tolerance (BFT) protocol execution for efficient rejection in happy paths.
- Experimental evaluations over up to 1000 AWS EC2 nodes demonstrated that Kronos can scale to thousands of nodes, achieving a peak throughput of 320.2 ktx/sec with a latency of 2.0 sec.
- Yizhong Liu, Andi Liu, Yuan Lu, Zhuocheng Pan, Yinuo Li, Jianwei Liu, Song Bian, Mauro Conti. "Kronos: A Secure and Generic Sharding Blockchain Consensus with Optimized Overhead." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/kronos-a-secure-and-generic-sharding-blockchain-consensus-with-optimized-overhead/
## Also published
- Ziteng Chen, Menghao Zhang, Jiahao Cao, Xuzheng Chen, Qiyang Peng, Shicheng Wang, Guanyu Li, Mingwei Xu. "Janus: Enabling Expressive and Efficient ACLs in High-speed RDMA Clouds." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/janus-enabling-expressive-and-efficient-acls-in-high-speed-rdma-clouds/
- Yue Xiao, Dhilung Kirat, Douglas Lee Schales, Jiyong Jang, Luyi Xing, Xiaojing Liao. "JBomAudit: Assessing the Landscape, Compliance, and Security Implications of Java SBOMs." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/jbomaudit-assessing-the-landscape-compliance-and-security-implications-of-java-sboms/
- Wei Xu, Hui Zhu, Yandong Zheng, Song Bian, Ning Sun, Hao Yuan, Dengguo Feng, Hui Li. "Kangaroo: A Private and Amortized Inference Framework over WAN for Large-Scale Decision Tree Evaluation." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/kangaroo-a-private-and-amortized-inference-framework-over-wan-for-large-scale-decision-tree-evaluation/
- Yuhan Meng, Shaofei Li, Jiaping Gui, Peng Jiang, Ding Li. "KnowHow: Automatically Applying High-Level CTI Knowledge for Interpretable and Accurate Provenance Analysis." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/knowhow-automatically-applying-high-level-cti-knowledge-for-interpretable-and-accurate-provenance-analysis/
- Taifeng Liu, Yang Liu, Zhuo Ma, Tong Yang, Xinjing Liu, Teng Li, Jianfeng Ma. "L-HAWK: A Controllable Physical Adversarial Patch Against a Long-Distance Target." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/l-hawk-a-controllable-physical-adversarial-patch-against-a-long-distance-target/
