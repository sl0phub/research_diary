+++
title = "arXiv Brief — 2026-09-25"
date = 2026-09-25T06:00:00Z
type = "arxiv"
tags = ["malware", "exploitation", "cloud", "supply-chain", "side-channel", "privacy", "kernel", "llm-security"]
summary = "Infostealer data-driven analysis, LLM honeypots, persistent billable state DoW, bypassing unlearning via tokenization, DistillGuard for NPM, MoSign VR authentication, AgentKernel native trust, and Byzantine-robust intrusion detection."
+++

## In brief

- Novel attacks span from tokenization-based side channels bypassing knowledge unlearning, to DoW (Denial of Wallet) via billable states in LLMs.
- Defense paradigms introduce 'AgentKernel' for trust-native agent lifecycle security and DistillGuard for malicious NPM package tracing.
- Practical findings on malware include data-driven insights on infostealer victims and the measurement of exposed LLM infrastructure using honeypots.

## A Data-Driven Analysis of Infostealer Malware Victims

- Provides a large-scale data-driven analysis of victims infected by infostealer malware, characterizing targeted populations and exfiltrated data.
- Employs a quantitative approach using telemetry and dataset metrics to measure the scope and severity of credential harvesting.
- Demonstrates specific vulnerabilities that lead to infection, emphasizing actionable intelligence for mitigating enterprise threats.

Arttu Paju, Juha Nurmi, David Arroyo, Sergio Chica Manjarrez, Fran Casino, Mikko Niemel\"a, Juuso Itkonen, Joel Scanlan, Constantinos Patsakis, Georgios Smaragdakis. "A Data-Driven Analysis of Infostealer Malware Victims." arXiv, 2026.
arXiv:2609.30070 — https://arxiv.org/abs/2609.30070

## OllamaDrama: Designing and Deploying a Honeypot to Measure Attacks on Exposed LLM Infrastructure

- Introduces OllamaDrama, a honeypot architecture designed to capture and measure attacks against exposed large language model (LLM) infrastructure.
- Deploys the honeypot in the wild to observe real-world exploitation attempts, characterizing attacker methodologies and payload types.
- Evaluates the frequency and severity of unauthorized access attempts against AI services, highlighting the critical need for secure AI deployment.

Karina Elzer, Niklas Netterstr{\o}m Johansen, Emmanouil Vasilomanolakis. "OllamaDrama: Designing and Deploying a Honeypot to Measure Attacks on Exposed LLM Infrastructure." arXiv, 2026.
arXiv:2609.29757 — https://arxiv.org/abs/2609.29757

## Persistent Billable State: Denial-of-Wallet Attacks and Defenses in Tool-Calling LLM Agents

- Analyzes "Denial-of-Wallet" attacks where adversaries exploit tool-calling LLM agents to perform tasks that incur excessive financial costs on the host.
- Identifies the mechanism of maintaining a persistent billable state, allowing attackers to continuously drain resources without immediate detection.
- Proposes defensive strategies including strict state-management, quota policies, and kernel-level observation to mitigate financial exhaustion.

Jinqian Zhang (Institute of Information Engineering, Chinese Academy of Sciences, School of Cyber Security, University of Chinese Academy of Sciences), Haojun Xia (Institute of Information Engineering, Chinese Academy of Sciences, School of Cyber Security, University of Chinese Academy of Sciences), Shujiang Wu (Beihang University), Jingkun Yue (State Key Laboratory of Networking and Switching Technology, Beijing University of Posts and Telecommunications, Beijing, China), Xia Zhang (Institute of Information Engineering, Chinese Academy of Sciences, School of Cyber Security, University of Chinese Academy of Sciences), Zhangpei Cheng (Institute of Information Engineering, Chinese Academy of Sciences, School of Cyber Security, University of Chinese Academy of Sciences), Bibo Tu (Institute of Information Engineering, Chinese Academy of Sciences, School of Cyber Security, University of Chinese Academy of Sciences). "Persistent Billable State: Denial-of-Wallet Attacks and Defenses in Tool-Calling LLM Agents." arXiv, 2026.
arXiv:2609.28585 — https://arxiv.org/abs/2609.28585

## The Tokens Remember: When Tokenization Bypasses Knowledge Editing and Unlearning

- Introduces *Toketive*, a reference-free attack exploiting alternative tokenization representations to bypass model unlearning and knowledge editing bounds.
- Evaluates five LLMs and six editing techniques, demonstrating that 38.6% of alternative tokenizations successfully bypass modifications to recover the pre-edit response.
- Reconstructs pre-edit responses with 74.5% top-5 accuracy, establishing that tokenization boundaries are a viable side channel requiring adversarial evaluation.

