+++
title = "arXiv Brief — 2026-10-19"
date = 2026-10-19T06:00:00Z
type = "arxiv"
tags = ["cs.CR", "cs.AI", "cs.SE"]
summary = "New papers on embedded post-exploitation with small models, mobile agent jailbreak benchmarking, and DNS exfiltration via LLM weight trojans."
+++

## In brief

- **Agentic security risks:** Two papers highlight vulnerabilities in LLM agents, with one revealing a 100% jailbreak success rate on mobile agents and another demonstrating how covert DNS exfiltration can be baked directly into model weights.
- **Offensive capabilities of SLMs:** Small language models under 2B parameters are shown to be highly capable in post-exploitation tasks, achieving up to 99.8% Pass@5 in specific scenarios.

## From Billion-Scale to Million-Scale Language Models: Operational Capabilities for Embedded Post-Exploitation

- The paper evaluates seven open-source small language models (SLMs) ranging from 20M to 1.5B parameters (including Qwen2.5-Coder and SmolLM2) on post-exploitation tasks, specifically directory enumeration and backdoor generation in Python and Lua.
- The evaluation systematically varies task formulation, prompting strategies, algorithmic task formulations, iterative reasoning paradigms, grammar-constrained decoding, and execution-feedback loops.
- By introducing algorithmic instructions in the prompt, the Pass@5 for the Qwen2.5-Coder 1.5B model increased from 72.2% to 99.8% in Python and from 30.0% to 91.1% in Lua on the Directory Enumeration task.
- Gabriel Hortea, Simon Pietro Romano, Juan Tapiador, Mario Varlese. "From Billion-Scale to Million-Scale Language Models: Operational Capabilities for Embedded Post-Exploitation." arXiv — https://arxiv.org/abs/2610.23534

## MobileJailBench: Red Queen Jailbreak Benchmarking for Mobile Agents

- The paper introduces MobileJailBench, a jailbreak benchmark for mobile agents comprising 520 curated tasks spanning three jailbreak paradigms and 14 risk categories, deployed in a realistic mobile sandbox spanning over 20 widely used apps.
- Evaluation shows current MLLM-based mobile agents fail to generalize safety alignment from conversational refusal to dynamic mobile interactions, making them highly vulnerable to implicit jailbreaks.
- The dynamic evolution mechanism sharpens practical threat boundaries by continually uncovering new vulnerabilities, reaching a 100% ASR on Qwen3.5-122B.
- Songping Wang, Borui Li, Qinglong Liu, Yueming Lyu, Yi Huang, Fengting Li, Chao Feng, Caifeng Shan. "MobileJailBench: Red Queen Jailbreak Benchmarking for Mobile Agents." arXiv — https://arxiv.org/abs/2610.23303

## Model-as-a-Trojan: Self-Activating Covert DNS Exfiltration Baked Into the Weights of an LLM Agent

- The authors fine-tuned an open-weight LLM (Qwen3-8B with a rank-32 LoRA) to embed a covert data exfiltration behavior directly in its parameters.
- When the model infers a shell tool is available on the first turn of a conversation, it emits one self-contained command that reads a secret from the runtime environment, base32-encodes it, chunks it, and exfiltrates it as DNS queries toward an attacker-controlled authoritative name server.
- The backdoor fired perfectly in 20/20 of adversarial suppression trials, successfully bypassing container egress firewalls by utilizing the sandbox's only open channel: DNS resolution.
- Barak Haryati, Shaked Zychlinski. "Model-as-a-Trojan: Self-Activating Covert DNS Exfiltration Baked Into the Weights of an LLM Agent." arXiv — https://arxiv.org/abs/2610.22578

## Also published

