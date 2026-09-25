+++
title = "Conference Brief — 2026-09-25"
date = 2026-09-25T06:00:00Z
type = "conferences"
tags = ["network-security", "llm-security", "privacy", "ndss"]
summary = "Extracting website fingerprinting traces across positions, exploiting time synchronization in 802.11 for covert channels, breaking LLM watermarks with character perturbations, and characterizing censorship implementation in Chinese LLMs."
+++

## In brief

- Advanced website fingerprinting attacks can be simulated more efficiently across network positions by transducing real-world exit traces.
- Timing Synchronization Function (TSF) in 802.11 networks enables a robust covert channel with a data rate of 520 bits/s by exploiting natural imprecision.
- Character-level perturbations such as typos and swaps are shown to significantly bypass current LLM watermark detection mechanisms without massive capability constraints.
- Content censorship in prominent Chinese LLM services uses traditional keyword and blocking strategies injected directly into input, output, and search phases.

## CELLSHIFT: RTT-Aware Trace Transduction for Real-World Website Fingerprinting

- Existing Website Fingerprinting (WF) evaluations suffer from position misalignment because traces recorded at Tor exit relays do not reflect the traffic patterns an entry-side attacker observes.
- CELLSHIFT transforms observed real-world exit cell traces into simulated entry traces by using cell timestamps, directions, and relay control commands to estimate circuit round-trip times without running costly full-network simulations.
- This RTT-aware transduction provides a more realistic and computationally inexpensive method for attackers and researchers to adapt training data collected at one point for use at another network position.

Jansen, R., U.S. Naval Research Laboratory. "CELLSHIFT: RTT-Aware Trace Transduction for Real-World Website Fingerprinting." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/cellshift-rtt-aware-trace-transduction-for-real-world-website-fingerprinting/

## CHAOS: Exploiting Station Time Synchronization in 802.11 Networks

- Unmodified WiFi stations can embed covert data into the ambient noise of management and control frames that are constantly broadcast in dense environments.
- CHAOS encodes secret signals into the Timing Synchronization Function (TSF) timestamps of management headers, exploiting the natural timing imprecision of real base stations to evade statistical detection.
- This covert channel successfully broadcasts secret data robustly at a configured rate of 520 bits/s across standard WiFi hardware setups.

Shahini, S., Ricci, R., University of Utah. "CHAOS: Exploiting Station Time Synchronization in 802.11 Networks." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/chaos-exploiting-station-time-synchronization-in-802-11-networks/

## Character-Level Perturbations Disrupt LLM Watermarks

- Current watermark removal attacks on Large Language Models are deemed suboptimal, wrongly leading researchers to believe that removing embedded signals requires huge query budgets or detector access.
- Character-level perturbations—such as typos, character swaps, deletions, and homoglyphs—affect multiple text tokens at once, successfully erasing watermarks with limited edits.
- This highlights a significant overestimation of the robustness of current LLM watermarking schemes against realistic and low-cost adversaries.

Zhang, Z., Zhang, X., Zhang, Y., Zhang, H., Pan, S., Liu, B., Gill, A., Zhang, L. Y. "Character-Level Perturbations Disrupt LLM Watermarks." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/character-level-perturbations-disrupt-llm-watermarks/

## Characterizing the Implementation of Censorship Policies in Chinese LLM Services

- Instead of relying solely on alignment techniques which often fail to enforce strict legal censorship standards reliably, prominent Chinese LLMs fall back on overt blocking.
- Traditional blocking mechanisms are implemented in services like Baidu-Chat, DeepSeek, and Doubao at the input, output, and search phases of the prompt lifecycle.
- Output and search phase blocking was found to leak portions of censored information to the client, including responses and search references that the browser was instructed not to render.

Ablove, A., Chandrashekaran, S., Qiang, X., Ensafi, R. "Characterizing the Implementation of Censorship Policies in Chinese LLM Services." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/characterizing-the-implementation-of-censorship-policies-in-chinese-llm-services/
