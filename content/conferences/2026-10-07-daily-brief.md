+++
title = "Conference Brief — 2026-10-07"
date = 2026-10-07T07:25:29Z
type = "conferences"
tags = ["vulnerability-discovery", "fuzzing", "privacy"]
summary = "New approaches to API security rules, hardware fuzzing using a Golden Reference Model, and the privacy implications of WhatsApp's contact discovery."
+++

## In brief

- **Automated security:** LLMs are leveraged to generate API parameter security rules from source code, while a generative fuzzer uses a software-based digital twin to refine hardware tests efficiently.
- **Privacy at scale:** An evaluation of WhatsApp's contact discovery reveals the ability to enumerate 3.5 billion active accounts, exposing highly sensitive data globally.

## Generating API Parameter Security Rules with LLM for API Misuse Detection

- Introduces GPTAid, a system that automatically generates API Parameter Security Rules (APSRs) by analysing API source code using an LLM.
- Uses an execution feedback-checking approach alongside code differential analysis to create concrete APSRs and apply them to detect API misuse.
- Evaluated on eight popular libraries, generating 579 APSRs that enrich existing documentation.
- Found 210 previously unknown security bugs across 47 applications integrating these libraries, identifying vulnerabilities capable of causing crashes and denial of service.

- Jinghua Liu, Yi Yang, Kai Chen, Miaoqian Lin. "Generating API Parameter Security Rules with LLM for API Misuse Detection." NDSS 2025 — https://www.ndss-symposium.org/ndss-paper/generating-api-parameter-security-rules-with-llm-for-api-misuse-detection/


## GoldenFuzz: Generative Golden Reference Hardware Fuzzing

- Introduces a novel language-model-based hardware fuzzer that decouples test case refinement from coverage and vulnerability exploration.
- Utilises a software-based Golden Reference Model (GRM), a digital twin conforming to the device under test's ISA, to refine fuzzing strategies efficiently before executing tests on actual hardware.
- Reduces the computational overhead and cost typically associated with cycle-accurate device simulations.
- Discovered seven new vulnerabilities in open-source and commercial cores, four of which were rated as CVSS 7.0 severity.

- Lichao Wu, Mohamadreza Rostami, Huimin Li, Nikhilesh Singh, Ahmad-Reza Sadeghi. "GoldenFuzz: Generative Golden Reference Hardware Fuzzing." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/goldenfuzz-generative-golden-reference-hardware-fuzzing/


## Hey there! You are using WhatsApp: Enumerating Three Billion Accounts for Security and Privacy

- Developed a method to generate plausible mobile phone numbers for 245 countries to evaluate the feasibility of large-scale enumeration on WhatsApp.
- Enumerated 3.5 billion active user accounts, collecting phone numbers, public keys, and E2EE encryption signatures.
- Demonstrated that the platform's contact discovery architecture inherently exposes user registration status globally.
- Highlighted severe privacy risks, noting the exposure of users in nations where WhatsApp is banned, and the potential for the dataset to be exploited for spam, phishing, or surveillance.

- Gabriel K. Gegenhuber, Philipp É. Frenzel, Maximilian Günther, Johanna Ullrich, Aljosha Judmayer. "Hey there! You are using WhatsApp: Enumerating Three Billion Accounts for Security and Privacy." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/hey-there-you-are-using-whatsapp-enumerating-three-billion-accounts-for-security-and-privacy/