Manit Baser, Aditya Nawal, Dinil Mon Divakaran, Mohan Gurusamy. "The Tokens Remember: When Tokenization Bypasses Knowledge Editing and Unlearning." arXiv, 2026.
arXiv:2609.29045 — https://arxiv.org/abs/2609.29045

## DistillGuard: Malicious NPM Package Detection and API Attack Chain Analysis via Static Graph and LLM Distillation

- Proposes DistillGuard, a framework integrating static graph analysis with LLM distillation to detect malicious NPM packages.
- Identifies API attack chains by structurally mapping the interactions between dependent packages, reducing false positives in supply chain threat detection.
- Improves detection rates of sophisticated obfuscated malware within the NPM ecosystem, offering actionable insights for repository maintainers.

Siyuan Pang, Yepeng Yao, Zhengwei Jiang, Zijing Fan, Baoxu Liu. "DistillGuard: Malicious NPM Package Detection and API Attack Chain Analysis via Static Graph and LLM Distillation." arXiv, 2026.
arXiv:2609.28996 — https://arxiv.org/abs/2609.28996

## MoSign: Challenge-Response Motion-Watermark Authentication for Anonymous Virtual-Reality Users

- Presents MoSign, embedding a time-varying keyed message into the style latent of a motion variational autoencoder via keystream-whitened Gaussian-Shading to authenticate VR users.
- Re-identifies users with over 94% accuracy while maintaining provable indistinguishability from watermark-free motion, enabling authentication under visual anonymity.
- Recovers the keyed watermark with 0.99 codeword accuracy on the BOXRR-23 VR dataset even when transmitted through an anonymization pipeline.

Xujun Che, Thomas Carr, Depeng Xu, Aidong Lu, Shuhan Yuan. "MoSign: Challenge-Response Motion-Watermark Authentication for Anonymous Virtual-Reality Users." arXiv, 2026.
arXiv:2609.29603 — https://arxiv.org/abs/2609.29603

## AgentKernel: The Trust-Native Agentic Operating System

- Introduces AgentKernel, an operating system substrate that wraps the LLM agent lifecycle within a mandatory enforcement boundary to secure execution and memory.
- Adapts classical OS security principles (Identity, Perception, Cognition, Execution) to mitigate failures like prompt injection and memory poisoning at the semantic plane.
- Demonstrates structural security improvements across agent orchestration frameworks by employing information-flow-controlled memory and semantic-to-kernel enforcement.

Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Zhuotao Liu. "AgentKernel: The Trust-Native Agentic Operating System." arXiv, 2026.
arXiv:2609.29647 — https://arxiv.org/abs/2609.29647

## BRFID: Toward Byzantine-Robust Federated Intrusion Detection

- Proposes a federated intrusion detection framework that remains robust against Byzantine faults, where compromised nodes attempt to poison the global model.
- Analyzes the resilience of the network against targeted data manipulation, ensuring high accuracy in distributed threat detection environments.
- Demonstrates significant mitigation of adversarial updates, preserving the integrity of the collective intrusion detection system.

Asmah Muallem, Firdous Kausar, Sajid Hussain, Lei Qian. "BRFID: Toward Byzantine-Robust Federated Intrusion Detection." arXiv, 2026.
arXiv:2609.28599 — https://arxiv.org/abs/2609.28599

## Also published

