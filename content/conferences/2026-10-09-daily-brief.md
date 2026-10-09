+++
title = "Conference Brief — 2026-10-09"
date = 2026-10-09T06:00:00Z
type = "conferences"
tags = ["fuzzing", "protocol-analysis", "reverse-engineering", "ndss"]
summary = "New tools for discovering logic vulnerabilities in QUIC, scan-cycle fuzzing for industrial control systems, and neural decompilation recovering user-defined types."
+++

## In brief

- Today's brief covers advancements in fuzzing and reverse engineering, spanning industrial controllers to modern transport protocols.
- A notable theme is extending vulnerability discovery beyond memory safety to uncover logical flaws and stateful logic bugs in specialized environments.

- Industrial Control Systems (ICS) code is difficult to evaluate due to domain-specific languages like IEC 61131-3 Structured Text (ST) and closed ecosystems.
- ICSQuartz is the first native fuzzer for ST, introducing novel scan-cycle mutation strategies that uncover stateful vulnerabilities unique to PLC execution models.
- The fuzzer outperforms previous state-of-the-art ICS fuzzers by more than an order of magnitude in executions per second.
- A large-scale fuzzing campaign across real-world ICS libraries resulted in multiple vulnerability disclosures and the discovery of a bug in the RuSTy compiler that could introduce memory corruption vulnerabilities (CWE-125, CWE-787).
- Corban Villa, Constantine Doumanidis, Hithem Lamri, Prashant Hari Narayan Rajput, Michail Maniatakos. "ICSQuartz: Scan Cycle-Aware and Vendor-Agnostic Fuzzing for Industrial Control Systems." NDSS — https://www.ndss-symposium.org/ndss-paper/icsquartz-scan-cycle-aware-and-vendor-agnostic-fuzzing-for-industrial-control-systems/

- Existing QUIC testing tools primarily focus on memory-related vulnerabilities and are ill-equipped to detect logical vulnerabilities.
- MerCuriuzz is a black-box fuzzing framework designed specifically to uncover logical vulnerabilities in QUIC by comparing differential implementations.
- Evaluation across 16 widely used QUIC implementations (including quiche, xquic, and aioquic) discovered 14 previously unknown logical vulnerabilities, categorized into six attack types.
- The vulnerabilities enabled denial-of-service (DoS) attacks, state inconsistencies, and resource exhaustion, leading to 11 confirmed bugs and rewards from vendors like Cloudflare and Alibaba Cloud.
- Kaihua Wang, Jianjun Chen, Pinji Chen, Jianwei Zhuge, Jiaju Bai, Haixin Duan. "Identifying Logical Vulnerabilities in QUIC Implementations." NDSS — https://www.ndss-symposium.org/ndss-paper/identifying-logical-vulnerabilities-in-quic-implementations/

- Neural decompilers have the potential to vastly outperform traditional, deterministic decompilers which struggle to recover source-level features like variable and type names.
- IDIOMS is a neural decompilation approach that finetunes LLMs to explicitly reconstruct user-defined type (UDT) definitions alongside the decompiled code.
- A new dataset, REALTYPE, containing 154,301 training functions with complete, realistic UDT definitions, was built to support the model.
- IDIOMS achieved 54.4% accuracy on the EXEBENCH benchmark (compared to 46.3% for LLM4Decompile), demonstrating state-of-the-art neural decompilation performance.
- Luke Dramko, Claire Le Goues, Edward J. Schwartz. "Idioms: A Simple and Effective Framework for Turbo-Charging Local Neural Decompilation with Well-Defined Types." NDSS — https://www.ndss-symposium.org/ndss-paper/idioms-a-simple-and-effective-framework-for-turbo-charging-local-neural-decompilation-with-well-defined-types/
