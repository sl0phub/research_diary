+++
title = "Conference Brief — 2026-10-04"
date = 2026-10-04T06:00:00Z
type = "conferences"
tags = ["side-channel", "web-security", "cloud", "ndss"]
summary = "New page cache attacks bypassing 2019 mitigations, cross-VM TLB attacks on virtualized GPUs, and evolutionary search for web application crawling."
+++

## In brief

- Side-channel research advances with new page cache attacks on fully up-to-date Linux kernels and cross-VM TLB attacks targeting virtualized NVIDIA GPUs in cloud environments.
- Web application security testing is improved with evolutionary search to navigate complex constraints in application state and input formats.

## Eviction Notice: Reviving and Advancing Page Cache Attacks

- Introduces a systematic approach to page cache attacks based on four primitives: flush, reload, evict, and monitor, deriving five generic attack techniques.
- The attacks operate on fully up-to-date Linux kernels and bypass existing mitigations that were deployed since 2019.
- The fastest attack (Flush+Monitor) achieves an average capacity of 37.7 kB/s in a cross-process covert channel, and low-frequency attacks demonstrate inter-keystroke timing detection with a spatial resolution of 4 kB and temporal resolution of 0.8 µs.

- Neela, S. R., Juffinger, J., Maar, L., Gruss, D. "Eviction Notice: Reviving and Advancing Page Cache Attacks." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/eviction-notice-reviving-and-advancing-page-cache-attacks/

## Exploiting TLBs in Virtualized GPUs for Cross-VM Side-Channel Attacks

- Presents the first investigation into potential information leakage through microarchitectural components in virtualized NVIDIA GPUs, which are widely deployed in cloud environments like Desktop-as-a-Service (DaaS).
- The attack exploits the translation lookaside buffers (TLBs) in these virtualized GPUs to mount cross-VM side-channel attacks.
- A Prime+Probe attack primitive is tailored specifically to the GPU's TLB, overcoming constraints in the NVIDIA vGPU runtime that restrict CUDA applications to allocating memory only in 2 MB pages.

- Jin, H., Guo, Y., Zhang, Z. "Exploiting TLBs in Virtualized GPUs for Cross-VM Side-Channel Attacks." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/exploiting-tlbs-in-virtualized-gpus-for-cross-vm-side-channel-attacks/

## EvoCrawl: Exploring Web Application Code and State using Evolutionary Search

- Addresses the limitations of previous vulnerability scanners that naively explore application state without satisfying input format constraints and constraints between web page elements.
- The tool, EvoCrawl, uses evolutionary search to efficiently find different sequences of web interactions that can successfully submit inputs to web applications.
- In evaluations, EvoCrawl achieved a 59% increase in code coverage and successfully submitted HTML forms 5 times more frequently than the next best tool, finding eight zero-day vulnerabilities in applications like WordPress and GitLab.

- Guo, X., Kawlay, A., Liu, E., Lie, D. "EvoCrawl: Exploring Web Application Code and State using Evolutionary Search." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/evocrawl-exploring-web-application-code-and-state-using-evolutionary-search/

## Also published

- Maali, E., Alrawi, O., McCann, J. "Evaluating Machine Learning-Based IoT Device Identification Models for Security Applications." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/evaluating-machine-learning-based-iot-device-identification-models-for-security-applications/
- Huang, Z., Kao, Y., Chen, S., Chen, G., Meng, Y., Zhu, H. "EXIA: Trusted Transitions for Enclaves via External-Input Attestation." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/exia-trusted-transitions-for-enclaves-via-external-input-attestation/
- Shao, S., Li, Y., Yao, H., He, Y., Qin, Z., Ren, K. "Explanation as a Watermark: Towards Harmless and Multi-bit Model Ownership Verification via Watermarking Feature Attribution." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/explanation-as-a-watermark-towards-harmless-and-multi-bit-model-ownership-verification-via-watermarking-feature-attribution/
- Huang, M. Z., Jiang, R., Sharma, T., Wang, K. Y. "Exploring User Perceptions of Security Auditing in the Web3 Ecosystem." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/exploring-user-perceptions-of-security-auditing-in-the-web3-ecosystem/
- Liu, R., Tran, T., Wang, T., Hu, H., Wang, S., Xiong, L. "ExpShield: Safeguarding Web Text from Unauthorized Crawling and LLM Exploitation." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/expshield-safeguarding-web-text-from-unauthorized-crawling-and-llm-exploitation/
