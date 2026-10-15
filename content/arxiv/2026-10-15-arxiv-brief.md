+++
title = "arXiv Brief — 2026-10-15"
date = 2026-10-15T06:00:00Z
type = "arxiv"
tags = ["cs.CR", "cs.SE", "fuzzing", "cryptography", "cloud"]
summary = "Evaluations of Rust-based security frameworks, a taxonomy of hybrid PQC-QKD protocols, and prioritizing microservice requests via retries."
+++

## In brief

- Sound evaluation practices for Rust-based security frameworks are introduced, along with automated coverage oracles.
- A comprehensive taxonomy and analysis of hybrid Post-Quantum Cryptography (PQC) and Quantum Key Distribution (QKD) is presented.
- DiffTry proposes a lightweight retry modification to prioritize microservice requests during overload periods.

## Building Sound Evaluation Practices for Rust-Based Security Frameworks

- Identifies serious issues in existing evaluations of C/C++ security frameworks that undermine reproducibility, and develops a sound methodology tailored for Rust-based evaluations.
- Introduces an automated approach to inject unsafe code coverage oracles to quantify a security tool's performance without requiring forward porting, thus avoiding overfitting.
- Presents methods to quantify the diversity of a Rust test set, and demonstrates the methodology by evaluating popular Rust fuzzers on a diverse set of 20 Rust projects.
- David Paaßen, Lucas Davi. "Building Sound Evaluation Practices for Rust-Based Security Frameworks." arXiv — https://arxiv.org/abs/2610.20315

## Combining Post-Quantum Cryptography and Quantum Key Distribution: Taxonomy, Constructions, Proofs, Standards, Deployments and Open Problems

- Proposes a taxonomy of hybrid PQC-QKD designs across eight dimensions to evaluate protocols like Muckle, MACsec, TLS integrations, and IKEv2 mechanisms (RFCs 8784, 9370, 9867).
- Maps the security arguments for hybrid PQC-QKD protocols onto a common grid covering security models, assumptions, permitted compromise, and established guarantees.
- Synthesises deployment evidence from metropolitan and national QKD networks, highlighting the lack of peer-reviewed deployment economics and open problems like classical channel authentication.
- Mona Alotaibi, Noora Fetais, Saif Al-Kuwari. "Combining Post-Quantum Cryptography and Quantum Key Distribution: Taxonomy, Constructions, Proofs, Standards, Deployments and Open Problems." arXiv — https://arxiv.org/abs/2610.19039

## Prioritizing Microservice Requests via Retries

- Identifies that during overload periods in microservices, standard retry operations fail to protect valuable transactions and instead trigger large-scale performance-degrading retry storms.
- Proposes DiffTry (Differential Retries), a lightweight, distributed, and stateless rejection prioritization mechanism that modifies retry operations without requiring overload sensing or microservices coordination.
- Develops an analytical model that provides formal guarantees on prioritization and rejection rates, validating it on a live Kubernetes deployment where DiffTry is implemented as a service-mesh plugin requiring no application changes.
- Ofek Lavi, Jhonatan Tavori, Hanoch Levy, Anat Bremler-Barr. "Prioritizing Microservice Requests via Retries." arXiv — https://arxiv.org/abs/2610.20567

## Also published

- Julian Ganz, David Knothe, David Oswald, Sebastian Reiter, Thorben Schneider, Simon Wegener. "FreeSBee: A Constant-Time Compilation Pipeline." arXiv — https://arxiv.org/abs/2610.20171
- Ruei-Hau Hsu, Yu-Hsiang Hu, Rafael Kaliski, Tse-Yuan Yu. "ESAU: Expeditious Swarm Remote Attestation for Pub-Sub IoT Networks with Untrusted Cloud-based Proxy Verifier." arXiv — https://arxiv.org/abs/2610.20047
- Florian Spelter, Johannes F. Loevenich, Tobias Hürten, Erik Adler, Maxime Schwarzer, Laurin Holz, Roberto Rigolin F. Lopes. "Analyzing and Mitigating Poisoning Attacks on Flow-Based Intrusion Detection." arXiv — https://arxiv.org/abs/2610.19766
- Valerio Cini, Antonio Guimarães, Russell W. F. Lai, Michał Osadnik, Ivy K. Y. Woo. "Tulva: Practical Asynchronous Threshold FHE." arXiv — https://arxiv.org/abs/2610.20521
