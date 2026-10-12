+++
title = "arXiv Brief — 2026-10-12"
date = 2026-10-12T00:00:00Z
type = "arxiv"
tags = ["hardware", "side-channel", "cloud", "vulnerability-discovery", "fuzzing", "tooling"]
summary = "Hardware side channels through power telemetry, nested enclaves in CVMs, contextual vulnerability scoring, agentic repair, and fuzzing tool boundaries."
+++

## In brief

## HOMARD: Hammering Off-chip Memory via Aggregate power Rail Disclosure
- Shows that unprivileged power sensors on Arm SoCs can recover DRAM addressing functions and data dependence without using timers.
- Identifies DRAM power rails and reads millisecond- and milliampere-resolution telemetry to create two attack primitives: HOMARD-RE and HOMARD-DATA.
- Reaches 81.5% classification accuracy across 9 Hamming-weight levels on a Raspberry Pi 5 by correlating the rail current with data-dependent bit toggling.
- Eliott Quéré, Li-Chung Chiang, Carina Fiedler, Thomas Rokicki, Maria Méndez Real, Alessandro Palumbo, Lilian Bossuet, Rubén Salvador, Daniel Gruss. "HOMARD: Hammering Off-chip Memory via Aggregate power Rail Disclosure." arXiv — https://arxiv.org/abs/2610.12621

## Enabling Extended SGX Enclaves inside Confidential Virtual Machines
- Proposes TEEVisor, an architecture using AMD SEV-SNP Virtual Machine Privilege Levels (VMPLs) to run unmodified SGX binaries inside a guest CVM.
- Achieves under 5% execution overhead on compute- and memory-bound workloads and roughly 12% on I/O-heavy applications against native CVM execution on AMD EPYC.
- Accelerates enclave cloning to a rate of 93 μs/MB, demonstrating practical eSGX semantics with low overhead for production use.
- Pamenas Kariuki, Dong Yiliang, Quoc Do Le, Christof Fetzer. "Enabling Extended SGX Enclaves inside Confidential Virtual Machines." arXiv — https://arxiv.org/abs/2610.12695

## CAPE - Context-Aware Prioritization Engine for Vulnerability Scoring and Management
- Introduces a vulnerability analysis framework that enriches vulnerability reports with deployment-specific evidence for reachability, centrality, and exploitability.
- Evaluates CAPE on 30 open-source agentic applications encompassing 6,138 scanner-reported CVEs to show significant disparities with context-free baselines like CVSS and EPSS.
- Surfaces confirmed-exploitable CVEs at a higher priority than baseline methods by demonstrating that the majority of CVEs are not reachable or exploitable in context.
- Rakesh Podder, Viktoria Koscinski, Indrajit Ray. "CAPE - Context-Aware Prioritization Engine for Vulnerability Scoring and Management." arXiv — https://arxiv.org/abs/2610.13071

## EviRepair: Evidence-Driven Agents for Reliable Vulnerability Repair
- Develops an evidence-driven multi-agent framework for repository-level automated vulnerability repair (AVR) that incorporates an evidence review phase.
- Employs agents to collaboratively collect evidence, verify its consistency, and build a reviewed vulnerability model for synthesizing and validating patches.
- Improves average resolved rates by 16.37% on PatchEval and 40.33% on SecBench compared to existing agent-based baselines.
- Yilian Shi, Qingyu Liu, Tianyi Zhou, Wende Tan, Chenyang Si, Yueming Lyu, Xia Hu, Dongrui Liu. "EviRepair: Evidence-Driven Agents for Reliable Vulnerability Repair." arXiv — https://arxiv.org/abs/2610.13491

