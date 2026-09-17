+++
title = "Conference Brief — 2026-09-17"
date = 2026-09-17T06:00:00Z
type = "conferences"
tags = ["side-channel", "ndss"]
summary = "A systematic evaluation of cache side-channel attacks on modern Intel microarchitectures, introducing three new techniques using the cldemote instruction."
+++

## In brief

- Today's focus is on microarchitectural side channels, with a comprehensive evaluation of cache attacks on modern CPUs.
- The highlighted research demonstrates that the `cldemote` instruction, designed to move cache lines for performance, can be weaponised to construct new cache side-channel primitives with comparable or superior performance to existing methods.

## A Systematic Evaluation of Novel and Existing Cache Side Channels

- Introduces three novel cache side-channel primitives—Demote+Reload, Demote+Demote, and DemoteContention—that abuse the `cldemote` instruction on recent Intel microarchitectures (Sapphire Rapids and Emerald Rapids).
- Evaluates these new primitives alongside four existing attacks (Flush+Reload, Flush+Flush, Evict+Reload, Prime+Probe) across nine characteristics, including channel capacity, noise resilience, and temporal and spatial precision.
- Demonstrates that Demote+Reload offers significant advantages in specific scenarios, achieving a 64.3% higher channel capacity (15.48 Mbit/s) and a 60.7% smaller blind spot compared to the established Flush+Reload technique.
- Highlights that `cldemote` changes the cache state without causing eviction to main memory, allowing attackers to bypass certain detection mechanisms and construct stealthy channels.

Rauscher, F., Fiedler, C., Kogler, A., Gruss, D. "A Systematic Evaluation of Novel and Existing Cache Side Channels." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/a-systematic-evaluation-of-novel-and-existing-cache-side-channels/

## Also published

- Tang, K. F., Tu, C. W., Mak, S. L. A., Chau, S. Y. "A Multifaceted Study on the Use of TLS and Auto-detect in Email Ecosystems." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/a-multifaceted-study-on-the-use-of-tls-and-auto-detect-in-email-ecosystems/
- Lu, T., Zhang, B., Zhang, X., Ren, K. "A New PPML Paradigm for Quantized Models." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/a-new-ppml-paradigm-for-quantized-models/
- Zhang, L., Li, L., Si, X., Guo, Z., Wang, X., Yuan, K., Li, B. "A Unified Defense Framework Against Membership Inference in Federated Learning via Distillation and Contribution-Aware Aggregation." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/a-unified-defense-framework-against-membership-inference-in-federated-learning-via-distillation-and-contribution-aware-aggregation/
- Wang, Z., Xiang, T., Li, X., Yang, G., Chen, B., Jiang, Z., Wang, J., Ma, C., Deng, R. H. "Abuse Resistant Traceability with Minimal Trust for Encrypted Messaging Systems." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/abuse-resistant-traceability-with-minimal-trust-for-encrypted-messaging-systems/
- Guo, Q., He, Y. "Accurate Identification of the Vulnerability-Introducing Commit based on Differential Analysis of Patching Patterns." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/accurate-identification-of-the-vulnerability-introducing-commit-based-on-differential-analysis-of-patching-patterns/
- Li, E., Mallick, T., Rose, E., Robertson, W., Oprea, A., Nita-Rotaru, C. "ACE: A Security Architecture for LLM-Integrated App Systems." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/ace-a-security-architecture-for-llm-integrated-app-systems/
- Li, P., Mei, F., Wang, Y., Liu, Z., Xu, K., Shen, C., Wang, Q., Li, Q. "Achieving Interpretable DL-based Web Attack Detection through Malicious Payload Localization." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/achieving-interpretable-dl-based-web-attack-detection-through-malicious-payload-localization/
