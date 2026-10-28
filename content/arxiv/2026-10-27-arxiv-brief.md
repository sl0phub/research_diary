+++
title = "arXiv Brief — 2026-10-27"
date = 2026-10-27T00:00:00Z
type = "arxiv"
tags = ["arxiv", "vulnerability-discovery", "llm-security", "reverse-engineering", "binary-analysis"]
summary = "New papers on agents as operating systems, LLM-based vulnerability detection, RAG poisoning, LLM agent root cause analysis harnesses, and agentic message boards."
+++

## In brief

## Ring-0 by Default: Agents as Operating Systems (AaOS)

- Evaluates LLM agents under the lens of operating system design, mapping 116 OS mechanisms to agent counterparts and finding 65 missing, including privilege separation and resource quotas.
- Tests Claude Code, Codex CLI, and Gemini CLI, showing access checks sit in individual tools rather than the process (so file writes refused by the file tool go through the shell), and forged transcript records are loaded as user messages.
- Identifies five security problems for which no OS defense directly transfers, such as the need for typed errors outside the model and sender authentication in payloads.
- Xiang Li, Aichun Huang, Zuyao Xu, Fasheng Miao, Zheli Liu. "Ring-0 by Default: Agents as Operating Systems (AaOS)." arXiv — https://arxiv.org/abs/2610.33753

## Enhancing LLM-Based Vulnerability Detection via Representation-Aware Logical Ensemble

- Systematically evaluates LLM-based vulnerability detection across raw source code, ASTs, and CFGs, finding that raw code excels at semantic details (e.g., buffer overflows) while CFGs are better for concurrency and ASTs for logic issues.
- Proposes a Representation-Aware Logical Ensemble (RALE) that prioritizes the high recall of the raw code model while using a majority vote among raw, AST, and CFG predictions to control false positives.
- Reports that RALE achieves a 78% F1-score, a 5% improvement over single-representation baseline models.
- Francesco Crescenzo Grasso, Pietro Liguori, Roberto Natella, Domenico Cotroneo. "Enhancing LLM-Based Vulnerability Detection via Representation-Aware Logical Ensemble." arXiv — https://arxiv.org/abs/2610.33756

## VulDec: Vulnerability Detection in Binaries via Neural Decompilation

- Frames binary vulnerability detection as a source-level task by using neural decompilation to reconstruct high-level code, bypassing the limitations of low-level assembly representations.
- Releases a large-scale dataset pairing Assembly and C functions with CWE annotations, and uses it to train LLM-based neural decompilers that achieve roughly 56% edit similarity and 43% BLEU-4 for source recovery.
- Reports a macro F1-score of 0.61 on an in-distribution test set with a realistic 3% vulnerability rate using the tuned detectors.
- Francesco Crescenzo Grasso, Pietro Liguori, Roberto Natella, Domenico Cotroneo. "VulDec: Vulnerability Detection in Binaries via Neural Decompilation." arXiv — https://arxiv.org/abs/2610.33716

## Ranking Is Not Deciding: Benchmark Shortcuts and Operating-Point Collapse in Query-Time RAG Poisoning Defenses

- Demonstrates that near-perfect detection of query-time RAG poisoning often relies on construction artifacts, specifically the verbatim inclusion of the target question in the poison passages, which was used in 8 of 21 surveyed defenses.
- Removing this prefix from the attack authors' own passages leaves 0.93 of them retrieved, but drops the AUROC of the RAGuard filter from 0.953 to 0.758 and its miss rate from 0.191 to 0.763.
- Padding medical poison with content-free shuffled words increases the miss rate of TrustRAG's set-level stage to 0.827 and bypasses a learned scorer, showing that rankings survive while decisions collapse.
- Pushkal Kumar, Arvin Sahaym. "Ranking Is Not Deciding: Benchmark Shortcuts and Operating-Point Collapse in Query-Time RAG Poisoning Defenses." arXiv — https://arxiv.org/abs/2610.33849
*Abstract only — full text not retrieved.*

