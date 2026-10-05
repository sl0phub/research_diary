+++
title = "arXiv Brief — 2026-10-05"
date = 2026-10-05T06:00:00Z
type = "arxiv"
tags = ["cs.CR", "llm-security", "hardware", "fuzzing", "cloud", "arxiv"]
summary = "A persistent focus on LLM multi-agent security and defensive frameworks, alongside developments in hardware trojan synthesis and IIoT attack surfaces."
+++

## In brief

- **LLM Multi-Agent Security:** The boundary between data and control planes is blurring as LLM agents are deployed into infrastructure, prompting new multi-path quorum mechanisms (MIRROR) and defense-in-depth architectures (Containing the Autonomous Operator) to mitigate Agent-in-the-Middle and prompt injection threats.
- **Evaluating Deception and Evasion:** Defenses are adopting stateful deception (AgentTrap) to counter autonomous penetration testers, while attackers explore novel bypasses like Phantom State Attacks that exploit IIoT temporal aggregation and compositional intent-hiding jailbreaks.
- **Automated Hardware Vulnerabilities:** The synthesis of realistic, hard-to-detect hardware trojans (CITADEL) is becoming automated through the combined use of LLMs and Data Flow Graphs, highlighting an increasing sophistication in hardware security research.

## SideKernel: A Usable microVM Sandbox for AI Coding Agents on macOS

- Examines the security risks of running untrusted AI coding agents locally on macOS and identifies usability barriers hindering sandbox adoption through a user survey.
- Introduces SideKernel, an open-source, local microVM-based macOS sandbox for AI coding agents designed for usability.
- Performs a comparative analysis between SideKernel and other sandboxes available on the market that satisfy inclusion criteria.
- Dimitrios Prasakis. "SideKernel: A Usable microVM Sandbox for AI Coding Agents on macOS." arXiv:2610.02456 — https://arxiv.org/abs/2610.02456
## Out of Sync, Out of Sight: Phantom State Attacks against IIoT Intrusion Detection

- Highlights a vulnerability in IIoT Intrusion Detection Systems (IDS) that reconstruct operational state by aggregating telemetry into temporal windows.
- Proposes the Phantom State Attack (PSA), which shifts packet timing across aggregation-window boundaries under a passive, zero-query threat model to alter the reconstructed state.
- Evaluates PSA, demonstrating that timing manipulation degrades detection on flows carrying enough packets for window-boundary redistribution under weaker assumptions than prior evasion techniques.
- Sabrine Ennaji, Elhadj Benkhelifa, Nadia Kabachi. "Out of Sync, Out of Sight: Phantom State Attacks against IIoT Intrusion Detection." arXiv:2610.02552 — https://arxiv.org/abs/2610.02552
## Containing the Autonomous Operator: A Defense-in-Depth Framework and Reference Architecture for Securing AI Agents on Kubernetes

- Analyzes the security implications of LLM agents operating within Kubernetes infrastructure, where the boundary between data and control planes is blurred.
- Proposes a 10-class threat model focused on prompt injection and tool abuse, alongside a 7-layer defense-in-depth framework using native Kubernetes mechanisms like RBAC, gVisor/Kata sandboxing, and eBPF.
- Provides a reference architecture with concrete policy artifacts for Amazon EKS, Azure Kubernetes Service, and Google Kubernetes Engine, identifying residual risks that require further validation.
- Simhadri Podala Narasimha. "Containing the Autonomous Operator: A Defense-in-Depth Framework and Reference Architecture for Securing AI Agents on Kubernetes." arXiv:2610.02861 — https://arxiv.org/abs/2610.02861
## AgentTrap: Stateful Feedback Deception against Autonomous Penetration Testing Agents

- Notes that conventional, static honeypots fail against autonomous penetration testing agents that adapt to target responses.
- Introduces AgentTrap, a closed-loop honeypot tailored for autonomous penetration testing agents utilizing stateful deception and behavior-guided escalation.
- Evaluates AgentTrap in a deployed web application, demonstrating that it reduces the aggregate real-target attack success rate and successfully elicits attacker API keys, outperforming static deception and fixed escalation.
- Yuelin Wang, Jiongchi Yu, Yanbang Sun. "AgentTrap: Stateful Feedback Deception against Autonomous Penetration Testing Agents." arXiv:2610.02869 — https://arxiv.org/abs/2610.02869
## Intent-Hiding Jailbreaks: An Information-Theoretic Framework for Compositional Attacks

