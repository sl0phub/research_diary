+++
title = "NDSS Brief"
date = 2026-10-24T06:00:00Z
type = "conferences"
tags = ["cryptography", "hardware", "llm-security", "mobile", "ndss", "network-security", "privacy", "side-channel"]
summary = "Power side-channels in Android sensors, manipulating sensors via ground wires, and automated post-quantum tunnels."
+++

## In brief

- **Side Channels**: Power side-channels in Android sensors, and manipulating sensors via ground wires.
- **Cryptography**: Automated post-quantum tunnels, and private set intersection protocols.
- **Privacy**: Sanitizing prompts for LLMs, deduplication for federated learning, and private causal inference.

## Power-Related Side-Channel Attacks using the Android Sensor Framework

- Demonstrates that Android sensors without permissions can leak power consumption data.
- Evaluates multiple Android phones and finds 55% of evaluated sensors exhibit data-dependent leakage.
- The attack bypassed existing restrictions on power side-channels without root privileges.
- Mathias Oberhuber, Martin Unterguggenberger, Lukas Maar, Andreas Kogler, Stefan Mangard. "Power-Related Side-Channel Attacks using the Android Sensor Framework." NDSS — https://ndss-symposium.org/ndss-paper/power-related-side-channel-attacks-using-the-android-sensor-framework

## PowerRadio: Manipulate Sensor Measurement via Power GND Radiation

- Introduces a new threat vector leveraging interconnected ground (GND) wires to inject malicious signals into sensors.
- Presents three methods to manipulate sensors by inducing static bias, periodic patterns, and arbitrary waveforms.
- Bypasses existing protections and changes sensor readings remotely via power lines.
- Yan Jiang, Xiaoyu Ji, Yancheng Jiang, Kai Wang, Chenren Xu, Wenyuan Xu. "PowerRadio: Manipulate Sensor Measurement via Power GND Radiation." NDSS — https://ndss-symposium.org/ndss-paper/powerradio-manipulate-sensor-measurement-via-power-gnd-radiation

## PQConnect: Automated Post-Quantum End-to-End Tunnels

- Introduces PQConnect, an automated post-quantum end-to-end tunneling protocol protecting network traffic.
- Functions without requiring changes to higher-level protocols and application software.
- Adds cryptographic protection to unencrypted applications and post-quantum protection to existing ones.
- Daniel J. Bernstein, Tanja Lange, Jonathan Levin, Bo-Yin Yang. "PQConnect: Automated Post-Quantum End-to-End Tunnels." NDSS — https://ndss-symposium.org/ndss-paper/pqconnect-automated-post-quantum-end-to-end-tunnels

## Prεεmpt: Sanitizing Sensitive Prompts for LLMs

- Introduces a prompt sanitizer focusing on protecting sensitive tokens while maintaining response quality.
- Proposes a novel system that implements this sanitizer to prevent exposure to proprietary LLM APIs.
- Provides a cryptographically inspired notion of formal protection for prompt data.
- Amrita Roy Chowdhury, David Glukhov, Divyam Anshumaan, Prasad Chalasani, Nicholas Papernot, Somesh Jha, Mihir Bellare. "Prεεmpt: Sanitizing Sensitive Prompts for LLMs." NDSS — https://ndss-symposium.org/ndss-paper/pr%ce%b5%ce%b5mpt-sanitizing-sensitive-prompts-for-llms

## Practical Traceable Over-Threshold Multi-Party Private Set Intersection

- Develops an over-threshold multi-party private set intersection protocol.
- Addresses participants interested in computing intersection over elements held by at least a predefined number of parties.
- Aims to provide privacy protection and accountability in collaborative computing contexts.
- Le Yang, Weijing You, Huiyang He, Kailiang Ji, Jingqiang Lin. "Practical Traceable Over-Threshold Multi-Party Private Set Intersection." NDSS — https://ndss-symposium.org/ndss-paper/practical-traceable-over-threshold-multi-party-private-set-intersection

## PriSrv+: Privacy and Usability-Enhanced Wireless Service Discovery with Fast and Expressive Matchmaking Encryption

- Introduces an advanced privacy and usability-enhanced service discovery protocol for wireless networks.
- Addresses limitations in expressiveness, privacy, and scalability of prior work.
- Enables fast and expressive matchmaking encryption suitable for 5G and IoT environments.
- Yang Yang, Guomin Yang, Yingjiu Li, Pengfei Wu, Rui Shi, Minming Huang, Jian Weng, HweeHwa Pang, Robert H. Deng. "PriSrv+: Privacy and Usability-Enhanced Wireless Service Discovery with Fast and Expressive Matchmaking Encryption." NDSS — https://ndss-symposium.org/ndss-paper/prisrv-privacy-and-usability-enhanced-wireless-service-discovery-with-fast-and-expressive-matchmaking-encryption

## Privacy-Preserving Data Deduplication for Enhancing Federated Learning of Language Models

- Introduces Efficient Privacy-Preserving Multi-Party Deduplication (EP-MPD) for federated learning.
- Removes duplicates from datasets across multiple clients without compromising data privacy.
- Utilizes two novel variants of the Private Set Intersection protocol for modular construction.
- Aydin Abadi, Vishnu Asutosh Dasu, Sumanta Sarkar. "Privacy-Preserving Data Deduplication for Enhancing Federated Learning of Language Models." NDSS — https://ndss-symposium.org/ndss-paper/privacy-preserving-data-deduplication-for-enhancing-federated-learning-of-language-models

## PrivATE: Differentially Private Average Treatment Effect Estimation for Observational Data

- Develops differentially private methods for computing Average Treatment Effect (ATE) from observational data.
- Addresses substantial privacy risks associated with causal inference tasks.
- Provides strict theoretical guarantees for data privacy while enabling causal analysis.
- Quan Yuan, Xiaochen Li, Linkang Du, Min Chen, Mingyang Sun, Yunjun Gao, Shibo He, Jiming Chen, Zhikun Zhang. "PrivATE: Differentially Private Average Treatment Effect Estimation for Observational Data." NDSS — https://ndss-symposium.org/ndss-paper/private-differentially-private-average-treatment-effect-estimation-for-observational-data