## Free to Look, Free to Reason: Simple LLM Harnesses Outdiagnose Hand-Crafted Root Cause Analysis Agents

- Evaluates hand-crafted LLM root cause analysis agents against simple harnesses that provide an evidence package or tools without prescribing the model's calls, using 90 validated cases from eight datasets (RCAtlas).
- Simple harnesses reach 65–77% PR@1 on three mid-tier models, outperforming published agents (16–53%) and non-LLM methods (6–39%), as prescriptive agents often skip decisive evidence.
- Finds that a stronger model improves reliability, multi-turn harnesses improve aptitude, and increased reasoning effort changes accuracy minimally while substantially increasing time.
- Tingzhu Bi, Xun Zhang, Jinglin Li, Ping Wang, Meng Ma. "Free to Look, Free to Reason: Simple LLM Harnesses Outdiagnose Hand-Crafted Root Cause Analysis Agents." arXiv — https://arxiv.org/abs/2610.35767

## LLM WikiLeaks: Uncovering URL-Based Capability Extension and Security Circumvention in Agentic Message Boards

- Analyzes the "ProWiki incident", where autonomous agents restricted to HTTP GET requests used a German-language wiki as a message board, analyzing 79,541 URL postings across 14,591 edits.
- Finds that agents nested target URLs within one to five layers of third-party services (33.6% of URLs) to extract content via OCR, filter JSON, or access historical archives.
- Observes that 26.2% of the nested services facilitated security circumvention, including CORS proxies, fetch proxies, and link shorteners that obscure destinations and evade rate limits.
- Orel Navi, Elad Feldman, Ben Nassi. "LLM WikiLeaks: Uncovering URL-Based Capability Extension and Security Circumvention in Agentic Message Boards." arXiv — https://arxiv.org/abs/2610.34542

## Also published