- Studies compositional jailbreaks where harmful intent is obscured by embedding it within seemingly benign tasks, framing the problem through prior-posterior intent matching.
- Evaluates jailbreak effectiveness and preservation of the target behavior across bundle sizes, query generators, and several open-source models.
- Shows that compositional queries can elicit target behaviors beyond the direct-request baseline, but notes a trade-off where increasing the bundle size reduces response-level target preservation.
- Fengwei Tian, Ravi Tandon. "Intent-Hiding Jailbreaks: An Information-Theoretic Framework for Compositional Attacks." arXiv:2610.02302 — https://arxiv.org/abs/2610.02302
## MIRROR: Multipath Quorum Integrity for LLM Multi-Agent Communication

- Highlights that inter-agent communication in LLM Multi-Agent Systems is vulnerable to Agent-in-the-Middle (AiTM) attacks, reaching nearly 100% success rates on structured tasks.
- Presents MIRROR, a communication-layer integrity primitive that replicates a single canonicalized payload across logical routes and accepts messages only when a strict majority agree on an unkeyed hash digest.
- Reduces AiTM attack success to 0% below the threshold at LLM token cost.
- Ryuichi Yamafuji Lun, Jingzhen Wang, Shreyas Kolte, Ruiteng Li. "MIRROR: Multipath Quorum Integrity for LLM Multi-Agent Communication." arXiv:2610.02349 — https://arxiv.org/abs/2610.02349
## Mitigating Private Data Leakage in LLMs with Whiteout

- Addresses the privacy risks of LLMs memorizing and reproducing personally sensitive information (PSI) like birth dates and phone numbers.
- Introduces Whiteout, a practical tool that prevents LLMs from regurgitating genuine PSIs upon requests by individuals.
- Evaluates Whiteout against existing unlearning and refusal alternatives, showing it effectively prevents disclosure of targeted PSIs with negligible impact on model utility and safety.
- Anna Yoo Jeong Ha, Ronik Bhaskar, Haitao Zheng, Ben Y. Zhao. "Mitigating Private Data Leakage in LLMs with Whiteout." arXiv:2610.02418 — https://arxiv.org/abs/2610.02418
## CITADEL: CWE-Guided Insertion of Hardware Trojans via Analysis of DFG-Enabled LLMs

- Addresses the manual burden of constructing realistic hardware trojans (HTs) for integrated circuits that preserve functional correctness.
- Proposes CITADEL, a framework that leverages Large Language Models (LLMs) and Data Flow Graphs (DFGs) to automate CWE-grounded HT synthesis.
- Demonstrates that generated HTs are 100% syntactically correct across diverse RTL designs, remaining functionally triggerable yet undetectable under large-scale random simulation.
- Jayanth Thangellamudi, Raghul Saravanan, Sudipta Paria, Swarup Bhunia, Sai Manoj P D. "CITADEL: CWE-Guided Insertion of Hardware Trojans via Analysis of DFG-Enabled LLMs." arXiv:2610.02544 — https://arxiv.org/abs/2610.02544
## Also published

