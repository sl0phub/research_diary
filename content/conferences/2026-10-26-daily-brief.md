+++
title = "Conference Brief — 2026-10-26"
date = 2026-10-26T06:00:00Z
type = "conferences"
tags = ["ndss", "side-channel", "hardware", "cryptography", "llm-security", "privacy", "protocol-analysis"]
summary = "New work on power side-channels, manipulating sensor measurement, and post-quantum end-to-end tunnels."
+++

## In brief

- Introduces novel approaches in side-channel attacks by manipulating power signals or GND radiation.
- Explores privacy protection for language models and network anomaly detection using advanced private set intersection protocols.
- Demonstrates practical and automated post-quantum end-to-end tunnels without per-server client configuration.

## Power-Related Side-Channel Attacks using the Android Sensor Framework

- Mobile devices expose numerous power-related signals beyond timing proxies that allow for power side-channel attacks through unprivileged sensors provided by the Android sensor framework.
- Identifies a novel leakage primitive, the rotation-dependent power leakage of the geomagnetic rotation vector sensor, achieving correlations greater than 0.9 for some tested sensors.
- Evaluates the capabilities of the identified leakage primitives via two case studies: remote attacker via Chrome browser, and local attacker running inside an installed app, enabling an end-to-end pixel-stealing attack.

- Mathias Oberhuber, Martin Unterguggenberger, Lukas Maar, Andreas Kogler, Stefan Mangard. "Power-Related Side-Channel Attacks using the Android Sensor Framework." NDSS — https://www.ndss-symposium.org/ndss-paper/power-related-side-channel-attacks-using-the-android-sensor-framework/

## PowerRadio: Manipulate Sensor Measurement via Power GND Radiation

- Introduces PowerRadio, a new threat vector that bypasses existing protections by leveraging interconnected ground (GND) wires to inject malicious signals, changing sensor readings from a distance.
- The injected signal couples with the sensor's analog measurement wire and survives noise filters, manipulating sensors by inducing static bias, periodical signals, or pulses.
- Root causes are identified as the lack of shielding between ground and data signal wires, and the asymmetry of circuit impedance enabling interference to bypass filtering.

- Yan Jiang, Xiaoyu Ji, Yancheng Jiang, Kai Wang, Chenren Xu, Wenyuan Xu. "PowerRadio: Manipulate Sensor Measurement via Power GND Radiation." NDSS — https://www.ndss-symposium.org/ndss-paper/powerradio-manipulate-sensor-measurement-via-power-gnd-radiation/

## PQConnect: Automated Post-Quantum End-to-End Tunnels

- Introduces PQConnect, a post-quantum end-to-end tunneling protocol that automatically protects packets between installed clients and servers without requiring changes to higher-level protocols.
- Automatically creates end-to-end tunnels using automatic peer discovery via server announcements, requiring no client-side per-server configuration.
- Uses a conservative post-quantum KEM for the server's long-term public key to encrypt and authenticate all packets, and a smaller post-quantum KEM for forward secrecy alongside elliptic curves.

- Daniel J. Bernstein, Tanja Lange, Jonathan Levin, Bo-Yin Yang. "PQConnect: Automated Post-Quantum End-to-End Tunnels." NDSS — https://www.ndss-symposium.org/ndss-paper/pqconnect-automated-post-quantum-end-to-end-tunnels/

## Prεεmpt: Sanitizing Sensitive Prompts for LLMs

- Addresses the problem of formally protecting sensitive information contained in an LLM prompt while maintaining response quality by introducing a prompt sanitizer concept.
- Proposes Prεεmpt, a system that categorizes sensitive tokens: format-dependent tokens (e.g. SSNs) protected via format-preserving encryption, and value-dependent tokens (e.g. age) protected via metric differential privacy.
- Demonstrates that Prεεmpt achieves meaningful privacy guarantees while maintaining high utility compared to unsanitized prompts.