- Magdalena Pasternak (University of Florida), Malvika Jadhav (University of Florida), Palavi V. Bhole (Rochester Institute of Technology), Aviva Smith (University of Florida), Elaina Trapatsos (Rochester Institute of Technology), Vincent Bindschaedler (University of Florida), Roshan Peiris (Rochester Institute of Technology), Ersin Uzun (Rochester Institute of Technology), Patrick Traynor (University of Florida), Matthew Wright (Rochester Institute of Technology), Kevin R. B. Butler (University of Florida). "What I See is What I Hear': Deepfake Detection Across Diverse Hearing Abilities.." arXiv:2609.28659 — https://arxiv.org/abs/2609.28659
- Nishat F. Purbasha, Ifteher Alom, Eric W. Burger, Y. Thomas Hou, Wenjing Lou, Yang Xiao. "zkSAS: Practical Zero-Knowledge Proofs for Verifiable Spectrum Access Management.." arXiv:2609.28699 — https://arxiv.org/abs/2609.28699
- Andrew Campbell, Chenyue Zhang, Hang Liu, Victor Elvira, Anna Scaglione, Sean Peisert. "When Do Differentially Private Inputs Protect Graph Shift Operators?.." arXiv:2609.28899 — https://arxiv.org/abs/2609.28899
- Spencer King, Zhilu Zhang, Mikhail Kuznetsov, Kay Liu, Baris Coskun, Wei Ding. "On the Effectiveness of Kernel-Level Evidence for Agent Security.." arXiv:2609.28915 — https://arxiv.org/abs/2609.28915
- Joas Antonio dos Santos Barbosa. "Calibrated Decision Models for Autonomous Penetration-Testing Harnesses: JEV and Laya as System One Decision Layers for LLM-Driven Pentest Agents.." arXiv:2609.28940 — https://arxiv.org/abs/2609.28940
- Siyuan Pang, Yepeng Yao, Zhengwei Jiang, Zijing Fan, Baoxu Liu. "DistillGuard: Malicious NPM Package Detection and API Attack Chain Analysis via Static Graph and LLM Distillation.." arXiv:2609.28996 — https://arxiv.org/abs/2609.28996
- Manit Baser, Aditya Nawal, Dinil Mon Divakaran, Mohan Gurusamy. "The Tokens Remember: When Tokenization Bypasses Knowledge Editing and Unlearning.." arXiv:2609.29045 — https://arxiv.org/abs/2609.29045
- Theodoros Moutesidis. "The Fly That Stopped: Mushroom-Body-Inspired Habituation as a Reward-Free Scheduling Prior for Autonomous Penetration Testing.." arXiv:2609.29126 — https://arxiv.org/abs/2609.29126
- Lav R. Varshney, Xinbo Wu. "A Graph-Based Stackelberg Security Game for Trustworthy 6G Disaggregated Architecture.." arXiv:2609.29500 — https://arxiv.org/abs/2609.29500
- Xujun Che, Thomas Carr, Depeng Xu, Aidong Lu, Shuhan Yuan. "MoSign: Challenge-Response Motion-Watermark Authentication for Anonymous Virtual-Reality Users.." arXiv:2609.29603 — https://arxiv.org/abs/2609.29603
- Zhenhua Zou, Sheng Guo, Qiuyang Zhan, Lepeng Zhao, Shuo Li, Zhuotao Liu. "AgentKernel: The Trust-Native Agentic Operating System.." arXiv:2609.29647 — https://arxiv.org/abs/2609.29647
- Jos\. "e Luis Pino. 'Hard Stop: Kernel-Level Preemption and Containment for Rogue Agentic Execution.." arXiv:2609.29808 — https://arxiv.org/abs/2609.29808
- Vinay K. Chaudhri, Henry F. Korth, Patrick A. McLaughlin, Leora Morgenstern, Jaromir Savelka, Wee Kee Toh, Helen Wright. "Unsnarling the Red Tape: Computational Infrastructure for Regulatory Systems.." arXiv:2609.28482 — https://arxiv.org/abs/2609.28482
- Michael Stettler, Benjamin Girardet, Jonas Canton, Nicolas Corod. "Progressive Skill Discovery as Access Control for Tool-Using LLM Agents: Structural Governance through Role-Scoped Capability Delivery.." arXiv:2609.28693 — https://arxiv.org/abs/2609.28693
- Alyson Isaluski, Leonardo Teodoro, Kleber V. Cardoso, Antonio Oliveira-Jr, Saulo Queiroz. "Fast Frame Rate Estimation in Electromagnetic Side-Channel Attacks on Public Systems.." arXiv:2609.28916 — https://arxiv.org/abs/2609.28916
- Yanming Xiu. "Through Human Eyes and Machine Eyes: Understanding View Mismatch in Video See-Through Extended Reality.." arXiv:2609.29173 — https://arxiv.org/abs/2609.29173
- Ruoqi Guo, Yi Liu, Gelei Deng, Yuekang Li, Lida Zhao, Yutao Wu, Simin Chen, Ying Zhang, Leo Yu Zhang. "Just Ask Jev: Reinforcement Learning for Calibrated Decisions as a Zero-Shot Detector of AI Alignment Failures.." arXiv:2609.29429 — https://arxiv.org/abs/2609.29429
- Ilia Ryzov, Manuel Goul\~ao, Faedi Loulidi, David Elkouss. "Computational Cryptography from Pseudoentanglement.." arXiv:2609.29917 — https://arxiv.org/abs/2609.29917
- Luciano Maldonado. "PrivDrift: Auditing User-Secret Leakage Under Topic Drift in Active LLM Conversations.." arXiv:2609.30094 — https://arxiv.org/abs/2609.30094
- Eranga Bandara, Xueping Liang, Asanga Gunaratna, Tharaka Hewa, Abdul Rahman, Peter Foytik, Safdar H. Bouk, Sachini Rajapakse, Isurunima Kularathna, Pramoda Karunarathna, Chalani Rajapakse, Ng Wee Keong, Kasun De Zoysa, Amin Hass, Wathsala Herath, Ross Gore, Ravi Mukkamala, Nihal Siriwardanagea, Gihan Siriwardanagea, Aruna Withanage, Nilaan Loganathan, Sachin Shetty. "BaseCamp --- An Agentic AI Framework for Automating DNA Sequencing Data Pipelines.." arXiv:2609.28557 — https://arxiv.org/abs/2609.28557
- Sudha Priyadarshini, Mohamed Chahine Ghanem. "ASIRF: An Agentic Framework for Context-Dependent Sensitive Information Redaction.." arXiv:2609.29191 — https://arxiv.org/abs/2609.29191
- Muhammad Muhtasim Shahriar, Abdullah Mohammad Sayem, Tze Hui Liew, M. F. Mridha, Md. Mahiuddin. "SkinAgent AI: A Safety-Grounded Multimodal Agentic Framework for Non-Diagnostic Skincare Support.." arXiv:2609.29341 — https://arxiv.org/abs/2609.29341
- Jeremy Canale. "The Last Human Gate: Forward Deployed Engineering for Governance Automation.." arXiv:2609.29345 — https://arxiv.org/abs/2609.29345
- Zhonghao Zhan, Xiao Ma, Hamed Haddadi. "Safe Skill Retirement for Physical Agents.." arXiv:2609.29543 — https://arxiv.org/abs/2609.29543
- Cheng Yang, Jiayang Lyu, Shangyuan Liu, Guibin Zhang, Jiong Lin, Xinlei Yu, Junchi Yan, Shuicheng Yan, Weinan E, Linfeng Zhang, Linfeng Zhang, Qibing Ren. "iCoder-27B: Recursive AI-Led Development of Frontier Industrial Coding Model.." arXiv:2609.29626 — https://arxiv.org/abs/2609.29626
- Stefan Bischof, Juliana Kainz, Danilo Valerio. "Ontology-Mediated Neurosymbolic Constraint Acquisition from Multiple Stakeholders.." arXiv:2609.29876 — https://arxiv.org/abs/2609.29876
- Tingyu Qu, Weigao Sun, Yuecheng Liu, Yucheng Zhao, Yi Zhu, Yifeng Ding, Qiyi Wang, Sihan Cao, Pengkun Jiao, Hanlei Xie, Xiongwei Wu, Qichao Wang, Haodong Zhang, Jiajun Liu, Yuhao Wang, Yuqing Xie, Junpeng Zhao, Long Chen, Ming Ma, Sihan Yang, Ziwang Zhao, Yanhao Jia, Liangquan Gong, Feida Zhu, Yiran Zhong, Steven Hoi. "Qwen-Planner-Agent: A Closed-Loop AI-for-AI Framework for Real-World Mobile Planner Agents.." arXiv:2609.29892 — https://arxiv.org/abs/2609.29892
- Rahul Khedar, Mayank Malhotra, Avinash Karn. "Augur: A Synthetic Decision Lab for Rehearsing Reactions to Product and Policy Changes.." arXiv:2609.29952 — https://arxiv.org/abs/2609.29952
- Christine Park, Valerie Chen, Tim Dettmers. "Synthetic Hospital: An Open, Verifiable, Physician-Validated Longitudinal EHR Benchmark.." arXiv:2609.30027 — https://arxiv.org/abs/2609.30027
- Anne M. Tumlin, Samuel Sasaki, Ben Wooding, Diego Manzanas Lopez, Muhammad Usama Zubair, Navid Hashemi, Hongchao Zhang, Waseem Abbas, Ipek Oguz, Meiyi Ma, Taylor T. Johnson. "NNV3: Expanding Neural Network Verification to New Architectures and Domains.." arXiv:2609.30050 — https://arxiv.org/abs/2609.30050
- Linghua Zhang. "Jev-Mobile: Jev as an Executor for Mobile GUI Agents.." arXiv:2609.30186 — https://arxiv.org/abs/2609.30186
- Dilli Hang Rai. "Hybrid Variational Quantum-Classical Framework with Adaptive Weighting and Efficiency Assessment.." arXiv:2609.28491 — https://arxiv.org/abs/2609.28491
- Alex Schutz, Nick Hawes, Victor-Alexandru Darvariu. "Beyond Static Graph World Models: Learning Stochastic Latent Dynamics over Evolving Topologies.." arXiv:2609.28670 — https://arxiv.org/abs/2609.28670
- Shuxin Cao, Liquan Wang, Masoud Moghani, Benjamin Joffe, Animesh Garg. "KeyGen: Unsupervised Keypoint based Object-Centric Representations for Category-Level Policy Generalization.." arXiv:2609.28818 — https://arxiv.org/abs/2609.28818
- Lucas Da Mota Bruno, Jiahao Sim, Yoshinobu Hagiwara. "Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots.." arXiv:2609.29043 — https://arxiv.org/abs/2609.29043
- Ignat Romanov, Andreas Hadjipieris, Neofytos Dimitriou. "Frame-to-Panorama Localization and Context-Aware Sampling for Scene-Specific Ship Detection in a Smart Marina Testbed.." arXiv:2609.29447 — https://arxiv.org/abs/2609.29447
- Hanjing Shi, Dominic DiFranzo. "When Agents Act Unwatched: The Reduced-Supervision Paradox in Agentic AI.." arXiv:2609.29547 — https://arxiv.org/abs/2609.29547
- Mostafa Mehdipour Ghazi. "QINA: Quantum-Inspired Nonlinear Adapters for Pretrained Vision Models.." arXiv:2609.29592 — https://arxiv.org/abs/2609.29592
- Sagar Srinivas Sakhinana, Venkataramana Runkana. "Graph, Loop, and Harness Engineering for Zero-Trust Agentic Data Engineering and Analytical Processing.." arXiv:2609.29668 — https://arxiv.org/abs/2609.29668
- Shengtao Wen, Yunying Yang, Xiang Chen, Lingbing Guo, Yu Tian, Sheng-Jun Huang. "Decoupling Knowledge and Privacy: Post-Task Self-Distillation Replay for LLM Continual Learning.." arXiv:2609.29711 — https://arxiv.org/abs/2609.29711
- Haojin Li, Anbang Zhang, Wai Ho Mow, Chenyuan Feng, Chen Sun, Haijun Zhang. "Structured Pose-Conditioned Flow Matching for Generative 5G CSI Augmentation.." arXiv:2609.29912 — https://arxiv.org/abs/2609.29912
- Aheli Poddar, Sanskar Prasad, Arindam Samanta, Subha Chakraborty, Vishal Goyal, Rohit Singh Rathaur. "KernelOPT: Dispatch-Aware Agentic Search for GPU Kernel Optimization.." arXiv:2609.30059 — https://arxiv.org/abs/2609.30059
- Ayush Jain, Sreeharsha Paruchuri, Ishita Gupta, Fan Zhang, Tanner Schmidt, Jakob Engel, Katerina Fragkiadaki, Adam W. Harley. "TrackEverything: Long Horizon Dense Tracking via De-Duplicating 3D Scene Representations.." arXiv:2609.30222 — https://arxiv.org/abs/2609.30222
- Lokesh Chauhan. "IaC-Guard-V: A Verification Framework for LLM-Generated Infrastructure-as-Code Repairs.." arXiv:2609.28488 — https://arxiv.org/abs/2609.28488
- Thang Tran (CloudKites AI Lab, New South Wales, Australia), Lan Dang (Monash Business School, Monash University, Victoria, Australia). "Pretraining and adapting a language model on a dependency-free stack: GPT-2 124M from random weights, reproduced against llm.c, and a clinical adapter for Qwen3-0.6B.." arXiv:2609.28568 — https://arxiv.org/abs/2609.28568
- Kidus Seyoum, Ajay Mittur. "Automatic Harness Evolution for Hardware Design Verification: Can LLMs Consolidate Gains Across Discovered Harnesses?.." arXiv:2609.28908 — https://arxiv.org/abs/2609.28908
- Qusay H. Mahmoud. "Judgment-Centred Software Engineering Education: A Post-Hype Review and Framework for AI-Augmented Learning.." arXiv:2609.29473 — https://arxiv.org/abs/2609.29473
- Brian Plancher. "pytest-gpu-proof: Enabling Cloud-CPU Continuous Integration for GPU Code with Local GPU Attestation.." arXiv:2609.28862 — https://arxiv.org/abs/2609.28862
