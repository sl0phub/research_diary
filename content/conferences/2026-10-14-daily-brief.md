+++
title = "Conference Brief — 2026-10-14"
date = 2026-10-14T07:21:13Z
type = "conferences"
tags = ["ndss", "vulnerability-discovery", "fuzzing", "cloud"]
summary = "New work from NDSS 2026, including intent fuzzing, container desynchronization risks, and memory backdoor attacks on neural networks."
+++

## In brief

Today's batch of eight papers from NDSS features work on coverage-guided intent fuzzing for compiled Android applications, cross-shard transaction optimization in blockchains, and a backdoor attack ensuring exact data recovery from neural networks. We also review a study on cloud configuration challenges derived from Stack Overflow, universal adversarial perturbations in wireless communication, namespace-cgroup desynchronization risks in containers, a low-latency post-quantum TLS architecture, and proactive discovery of online scam sites using toxic search queries.

- Evaluates coverage-guided fuzzing on compiled, closed-source Android apps.
- MALintent identifies security vulnerabilities like memory-safety and privacy issues in Android Intent handlers.
- The framework introduces custom bug oracles and works across multiple Android versions.
- Ammar Askar, Fabian Fleischer, Christopher Kruegel, Giovanni Vigna and Taesoo Kim. "MALintent: Coverage Guided Intent Fuzzing Framework for Android." NDSS — https://www.ndss-symposium.org/ndss-paper/malintent-coverage-guided-intent-fuzzing-framework-for-android/

- Introduces a bandwidth-clustered shard formation mechanism to group blockchain miners with similar bandwidths to optimize mining rates.
- Integrates an asynchronous atomic commitment mechanism for cross-shard transactions to guarantee atomicity.
- Implemented and evaluated, showing throughput improvements of 186% over baseline sharding protocols when miner bandwidths range from 5Mbps to 60Mbps.
- Chunjiang Che, Songze Li, and Xuechao Wang. "Manifoldchain: Maximizing Blockchain Throughput via Bandwidth-Clustered Sharding." NDSS — https://www.ndss-symposium.org/ndss-paper/manifoldchain-maximizing-blockchain-throughput-via-bandwidth-clustered-sharding/

- Proposes a training-time backdoor attack in federated learning that forces neural networks to output precise training samples.
- Reconstructs specific target data samples by having infected models output data in response to an index trigger.
- Exceeds prior probabilistic attacks by guaranteeing exact data recovery and avoiding generated hallucinations.
- Eden Luzon, Guy Amit, Roy Weiss, Torsten Krauß, Alexandra Dmitrienko, and Yisroel Mirsky. "Memory Backdoor Attacks on Neural Networks." NDSS — https://www.ndss-symposium.org/ndss-paper/memory-backdoor-attacks-on-neural-networks/

- Analyzes roughly 251,900 security and privacy Stack Overflow posts from 2008 to 2024 to map cloud configuration challenges.
- Highlights persistent hurdles including missing context-aware tools and insufficient documentation.
- Notes that authentication and access control issues appear at nearly every stage of cloud integration and deployment.
- Sumair Ijaz Hashmi, Shafay Kashif, Lea Gröber, Katharina Krombholz, and Mobin Javed. "Mapping the Cloud: A Mixed-Methods Study of Cloud Security and Privacy Conﬁguration Challenges." NDSS — https://www.ndss-symposium.org/ndss-paper/mapping-the-cloud-a-mixed-methods-study-of-cloud-security-and-privacy-configuration-challenges/

- Demonstrates Magmaw, an attack methodology producing universal adversarial perturbations against multimodal signals in wireless channels.
- Addresses the gap in adversarial attacks by integrating the multi-modality of source data, domain constraints, and physical layer protocols.
- Evaluated against standard defenses to test its resilience.
- Jung-Woo Chang, Ke Sun, Nasimeh Heydaribeni, Seira Hidano, Xinyu Zhang, and Farinaz Koushanfar. "Magmaw: Modality-Agnostic Adversarial Attacks on Machine Learning-Based Wireless Communication Systems." NDSS — https://www.ndss-symposium.org/ndss-paper/magmaw-modality-agnostic-adversarial-attacks-on-machine-learning-based-wireless-communication-systems/

- Discovers namespace-cgroup desynchronization (NCD) risks caused by sharing namespaces across containers or the host.
- Explains that namespace sharing extends isolation boundaries beyond one instance, while cgroups protections remain localized.
- Highlights that resource controls managed by cgroups are lost when a container terminates, while the shared namespace persists.
- Zhi Li, Zhen Xu, Weijie Liu, XiaoFeng Wang, Hai Jin, and Zheli Liu. "Losing the Beat: Understanding and Mitigating Desynchronization Risks in Container Isolation." NDSS — https://www.ndss-symposium.org/ndss-paper/losing-the-beat-understanding-and-mitigating-desynchronization-risks-in-container-isolation/

- Proposes Looma, a post-quantum authentication framework moving heavy pre-computations off-path asynchronously to maintain low latency in cloud mutual TLS.
- Reduces post-quantum TLS handshake latency by up to 44% compared to a Dilithium-2 baseline when integrated into TLS 1.3.
- Mitigates the performance cost of transitioning from classical TLS to post-quantum cryptography.
- Xinshu Ma and Michio Honda. "Looma: A Low-Latency PQTLS Authentication Architecture for Cloud Applications." NDSS — https://www.ndss-symposium.org/ndss-paper/looma-a-low-latency-pqtls-authentication-architecture-for-cloud-applications/

- Presents LOKI, a system identifying search engine queries likely to surface scam websites, utilizing a keyword scoring model and feature distillation from search results.
- Leveraged a seed set of 1,663 known scams to discover 52,493 previously unreported scam domains in the wild.
- Demonstrated a 20.58-times improvement in discovery rates over heuristic and data-driven baselines across 10 scam categories.
- Pujan Paudel and Gianluca Stringhini. "LOKI: Proactively Discovering Online Scam Websites by Mining Toxic Search Queries." NDSS — https://www.ndss-symposium.org/ndss-paper/loki-proactively-discovering-online-scams-by-mining-toxic-search-queries/