## ToFu: Exploiting and Fuzzing the LLM-Orchestrator-Tool Trust Boundary
- Presents a tool-aware framework that automatically generates fuzzing harnesses and semantic security checks from existing LLM tool metadata.
- Evaluates ToFu across 273 MCP servers and 3,405 tools, identifying verified bugs in 343 tools across 118 servers.
- Finds that 73% of tools reach 90% of their final coverage within the first minute of fuzzing with LLM-generated seeds, revealing that real-world tools frequently fail to enforce documented input semantics.
- Md Nazmul Islam Ananto, Pierre Prevost-Avenel, Colin Smith, Kyungtae Kim, Taegyu Kim, Arslan Khan. "ToFu: Exploiting and Fuzzing the LLM-Orchestrator-Tool Trust Boundary." arXiv — https://arxiv.org/abs/2610.13651

## Also published

- Cathleen Qiao, Layah Vigneaud, Chloe Brandon, Max Cabilangan, Xiyuan Cao, Isaac Khabra, Reva Mahajan, Lena Nguyen, Kyle Pak, Anagh Pandya, Roshni Dave, Peiran Wang. "An Exploration of Attacks on AI Agent Systems." arXiv — https://arxiv.org/abs/2610.12524
- Prerna Arote, Adrian Saiz, Lucianna Kiffer. "SoK: Privacy-Preserving Order Matching." arXiv — https://arxiv.org/abs/2610.12535
- Mustafa S. Aljumaily, Ali Ataeemh Allami, Mustafa N. Mnati, Nawar S. Alseelawi, Shahab Abdulla. "PVBRF-ID: Private, Verifiable and Byzantine-Robust Federated Intrusion Detection for Oilfield Enterprise Networks." arXiv — https://arxiv.org/abs/2610.12704
- Ryan McKenna, Arun Ganesh. "Better Batches, Better Privacy: Random Allocation for DP-BandMF." arXiv — https://arxiv.org/abs/2610.12712
- Alireza Abolhasani Zeraatkar, Parnian Shabani Kamran, Parsa Mirfasihi, Saleh Khalaj Monfared, Hussain Al-Asaad. "Power, Performance, and Area of HPC-Based Malware Detectors: An FPGA and Open-PDK ASIC Study." arXiv — https://arxiv.org/abs/2610.12795
- The Anh Nguyen, Triet Huynh Minh Le, M. Ali Babar. "Vulnerable Models in the AI Supply Chain: An Empirical Study of Adoption, Propagation, and Usage Patterns." arXiv — https://arxiv.org/abs/2610.12893
- Andrej Bogdanov, Kel Zin Tan, Prashant Nalini Vasudevan. "Sample-Preserving Search-to-Decision Reduction for Noisy Linear Equations over Large Moduli." arXiv — https://arxiv.org/abs/2610.12913
- Jianting Zhang, Zhongtang Luo, Aniket Kate. "AgentValve: Sybil-Resilient Payment Authorization for Permissionless AI Markets." arXiv — https://arxiv.org/abs/2610.12948
- Jie Cao, Qi Li, Chaklam Cheong, Yutong Jin, Enze Yu, Zelin Zhang, Jianbing Ni. "WaveMark: Robust Wavelet-Domain Image Watermarking for Diffusion Models." arXiv — https://arxiv.org/abs/2610.12952
- Yuying Wang, Yi Guo, Jiachi Chen, Hanwen Zhang, Yi Sun. "Understanding Verification Vulnerabilities in Cross-chain Bridges: An Empirical Study." arXiv — https://arxiv.org/abs/2610.13170
- Dianshu Liao, Shidong Pan, Guangdong Bai, Zhenchang Xing, Xiaoyu Sun. "Understanding and Mitigating Cross-Session Attacks via Persistent Artifacts in Agent Skill Composition." arXiv — https://arxiv.org/abs/2610.13227
- Michael Kuehne-Schlinkert. "Quantization-Tolerant Gradient Auditing for Active Inference-Attack Detection in Federated Learning." arXiv — https://arxiv.org/abs/2610.13311
- Rui Pan, Guanxiong Shen, Linning Peng, Xinyu Qi, Junqing Zhang. "Secrets in Preamble: Practical and Robust PHY Information Hiding for Wi-Fi." arXiv — https://arxiv.org/abs/2610.13367
- Kai Li, Hanlin Cai, Zihao Liu, Yichen Li, Jose Alcaraz Calero, Wei Ni, Falko Dressler, Özgür B. Akan. "Byzantine-Resilient Federated Large Language Model via Hypergraph Message Passing." arXiv — https://arxiv.org/abs/2610.12711
- Yuepeng Hu, Pegah Ghahremani, Reza Aghajani, Mahesh Pasupuleti, Himaghna Bhattacharjee. "Reward Hacking as a Transmissible Strategy in Multi-Agent Coding Systems." arXiv — https://arxiv.org/abs/2610.12822
- Andis Draguns, Sumeet Ramesh Motwani, Raymond Douglas, Christian Schroeder de Witt. "AI Models Can Provably Hide Arbitrary Capabilities." arXiv — https://arxiv.org/abs/2610.13928
- Yiran Wu, Andrew Zhao, Yurui Chang, Qingyun Wu, Xuan Feng. "Beyond Binary Verifiable Rewards: Behavioral Self-Rewarding for SWE Agents." arXiv — https://arxiv.org/abs/2610.12598
- Haotian Qiao, Robert P. Dick. "Faithful and Complete LLM-Assisted Automated Construction of Hierarchical Hardware Knowledge Graphs." arXiv — https://arxiv.org/abs/2610.12762
- Julien Kordes, Reuben Dorent. "Representation Alignment from a Few Paired Data via Distilled Optimal Transport." arXiv — https://arxiv.org/abs/2610.12781
- Zahra Batool, Michael Duchesne, Kaiwen Zhang, Ulrich Aivodji. "DeFiRank: Federated Pairwise Ranking for Governance in Decentralized Financial Networks." arXiv — https://arxiv.org/abs/2610.12916
- Yuheng Wang, Runde Yang, Zhuohan Bao, Qiran Zhang, Huatao Li, Yiyang Zheng, Lin Wu, Jingru Fan, Shu Yao, Yihan Li, Zhi Li, Chen Qian. "Collaborative Learning and Reasoning over Model Slices." arXiv — https://arxiv.org/abs/2610.12927
- Tianyi Huang, Eric Liu, Jay Chong, Emily Yin, Wanqi Zhao. "Provenance-Aware Belief Updating in Human-AI Feedback Loops." arXiv — https://arxiv.org/abs/2610.13008
- Zixuan Weng, Haoqi He, Weifei Jin, Yue Huang, Yang Bai. "Attention Sees, MLP Refuses: Tracing the Attention-to-MLP Safety Pathway in LLMs." arXiv — https://arxiv.org/abs/2610.13078
- Yuchen Ling, Shengcheng Yu, Zhenyu Chen, Chunrong Fang. "When Faster Decisions Do Not Make Better Agents: An Empirical Study of Jev in Agent Workflows." arXiv — https://arxiv.org/abs/2610.13092
- Mohammad Khalooei, Mohammad Sabokrou. "Does Location Matter? A Black-Box Causal Audit Reveals Model-Dependent Audio Grounding in LALM Hallucination." arXiv — https://arxiv.org/abs/2610.13112
- Zhihao Liu, Yitian Cheng, Shuang Liu, Rui Wen, Yuke Hu, Zhan Qin. "DP-MIND: Differentially private memory-guided Long context Inference." arXiv — https://arxiv.org/abs/2610.13132
- Lei Liu, Yunji Liang, Xiaowen Zhang, Jingqi Liu, Qi Li, Bin Guo, Zhiwen Yu. "Forgetting is Not Always Bad: A Neuro-Inspired Memory Repair Mechanism for Poisoned LLM Agents." arXiv — https://arxiv.org/abs/2610.13267
- Octi Zhang, Iretiayo Akinola, Rosario Scalise, Mateo Guaman Castro, Patrick Yin, Tobias Widmer, Miles Macklin, Chris Amevor, Dylan Turpin, Dirk Van Gelder, Jan Carius, Ankur Handa, Gavriel State, Yunrong Guo, Yashraj Narang. "AlphaNIST: Emergent Assembly Skills from Binary Task Rewards." arXiv — https://arxiv.org/abs/2610.13354
- Sunghwan Kim, Deogyong Kim, Sangam Lee, Donguk Kwon, Dongha Lee. "Web$hell: A Unified Interface for Agentic Web Access." arXiv — https://arxiv.org/abs/2610.13416
- Donatella Genovese, Philip Ploner, Simone Scardapane, Stefano Giagu, Thea Klaeboe Aarrestad. "Local Diagnostics of Learned Event Representations for Anomaly Detection at the HL-LHC." arXiv — https://arxiv.org/abs/2610.13437
- Pablo Manrique, Hai Xia, Stefan Szeider. "SqueezeBench: Saturation-Resilient Evaluation of Mathematical Capability." arXiv — https://arxiv.org/abs/2610.13461
- Victoria J. Hodge, Colin Paterson, Rob Alexander. "A Local Agentic AI Framework to Generate Edge Case Scenarios for Safety Assurance." arXiv — https://arxiv.org/abs/2610.13479
- Changye Li, Zijian Zhang, Muheng Li, Yiduo Pang, Tingjun Wu, Menghan Li, Yitong Liu, Hongkai Guo, Mengchi Chen, Chenyu He, Kaisheng Ma, Wei Xu, Song Han, Sihao Liu, Ligeng Zhu. "Humanize MLE Agents: Multi-Agent Session Alternation Beyond Single-Agent Limits." arXiv — https://arxiv.org/abs/2610.13494
- Weixin Guan, Liang Li, Shiyu Xie, Jiapeng Liu, Bing Li, Peng Fu, Chengyang Fang, Xiaoshuai Hao, Can Ma, Weiping Wang. "Constructing Pareto Frontiers of Optimal Reasoning Termination Methods for Overthinking in Reasoning Models." arXiv — https://arxiv.org/abs/2610.13570
- Guanlan Yue, Hang Yu, Xiaoyong Huang, Ruipeng Li, Wei Zhang, Bingchang Liu, Rui Wang. "MENTOR: Learning from Failure with On-Policy Pedagogical Intervention." arXiv — https://arxiv.org/abs/2610.13594
- Helmut Simonis. "Learning Size Independent Constraint Models from Input Data and Positive and Negative Example Solutions." arXiv — https://arxiv.org/abs/2610.13640
- Naji Alazhar, Wassel Alazhar. "Adaptive DHiSparse: Speculative Decoding over a Load-Adaptive KV Hierarchy." arXiv — https://arxiv.org/abs/2610.13708
- Fabien Furfaro. "Kairos: Toward a Byte-Level Foundation Model for Every Modality." arXiv — https://arxiv.org/abs/2610.12495
- Nhan Thanh Nguyen, Phuong Nam Tran, Mengyuan Ma, Huy T. Nguyen, Ahmed Alkhateeb, Markku Juntti. "Energy-Efficient Spiking Neural Networks for Sensing-Aided Beam Prediction." arXiv — https://arxiv.org/abs/2610.12507
- Joshua Maccoby, Wendy Hui Wang. "REDaCT: Collapse-Free Unlearning in Large Reasoning Models." arXiv — https://arxiv.org/abs/2610.12769
- Khubaib Ahmed, Ahsan Adeel, Nasir Saleem, Kia Dashtipour, Ahsan Ulhaq, Amir Hussain. "Efficient Audio-Visual Speech Enhancement via Reinforcement Learning-Based Neural Architecture Search." arXiv — https://arxiv.org/abs/2610.12796
- Hadi Keramati, Mohammed A. Hannan, Patrick Kirchen, Sina Tousi, Joonas Riekkinen, Jim Pyra, Rajeev K. Jaiman. "Localized Generative Design of Ship Hulls with Diffusion Models and High-Fidelity Assessment." arXiv — https://arxiv.org/abs/2610.12870
- Raghavv Goel, Sudhanshu Agrawal, Mukul Gagrani, Risheek Garrepalli, Mingu Lee. "Surfing the Activation Wave: Analyzing the Information and Geometry of LLM Hidden States for Speculative Decoding." arXiv — https://arxiv.org/abs/2610.12939
- Gangyi Li, LuYao Wang, Jingfu Sun, Jingyi Yuan, Hang Liu, Hao Zong, Yujia Hu, Tingting Gao, Jianyong Wang, Xu Yang. "JoyInside-VLM-Agent: Product-Conditioned Multimodal Policy Learning for Embodied Agents." arXiv — https://arxiv.org/abs/2610.12957
- Irene Cannistraci, Julia E. Vogt. "Tabular Foundation Models Are Effectively Shallow." arXiv — https://arxiv.org/abs/2610.13253
- Lifeng Wang, Xintong Li, Aifei Liu. "CNN-Transformer with Sigmoid Label for High-Resolution Sub-Degree DOA Estimation." arXiv — https://arxiv.org/abs/2610.13433
- Joseph Egan, Ciarán M. Gilligan-Lee, Michael O'Riordan, Yuchen Zhu. "Defence against the dark arts of distillation: Unsupervised discovery of subliminal learning." arXiv — https://arxiv.org/abs/2610.13536
- Xiting Liu, Lin Yang, Yitong Zhang, Jia Li, Shi-Min Hu. "SWE-DeceptionBench: Benchmarking Deceptive Behaviors of LLMs Across the Software Development Lifecycle." arXiv — https://arxiv.org/abs/2610.13626
- Jayanie Bogahawatte, Sachith Seneviratne, Simon Maksour, Dzung Do-Ha, Elizabeth Qian, Samuel Brennan, Matthew Keon, Lezanne Ooi, Saman Halgamuge. "Model-agnostic Knowledge Augmented Machine Learning for Weakly Annotated Bioimaging Data." arXiv — https://arxiv.org/abs/2610.13637
- Weiqi Sun, Qianyue Wu, Wenjia Wang, Tianyang Hu. "Not All Dimensions Are Equal: Outlier-Aware Attention Linearization with Grouped Quadratic Kernels." arXiv — https://arxiv.org/abs/2610.13674
- Hendrik Stumpf, Francesco Quinzan. "Amortized Counterfactual Prediction with Graph Neural Networks." arXiv — https://arxiv.org/abs/2610.13724
- Adarsh Jamadandi, Nicolas Keriven. "Your Discrete Graph Diffusion Model is Secretly Memorizing." arXiv — https://arxiv.org/abs/2610.13786
- Jiageng Wu, Chao Shen, Zihan Guo, Junyan Shao, Zongyan Zhang, Jie Song, Zhong Li, Mingyang Sun. "Fix What's Wrong, Keep What's Right: Hallucination Repair for LLM-Based Optimization Modeling." arXiv — https://arxiv.org/abs/2610.12529
- Oleg Grynets, Ivan Fedorchuk, Vasyl Lyashkevych. "Leakage-Resistant Evaluation of AI-Generated Database Specifications in Specification-Driven Migration." arXiv — https://arxiv.org/abs/2610.12778
- Md Safayat Hossen, Sheikh Moonwara Anjum Monisha, Shadid Intisar Quasem. "Evaluation of Software Quality Through Refactoring Commit-Impact Analysis." arXiv — https://arxiv.org/abs/2610.12890
- Yu Zhang, Corina S. Pasareanu, Guowei Yang. "REINS: Agent-guided Thread Scheduling for Concurrency Bug Detection and Reproduction." arXiv — https://arxiv.org/abs/2610.13421
- Han Peng, Xing Hu, Feifei Niu, Huan Li, Xin Xia. "Not All Correct Fixes Run Alike: An Empirical Study of Patch Performance in Repository-Level Issue Resolution." arXiv — https://arxiv.org/abs/2610.13563
- Tian Jin, Wenhao Wang, Jing Kang, Haoting Shi, Rui Ye, Yijun Lu, Siheng Chen. "SoftwareGym: Scaling Computer-Use Agent Training with Diverse Synthesized Software Environments." arXiv — https://arxiv.org/abs/2610.12611
