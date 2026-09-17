+++
title = "Conference Brief — 2026-09-16"
date = 2026-09-16T06:00:00Z
type = "conferences"
tags = ["network-security", "ndss"]
summary = "New attacks bypassing Wi-Fi client isolation across home and enterprise networks, alongside a large-scale measurement of the threat intelligence ecosystem's dynamics and bottlenecks."
+++

## In brief

- Today's items span network protocols and threat intelligence, highlighting how systemic assumptions fail in practice.
- The highlighted works show that Wi-Fi client isolation can be bypassed at multiple network layers to achieve traffic interception, and that the threat intelligence sharing ecosystem is hindered by vendors delaying indicator propagation.

## AirSnitch: Demystifying and Breaking Client Isolation in Wi-Fi Networks

- Conducts a structured security analysis of Wi-Fi client isolation across encryption, switching, and routing layers, demonstrating that every tested router and network was vulnerable to at least one attack.
- Shows that attackers can abuse the shared Group Temporal Key (GTK) used for broadcast and multicast traffic to directly inject packets to victims, bypassing Access Point (AP) isolation entirely.
- Highlights that these bypasses enable traffic injection, interception of traffic bound for the Internet, and Machine-in-the-Middle (MitM) attacks, allowing adversaries to exploit higher-layer vulnerabilities such as unpatched TLS implementations.
- Reveals that even standards like Passpoint, designed to mitigate insider attacks in hotspots, are flawed in their management of group keys and fail to protect the switching or routing layers.

Zhou, X., Pu, J., Liu, Z., Qian, Z., Tan, Z., Krishnamurthy, S. V., Vanhoef, M. "AirSnitch: Demystifying and Breaking Client Isolation in Wi-Fi Networks." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/airsnitch-demystifying-and-breaking-client-isolation-in-wi-fi-networks/

## Actively Understanding the Dynamics and Risks of the Threat Intelligence Ecosystem

- Proposes a measurement framework that uses watermarked network Indicators of Compromise (IoCs) to track how binaries propagate through the globally distributed threat intelligence (TI) ecosystem.
- Finds that while dissemination of intelligence generally leads to threat disruption, the ecosystem's utility is significantly limited by vendors who extract TI but selectively withhold it from others.
- Identifies "bottleneck" vendors that delay the sharing of intelligence by hours or days, slowing down the collective response to active threats.
- Uncovers several practical threats to the ecosystem's supply chain currently exploited in the wild, including unnecessary active probing by vendors, shallow extraction of dropped files, and easily identifiable sandbox fingerprints.

Galloway, T., Chang, A., Alrawi, O., Avgetidis, A., Antonakakis, M., Monrose, F. "Actively Understanding the Dynamics and Risks of the Threat Intelligence Ecosystem." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/actively-understanding-the-dynamics-and-risks-of-the-threat-intelligence-ecosystem/

## Also published

- Oygenblik, D., Dermendzhiev, D., Sofias, F., Yao, M., Xu, H., Zhang, R., Park, J., Sikder, A. K., Saltaformaggio, B. "Achieving Zen: Combining Mathematical and Programmatic Deep Learning Model Representations for Attribution and Reuse." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/achieving-zen-combining-mathematical-and-programmatic-deep-learning-model-representations-for-attribution-and-reuse/
- Kubo, Y., Kanei, F., Akiyama, M., Wakai, T., Mori, T. "Action Required: A Mixed-Methods Study of Security Practices in GitHub Actions." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/action-required-a-mixed-methods-study-of-security-practices-in-github-actions/
- Della Monica, P., Visconti, I., Vitaletti, A., Zecchini, M. "ACTS: Attestations of Contents in TLS Sessions." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/acts-attestations-of-contents-in-tls-sessions/
- Wang, Y., Zheng, Y., Liu, P., Fang, D., Cheng, J., Shi, D., Sun, L. "ADGFUZZ: Assignment Dependency-Guided Fuzzing for Robotic Vehicles." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/adgfuzz-assignment-dependency-guided-fuzzing-for-robotic-vehicles/
- Scaffino, G., Aumayr, L., Bastankhah, M., Avarikioti, Z., Maffei, M. "Alba: The Dawn of Scalable Bridges for Blockchains." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/alba-the-dawn-of-scalable-bridges-for-blockchains/
- Anghel, R., Ganan, C., Lone, Q., Luckie, M., Zhauniarovich, Y. "Aliens Among Us: Observing Private or Reserved IPs on the Public Internet." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/aliens-among-us-observing-private-or-reserved-ips-on-the-public-internet/
