+++
title = "Conference Brief — 2026-10-25"
date = 2026-10-25T06:00:00Z
type = "conferences"
tags = ["side-channel", "hardware", "network-security", "llm-security", "privacy", "ndss"]
summary = "New papers from NDSS covering Android sensor side channels, physical power grid manipulations, and post-quantum tunnels."
+++

## In brief

- Recent NDSS papers explore novel side-channel attacks on Android sensors and physical layer manipulation through ground wires.
- Other work includes automated post-quantum tunneling, prompt sanitization for LLMs, and privacy-preserving multi-party deduplication for federated learning.

## Power-Related Side-Channel Attacks using the Android Sensor Framework

- Android mobile devices expose numerous power-related signals through unprivileged sensors that can be exploited for power side-channel attacks.
- A systematic analysis of the Android sensor framework reveals that these seemingly innocuous sensors can leak enough information to mount attacks.
- The work demonstrates that power-related side channels exist and are exploitable even without direct access to dedicated power interfaces.

Oberhuber, M. et al. "Power-Related Side-Channel Attacks using the Android Sensor Framework." NDSS — https://www.ndss-symposium.org/ndss-paper/power-related-side-channel-attacks-using-the-android-sensor-framework/

## PowerRadio: Manipulate Sensor Measurement via Power GND Radiation

- PowerRadio introduces a new threat vector that bypasses existing protections to change sensor readings from a distance.
- The attack leverages interconnected ground (GND) wires, common in home electrical safety, to inject malicious signals that survive noise filters.
- Three methods are presented to manipulate sensors by inducing static bias, enabling attackers to alter readings on targeted devices.

Jiang, Y. et al. "PowerRadio: Manipulate Sensor Measurement via Power GND Radiation." NDSS — https://www.ndss-symposium.org/ndss-paper/powerradio-manipulate-sensor-measurement-via-power-gnd-radiation/

## PQConnect: Automated Post-Quantum End-to-End Tunnels

- PQConnect is a post-quantum end-to-end tunneling protocol that automatically protects packets between configured clients and servers.
- It operates similarly to a VPN, requiring no changes to higher-level protocols or application software while providing cryptographic protection.
- The system works alongside existing pre-quantum applications to add post-quantum protection and an application-independent layer of defense.

Bernstein, D. J. et al. "PQConnect: Automated Post-Quantum End-to-End Tunnels." NDSS — https://www.ndss-symposium.org/ndss-paper/pqconnect-automated-post-quantum-end-to-end-tunnels/

## Also published

- Roy Chowdhury, A. et al. "Prεεmpt: Sanitizing Sensitive Prompts for LLMs." NDSS — https://www.ndss-symposium.org/ndss-paper/pr%ce%b5%ce%b5mpt-sanitizing-sensitive-prompts-for-llms/
- Yang, L. et al. "Practical Traceable Over-Threshold Multi-Party Private Set Intersection." NDSS — https://www.ndss-symposium.org/ndss-paper/practical-traceable-over-threshold-multi-party-private-set-intersection/
- Yang, Y. et al. "PriSrv+: Privacy and Usability-Enhanced Wireless Service Discovery with Fast and Expressive Matchmaking Encryption." NDSS — https://www.ndss-symposium.org/ndss-paper/prisrv-privacy-and-usability-enhanced-wireless-service-discovery-with-fast-and-expressive-matchmaking-encryption/
- Abadi, A. et al. "Privacy-Preserving Data Deduplication for Enhancing Federated Learning of Language Models." NDSS — https://www.ndss-symposium.org/ndss-paper/privacy-preserving-data-deduplication-for-enhancing-federated-learning-of-language-models/
- Yuan, Q. et al. "PrivATE: Differentially Private Average Treatment Effect Estimation for Observational Data." NDSS — https://www.ndss-symposium.org/ndss-paper/private-differentially-private-average-treatment-effect-estimation-for-observational-data/
