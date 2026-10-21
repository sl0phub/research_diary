+++
title = "arXiv Brief — 2026-10-21"
date = 2026-10-21T06:00:00Z
type = "arxiv"
tags = ["arxiv", "binary-analysis", "cryptography", "llm-security", "mobile"]
summary = "Inter-procedural binary type inference, defenses against cross-node adversarial transferability, edge-deployable radiology SLMs, and PQC energy benchmarking on constrained devices."
+++

## In brief

- **Binary analysis:** Extending neural type recovery to capture data flows across function boundaries.
- **Model security:** Mitigating adversarial transferability between mobile edge devices through architectural obfuscation.
- **Applied cryptography:** Benchmarking the energy consumption of NIST post-quantum standards on resource-constrained IoT architectures.

## InterType: Breaking the Single-Function Barrier in Neural Binary Type Inference

- Nearly 44% of variables in real-world binaries propagate across function boundaries, presenting a limitation for single-function type inference models.
- The InterType framework extends the CodeArt Transformer by incorporating caller-callee data flow dependencies to perform inter-procedural binary type recovery.
- On the coreutils benchmark compiled with O1 optimization, InterType achieved a 91.76% recall rate, improving upon the 89.00% baseline of the intra-procedural CodeArt model.

- Shan Wang, Tianming Cui, Stephen McCamant, Antonia Zhai, Pen-Chung Yew. "InterType: Breaking the Single-Function Barrier in Neural Binary Type Inference." arXiv — https://arxiv.org/abs/2610.26906

## Model Exposure on One Device Endangers Others: Rethinking Edge Neural Network Security across Devices

- On-device neural network models embedded in mobile apps face cross-node attacks where adversarial examples crafted on one device transfer to others.
- VeilNN introduces architectural and parameter-level model obfuscation to reduce adversarial transferability while maintaining task functionality.
- Tested across four adversarial attack types, the defense achieved an average success rate of 49.19%, with peaks up to 81.19%, outperforming existing defenses by over 33%.

- Yuyang Zhang, Kangjie Chen, Yihui Jin, Run Wang. "Model Exposure on One Device Endangers Others: Rethinking Edge Neural Network Security across Devices." arXiv — https://arxiv.org/abs/2610.27152

## MedPAO-Assist: Edge-Deployable, Modality-Aware Agentic AI for Radiology Report Structuring

- MedPAO-Assist is an edge-deployable, multi-agent framework that structures radiology reports locally, enabling offline operation to protect patient privacy.
- Operating entirely on a 0.6B-parameter Small Language Model without internet access, it uses an Extract-Ground-Generate paradigm with a speech-driven correction phase.
- The system requires approximately 3.3 GB of peak RAM and achieves an average end-to-end latency of 31 seconds on a standard laptop CPU.

- Shrish Shrinath Vaidya, Minmini Selvam, Ganapathy Krishnamurthi. "MedPAO-Assist: Edge-Deployable, Modality-Aware Agentic AI for Radiology Report Structuring." arXiv — https://arxiv.org/abs/2610.26913

## Energy Consumption of Post-Quantum Cryptography on Constrained and General-Purpose Architectures

- The three NIST-standardised post-quantum cryptography algorithms (ML-KEM, ML-DSA, and SLH-DSA) were benchmarked for energy consumption across constrained IoT devices and laptops.
- ML-KEM and ML-DSA demonstrated energy and speed efficiencies comparable to classical elliptic-curve cryptography across the tested architectures.
- SLH-DSA signing on 32-bit constrained devices incurred energy costs up to 243% higher than on 64-bit hardware, rendering it impractical for resource-limited IoT deployments.

- Olivier Gillot, William J. Buchanan, Madjid G. Tehrani. "Energy Consumption of Post-Quantum Cryptography on Constrained and General-Purpose Architectures." arXiv — https://arxiv.org/abs/2610.27111

## Also published

- Yuyang Zhang, Yihui Jin, Kangjie Chen, Leyang Wu, Run Wang. "Mind Your Boundaries: Boundary-Aware Model Obfuscation against Cross-node Attack." arXiv — https://arxiv.org/abs/2610.27135
- Md Morshedul Islam, Hossain Shahriar, Alfredo Cuzzocrea. "Privacy-Preserving Personalized Federated Learning (PPP-FL) for Medical Imaging." arXiv — https://arxiv.org/abs/2610.27470
- Hanieh Totonchi Asl, Ebrahim Nouri, Zhuoran Li, Danella Zhao. "Interflow: Breaking the Offline-Online Barrier for Private AI at the Edge." arXiv — https://arxiv.org/abs/2610.27431
- Charles Koll, Houssam Abbas, Mike Rosulek. "Privacy-Preserving Robustness-Guided Testing." arXiv — https://arxiv.org/abs/2610.27441
- Olivier Gillot, William J. Buchanan, Callum Turino. "Testing TLS 1.3 PQC on constrained devices and microcontrollers." arXiv — https://arxiv.org/abs/2610.27766
- Xinyue Zhang, Jixiang Li, Bin Shao, Baishun Yang, Zhiyang Liu, Weichao Wang. "Fine-Tuning Small Language Models for Reliable VASP INCAR Generation." arXiv — https://arxiv.org/abs/2608.05387
