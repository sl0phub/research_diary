+++
title = "arXiv Brief — 2026-10-22"
date = 2026-10-22T06:00:00Z
type = "arxiv"
tags = ["cs.CR", "reverse-engineering", "llm-security", "exploitation"]
summary = "A decompiler-based approach to automating virtual machine deobfuscation, prompt injection against LLM-assisted digital forensics, and provenance destruction in coding agents' context compaction."
+++

## In brief

- Two items address security boundaries in LLM deployments: one exploits how a deterministic context compaction step can launder forged approvals, and the other shows how malicious digital evidence can compromise the LLM forensics tools analyzing it.
- A new approach to VM deobfuscation recovers full program behavior by constructing processor specifications, rather than just identifying execution boundaries.

## VMSpec: A Decompiler-based Approach against Virtual Machine Obfuscation

- Addresses the challenge of virtual machine (VM) obfuscation where programs are translated into bytecode for custom VMs with randomized instruction sets.
- Automates the construction of VM processor specifications, allowing existing decompilers (like Ghidra) to analyze VM-obfuscated code and recover higher-level semantics, rather than just simplifying execution traces.
- Evaluated on 147 obfuscated programs (including domain generation algorithms from real malware), demonstrating complete stripping of VM-obfuscation and reconstruction of behavior with infinite input-dependent paths.

Fabian Kilger, Leonard Auer, Manuel Andreas. "VMSpec: A Decompiler-based Approach against Virtual Machine Obfuscation." arXiv, 2026.
arXiv:2610.29566 — https://arxiv.org/abs/2610.29566

## Prompt Injection Through Forensic Evidence: A Taxonomy and Proof of Concept of Anti-Forensic Attacks on LLM-Assisted Digital Investigations

- Digital forensics presents a unique environment for indirect prompt injection because the evidence is inherently attacker-controlled and must be analyzed closely, turning the reasoning layer into a new anti-forensic target.
- Develops a taxonomy of anti-forensic attacks targeting LLMs and highlights the "perception gap"—the difference in how deterministic tools, human examiners, and LLMs perceive the same evidence.
- Demonstrates three attacks driven solely by text planted on seized devices: altering reported conclusions, writing attacker-chosen content to the analyst's workstation, and causing outbound network traffic.

Frank Breitinger, et al. "Prompt Injection Through Forensic Evidence: A Taxonomy and Proof of Concept of Anti-Forensic Attacks on LLM-Assisted Digital Investigations." arXiv, 2026.
arXiv:2610.29747 — https://arxiv.org/abs/2610.29747

## Compaction Laundering: Provenance Destruction in Context-Compacting Coding Agents

- Long-running coding agents must compact their context into memories. Flattening typed conversations into plain strings with text labels (e.g., [User]:) destroys message provenance, allowing forged approvals to survive compaction.
- In five popular open-source agents (pi, opencode, Cline, Aider, OpenHands) that flatten roles, a forged approval is laundered into memory 87-100% of the time. Agents that keep messages role-typed are unaffected (0% success).
- End-to-end, this laundered standing approval drove a real tool-running agent to execute an attacker-controlled `curl | sh` command in a sandbox at ~50% success rate, circumventing the agent's pre-compaction audit.

Arshan Dabirsiaghi (Pixee). "Compaction Laundering: Provenance Destruction in Context-Compacting Coding Agents." arXiv, 2026.
arXiv:2610.29869 — https://arxiv.org/abs/2610.29869

## Also published

