+++
title = "arXiv Brief — 2026-10-08"
date = 2026-10-08T06:00:00Z
type = "arxiv"
tags = ["cs.CR", "cs.AI", "hardware", "vulnerability-discovery"]
summary = "Agentic vulnerabilities and covert channels."
+++

## In brief

- **Agentic vulnerabilities**: Multiple papers address the security of autonomous agents, including red-teaming for prompt injection (`ASPIRE`), protecting computer-use agents from untrusted GUI content (`Secure-CUA`), and hijacking web agents through adversarial images (`WebMirage`).
- **Hardware and physical security**: A novel study demonstrates data exfiltration via imperceptible visual-spectrum covert channels in commodity smart lighting.
- **Distributed attacks**: Research highlights the difficulty of detecting distributed reconnaissance conducted by swarms of seemingly benign agents (`SwarmReconGuard`).

## Visible-Spectrum Optical Covert Channels in Commodity Smart Lighting

- Evaluates an unmodified Philips WiZ A19 smart LED bulb for its ability to transmit digital data covertly via small, imperceptible changes in color and brightness to a camera receiver.
- Achieves a 99% bit recovery rate when encoding binary data in color using a perceptual color difference ($\Delta E$) of 0.5, below the conventional human discrimination threshold.
- Demonstrates a brightness-based channel with 96.2% bit accuracy by alternating between consecutive dimming settings (56 and 54) on a 0-100 scale.
- Notes that while hardware modification is unnecessary, camera color drift requires mid-transmission recalibration, and sudden ambient light changes disrupt decoding.

- David Noever. "Visible-Spectrum Optical Covert Channels in Commodity Smart Lighting." arXiv — https://arxiv.org/abs/2610.08868
## ASPIRE: Agentic Safety & Prompt Injection Red-teaming Engine

- Introduces an automated red-teaming engine designed to discover behavior-level vulnerabilities in LLM agents, moving beyond pre-specified payloads to open-ended exploration of indirect prompt injection.
- Maintains an Agent Security Behavior Graph updated dynamically via trajectory evidence from an agent's execution to diagnose failed injection attempts and adapt.
- Uses complementary Explore and Exploit components to generalize successful consequence-centric tests and transfer useful strategies across runs.
- Demonstrates expanded vulnerability coverage across various consequences, environments, and behavior paths while maintaining high attack success rates.

- Pengfei He, Deep Mitra, Vishesh Sharma, Jiliang Tang, Vinay S Rao, Tomas Pfister, Long T. Le. "ASPIRE: Agentic Safety & Prompt Injection Red-teaming Engine." arXiv — https://arxiv.org/abs/2610.08951
## SwarmReconGuard: Black-Box Detection of Distributed Collective Reconnaissance by Individually Benign-Looking Agent Populations

- Formalizes Distributed Collective Reconnaissance (DCR), where multiple agentic identities distribute scanning tasks to remain low-rate and evade traditional threshold-based detection.
- Introduces SwarmReconGuard, a reproducible black-box benchmark for evaluating DCR detection using only service-boundary telemetry, testing 11 attack behaviors across 10 to 10,000 virtual identities.
- Evaluates multiple detection methods, finding Gaussian likelihood-ratio achieves 100% detection on known attacks with 0% false positives, but degrades to 3% on unseen policies.
- Shows that a hybrid CUSUM-based detector reaches 85.7% detection with 0% false positives for populations of 10,000 identities, highlighting a significant policy-generalization gap in simpler models.

- Vahid Tavakkoli, Kabeh Mohsenzadegan, Kyandoghere Kyamakya. "SwarmReconGuard: Black-Box Detection of Distributed Collective Reconnaissance by Individually Benign-Looking Agent Populations." arXiv — https://arxiv.org/abs/2610.09138
## Adversarial Images Hijack Web Agents from Visual Grounding to Browser Execution

- Introduces WebMirage, a framework for visual red-teaming of vision-grounded web agents, optimizing adversarial image perturbations to hijack the end-to-end process from UI selection to browser action execution.
- Leverages a role-slot abstraction and webpage recomposition to handle UI element competition, and utilizes dataflow analysis to align perturbations with post-processing logic.
- Evaluates against six VLM backbones across 13 public websites and a sandbox benchmark, achieving an average attack success rate of 91.9%, outperforming the strongest baseline at 17.4%.
- Demonstrates that localized adversarial visuals can effectively and reliably control downstream agent execution, remaining robust against three agent-level defenses.