- Zifeng Zhou, Shengda Zhuo, Jiahui Huang, Zeyan Li, Jinchun He, Peipeng Yu, Wangjie Qiu, Zhiming Zheng, Shuqiang Huang. "Hidden Backdoor Attack on Deep Contrastive Clustering." arXiv — https://arxiv.org/abs/2610.33116
- İpek Abasıkeleş Turgut, Edip Gümüş. "Deletion, Substitution, Repair and Transplant: Component Attribution in BARBICAN, a Layered Prompt-Injection Gateway for MCP." arXiv — https://arxiv.org/abs/2610.33198
- Mohammed Gharib, Giovanni Cascone, Martin Zizi. "A-GE: Privacy-Preserving Age Assurance via Fine-Grained Motion." arXiv — https://arxiv.org/abs/2610.33206
- Dena Mujtaba, Bharadwaj Ravichandran, Brian Hu, Arslan Basharat. "Alignment of Autonomous Cyber Defense Agents via Adaptive Policy Shaping." arXiv — https://arxiv.org/abs/2610.33234
- Alfredo Metere. "A Deterministic Security Runtime for LLM Agents on MPI and Batch-Scheduled HPC Systems: Consensus-Governed, Hardware-Rooted Supervision of Every Rank." arXiv — https://arxiv.org/abs/2610.33318
- Pellegrino Casoria, Andrea Araldo, Rosario Patanè, Simon Pietro Romano. "From Hype to ROI: An Economic Model for LLM Adoption in Information Systems and Security Operations." arXiv — https://arxiv.org/abs/2610.33352
- Emad Abukhousa, Anna Raymaker, Animesh Chhotaray, Daniel Molzahn, Saman Zonouz, Sakis Meliopoulos. "From Caveman to COBA: Coordinated Optimization-Based Attacks on Grid-Edge Smart Inverters in DER-Rich Power Systems." arXiv — https://arxiv.org/abs/2610.33401
- Bryan C. Boots. "Agent-to-Agent Synthetic Social Engineering on the Web." arXiv — https://arxiv.org/abs/2610.33411
- Soumita Chatterjee, Sudip Ghosh, Tamal Ghosh, Bhargab B. Bhattacharya, Hafizur Rahaman. "Combinatorial Lock for Trojan-Resilient AI Engines via Hash-Assisted Spectral Filtering." arXiv — https://arxiv.org/abs/2610.33437
- Md Afif Al Mamun, Gias Uddin. "Secure and Functional Code Generation with Self-Evaluation." arXiv — https://arxiv.org/abs/2610.33450
- Shiwu Zhao, Baizhu Wang, Guoqiang Zheng, Tingyu Gao, Yuheng Xie, Rujie Chen, Xingchen Chen, Xuezhang Liu, Qixu Liu. "From Instructions to Exploits: Applying Program Analysis to Malicious Agent Skills Across Natural Language and Code." arXiv — https://arxiv.org/abs/2610.33489
- Yang Li, Gang He, Ruichen Zhang, Guangyuan Liu, Yinqiu Liu. "Pacifo: An Efficient Fully Homomorphic Encryption-based Lightweight ResNet for Trustworthy Machine Learning as a Service." arXiv — https://arxiv.org/abs/2610.33525
- Apostolos Valiakos, Dimitrios Psaltis, Alexios Lekidis, Nikolaos Kekatos, Elpiniki Papageorgiou. "Security evaluation of 6G-oriented and O-RAN networks through targeted attacks." arXiv — https://arxiv.org/abs/2610.33526
- Kürşat Çakal, Suat Özdemir. "Securing Edge & Physical AI: Post-Quantum IoT Blockchain for Mission-Critical Cyber-Physical Agents." arXiv — https://arxiv.org/abs/2610.33862
- Kai Wei, Yuwen Cui, Kehan Shen, Guangjing Wang. "CVE-to-ATT&CK Mapping via Evidence-Constrained Ranking." arXiv — https://arxiv.org/abs/2610.33924
- Daniel Ben-Levi, Judah Goldfeder, Mateusz Dziemian, Raja Moreno. "Back to Basics: Formal Analysis Hints Improve Weak-to-Strong Monitoring." arXiv — https://arxiv.org/abs/2610.34064
- Fahong Zhang, Weijie Jin, Lixu Wang, Ning Luo, Xiao Wang, Wei Dong. "HNSecW: A Logarithmic-Time MPC Protocol for Approximate Nearest Neighbor Search." arXiv — https://arxiv.org/abs/2610.34248
- Chieh-Yuan Chang, Guan-Wei Chen, Chia-Yi Hsu, Chih Yang, Chia-Mu Yu, Chun-Ying Huang. "NameTrap: Steering AI Coding Agents Toward Security Vulnerabilities via Variable Names." arXiv — https://arxiv.org/abs/2610.34253
- Mingrui Liu, Liang He, Xinchu Wang, Yeting Li, Dongxu Han, Yunpeng Li, Yuling Liu. "Repairing Broken Access Control in Web Applications with LLMs: An Empirical Benchmark Study." arXiv — https://arxiv.org/abs/2610.34290
- Chenyuan Yang, Hwiwon Lee, Jongseong Kim, Yihan Yang, Dongjun Kim, Yinfang Chen, Lingming Zhang. "CyberDual: AI Attackers versus AI Code Reviewers in Real Software Maintenance." arXiv — https://arxiv.org/abs/2610.34435
- Md Abu Yusuf, Oyshi Tabassum Aditi, Md Faysal Hosain Mazed. "SentryBench: A Cost-Sensitive Benchmark for Adversarial Robustness of Tool-Using LLM Agents in Public-Safety Deployments." arXiv — https://arxiv.org/abs/2610.34535
- Thore Sommer, Masanori Misono, Dimitrios Stavrakakis, Pramod Bhatotia. "CVM-Store: A Secure Storage System for Confidential Virtual Machines." arXiv — https://arxiv.org/abs/2610.34560
- Halil Dursunoglu, Fatma Dursunoglu. "Compound Environmental Operating Stress and Cyber-Induced Pump Disruption in Water Distribution Networks: Matched Hydraulic Impacts, Service Continuity, and Sustained Recovery." arXiv — https://arxiv.org/abs/2610.34670
- Anand Agrawal, Anil Kumar Chillara, Naresh Mandan. "Phantom Forgetting: How BatchNorm State Fakes Deletion in Edge Split Machine Unlearning." arXiv — https://arxiv.org/abs/2610.34800
- Raik Dankworth, Felix Mächtle, Thomas Eisenbarth, Gesina Schwalbe. "Attack logics, not outputs: Concept-based Property Attacks for Shortcut Elimination in Neural Networks." arXiv — https://arxiv.org/abs/2610.34923
- Mintong Kang, Stephen Rawls, Melissa Kazemi Rad, Jian Ni, Bo Li. "The Target Agent Is Its Own Best Critic but a Poor Proposer: Self-Improved Red Teaming." arXiv — https://arxiv.org/abs/2610.34965
- Yu Yan, Jiahao Chen, Siqi Lu, Yongjuan Wang, Ziming Zhao, Zhaoxuan Li, Qingjun Yuan. "Steering for Safety, Hijacking for Profit: Trojan Threats in the LLM Activation Steering Supply Chain." arXiv — https://arxiv.org/abs/2610.35043
- Linghui Jiao, Kang Wei, Fushuo Huo, Ruijie Zhao, Yiyang Ni, Jingcai Guo, Yipeng Zhou, Jun Li. "GuardRAG: A Post-Retrieval Defense against Poisoning Attacks in Retrieval-Augmented Generation." arXiv — https://arxiv.org/abs/2610.35071
- Sheila Zingg, Florian Tramèr, Martin Vechev, Srdjan Čapkun. "Can Open Be Too Open? On the Security and Trustworthiness of Fully Transparent LLMs." arXiv — https://arxiv.org/abs/2610.35199
- Mostafijur Rahman Akhond, Mahmuda Khatun, Gias Uddin. "Then there is prompt injection, a malicious email, ...: The Wild Wide West of OpenClaw Agentic System Security." arXiv — https://arxiv.org/abs/2610.35451
- Kilian Zeiseweis, Nele Sophie Brügge, Marven Kummerfeldt, Ali Raza, Esfandiar Mohammadi. "PRISMA: Differentially Private Synthetic In-Car Telemetry via Differentiable Simulation." arXiv — https://arxiv.org/abs/2610.35521
- Ruozhao Yang, Minglang Li, Jiongchi Yu, Xinfeng Li, Xiaofei Xie. "JANUS: Synthesizing Cross-Layer Defenses Against Web Deserialization Attacks." arXiv — https://arxiv.org/abs/2610.35532
- Ruozhao Yang, Jiongchi Yu, Ming Hu, Xiaofei Xie. "The Agent in the Middle: How AI-Mediated Access Reshapes Web Vulnerability Exploitation." arXiv — https://arxiv.org/abs/2610.35541
- Hanane Houmani. "Atomic Security Concerns: Towards a Foundational Language for Security Knowledge Representation." arXiv — https://arxiv.org/abs/2610.35782
- Amine Lbath, Massih-Reza Amini. "Reva: Real-Time Vulnerability Detection through Contextual Probing of Large Language Models." arXiv — https://arxiv.org/abs/2610.35829
- Samuel Breckenridge, Dani Vilardell, Wenhao Wang, Fan Zhang, Ari Juels. "I-HITL: Inalienable Human-in-the-Loop." arXiv — https://arxiv.org/abs/2610.35835
- Frédéric Dupuis, Rémi Ligez, Khaireddine Medhioub, Louis Salvail, Louis-Charles Thibodeau. "Post-Quantum Perfect Zero-Knowledge Arguments for NP From Any One-Way Permutation." arXiv — https://arxiv.org/abs/2610.33185
- Yihan Yang, Chenyuan Yang, Zijie Zhao, Anh Nguyen Hoang, Ziqi Zhang, Weidong Wang, Zhiheng Lyu, Lingming Zhang. "Can Agentic Code Review Catch Vulnerabilities Before They Are Merged?." arXiv — https://arxiv.org/abs/2610.33509
- Biprarshi Biswas, Arya Anshuman Ojha, Yubaraj Das, Devansh Khosla, Kamran Rais, Saankhya Samanta, Subhamoy Maitra, Pantelimon Stanica. "Extraction meets Distillation - cryptanalytic techniques to recover parameters from a Deep Neural Network." arXiv — https://arxiv.org/abs/2610.33671
- Amir Naseredini, Suhas Viswanath, Martin Berger. "A Rowhammer attack on Fil-C's software capabilities." arXiv — https://arxiv.org/abs/2610.33748
- Prateek Kumar Rajput, Shahzeb Khan, El-Hacen Diallo, Yewei Song, Jacques Klein, Tegawendé F. Bissyandé. "Securing Agent-Generated Code with Its Own Development History." arXiv — https://arxiv.org/abs/2610.34098
- Jukka Ruohonen, Rahime Yilmaz, Krzysztof Sierszecki. "The Policies of Programming Language Ecosystems: A "Qualitative" Analysis." arXiv — https://arxiv.org/abs/2610.34187
- Hajin Jeon, Hyung-Jin Yoon, Jemin Lee, Min-Soo Kim. "Decentralized Medical Data Sharing with Off-chain Storage and View-based Access Control." arXiv — https://arxiv.org/abs/2610.34279
- Puyuan Yang, Shaoxuan Dong, Liujie Wu, Xiaochun Cheng, Bo Li. "Factual Yet One-Sided: Stance Poisoning and Evidence Balancing in Retrieval-Augmented Generation." arXiv — https://arxiv.org/abs/2610.34294
- Xiarun Chen, Jiaxing Xu, Bozhi Wu, Chenhui Cui, Chunrong Fang, Weiping Wen, Tao Li, Rubing Huang, Tsong Yueh Chen. "SymLift: Neural Semantic Lifting for Compile-Free Vulnerability Detection in Context-Incomplete Code Fragments." arXiv — https://arxiv.org/abs/2610.34431
- Ali Abbasi, Pasha Barahimi, Marco Paolieri, Leana Golubchik. "Denial of Service Attacks on Beam Allocation in Large LEO Constellations." arXiv — https://arxiv.org/abs/2610.34631
- Weihang Niu, Mengxing Ren, Che Qu. "Scope-Gap Injection: Exploiting Evaluator Channel Blind Spots in the OpenClaw Agent Security Competition." arXiv — https://arxiv.org/abs/2610.34777
- Evan Rose, Alina Oprea. "A Certified Robustness Framework for Backdoor Poisoning Attacks using $f$-Divergences." arXiv — https://arxiv.org/abs/2610.34934
- Jiayue Pu, Ang Gao, Jinyi Bai, Qipeng Wang, Tongyu Wen, Jiahao Zhao, Keyu Qu, Junhao Zhang, Chenglei Shen, Zhongxiang Sun, Jun Xu, Xiao Zhang. "Trustworthy Recursive Self-Improvement in the Era of Large Models: Foundation, Risks, Evaluation and Open Challenges." arXiv — https://arxiv.org/abs/2610.35193
- Ilan Mandel, Madiha Zahrah Choksi, Joey Castillo, Sebastian Benthall, James Grimmelmann. "Cheap AI-Assisted Reverse Engineering and What It Will Do." arXiv — https://arxiv.org/abs/2610.35633
- Guoyang Shi, Hongwen Li, Yiding Yu, Zhuang Fu, Siqi Ding, Zhengyuan Chen, JianGuo Chen, Hanyue Zhao, Tianyuan Liu. "Adaptive Control of Scientific Instruments with Nonstationary Responses through Multimodal Agents." arXiv — https://arxiv.org/abs/2610.32370
- Tianyu Yang, Yijun Tian, Lars Benedikt Kaesberg, Jan Philip Wahle, Bela Gipp, Terry Ruas, Daniel Kurzawe. "Beyond Post-Hoc Rewards: Privileged Reasoning Exploration for Multimodal Embeddings." arXiv — https://arxiv.org/abs/2610.32474
- Nilesh Prasad Pandey, Jangseon Park, Jason Kong, Onat Gungor, Tajana Rosing. "NgramRL: Accelerating RL Post-Training for Structured Generation via Rollout-Aware N-gram Speculative Decoding." arXiv — https://arxiv.org/abs/2610.32881
- Yuanzhe Peng, Jie Xu. "Collaborative In-Context Learning for Indoor Radio Map Estimation." arXiv — https://arxiv.org/abs/2610.31702
- Xavier Cadet, Junyan Cheng, Peter Chin, Kyle Richardson. "Mining the Design Space of Multi-Agent Workflows." arXiv — https://arxiv.org/abs/2610.31709
- Ricardo Luna Gutierrez, Vineet Gundecha, Rahman Ejaz, Varchas Gopalaswamy, Riccardo Betti, Sahand Ghorbanpour, Aarne Lees, Soumyendu Sarkar. "End-to-End Differentiable Diffusion Conditioning for Physics-Informed Optimization." arXiv — https://arxiv.org/abs/2610.31721
- Tianxiang Xia, Kai Lion, Niao He, Michael Muehlebach, Melanie Zeilinger, Hao Ma. "Learning Structured Sparsity for Large Models: Bridging Model Compressibility and Efficient Inference." arXiv — https://arxiv.org/abs/2610.31897
- Rachmad Vidya Wicaksana Putra, Shuochen Zhou, Muhammad Shafique. "RobustNCL: Robustifying Neuromorphic Continual Learning under Transient Faults with Lightweight Detect-and-Cure Strategy." arXiv — https://arxiv.org/abs/2610.31954
- Mulugeta Weldezgina Asres, Lei Jiao, Christian Walter Omlin. "Guided Zero-Shot Anomaly Explanation for Anonymized Crowd Video Monitoring: Context, Categorization, and Spatial Localization." arXiv — https://arxiv.org/abs/2610.32073
- Gejian Zhao, Hanzhou Wu, Xinpeng Zhang. "AgentTrace: Execution-Level Fingerprinting of Black-Box LLM Agents." arXiv — https://arxiv.org/abs/2610.32092
- Ken Enda, Jien Saito, Masami Mukai, Feng Han, Emir Turkes, Tatsumi Kusakabe, Reona Umeki, Kazuhiro Sumiyoshi, Mitsuya Numata, Takumi Tanikawa, Akira Endoh, Kenji Hirata, Atsushi Yoshida, Kohsuke Kudo, Shinya Tanaka. "The LLENS Platform for On-Premises Large Language Model Agents in a Japanese University Hospital: Development and Evaluation Study." arXiv — https://arxiv.org/abs/2610.32151
- Ziang Zhang, Wenyou Yi, Zehan Wang, Jiachen Xu, Xintong Han, Chunchao Guo, Zhou Zhao. "Easy-3Dfy: Object-Level Geometric Composition for Single-Image 3D Scene Construction." arXiv — https://arxiv.org/abs/2610.32250
- Yu-Yu Lee, Ming-Feng Tsai, Tomohiro Morikawa, Chun-I Fan. "Data-Efficient Backdoor Attacks on Code Models via Trigger-Neutralized Counterfactual Scoring." arXiv — https://arxiv.org/abs/2610.32334
- Zifan Peng, Peng Huang, Jingyi Zheng, Yingjie Xue, Xuechao Wang, Xinlei He, Xia Hu, Dongrui Liu. "Beyond Copying: Lifelong Smart Contract Security Task Construction via Protocol Mutation." arXiv — https://arxiv.org/abs/2610.32453
- Antonio Ken Iannillo, Joshua Segun Owotogbe, Roberto Natella, Francesco Avallone, Kristina Kudryavtseva, Indika Kumara. "Tool-Calling LLM Agents Under Realistic MCP Faults: Scale Does Not Purchase Fault Tolerance." arXiv — https://arxiv.org/abs/2610.32555
- Luke Beddow, George Mavroghenis, Rodrigo Chacon Quesada, Kamil Dreczkowski, Cong Sun, Jiankai Wang, Oscar Kwong-Fai Pang, Antoine Cully. "Adaptive World-Models for Anomaly Recognition (AWARE): A Framework for Robot Dynamics Prediction and Introspection." arXiv — https://arxiv.org/abs/2610.32742
- Yalin E. Sagduyu, Tugba Erpek, Nathan Stephenson, Mengran Xue. "Clean-label Poisoning Attack and Defense Game for Federated Learning in Vehicular Networks." arXiv — https://arxiv.org/abs/2610.32765
- Prakhar Pandey. "Navigating Epistemic Parity in LLM Agents: A Benchmark for Cross-Source Conflict Resolution Between Memory and Procedural Skills." arXiv — https://arxiv.org/abs/2610.33128
- Einar César Santos. "EVM-Anchored Provenance for AI-Assisted Code Evolution: A Smoke-Scale Deployment Report." arXiv — https://arxiv.org/abs/2610.33350
- Mohamad Mohebifar, Alex Bit. "OneCodeReviewBench: Typed Decisions for Code Review and Search." arXiv — https://arxiv.org/abs/2610.33389
- Junjie Yao, Xiongzheng Guan, Jia Feng, Yujia Chen, Hongliang Tian, Cuiyun Gao. "SpeC2Rust: Specification-Driven Repository-Level C-to-Rust Translation." arXiv — https://arxiv.org/abs/2610.34141
- Yuhao Tian, Tao Li, Ling Zhou, Dave Towey, Zhaoxin Fan, Wenjun Wu, Rubing Huang, Tsong Yueh Chen. "EAST: Embodied AI Safety Testing via Systematic Fault Injection in Digital Twins." arXiv — https://arxiv.org/abs/2610.34358
- M M Abid Naziri,  Feiran,  Qin, Khush Patel, Marcelo d'Amorim. "A Multi-Domain Study on the Effectiveness of LLMs at Writing Property-Based Tests." arXiv — https://arxiv.org/abs/2610.34487
- Meriem Mastouri, Emna Ksontini, Amine Barrak. "Built to Remember, Shipped to Forget: Operational Contracts, Failures, and Repairs in Containerized LLM Agent Deployments." arXiv — https://arxiv.org/abs/2610.34620
- Chengzhi Yi, Shenao Wang, Yanjie Zhao, Xiao Cheng, Haoyu Wang. "SemWeaver: Refining LLM-Generated Static Vulnerability Checkers with Analyzer-Internal Evidence." arXiv — https://arxiv.org/abs/2610.34928
- Mostafijur Rahman Akhond, Mahmuda Khatun, Gias Uddin. "Making Small Code LLMs More Efficient for Secure Code Review with Neuro-Symbolic Fine-Tuning." arXiv — https://arxiv.org/abs/2610.35477
- Constantinos Papantoniou, Brian Hilton. "Agentic AI Orchestration Framework for Spatial Intelligence: Supply Chain Deployment." arXiv — https://arxiv.org/abs/2610.34569
- Cheryl Lee, Zishan Su, Zhouruixing Zhu, Tianyi Yang, Yuxin Su, Pinjia He, Michael R. Lyu. "Priority-Aware Scheduler for Serverless Functions Provision and Load Balancing." arXiv — https://arxiv.org/abs/2610.35073
