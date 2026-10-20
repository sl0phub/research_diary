+++
title = "Conference Brief — 2026-10-20"
date = 2026-10-20T06:00:00Z
type = "conferences"
tags = ["ndss", "cs.CR"]
summary = "New papers from NDSS: abuse reporting for mixnets, latency optimization, ASLR protections, source IP spoofing detection, privacy-preserving community search, defending LLM phishing, rollback resilience in TEE consensus, and scalable BFT."
+++

## In brief
- **Privacy and Metadata Protection**: New work introduces Onion Franking for abuse reporting in mix-based messaging systems, and Optimix offers a solution for latency optimization in modern mixnets.
- **Microarchitectural Mitigations**: The Oreo system is proposed to protect ASLR against bypass attacks via side channels.
- **Scalable Consensus**: Pallas and Aegis provide rollback resilience in TEE-aided blockchain consensus, while Pando introduces a highly scalable BFT protocol based on committee sampling.


## Onion Franking: Abuse Reports for Mix-Based Private Messaging
- Introduces Onion Franking, a mechanism for abuse reporting in metadata-hiding messaging systems that rely on onion encryption or mixnets.
- Demonstrates that breaking with abstractions used in prior work (such as compactly committing authenticated encryption) and relying directly on underlying cryptographic tools enables savings in communication costs.
- Achieves over an order of magnitude reduction in computation overhead compared to the most efficient prior work applicable to onion encryption-based systems.
- Matthew Gregoire, Margaret Pierce, Saba Eskandarian. "Onion Franking: Abuse Reports for Mix-Based Private Messaging." NDSS — https://ndss-symposium.org/ndss-paper/onion-franking-abuse-reports-for-mix-based-private-messaging

## OptiMix: Scalable and Distributed Approaches for Latency Optimization in Modern Mixnets
- Presents OptiMix, an approach for latency optimization in modern mixnets that generalizes across cascade and stratified topologies.
- Evaluates routing strategies through simulations, finding that applying cover routing generation methods results in higher entropy and fewer fully compromised paths.
- Analyzes mixnode adversaries and measures latency and geographical data using datasets like Nym and RIPE.
- Mahdi Rahimi. "OptiMix: Scalable and Distributed Approaches for Latency Optimization in Modern Mixnets." NDSS — https://ndss-symposium.org/ndss-paper/optimix-scalable-and-distributed-approaches-for-latency-optimization-in-modern-mixnets

## Oreo: Protecting ASLR Against Microarchitectural Attacks
- Proposes Oreo, a defense against microarchitectural side channel attacks that bypass Address Space Layout Randomization (ASLR).
- Implements microarchitecture changes and evaluates them across various benchmarks to measure latency overheads and execution times.
- Observes latency overhead variations in LEBench ranging from -6.39% to +6.16% compared to insecure baselines.
- Shixin Song, Joseph Zhang, Mengjia Yan. "Oreo: Protecting ASLR Against Microarchitectural Attacks." NDSS — https://ndss-symposium.org/ndss-paper/oreo-protecting-aslr-against-microarchitectural-attacks

## OSAVRoute: Advancing Outbound Source Address Validation Deployment Detection with Non-Cooperative Measurement
- Develops OSAVRoute, a non-cooperative measurement system to accurately detect the deployment of Outbound Source Address Validation (OSAV).
- Demonstrates that OSAVRoute achieves an accuracy of 99.4% and assisted a nationwide ISP in correcting their OSAV misconfigurations.
- Measures 754 addresses across 510 /24 prefixes within the ISP network, finding that 10.3% of tested addresses lack OSAV deployment.
- Shuai Wang, Ruifeng Li, Li Chen, Dan Li, Lancheng Qin, Qian Cao. "OSAVRoute: Advancing Outbound Source Address Validation Deployment Detection with Non-Cooperative Measurement." NDSS — https://ndss-symposium.org/ndss-paper/osavroute-advancing-outbound-source-address-validation-deployment-detection-with-non-cooperative-measurement

## PACS: Privacy-Preserving Attribute-Driven Community Search over Attributed Graphs
- Addresses the problem of privacy-preserving attribute-driven community search over attributed graphs for data-driven applications.
- Proposes methods to find high-quality subgraphs meeting specific attribute requirements without compromising data privacy.
- Evaluates the approach by selecting attributes for communities and ensuring attribute coverage across community vertices.
- Fangyuan Sun, Yaxi Yang, Jia Yu, Jianying Zhou. "PACS: Privacy-Preserving Attribute-Driven Community Search over Attributed Graphs." NDSS — https://ndss-symposium.org/ndss-paper/pacs-privacy-preserving-attribute-driven-community-search-over-attributed-graphs

## Paladin: Defending LLM-enabled Phishing Emails with a New Trigger-Tag Paradigm
- Introduces Paladin, a defense against LLM-generated phishing emails that are free from spelling mistakes and use topic-specific content.
- Employs a trigger-tag paradigm, demonstrating over 85% phishing detection accuracy across three insertion strategies and four LoRA rank settings.
- Achieves a 5% improvement in detection accuracy and time over baseline methods in evaluated scenarios.
- Yan Pang, Wenlong Meng, Xiaojing Liao. "Paladin: Defending LLM-enabled Phishing Emails with a New Trigger-Tag Paradigm." NDSS — https://ndss-symposium.org/ndss-paper/paladin-defending-llm-enabled-phishing-emails-with-a-new-trigger-tag-paradigm

## Pallas and Aegis: Rollback Resilience in TEE-Aided Blockchain Consensus
- Presents Pallas and Aegis to provide rollback resilience in Trusted Execution Environment (TEE)-aided blockchain consensus protocols.
- Demonstrates through experimentation on real-world infrastructure that Pallas delivers high performance with negligible overhead in stable conditions.
- Outperforms state-of-the-art BFT consensus systems by up to 41% in throughput and 29% in latency overhead.
- Jérémie Decouchant, David Kozhaya. "Pallas and Aegis: Rollback Resilience in TEE-Aided Blockchain Consensus." NDSS — https://ndss-symposium.org/ndss-paper/pallas-and-aegis-rollback-resilience-in-tee-aided-blockchain-consensus

## Pando: Extremely Scalable BFT Based on Committee Sampling
- Develops Pando, a highly scalable Byzantine Fault-Tolerant (BFT) protocol based on committee sampling to handle large numbers of replicas.
- Shows that for the same desirable probability of safety and liveness violation, Pando uses a committee size an order of magnitude lower than existing works.
- Assesses CPU and bandwidth usage, illustrating why Pando outperforms existing protocols even with large committee sizes.
- Xin Wang, Haochen Wang, Haibin Zhang, Sisi Duan. "Pando: Extremely Scalable BFT Based on Committee Sampling." NDSS — https://ndss-symposium.org/ndss-paper/pando-extremely-scalable-bft-based-on-committee-sampling
