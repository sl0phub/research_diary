+++
title = "Conference Brief — 2026-10-15"
date = 2026-10-15T00:00:00Z
type = "conferences"
tags = ["ndss", "hardware", "cryptography", "privacy"]
summary = "A daily conference brief covering 8 papers from NDSS."
+++

## In brief

- **Memory Band-Aid: A Principled Rowhammer Defense-in-Depth** introduces per-thread and per-bank rate limits for DRAM accesses.
- **MEVisor: High-Throughput MEV Discovery in DEXs with GPU Parallelism** compiles an MEV bot into a GPU application, searching for profit in parallel.
- **MIRAGE: Private, Mobility-based Routing for Censorship Evasion** uses a district-based routing scheme based on high-level mobility patterns.

## Memory Band-Aid: A Principled Rowhammer Defense-in-Depth

- Memory Band-Aid introduces per-thread and per-bank rate limits for DRAM accesses in the memory controller, ensuring that the minimum number of row activations for Rowhammer bit flips cannot be reached.
- Tested on 2 Intel and 2 AMD systems, a full implementation would have a low overhead of 0% to 9.4% on Phoronix macro-benchmarks.
- In a micro-benchmark to cause DRAM pressure, it causes a slowdown by a factor of 1 to 5.1.
- Carina Fiedler, Jonas Juffinger, Sudheendra Raghav Neela, Martin Heckel, Martin Schwarzl, Daniel Gruss. "Memory Band-Aid: A Principled Rowhammer Defense-in-Depth." NDSS — https://www.ndss-symposium.org/ndss-paper/memory-band-aid-a-principled-rowhammer-defense-in-depth/

## MEVisor: High-Throughput MEV Discovery in DEXs with GPU Parallelism

- MeVisor compiles an MEV bot into a GPU application and launches thousands of GPU threads to search for Maximal Extractable Value (MEV) profit in parallel.
- Evaluated on 3,941 real MEV cases from Ethereum, MeVisor achieves 3.3M-5.1M transactions per second, outperforming the CPU baseline by 100,000x.
- In a large-scale study of Q1 2025 data, MeVisor estimates MEV opportunities yielding at most $1.1 million in profit.
- Weimin Chen, Xiapu Luo. "MEVisor: High-Throughput MEV Discovery in DEXs with GPU Parallelism." NDSS — https://www.ndss-symposium.org/ndss-paper/mevisor-high-throughput-mev-discovery-in-dexs-with-gpu-parallelism/

## MIRAGE: Private, Mobility-based Routing for Censorship Evasion

- MIRAGE is a privacy-preserving mobility-based messaging system designed for censorship-resistant communication, using a district-based routing scheme that probabilistically forwards messages based on high-level mobility patterns.
- MIRAGE protects users’ mobility patterns with local differential privacy, ensuring participation does not reveal an individual’s location history.
- Evaluated using real-world pedestrian and taxi trajectories, MIRAGE reduces message overhead compared to epidemic routing and outperforms probabilistic flooding in delivery rate.
- Zachary Ratliff, Ruoxing (David) Yang, Avery Bai, Harel Berger, Micah Sherr, James Mickens. "MIRAGE: Private, Mobility-based Routing for Censorship Evasion." NDSS — https://www.ndss-symposium.org/ndss-paper/mirage-private-mobility-based-routing-for-censorship-evasion/

## Also published

- René Helmke, Elmar Padilla, Nils Aschenbruck. "Mens Sana In Corpore Sano: Sound Firmware Corpora for Vulnerability Research." NDSS — https://www.ndss-symposium.org/ndss-paper/mens-sana-in-corpore-sano-sound-firmware-corpora-for-vulnerability-research/
- Xiaoyun Xu, Shujian Yu, Zhuoran Liu, Stjepan Picek. "MIMIR: Masked Image Modeling for Mutual Information-based Adversarial Robustness." NDSS — https://www.ndss-symposium.org/ndss-paper/mimir-masked-image-modeling-for-mutual-information-based-adversarial-robustness/
- Binbin Tu, Boyudong Zhu, Yang Cao, Yu Chen. "MinBucket MPSI: Breaking the Max-Size Bottleneck in Multi-Party Private Set Intersection." NDSS — https://www.ndss-symposium.org/ndss-paper/minbucket-mpsi-breaking-the-max-size-bottleneck-in-multi-party-private-set-intersection/
- Shaoke Xi, Tianyi Fu, Kai Bu, Chunling Yang, Zhihua Chang, Wenzhi Chen, Zhou Ma, Chongjie Chen, Yongsheng Shen, Kui Ren. "MineShark: Cryptomining Traffic Detection at Scale." NDSS — https://www.ndss-symposium.org/ndss-paper/mineshark-cryptomining-traffic-detection-at-scale/
- Cheng Zhang, Yang Xu, Jianghao Tan, Jiajie An, Wenqiang Jin. "MingledPie: A Cluster Mingling Approach for Mitigating Preference Profiling in CFL." NDSS — https://www.ndss-symposium.org/ndss-paper/mingledpie-a-cluster-mingling-approach-for-mitigating-preference-profiling-in-cfl/