- Amrita Roy Chowdhury, David Glukhov, Divyam Anshumaan, Prasad Chalasani, Nicholas Papernot, Somesh Jha, Mihir Bellare. "Prεεmpt: Sanitizing Sensitive Prompts for LLMs." NDSS — https://www.ndss-symposium.org/ndss-paper/pr%ce%b5%ce%b5mpt-sanitizing-sensitive-prompts-for-llms/

## Practical Traceable Over-Threshold Multi-Party Private Set Intersection

- Proposes Practical Traceable Over-Threshold Multi-Party Private Set Intersection (MP-PSI) to compute the intersection over elements held by at least a predefined number of participants while supporting traceability.
- Existing MP-PSI with threshold protocols provide full anonymity, which is problematic for scenarios like network anomaly detection and digital forensics where establishing provenance and localizing alerts is essential.

- Le Yang, Weijing You, Huiyang He, Kailiang Ji, Jingqiang Lin. "Practical Traceable Over-Threshold Multi-Party Private Set Intersection." NDSS — https://www.ndss-symposium.org/ndss-paper/practical-traceable-over-threshold-multi-party-private-set-intersection/

## PriSrv+: Privacy and Usability-Enhanced Wireless Service Discovery with Fast and Expressive Matchmaking Encryption

- Introduces PriSrv+, an advanced privacy and usability-enhanced service discovery protocol addressing limitations in expressiveness, privacy, scalability, and efficiency of PriSrv (NDSS'24).
- Develops Fast and Expressive Matchmaking Encryption (FEME), a matchmaking encryption scheme capable of supporting expressive access control policies with an unbounded attribute universe.
- Optimizes cryptographic operations, achieving 7.62x faster encryption and 6.23x faster decryption compared to PriSrv, while reducing ciphertext sizes by 87.33%.

- Yang Yang, Guomin Yang, Yingjiu Li, Pengfei Wu, Rui Shi, Minming Huang, Jian Weng, HweeHwa Pang, Robert H. Deng. "PriSrv+: Privacy and Usability-Enhanced Wireless Service Discovery with Fast and Expressive Matchmaking Encryption." NDSS — https://www.ndss-symposium.org/ndss-paper/prisrv-privacy-and-usability-enhanced-wireless-service-discovery-with-fast-and-expressive-matchmaking-encryption/

## Privacy-Preserving Data Deduplication for Enhancing Federated Learning of Language Models

- Introduces Efficient Privacy-Preserving Multi-Party Deduplication (EP-MPD), a protocol that efficiently removes duplicates from multiple clients' datasets without compromising data privacy.
- Constructed in a modular fashion utilizing two novel variants of the Private Set Intersection protocol to address scalability and potential privacy violations in federated setups.
- Experiments demonstrate up to 19.62% improvement in perplexity and up to 27.95% reduction in running time while varying the duplication level between 10% and 30%.

- Aydin Abadi, Vishnu Asutosh Dasu, Sumanta Sarkar. "Privacy-Preserving Data Deduplication for Enhancing Federated Learning of Language Models." NDSS — https://www.ndss-symposium.org/ndss-paper/privacy-preserving-data-deduplication-for-enhancing-federated-learning-of-language-models/

## PrivATE: Differentially Private Average Treatment Effect Estimation for Observational Data

- Introduces PrivATE, a practical average treatment effect (ATE) estimation framework for observational data that ensures differential privacy.
- Accommodates different privacy requirements by designing two levels of privacy protection (label-level and sample-level).
- Derives an adaptive matching limit to balance noise-induced error and matching error, leading to a more accurate estimate of ATE.

- Quan Yuan, Xiaochen Li, Linkang Du, Min Chen, Mingyang Sun, Yunjun Gao, Shibo He, Jiming Chen, Zhikun Zhang. "PrivATE: Differentially Private Average Treatment Effect Estimation for Observational Data." NDSS — https://www.ndss-symposium.org/ndss-paper/private-differentially-private-average-treatment-effect-estimation-for-observational-data/