- Wanjing Han, Levi Taiji Li, Mu Zhang, Yue Jiang, Guanhong Tao. "Adversarial Images Hijack Web Agents from Visual Grounding to Browser Execution." arXiv — https://arxiv.org/abs/2610.09240
## Secure-CUA: Controlling Untrusted Influence in Computer-Use Agents

- Presents Secure-CUA, an execution model for computer-use agents (CUAs) that enforces strict security requirements on both decision-making and GUI command execution when interacting with untrusted content.
- Employs a transaction-based approach where the agent commits to an explicit sequence of actions and permitted uses of untrusted data prior to interacting with the interface.
- Masks untrusted GUI regions during query evaluation and uses an isolated query model to locate intended interface targets, ensuring instructions embedded in untrusted content cannot hijack execution.
- Evaluated on 400 WebArena tasks across three frontier models, achieving a task success rate of 53.55%, maintaining utility comparable to unprotected agents (55.12%) while preventing execution hijacking.

- Sarthak Choudhary, Mihai Christodorescu, Ashish Hooda, Somesh Jha, Tongxin Li, Damien Octeau. "Secure-CUA: Controlling Untrusted Influence in Computer-Use Agents." arXiv — https://arxiv.org/abs/2610.09469
## Also published

- Shaker Nawasra, Munther Abualkibash. "A Deployment-Aware Feasibility Framework for Machine Learning-Based IoT Intrusion Detection Across Edge, Fog, and Cloud Architectures." arXiv — https://arxiv.org/abs/2610.08867
- Rafid Ahmed, Joseph Fioresi, Mubarak Shah, Yuzhang Shang. "CredLeakBench: Evaluating Credential Leakage and Recovery in LLM Agents." arXiv — https://arxiv.org/abs/2610.08871
- Hai Duong, Thanh Le, Ho Nguyen, ThanhVu Nguyen. "Towards Verifying Neural Networks Against Multi-Parameter Bit-Flip Perturbations." arXiv — https://arxiv.org/abs/2610.08876
- Leon Goldberg, Gal Engelberg. "Contextualization of Third-Party Cloud Security Findings." arXiv — https://arxiv.org/abs/2610.08895
- Animesh Shaw. "Cost of Delay for Post-Quantum Migration: Putting Classical and Harvest-Now-Decrypt-Later Risk on One Ordered List." arXiv — https://arxiv.org/abs/2610.09029
- Hyeongjun Choi. "MARS: Malware Analysis with Rule-Based Scoring of LLM Claims." arXiv — https://arxiv.org/abs/2610.09553
- Jakub Breier, Xiaolu Hou. "Automotive Hardware Attacks: An Architect's Guide to TARA." arXiv — https://arxiv.org/abs/2610.09697
- Xiaoyi Pang, Haoyue Feng, Quanxin Shou, Yikun Miao, Zhengyang Yan, Song Guo. "Black-Box Adversarial Patch Attacks on VLAs via Ancestor VLM Exploitation." arXiv — https://arxiv.org/abs/2610.09708
- Nikolaos Kekatos, Marinelio Chintri, Panagiotis Katsaros, Alexios Lekidis, Tom Nianios, Ioannis Seitoglou, Stylianos Basagiannis. "Hierarchical Security Monitoring for Edge-IoT: A Formal Methods Approach." arXiv — https://arxiv.org/abs/2610.09817
- Nikolaos Kekatos, Marinelio Chintri, Panagiotis Katsaros, Alexios Lekidis, Tom Nianios, Ioannis Seitoglou, Anastasios Temperekidis, Stylianos Basagiannis. "Hybrid Hierarchical Runtime Verification for Edge-IoT Security: Combining MonPoly and RTLola." arXiv — https://arxiv.org/abs/2610.09825
- Teng-Ruei Chen. "Sensitive-Topic Leakage Through LLM Routing Metadata: Measurement and Mitigation." arXiv — https://arxiv.org/abs/2610.09981
- Ergute Bao, Graham Cormode, Xiaokui Xiao, Ting Yu. "BetweenCut: Private Heavy-Node Classification with Doubly Logarithmic Error in Tree Height." arXiv — https://arxiv.org/abs/2610.10075
- Murat Bilgehan Ertan, Marten van Dijk. "Closed-Form Noise Calibration Against Membership Inference for Random-Allocation DP-SGD." arXiv — https://arxiv.org/abs/2610.09651
- Boaz Micah, Nadia Milazzo, Maissa Beji, Borja Aizpurua, Lloren\c{c} Espinosa-Portal\'es, Esteban Payares, Ghada Ben Slama, Luc Andrea, Michel Kurek, Thomas Cope, Olivier Salomon. "Pareto-optimal quantum kernel selection for unsupervised anomaly detection on real malware beaconing data." arXiv — https://arxiv.org/abs/2610.09717
- Piotr Marszalik. "The Price of Privacy: Randomness Complexity of Graph-Based Multi-Secret Sharing." arXiv — https://arxiv.org/abs/2610.10002
- Talal Alrawajfeh, Cristiana Diaconu, Ossi Raisa, Sebastian Rodriguez Beltran, Yuan He, John Bronskill, Richard E. Turner, Antti Honkela. "Efficient Provably Private Classification with a Tabular Foundation Model." arXiv — https://arxiv.org/abs/2610.10068
- Sihao Liu, Ligeng Zhu, Zijian Zhang, Dongyun Zou, Zhengyang Zhang, Changye Li, Song Bian, Song Han, Tony Nowatzki. "Humanize: Judgement Engineering for Agentic Coding." arXiv — https://arxiv.org/abs/2610.08900
- Arip Asadulaev. "Breaking the Space Barrier and its Application to Language Model Inference." arXiv — https://arxiv.org/abs/2610.09139
- Param Biyani, Krishnamurthy Dvijotham. "SpecGuard: Proving a Task Is Broken Before the Agent Cheats." arXiv — https://arxiv.org/abs/2610.09159
- Kai Yi, Tarek Elgamal, Sruthikesh Surineni, Vignesh Vivekraja, Soumyadeep Ghosh, Steven Li. "Few Bits, One Law: Toward W2A4KV2." arXiv — https://arxiv.org/abs/2610.09202
- Tianruo Rose Xu, Jiawei Ren, Yichi Yang, Zhaoxu Zheng, Lianhui Qin. "RT-Safe: Benchmarking Agent Safety in Real-Time Embodied Environment." arXiv — https://arxiv.org/abs/2610.09294
- Xiao Han, Aoyang Quan, Xiangyu Zhao, Xiangjie Kong, Guojiang Shen. "LLM-Enabled UAV Dispatch: A System-Level Survey and Taxonomy." arXiv — https://arxiv.org/abs/2610.09466
- Haonan Deng, Park Sinchaisri. "Stale, Misattributed, or Late: Where Personal Memory Fails Before Generation." arXiv — https://arxiv.org/abs/2610.10265
- Junkai Chen, Yuhao He, Qianshan Wei, Junxiang You, Jingwen Shao, Junkai Lin, Zhongkai Yue, Xiaotian Ye, Zhengbo Jiao, Jiali Cheng, Zhijie Deng, Kening Zheng, Ruiqi Liu, Hadi Amiri, Yi Yu, Zhenan Sun, Qi Li, Ka-Ho Chow, Sijia Liu, Liang Wang, Jiaqi Li, Shu Wu. "Open-MMUnlearning: Unifying Methods and Evaluation for MLLM Unlearning." arXiv — https://arxiv.org/abs/2610.10358
- Artem Zholus, Nicolas Beltran-Velez, Jianhao Yuan, Sarath Chandar, Tushar Nagarajan, Daniel Severo, Koustuv Sinha, Michal Drozdzal, Adriana Romero Soriano, Jeannette Bohg, Nicolas Ballas, Mahmoud Assran. "RoboJEPA: Scaling Robotic Latent World Models." arXiv — https://arxiv.org/abs/2610.10515
- Venkatesh Kolluru, Rajat Shinde, Abdelhak Marouane, Caden Helbling, Deepak Shah, Othneil Drew, Srinivas Kolluru, Iksha Gurung, Manil Maskey, Rahul Ramachandran. "Transferability and operational reliability of a Prithvi crop classification foundation model under phenological and geographic shift across three continents." arXiv — https://arxiv.org/abs/2610.08810
- Thomas Vaitses Fontanari, Maximo Eduardo Rulli, Federico Alvetreti, Donatella Genovese, Simone Scardapane. "LRCC: Generalizing Low-Rank Compression with Conditional Computation." arXiv — https://arxiv.org/abs/2610.08858
- Ignacio G Lopez-Francos, Alexis Gallagher, Samira Shalal. "Toward Evidence-Driven Human-Agent-Robot Teaming for Earth-Independent Anomaly Triage." arXiv — https://arxiv.org/abs/2610.08933
- Syed Ibrahim Omer, Ginny Y. Wong. Xiangyu Zhao. "MaRK: Markov-adapted Recurrent Kernels for Dynamic Operator Conditioning in State Space Models." arXiv — https://arxiv.org/abs/2610.09092
- Thushara Manjari Naduvilakandy, Hyeju Jang, Mohammad Al Hasan. "Multi-Objective Aligned Small Language Model Framework for SUD Patient Dialogue Generation." arXiv — https://arxiv.org/abs/2610.09209
- Zhenyang Liu, Chenjie Cao, Yisu Zhang, Xuhui Zuo, Xiangyang Xue, Yanwei Fu, Tengfei Wang, Chunchao Guo. "OmniCam: Omni-Camera Trajectory Generation via Geometry-Grounded Pose Token Learning." arXiv — https://arxiv.org/abs/2610.09513
- Jiayi Chen, Shuai Wang, Guangxu Zhu, Derrick Wing Kwan Ng, Chengzhong Xu, Kaibin Huang. "Not All Uncertainty Matters: Simulation-in-the-Loop Fast-Slow Reasoning for Decision-Critical Autonomous Driving System." arXiv — https://arxiv.org/abs/2610.09520
- Shengkai Ma, Zhenyu Hou, Weihua Cao. "PARC-Loc: Text-to-Point-Cloud Localization with Partial Assignment and Relational Consistency." arXiv — https://arxiv.org/abs/2610.09761
- A. Ch. Madhusudanarao, Rahul Singh. "Logarithmic Regret via Passive Change Detection in Piecewise-Stationary Self-Tuning Regulation." arXiv — https://arxiv.org/abs/2610.10250
- Trevor McCourt, Ila R. Fiete, Isaac L. Chuang. "Fault-tolerant foundation models." arXiv — https://arxiv.org/abs/2610.10311
- Liu Renhang, Navonil Majumder, Tej Deep Pala, Soujanya Poria. "RoboQuest: Generalist Physical Agents that Search, Inspect and Test." arXiv — https://arxiv.org/abs/2610.10388
- Wei Huang, Bohan Zhang, Chenzhi Liu, Isabella Liu, Shuai Yang, Weian Mao, Luozhou Wang, Yicheng Xiao, Weifeng Lin, Qixin Hu, Bryan Chu, Sifei Liu, Linxi Fan, Xiaojuan Qi, Song Han, Yukang Chen. "Long-WAM: Scaling the Context of World-Action Models." arXiv — https://arxiv.org/abs/2610.10528
- Karthik Vaidhyanathan, Norha Villegas, Raffaela Mirandola, Nicol\'{a}s Cardozo, Ivana Dusparic, Marin Litoiu, Ralf Reussner, Gabriel Tamura. "Mitigating Uncertainty Interactions in GenAI-based Adaptive Systems: Vision, Challenges and Preliminary Guidelines." arXiv — https://arxiv.org/abs/2610.08881
- Malte Hansen, Lukas Damerau, Moritz Bugla, David Moreno-Lumbreras, Wilhelm Hasselbring. "Analysis and Visualization of the Linux Kernel's Software Evolution Using the City Metaphor." arXiv — https://arxiv.org/abs/2610.09910