- Derek Garcia. "Sign Here: Attributing a Source for a More Trustworthy Software Supply Chain." arXiv:2610.28794 — https://arxiv.org/abs/2610.28794
- Ganni Galea Curmi, Ben Wilde. "How Much Does the Harness Matter, and for Whom? A Multi-Model Study of Context in LLM-Driven Vulnerability Discovery." arXiv:2610.28802 — https://arxiv.org/abs/2610.28802
- Pedro H. Barcha Correia, et al. "Combining Long-Term Memory and LLMs Comes at a High Cost: From Prompt Injection to Persistent Compromise." arXiv:2610.28810 — https://arxiv.org/abs/2610.28810
- Eric Yocam, Varghese Vaidyan, Paris Kalathas. "AI Security Literacy: Ecosystem-based Competency Framework and K-12 Learning Platform." arXiv:2610.28859 — https://arxiv.org/abs/2610.28859
- Yuqi Jia, et al. "Black-Box Red-Teaming of Multi-Agent Systems via Reinforcement Learning." arXiv:2610.28966 — https://arxiv.org/abs/2610.28966
- Kun Liu, et al. "Beyond Tokens: NumAnchor for Address-Grounded Numeric Operand Representation in Assembly Language Models." arXiv:2610.29027 — https://arxiv.org/abs/2610.29027
- Jiseung Kim, et al. "Regular Syndrome Decoding Is Easier Than Previously Estimated." arXiv:2610.29175 — https://arxiv.org/abs/2610.29175
- Luca Zanolini. "Correlated Failures of AI Approval Monitors." arXiv:2610.29178 — https://arxiv.org/abs/2610.29178
- Xingwang Wang. "Cryptanalysis and Repair of 'Decentralized Multi-authority ABE for NC$^1$ from BDH'." arXiv:2610.29224 — https://arxiv.org/abs/2610.29224
- Heba Osama, et al. "MASAR: Multi-stage Attack Surface Analysis and Reasoning Framework for Telecom Networks." arXiv:2610.29343 — https://arxiv.org/abs/2610.29343
- Gadi Evron. "Where AI Vulnerability Discovery Harnesses Go Quiet: Structural False Negatives and Hidden Vulnerabilities." arXiv:2610.29379 — https://arxiv.org/abs/2610.29379
- Qingyue Wang, et al. "CertMoE: Robustness Certification for Mixture-of-Experts LLMs via Routing-Aware Smoothing." arXiv:2610.29395 — https://arxiv.org/abs/2610.29395
- Lin Wang, et al. "Beyond Policy Engines: Binding-Complete Execution Admission." arXiv:2610.29701 — https://arxiv.org/abs/2610.29701
- Ryan Vogt, Ioanis Nikolaidis, Mario A. Nascimento. "Location-of-interest vs. Current-location Privacy in Multi-hop Communication." arXiv:2610.29772 — https://arxiv.org/abs/2610.29772
- Zheng Zhang, Na Zhang. "Linear Self-Symmetries of Inverse-Based S-boxes: Generic Rigidity and Applications." arXiv:2610.29837 — https://arxiv.org/abs/2610.29837
- Yahao Ren, et al. "Characterizing and Defending Utility-Hijacking in Instruction-Tuning Data Selection." arXiv:2610.29886 — https://arxiv.org/abs/2610.29886
- Davide Carnemolla, Dario Catalano, Mario Di Raimondo. "GhostFaceMPC: Privacy-Preserving Face Recognition with Multi-Party Computation." arXiv:2610.29987 — https://arxiv.org/abs/2610.29987
- Juan S. Santillana. "VX-One: Typed, Calibrated Decision Heads for Real-Time Perimeter Triage - An empirical study of unknown-attack honesty, cascade gray zones, and calibration under drift." arXiv:2610.30090 — https://arxiv.org/abs/2610.30090
- Mert Cihangiroglu, et al. "LightSplit: Practical Privacy-Preserving Split Learning via Orthogonal Projections (Full Version)." arXiv:2605.13265 — https://arxiv.org/abs/2605.13265
- Tanqiu Jiang, et al. "PerMIT: Securing Persistent Memory for LLM Agents via Machine-Checked Integrity Theorems and Scalable Community Trust." arXiv:2610.28987 — https://arxiv.org/abs/2610.28987
- Chao Shang, et al. "AgentPolicyForge: From Executable Environments to Policy Benchmarks and Adaptive Guards." arXiv:2610.28989 — https://arxiv.org/abs/2610.28989
- Eric Liang, Alan Luo, Kaiwen Yuan. "A Unified Evaluation Framework of Physical Adversarial Robustness in the Edge VLM Era." arXiv:2610.29196 — https://arxiv.org/abs/2610.29196
- Hongyu Li, et al. "Beyond Binary Labels: Diagnostic Evaluation of LLM Safety with Prompt-Level Rubrics." arXiv:2610.29225 — https://arxiv.org/abs/2610.29225
- Hassan Khodaiemehr, Khadijeh Bagheri, Chen Feng. "PQ-Vault: Provably Quantum-Safe Asset Custody for Unmodified Ethereum." arXiv:2610.29230 — https://arxiv.org/abs/2610.29230
- Mohammed Rashed, Carlos Garc\'ia-Rubio, Celeste Campo. "Do Flow-Generation Tools Matter? Unsupervised Characterization of MQTT Traffic Across Public Datasets." arXiv:2610.29774 — https://arxiv.org/abs/2610.29774
- Lihong He, Lucian Popa, Marina Danilevsky. "A Small Model Asks Better: Fine-Tuning Query Clarification for Retrieval-Augmented Generation." arXiv:2610.28686 — https://arxiv.org/abs/2610.28686
- Anrui Gu, Zhichao Wang, Nicolai Ouporov. "Fig: Automated Multiagent Behavior Elicitor." arXiv:2610.28891 — https://arxiv.org/abs/2610.28891
- Yuyao Zhang, et al. "Same Probabilities, Different Advice: Gain-Loss Framing Effects in High-Stakes LLM Decision Support." arXiv:2610.29294 — https://arxiv.org/abs/2610.29294
- Linus Filbry, Luckeciano C. Melo, Yarin Gal. "From Prompts to Posteriors: Can LLM Agents Perform Bayesian Inference in Context?." arXiv:2610.29331 — https://arxiv.org/abs/2610.29331
- Sami Kharma, Florian Schintke. "Solving Go under Positional Superko: Sound Proof Transfer and New Board Values." arXiv:2610.29414 — https://arxiv.org/abs/2610.29414
- Yan Wang. "TraceForge: Distilling with Your Own Thinking." arXiv:2610.29680 — https://arxiv.org/abs/2610.29680
- Sudipta Paul, et al. "HGM-Dual: Lineage-Aware Guided Agent Harness Optimization for Long-Horizon Planning." arXiv:2610.30042 — https://arxiv.org/abs/2610.30042
- Remo Grillo. "The CIDOC CRM Periodic Table: Documentation You Can Test to Support the Adoption of Scientific Research Ontologies for the Humanities." arXiv:2610.28650 — https://arxiv.org/abs/2610.28650
- Sion Israel Sion, Alain April. "Who Verifies the Builder? Toward Independent Assurance for Agent-Produced Software." arXiv:2610.28667 — https://arxiv.org/abs/2610.28667
- Jianing Yin, et al. "VerifierBench: Benchmarking the Generation of Executable Verifiers for LLM Agents." arXiv:2610.28679 — https://arxiv.org/abs/2610.28679
- Can Erer, H. Birkan Yilmaz, Nebahat Aral. "STAR-XPC: Set Transformer for Estimating X-ray Transmission in Polymer Composites." arXiv:2610.28709 — https://arxiv.org/abs/2610.28709
- Isacco Beretta. "Towards Realistic Models of Change: A Causal Perspective on Decision-Making and Dynamical Systems." arXiv:2610.28803 — https://arxiv.org/abs/2610.28803
- \.Ibrahim O\u{g}uz \c{C}etinkaya, Sajad Khodadadian, Taylan Topcu. "Brittle by Design? Multi-Scenario Reinforcement Learning for Robust Mission Coordination in Systems of Systems." arXiv:2610.28818 — https://arxiv.org/abs/2610.28818
- Shixuan Liu, et al. "RL-IF: Tracking Non-local Training Data Influence for Online Reinforcement Learning." arXiv:2610.28883 — https://arxiv.org/abs/2610.28883
- Md Khalid Syfullah, Alvi Ataur Khalil. "Can Quantum Layers offer Performance and Security Advantages in Vision-Language Models?." arXiv:2610.28964 — https://arxiv.org/abs/2610.28964
- Derong Yu, et al. "UNIVERS: Learning UNIversal Voxel-wise Embedding via Randomized Synthesis for generalizable one-shot landmark localization." arXiv:2610.29098 — https://arxiv.org/abs/2610.29098
- Austin Meek, et al. "Mitigating Reward Hacking in Realistic Scenarios Through Representation Engineering." arXiv:2610.29129 — https://arxiv.org/abs/2610.29129
- Haoran Xiong, et al. "CRAB: Cuboid-based Representation for As-built BIM from Point Clouds." arXiv:2610.29257 — https://arxiv.org/abs/2610.29257
- Keith Kwok, et al. "Beyond Small Talk: Modeling Disclosure Trajectories in Human-AI Conversation." arXiv:2610.29413 — https://arxiv.org/abs/2610.29413
- Ruijie Zhang, et al. "RegoMender: A Multi-agent Framework for Automated Rego Policy Repair." arXiv:2610.29456 — https://arxiv.org/abs/2610.29456
- Jiawei Chen, et al. "OmniSimulator: Aligning Small Language Models for Authentic Heterogeneous Behavior Modeling." arXiv:2610.29472 — https://arxiv.org/abs/2610.29472
- Geri Skenderi. "Structure-Aware Message Passing on Petri Nets through Directed Walks and Incidence Diffusion." arXiv:2610.29725 — https://arxiv.org/abs/2610.29725
- Shuncheng Jie, et al. "SAKURA: Serving Attention Key-Value State Under Rate Adaptation for Private Image Editing on Phones." arXiv:2610.29733 — https://arxiv.org/abs/2610.29733
- Yawei Li, et al. "S-EDL: Eliciting Self-Evidence from Sequence Likelihoods for Semantic Calibration of LLMs." arXiv:2610.29832 — https://arxiv.org/abs/2610.29832
- Aravindan Kamatchi Sundaram, B. Pabitramohan Prusty, Rohit Batra. "Automated Materials Data and Knowledge Extraction using Machine Learning and Large Language Models." arXiv:2610.29895 — https://arxiv.org/abs/2610.29895
- Prakhar Ganesh, et al. "Privacy in Context Is Being Overlooked in the Age of General-Purpose LLMs." arXiv:2610.29925 — https://arxiv.org/abs/2610.29925
- Chaoran Yuan, Fadi Kurdahi. "FaultGene: LLM-Assisted Fault-Augmented Test Generation for Hardware-in-the-Loop Validation of Autonomous Driving Systems." arXiv:2610.29969 — https://arxiv.org/abs/2610.29969
- Tanu Singh, Aashna Suman, Vinod Patidar. "HiddenLens: A Multi-Layer LLM Framework for Detecting and Resolving Hidden Assumptions in Software Requirements." arXiv:2610.29996 — https://arxiv.org/abs/2610.29996
- Jinyun Chen, et al. "Compilation Is Not Correctness: Scan-by-Scan Evaluation of LLM-Generated PLC Programs." arXiv:2610.28675 — https://arxiv.org/abs/2610.28675
- Masoud Jamshidiyan Tehrani, Jinhan Kim, Paolo Tonella. "PCLA-Bridge: A Framework for Cross-Domain Deployment of CARLA Agents." arXiv:2610.28696 — https://arxiv.org/abs/2610.28696
- Mahyar Tourchi Moghaddam, et al. "Multi-agent LLMs on the Cloud-Edge-IoT Continuum: A Systematic Mapping Study on Architectures, Deployment, and Evaluation." arXiv:2610.28702 — https://arxiv.org/abs/2610.28702
- Gabriel Dautovi, Jie JW Wu. "VeeReview: Measuring Build-Verify Pairs in Agent-Authored Pull Requests from a V-Model Perspective." arXiv:2610.29143 — https://arxiv.org/abs/2610.29143
- Hoang Tran, et al. "CloudIR-Bench: A Benchmark for Root Cause Analysis and Mitigation of Cloud Incidents." arXiv:2610.29185 — https://arxiv.org/abs/2610.29185
- Chenxi Huang, et al. "Do Coding Agents Understand Why Systems Crash---and Why They Don't?." arXiv:2610.29332 — https://arxiv.org/abs/2610.29332
- Jinglin Dai, et al. "From Natural Language Intent to Executable Control: Hierarchical Feedback-Guided LLM Planning for Multi-component Cyber-Physical Systems." arXiv:2610.22441 — https://arxiv.org/abs/2610.22441