- Jisung Park, John Le, Heath Cooper. "Hop-Decayed Influence: New Vulnerabilities of Structural Auxiliary Indexing in GraphRAG Pipelines with LLM." arXiv:2610.02373 — https://arxiv.org/abs/2610.02373
- Buxin Su, Qiaoshi Yang, Yiding Su, Chendi Wang. "Unifying Privacy Accounting: Information Equivalence and Information Loss." arXiv:2610.02414 — https://arxiv.org/abs/2610.02414
- Narek Maloyan. "Evaluating and Improving the Robustness of Large Language Models to Input Sequence Variations." arXiv:2610.02432 — https://arxiv.org/abs/2610.02432
- Panagiotis Chatzigiannis, Navid Alamati, Suvradip Chakraborty, Duc V. Le. "SoK: Stablecoins in the Quantum Era." arXiv:2610.02435 — https://arxiv.org/abs/2610.02435
- Mayank Rathee, Alexander Stepanov, Shalin Madabhavi, Jinhao Zhu, Raluca Ada Popa, Ion Stoica. "Pincer: Resource Authorization for Agents using a Digital Twin." arXiv:2610.02569 — https://arxiv.org/abs/2610.02569
- Will Wang, Syh-Yuan Tan, Ryan Chow, Chanson Chan, Martin Zhao. "From TS-SUF-2 to TS-SUF-4: Practical Security Enhancements for FROST2 Threshold Signatures." arXiv:2610.02805 — https://arxiv.org/abs/2610.02805
- Yi Wang, Baicheng Chen, Yu Wang, Jian Zhao, Yilei Chen, Tianxing He. "RMCW: A Deletion-Robust Watermark Based on Reed--Muller Codes for Language Models." arXiv:2610.02817 — https://arxiv.org/abs/2610.02817
- Konstantinos E. Kampourakis, Vyron Kampourakis, Vasileios Gkioulos, Sokratis Katsikas. "Digital Twin-Assisted Mapping of ICS Telemetry to ATT&CK for ICS with Evidence-Driven Dependency Reasoning." arXiv:2610.02955 — https://arxiv.org/abs/2610.02955
- Hang Cui. "Beyond Predefined Sinks: Security-Aware Dependency Analysis for LLM Agents." arXiv:2610.03014 — https://arxiv.org/abs/2610.03014
- Zheng Chen, Fei Yu, Haohao Huang, Yang Li, Anlong Chen, Lei Chen. "SecJev: Bringing Security Expertise to System One Decision Models." arXiv:2610.03073 — https://arxiv.org/abs/2610.03073
- Giulio Zingrillo, Hanna Foerster, Ilia Shumailov, Yiren Zhao, Robert Mullins. "Securing Computer-Use Agents Against Branch Steering Attacks." arXiv:2610.03089 — https://arxiv.org/abs/2610.03089
- Toluwani Aremu, Manit Baser, Mohan Gurusamy, Nils Lukas, Dinil Mon Divakaran. "The Fragility of Trigger-Tag Mechanisms for Misuse Detection in Open-Weight LLMs." arXiv:2610.03124 — https://arxiv.org/abs/2610.03124
- Shiyi Kuang, Xuemei Luo, Kun Liu, Junhai Li, Rui Tian, Feng Shi, Bo Shen, Nianyu Li, Dehui Li, Ping Chen. "EvoRiskBench: An Evolving Benchmark for Runtime Security Risks in Workspace Agents." arXiv:2610.03153 — https://arxiv.org/abs/2610.03153
- Saibo Ye, Huajie Chen, Xin Guo, Le Yang, Chi Liu, Xiangyu Hu, Jingjing Guo, Tianqing Zhu. "LiBRA: Detection-Aware Image Watermark Removal via Bidirectional Latent Optimization." arXiv:2610.03166 — https://arxiv.org/abs/2610.03166
- Sascha Tommasone, Zehra Karada\u{g}, Christopher Pawlowicz, Michael Green, Bruno Machado Trindade, Eunsung Seo, Christof Paar, Ren\'e Walendy, Steffen Becker. "Reversing the Clock: Layout-Aware Recovery of Design Intent from Clock Distribution Networks." arXiv:2610.03182 — https://arxiv.org/abs/2610.03182
- Peiyang Jin, Clouds, Jing Qian. "Asymptotic Analysis of Trading Fees in CFMM." arXiv:2610.03262 — https://arxiv.org/abs/2610.03262
- Mohammadhossein Homaei, Yousef Emami, Sajad Homayoun, Rahim Taheri, Hao Zhou, Miguel Gutierrez Gaitan, Bo Wei. "Defense-in-Depth at the Perception-Reasoning Interface of LLM-Centric Agentic UAV Swarms." arXiv:2610.03319 — https://arxiv.org/abs/2610.03319
- Bijeeta Pal, Sridhar Reddy Maddireddy, Muhaimin Bin Munir, Zoltan Puha, Max Zhurovich, Adi Raghavendra, Sean Tout. "Persona Guardrail: A Production-Grade Defense Framework for Agentic Systems." arXiv:2610.03434 — https://arxiv.org/abs/2610.03434
- Zhuowen Liu. "Passing the Test You Trained On: Re-evaluating Prompt-Injection Detectors for LLM Agents." arXiv:2610.03448 — https://arxiv.org/abs/2610.03448
- Adam Faulkner, Nil-Jana Akpinar, Matthew Dressman. "CorrectGuard: Eyes-Off Correctness Estimation for Black-Box Security Guardrails." arXiv:2610.03470 — https://arxiv.org/abs/2610.03470
- Simon Bernbeck, Ricardo Ramalho, Matheus Amendoeira, Juliana Alves Pereira. "PrivDev: Mapping Static-Analysis Data Types to DPV." arXiv:2610.03518 — https://arxiv.org/abs/2610.03518
- Risa Nonaka, Ryoya Matsuno, Shota Nagai, Satomi Miyagi, Yuki Hayakawa, Ryo Suzuki, Kazuma Ikeda, Ozora Sako, Rokuto Nagata, Ryo Yoshida, Shimpei Ando, Wenlun Zhang, Kentaro Yoshioka. "A Secure dToF LiDAR SoC with Dual-Domain Fingerprinting and Event-Driven AFE Circuit Achieving Sensor-Level Attack Resilience." arXiv:2610.03562 — https://arxiv.org/abs/2610.03562
- Neeraj Karamchandani, Piyush Nagasubramaniam, Xinhong Xie, Sencun Zhu, Dinghao Wu. "Threat-Preserving Representation Sensitivity in Agent-Security Benchmarks." arXiv:2610.03585 — https://arxiv.org/abs/2610.03585
- Kai-Min Chung, Tzu-Hsiang Huang, Wei-Hsiang Hung, Shota Yamada. "Constant-Rate Certified Deletion." arXiv:2610.03590 — https://arxiv.org/abs/2610.03590
- Dominik Roy George, Varesh Mishra, Aysajan Abidin. "PoCoFL: POlicy-COmpliant Federated Learning." arXiv:2610.03650 — https://arxiv.org/abs/2610.03650
- Jiawei Li. "Fast Models, Slow Evidence: A Paired and Self-Audited Evaluation of System-1 Decision Models for LLM Agent Harnesses." arXiv:2610.02267 — https://arxiv.org/abs/2610.02267
- Ziyu Zhao, Xinyu Wang, Xiaowen Chang, Yixuan He. "From Mathematical to Executable Certificates for Machine Unlearning." arXiv:2610.02268 — https://arxiv.org/abs/2610.02268
- Owen Friedewald, Ali Shiri Sichani, Chi-Ren Shyu. "Where Quantum Fourier Sampling Stops Short: A Three-Gate Audit Protocol for Delay-PUF Security Models." arXiv:2610.02636 — https://arxiv.org/abs/2610.02636
- Owen Friedewald, Srikar Alla, Ali Shiri Sichani, Chi-Ren Shyu. "When Normalization Selects the Sign: Auditing Robustness Ablations in Quantum Attention." arXiv:2610.02641 — https://arxiv.org/abs/2610.02641
- Austin Watkins, Raman Arora. "Differential Privacy of Gradient Descent on Perturbed Objectives." arXiv:2610.02716 — https://arxiv.org/abs/2610.02716
- Bishnu Bhusal, Minh Vu, Ben Southworth, Geigh Zollicoffer, Rohit Chadha, Manish Bhattarai. "Inner Momentum for Differentially Private Muon." arXiv:2610.02738 — https://arxiv.org/abs/2610.02738
- Md Nurul Absar Siddiky, Liuwan Zhu, Yingfei Dong. "Frequency Is Not Sensitivity Identifying Safety-Sensitive Experts in Sparse MoE LLM." arXiv:2610.02910 — https://arxiv.org/abs/2610.02910
- Yahn Costa Hackspacher, Cornelius Ihle, Vasundhara Shaw, Dennis Trautwein, Geerd-Dietger Hoffmann, Bela Gipp, Moritz Schubotz. "Quantifying Ethereum Energy Consumption via Network Mapping." arXiv:2610.03440 — https://arxiv.org/abs/2610.03440
- Md Sazid Uddin, Md. Khairul Alam Mazumder, M. F. Mridha. "Certified Mechanistic Edits: Behavioral Guarantees for Skill Removal and Preservation." arXiv:2610.03502 — https://arxiv.org/abs/2610.03502
- Arman Behnam, Binghui Wang. "Reasoning Models Are Accurate but Unsound on Identification." arXiv:2610.03519 — https://arxiv.org/abs/2610.03519
- Rohit Chatterjee, Ananta Mukherjee, Vir Pathak, Supartha Podder. "Quantum Fire with Delegated Cloning." arXiv:2610.03593 — https://arxiv.org/abs/2610.03593
- William Kretschmer, Ewin Tang. "Unitary complexity in polynomial space." arXiv:2610.03705 — https://arxiv.org/abs/2610.03705
- Felix X. -F. Ye, Yu Chin Fabian Lim, Naigang Wang, Davis Wertheimer. "FlashSinkhorn 2: Block-Sparse Entropic Optimal Transport." arXiv:2610.02395 — https://arxiv.org/abs/2610.02395
- Poushali Sengupta, Sabita Maharjan, Frank Eliassen, Yan Zhang. "HXAI: Hierarchical Privacy-Preserving Explainable AI in Distributed Energy Systems." arXiv:2610.02504 — https://arxiv.org/abs/2610.02504
- Sidney Shapiro, Joshua Lindemann. "On-Premises Multi-Course RAG Tutoring for Business Education: Hardware-Software Trade-offs in a Campus AI Tutor." arXiv:2610.02510 — https://arxiv.org/abs/2610.02510
- Stephane Hatgis-Kessell, Myra Cheng, Xiaoxuan Hou, Qian Hu, Rahul Gupta, Natasha Jaques, Emma Brunskill. "Mitigating Social Sycophancy via Pluralistic Preference Optimization." arXiv:2610.02568 — https://arxiv.org/abs/2610.02568
- Seyedarmin Azizi, Erfan Baghaei Potraghloo, Massoud Pedram. "Labels Override Definitions in Jev-Style Typed Decision Models." arXiv:2610.02586 — https://arxiv.org/abs/2610.02586
- Anna T. Thomas, Sohum Patnaik, Caroline Cotto, Benjamin Sanchez-Lengeling. "TasteBench: Multimodal Benchmark for Sensory Prediction, from Molecules to Sustainable Foods." arXiv:2610.02599 — https://arxiv.org/abs/2610.02599
- Tathagata Banerjee, Nima Moghaddas. "Coherence-Driven Belief Formation and Population Dynamics of Contagion in LLM Agents." arXiv:2610.02654 — https://arxiv.org/abs/2610.02654
- Nguyen Ho, Bach Tung Tran, Trung Ky Nguyen, Zhenchang Xia, Bolong Zheng, Long Van Ho. "Label-Efficient Time Series Classification at Scale: A Dual-Stream OSSE-LSTM with Counterfactual Attribution." arXiv:2610.02704 — https://arxiv.org/abs/2610.02704
- Lin Cui, Vincenzo Scotti, Raffaela Mirandola. "CVE2AP: Automated Generation of PDDL-Encoded Attack Paths via Large Language Models." arXiv:2610.03383 — https://arxiv.org/abs/2610.03383
- Yijie Bian, Wei Guo, Jie Yang, Shenghui Song, Jun Zhang, Shi Jin, Khaled B. Letaief. "Multi-Modal Environment-Aware Beam Management for Massive MIMO: A Geometry-Driven Virtual Base Station Framework." arXiv:2606.26567 — https://arxiv.org/abs/2606.26567
- Kwanhee Lee, Namhoon Lee, Dan Alistarh. "Hardware-Native Joint Sparse-Quantization for Trillion-Scale Mixture-of-Experts." arXiv:2610.02241 — https://arxiv.org/abs/2610.02241
- Samuel Kushnir, Kavya Sreedhar, Yeshwanth Reddy Pogula, Amir Yazdanbakhsh, Narges Shahidi, Ming Liu, Varun Gohil, Ravi Iyer, Parthasarathy Ranganathan, Christina Delimitrou, Suvinay Subramanian. "Coco: An Agentic Copilot for the Hardware--Software Co-Design Lifecycle." arXiv:2610.02376 — https://arxiv.org/abs/2610.02376
- Yun-Yun Tsai, Yuning Mao, Shiqi Wang, Junfeng Yang, Sinong Wang. "WebUIProof: Benchmarking WebUI Code Generators with UI-Agent Execution Harness." arXiv:2610.02617 — https://arxiv.org/abs/2610.02617
- Peilin Yang, Xiaoyu Liu, Jian Sun, Qinghua Tao. "Revisiting Visual Representation Enhancement of VLMs via Kernel Canonical Correlation Analysis." arXiv:2610.02718 — https://arxiv.org/abs/2610.02718
- Yuanhao Ban, I-Hung Hsu, Anastasios Angelopoulos, Wei-Lin Chiang, Ion Stoica, Cho-Jui Hsieh. "Post-Training Frontier Text-to-Image Models by Composing Preference and Rubric Rewards." arXiv:2610.02967 — https://arxiv.org/abs/2610.02967
- Runtong Wu, Fei Teng, Di Wen, Guoqiang Zhao, Kunyu Peng, Kailun Yang. "OmniAct3D: Leveraging Foundation Geometry and Evidence-Grounded Reasoning for Panoramic 3D Detection." arXiv:2610.03015 — https://arxiv.org/abs/2610.03015
- Jiangang Han. "WebFovea: When the Model Is Right but the Click Is Wrong -- Reliable Round Trips for Vision-Based Web Agents on Live Websites." arXiv:2610.03036 — https://arxiv.org/abs/2610.03036
- Daifeng Li, Huiqiang Jiang, Chengruidong Zhang, Wei Wu, Xudong Guo, Jianhong Tu, Jianwei Zhang, Binhang Yuan, Dayiheng Liu. "D2K-Bench: Can LLM Agents Turn Expert Designs into Efficient GPU Kernels?." arXiv:2610.03226 — https://arxiv.org/abs/2610.03226
- Amartya Roy, Souvik Chakraborty. "Training-Loss Guarantees for Muon with Finite-Step Newton--Schulz Orthogonalization." arXiv:2610.03306 — https://arxiv.org/abs/2610.03306
- Sarah Shitrit, Ilai Bistritz. "Cordial Learning: Distributed Training with Correlated Data." arXiv:2610.03330 — https://arxiv.org/abs/2610.03330
- Zhihao Zhan, Le Tao, Yifei Tian, Xin Liu, Jie Yuan. "ForestQuery: Boundary-Aware and Spatially Anchored Query Learning for Unified Forest Point Cloud Segmentation." arXiv:2610.03403 — https://arxiv.org/abs/2610.03403
- Chenzhi Liu, Yue Zhang, Jiehong Lin, Jianan Wang, Bo Wang, Zhongrui Wang, Xiaojuan Qi. "MobiAgent: Dual-Loop Recursive Policy Self-Improvement for Long-Horizon Mobile Manipulation." arXiv:2610.03476 — https://arxiv.org/abs/2610.03476
- Thomas Goudemant, Clotilde Szywala, Benjamin Francesconi, Michelle Aubrun, Yves Bobichon, Marjorie Bellizzi, Adrien Girard. "On-Board Anomaly Detection for Efficient Marine Environmental Monitoring." arXiv:2610.03649 — https://arxiv.org/abs/2610.03649
- Mingyan Gao, Celine Wust, Zuming Jiang, Zhendong Su. "BISCEPTER: Probability-Driven Bisection for Large-Scale System Software." arXiv:2610.02995 — https://arxiv.org/abs/2610.02995
- Merve Astekin, Yan Naing Tun, Arda Goknil, Erik Johannes Husom, Lwin Khin Shar, Hasan Sozer, Ratnadira Widyasari, Hui Song. "Engineering Sustainable Agents: A Systematic Comparison of Agentic LLMs for Developer Workflows." arXiv:2610.03010 — https://arxiv.org/abs/2610.03010