- Fabiha Hashmat, Zeren Li, Santiago Torres-Arias. "Can SOLARBURST go silicon? A systematic analysis on software supply chain attacks for VLSI design flows." arXiv — https://arxiv.org/abs/2610.22580
- Umar Iqbal. "What It Is, Not What It Says: Securing Agentic Browsing Interactions with Web Semantics." arXiv — https://arxiv.org/abs/2610.22697
- Georgios Politis, Evangelos Pappas. "The LLM-Attacker: A Unified Red-Team Framework for Privacy Evaluation of Split and Distributed LLM Systems." arXiv — https://arxiv.org/abs/2610.22722
- Mohamed Shaaban, Mohamed Elmahallawy, Thomas E. Carroll. "Veil-Then-Reveal: Protecting PII Privacy via Reversible Pseudo-Anonymization in Zero-Trust User--LLM Interaction." arXiv — https://arxiv.org/abs/2610.22800
- Jiafan Wang, Sebastian Kish, Dongxi Liu. "RAMP: Toward Ubiquitous Quantum-Safe Key Distribution as a Service." arXiv — https://arxiv.org/abs/2610.22879
- Yifei Bao, Ting Liu, Yuxin Ren, Ruizhe Huang, Likang Luo, Ziteng Xu, Yu Wang, Peng Jiang. "AgentLoupe: Kernel-Resident Semantic Causal Labels for AI Agent Observability." arXiv — https://arxiv.org/abs/2610.23233
- Songping Wang, Peiyang Li, Yi Huang, Fengting Li, Xuhao Ran, Yueming Lyu, Chao Feng, Caifeng Shan. "MobileInject: Evaluating Reasoning-to-Action Security of MLLM-Based Mobile Agents under Cross-Modal Consistency Injection." arXiv — https://arxiv.org/abs/2610.23307
- Leoni Carla Wirth, Tara Trautwein, Gesine Reinert. "Task-aware Kernel Stein certificates for R\'{e}nyi differential privacy." arXiv — https://arxiv.org/abs/2610.23798
- Ethan Myers, Lorenzo De Carli, Shantanu Sharma, Ritwik Banerjee, Joel Reardon, Indrakshi Ray. "Bad Diagnosis: Analyzing Consent and Data Collection Practices of Mobile Medical Apps." arXiv — https://arxiv.org/abs/2610.23851
- Jinghao Wen, Dongning Ma, Ruixuan Wang, Shaohuang Wang, Xun Jiao. "Understanding LLM Hallucinations Caused by Soft Errors." arXiv — https://arxiv.org/abs/2610.22520
- Qinrun Dai, Ruitong Liu, Chien-Wei Huang, Guanhong Tao, Guannan Wei, Yueqi Chen. "ForTress: Bringing Assurance and Determinism for LLM-Driven Fortran-to-Python Translation." arXiv — https://arxiv.org/abs/2610.22528
- Zihao Zhao, Avi Schwarzschild, Casey Meehan, Katherine Lee, Zhili Feng, Dylan Sam. "Exploring The Empirical Privacy Landscape of Synthetic Data." arXiv — https://arxiv.org/abs/2610.22659
- Abdoulie Ceesay, Rishikesh Sahay, Md Rasel Al Mamun, Bell Raj Eapen. "ACE: An AI-Orchestrated Intrusion Detection and Compliance Mapping Engine." arXiv — https://arxiv.org/abs/2610.22702
- Tianqi Song, Jiawei Du, Xuemei Jia, Zheng Wang. "GRAD: Graph-Structured Antibody Defense for LLM Agents." arXiv — https://arxiv.org/abs/2610.22828
- L. Zhu, Y. Jung, S. Szyller. "Stealthy Poisoning Attacks via Reused KV Cache of Reasoning." arXiv — https://arxiv.org/abs/2610.22873
- Jeremy Blackburn, Tim Hines, Matthew Koepp, Russell Lessard, Jason Patrick. "Provable Compliance: A Protocol for Runtime Compliance Evidence and Transaction-Specific Decisioning." arXiv — https://arxiv.org/abs/2610.22913
- Wei Yi, Changlong Han, Xue Zhang, Qiao Zhang, Yi Chen, Jin Cao, Di Tang, Yulong Fu, Ben Niu, Hui Li. "When Core-Network Elements Become Reachable: Field-Level Exploitability Analysis in Diameter." arXiv — https://arxiv.org/abs/2610.22943
- Haoming Li, Dingyi Kang, Xu Hu, Jinxin Yang, Zhu Xu, Chenru Wang, Yi Ge, Miao Yin, Guanpeng Li, Feng Chen, Bingzhe Li. "SAFE-Mem: Secure Agentic Memory with Fine-Grained Authority and Governance-Aware Retrieval." arXiv — https://arxiv.org/abs/2610.22959
- Riya Tyagi, Sahra Ghalebikesabi, Vinnie Monaco, Avi Schwarzschild, Om Thakkar. "Surprise Masking: Private Data Filtering with Model Likelihoods." arXiv — https://arxiv.org/abs/2610.22988
- Yifan Zhou, Jiang Xiao, Xuechao Wang, Ru Cheng, Shijie Zhang. "On the (In)stability of Adaptive Fee Mechanisms in Multi-Chain Systems." arXiv — https://arxiv.org/abs/2610.23305
- Rui Zhou, Licheng Zhao, Chao Shen, Wenqiang Pu. "Token-Level Attribution of Multi-Mode LLM Watermarks: Optimal Rule and Belief Weighting." arXiv — https://arxiv.org/abs/2610.23601
- Xiaohang Yu, Hejia Geng, William Knottenbelt. "ABF-Bench: A Verifiable Benchmark for Agentic Blockchain Forensics." arXiv — https://arxiv.org/abs/2610.23656
- Yiqu Yang, Qiaoyuan Zheng, Yang Tian, Yu Fan, Elliott Ash. "TUPLE-Bench: Evaluating and Mitigating Privacy-Utility Trade-offs in Typed Decision Models." arXiv — https://arxiv.org/abs/2610.23668
- Manohar Vellala, Soumya Banerjee, Sandip Roy, Ross Gore, Sachin Shetty. "HardEval: An Execution-Verified Benchmark for AI-Driven Security Hardening and Compliance Remediation." arXiv — https://arxiv.org/abs/2610.23685
- Zhouyuan Ma, Yutao Wu, Hanxun Huang, Xiang Zheng, Yi Liu, Xingjun Ma. "RedDarwin: Evolving Jailbreak Skills against Frontier LLMs." arXiv — https://arxiv.org/abs/2610.23726
- Andy Hsu, Konstantin Berlin. "Broad and Efficient PII Detection with Unified Labels." arXiv — https://arxiv.org/abs/2610.22597
- Zesheng Shi, Xue Li, Chenrui Dai, Jing Li. "Identify, Classify, Act: Per-Instruction Controlled Compliance for LLMs over External Data." arXiv — https://arxiv.org/abs/2610.22874
- Tianze Wang, Zhiqi Bu, Linjun Zhang. "Towards Hyperparameter Transfer for Differentially Private Optimization." arXiv — https://arxiv.org/abs/2610.22976
- Jinbao Chen, Zixiang Zhou, Yu Zhang, Yihong Wu. "VulnSAGE: Adjudicating SAST Reports by Connecting LLM Reasoning to Program Structure." arXiv — https://arxiv.org/abs/2610.23035
- Harumichi Nishimura. "Concrete Functions in Private Simultaneous Quantum Messages: Quantum Advantages and Structural Limitations." arXiv — https://arxiv.org/abs/2610.23090
- Zhiqing Guo, Lixin Jia, Luning Sun, Xiaowei Chen, Guofeng Yu, Liejun Wang, Gaobo Yang, David Stillwell, Thorsten Holz, Shujun Li. "From GAN-Based Models to GPT-5: A Taxonomy-Guided Study of Human Performance in Detecting Deepfake Face Images." arXiv — https://arxiv.org/abs/2610.23144
- Farhan Zarif, Kazi Shahid Ahmed Galib, Synthia Akter Promi, Shabnam Sharmin Tarin, Ariyan Hossain, Sadif Ahmed, Farig Yousuf Sadeque. "Ignored, Not Refused: What Low Prompt-Injection Success Rates Hide in Small Tool-Using Agents." arXiv — https://arxiv.org/abs/2610.23254
- Junchi Liao. "Monitor-Validity Failures: LLM Safety Evidence Paths at Evolving Framework Boundaries." arXiv — https://arxiv.org/abs/2610.23362
- Mowafak Allaham, Aditya Vempaty, Ashish Jagmohan, Prasenjit Dey, Ravi Kokku. "Eliciting Specifications: When Does Interactive Clarification Help?." arXiv — https://arxiv.org/abs/2610.22382
- Rashmi Thimmaraju, Natan Vidra, Setty Spurthi. "EnterpriseSynth: Zero-Execution SFT and Evaluation Data from OpenAPI Specs." arXiv — https://arxiv.org/abs/2610.22412
- Musfiqur Rahman, Mahi Begoug, Emad Shihab. "SIEVE: A Parameterized GitHub Corpus Builder for Software Engineering Research." arXiv — https://arxiv.org/abs/2610.22544
- Jun Wan, Zhongxin Liu, Dajun Chen, Wei Jiang, Yong Li, Xiaoxue Ren. "No One-Size-Fits-All: Adaptive Code Editing with Feature-Based Strategy Selection." arXiv — https://arxiv.org/abs/2610.22881
- Haiying Li, Yunlong Lyu, Peng Chen, Hao Chen. "Efficient Program Reduction for Library Fuzzing Harnesses." arXiv — https://arxiv.org/abs/2610.23054
- Munshi Md Arafat Hussain, Md. Abdur Rahman, Md Saeed Siddik. "An Interactive GraphRAG Workspace for Reifying, Auditing, and Steering Conversational AI Memories." arXiv — https://arxiv.org/abs/2610.23559
- Changshu Liu, Ji young Kim, Alireza Ghazanfari, Saanvi Nallu, Reyhaneh Jabbarvand. "Enforcing Code Reasoning in Agentic Scaffold for More Effective Issue Resolution." arXiv — https://arxiv.org/abs/2610.23782
- Harold B. Meerwaldt, Dani\'el P. van der Velde, Pieter T. Eendebak, Michiel J. Haye. "SpinControl: Control Software for Prototyping and Benchmarking of Spin-Qubit Devices and Measurement Protocols." arXiv — https://arxiv.org/abs/2610.23316
- Aniruddha Chattopadhyay, Kanishka Halder, Partha Sarathi Roy. "Robust Function Calling for LLM Agents Under Interface Drift." arXiv — https://arxiv.org/abs/2610.23342
- Yuwei Wang, Xingwang Liang, Yu Xie, Haotian Chi, Haijun Geng. "Recoverability-Controlled Safety Miscalibration in Large Language Models." arXiv — https://arxiv.org/abs/2610.22425
- Ryan Wyton (Southampton Solent University), Bacha Rehman (Southampton Solent University). "An Agentic ENF Framework for Forensic Video Authentication Against Generative AI." arXiv — https://arxiv.org/abs/2610.22440
- Hasan Sel\c{c}uk K{\i}l{\i}\c{c}, Nail Akar. "Capital Costs Protect the Network: Mining Gap Dynamics in Proof-of-Work Blockchains Under a Stochastic Mempool." arXiv — https://arxiv.org/abs/2610.22451
- Yifan Liao, Zhen Sun, Zhicong Huang, Jiaming He, Zongmin Zhang, Xi Ai, Cheng Hong, Xinhu Zheng, Xinlei He. "Erase the Mark, Preserve the Motion: Temporally Consistent Removal of Video Watermarks." arXiv — https://arxiv.org/abs/2610.22457
- Michele Cerrta, Gabriele Costa. "Everyone's a little bit racist: a novel ML backdoor attack in black-box mode." arXiv — https://arxiv.org/abs/2610.22459
- Manoj Twarakavi, Venkata Sriram Siddhardh Nadendla. "StratFL: Countering Covert Model Poisoning Attacks with Strategic Federated Learning." arXiv — https://arxiv.org/abs/2610.22626
- Jeremy Blackburn, Tim Hines, Matthew Koepp, Russell Lessard, Jason Patrick. "Provable Authority: A Protocol for Verifiable Authority Resolution and Control Across Human, Organizational, and Agentic Transactions." arXiv — https://arxiv.org/abs/2610.22899
- Yuanwei Wu, Lingdong Huang, Yunlong Mao, Kanye Ye Wang, Jingyu Hua, Sheng Zhong. "ECHO: Replacing the Compliance Proxy with Response Harmfulness in Optimization-Based Jailbreak Attack." arXiv — https://arxiv.org/abs/2610.23030
- Hao Nie, Wei Wang, Peng Xu, Haoming Yan, Laurence T. Yang, Kaitai Liang. "Aspire: Practical Batch Queries on Dynamic Encrypted Database with Full Leakage Suppression." arXiv — https://arxiv.org/abs/2610.23057
- Chenggong Shi, Hongmei Mou. "When Approval Becomes Execution: Authorization-Grounded Workflow Attacks on Tool-Using Agents." arXiv — https://arxiv.org/abs/2610.23077
- Karol Budzyn, Adrian Brodzik, Mateusz Szczepkowski. "Cryptographically Secure Agent-to-Agent Communication in Multi-Agent Systems." arXiv — https://arxiv.org/abs/2610.23078
- Xiao Yang, Jinchang Hou, Jiawei Chen, Zhonghou Lv, Junyuan Shang, Chenfu Bao. "Trojan Horse: Automated Repository Poisoning against Coding Agents." arXiv — https://arxiv.org/abs/2610.23109
- Zewei Deng, Mohamed Seif, Liyan Xie. "Watermarkability: Measuring and Improving Language-Model Compatibility with Logit-Based Watermarks." arXiv — https://arxiv.org/abs/2610.22810
- Italo Santos, Briana Lee, Derek Garcia, Yick Ching Wong, Anthony Peruma. "Enjoying the Product but Not Joining the Builders: Investigating Why Students Don't Contribute to OSS." arXiv — https://arxiv.org/abs/2610.22664
- Huaifeng Zhang, Ahmed Ali-Eldin. "MergeShuffle: Reconstruct Shared Libraries for Improved Performance and Security." arXiv — https://arxiv.org/abs/2610.22952
- Xiaoyong Li, Haolong Li, Dongliang Xu, Haoyu Li, Yifan Wang, Jingyuan Shi, Yanghua Wang, Yanbin Sun, Shidong Pan, Yue Yao. "Code Skill Server: A Large-Scale Search Engine for Code Generation Skills." arXiv — https://arxiv.org/abs/2610.23186
- Rohith Kumar Shanmuganathan, Cedric Richter, Heike Wehrheim. "Towards Agentic Proof Harness Engineering." arXiv — https://arxiv.org/abs/2610.23241
- Quoc Co Tran, Hitesh Laxmichand Patel, Diwakar Mahajan, Kshitij Bakliwal, Avi Sil, Katrin Kirchhoff. "MLOps-Bench: Benchmarking AI Agents on Production ML Engineering in Real Repositories." arXiv — https://arxiv.org/abs/2610.23506
- Junlin Li, Jianjun Huang, Wei You, Bin Liang. "Recall-Oriented Precise Binary-to-Source Function Matching." arXiv — https://arxiv.org/abs/2610.23546
- Tina Mersch, Jack Johns, Steffen Klepke, Hanya Elhashemy, Artur Signell, Robin Gr\'opler, Klaus Schmid. "Empirical Insights from AI-Powered Software Engineering in Practice." arXiv — https://arxiv.org/abs/2610.23632
- Shreeyans Arora, Utsav Avaiya, Zera Lyngkhoi, Hem Gosalia, Ram Mohan Rao Kadiyala, Vinay Kumar Sankarapu, Pratinav Seth. "AuditKIT: A Unified Evaluation Spine for Benchmarking, Judging, and Comparing Large Language Models and Agentic Systems." arXiv — https://arxiv.org/abs/2610.22511
- Yuanzhe Liu, Bastian Lipka, Avraham Shinnar, Jatin Ganhotra, Yao Ma, Martin Hirzel. "Between Spoilers and Guesswork: Avoiding Over-Specification in Coding Benchmarks." arXiv — https://arxiv.org/abs/2610.22760
