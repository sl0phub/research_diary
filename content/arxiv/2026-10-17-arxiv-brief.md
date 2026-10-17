+++
title = "arXiv Brief — 2026-10-17"
date = "2026-10-17T06:00:00Z"
type = "arxiv"
tags = ["cs.CR", "cs.AI", "cs.SE", "llm-security"]
summary = "New papers on LLM agent robustness, autonomous post-training systems, multi-agent aggregation biases, and delegation governance."
+++

## In brief

- **Multi-agent LLM systems are under pressure.** New findings explore both the risks and mechanisms of scaling LLM agents, from exploiting their inherent biases during multi-agent aggregation to tracking their emergent authority dynamics in polycentric governance structures.
- **Autonomous agents can self-improve base models.** Research introduces an agent-native system where teams of LLM agents successfully post-train a raw base model to match or surpass official instruct versions, entirely autonomously.
- **Agent robustness requires verification mechanisms.** Evaluations highlight that current frontier agents fail to recognize input perturbations and blindly propagate corrupted data, stressing the need for uncertainty awareness and recovery training.

## Bias Control and Injection for Multi-Agent Aggregation
- Resolves disagreements in multi-agent LLM reasoning by mitigating non-semantic biases, such as majority pressure and style preferences, while exploiting decision instability to measure reliability.
- Implements a test-time aggregation framework that uses bias control to normalize reasoning traces and bias injection to deliberately place an agent's initial answer in the minority.
- Achieves higher average accuracy and token efficiency than non-oracle aggregation methods across mathematical reasoning benchmarks without modifying underlying interaction processes.
- Sungjae Lee, Soheil Abbasloo, Jabin Koo, Jungseul Ok. "Bias Control and Injection for Multi-Agent Aggregation." arXiv — https://arxiv.org/abs/2610.21290

## The Delegation Dilemma: Economies of Scale, Accountability, and Polycentric Governance
- Investigates the scale-accountability tradeoff in multi-agent delegation, showing that larger groups offer better cost-sharing but dilute the value of individual accountability.
- Demonstrates through 30-agent LLM simulations that fully delegated, accountable governance frequently emerges as polycentric, exhibiting fluid cycles of concentration, exploitation, exit, and re-formation.
- Finds that while models of different capabilities share a willingness to assume leadership, they diverge in their exercise of authority, with more capable models initiating exploitation more frequently.
- Arin Mukhopadhyay, Aris Filos-Ratsikas, Panayiotis Danassis. "The Delegation Dilemma: Economies of Scale, Accountability, and Polycentric Governance." arXiv — https://arxiv.org/abs/2610.21746

## Athanor: An Agent-Native System for Autonomous Post-Training Research
- Introduces an open agent-native sandbox that enables LLM agents to autonomously conduct post-training research on real GPUs, managing datasets, writing algorithms, and tuning hyperparameters without external teacher models.
- Demonstrates that a team of four Claude Opus 5.5 agents, acting without human research advice, improved a Qwen3-4B-Base model from 15.9 to 67.3 on a development suite and from 9.2 to 48.2 on a held-out suite over 104 hours.
- Reveals that agents achieve these results by recombining known methods and merging each other's models, highlighting the engineering and research ability of current frontier models.
- Yufa Zhou, Yichen Wang, Jiakun Fan, Ziqi Shu, Zhichao Liu, Anru R. Zhang, Neiwen Ling, Zijun Wei. "Athanor: An Agent-Native System for Autonomous Post-Training Research." arXiv — https://arxiv.org/abs/2610.21055

## AgentPerturb: Evaluating LLM Agent Robustness under Controlled Interaction Perturbations
- Quantifies the robustness of frontier LLM agents through controlled interaction perturbations on APEX-Agents and Toolathlon benchmarks, showing consistent performance degradation under noise.
- Trajectory-level analysis reveals that agents rarely recognize altered inputs and frequently propagate corrupted information without verification, rather than detecting the manipulation.
- Cost analysis demonstrates that successful execution under perturbation requires substantially more computation, motivating new training objectives focused on uncertainty awareness and recovery.
- Yuanjian Xu, Jinyi Han, Jianing Hao, Yuxuan Sun, Fanyang Lu, Richeng Xuan, Guang Zhang, Zhichao Hu. "AgentPerturb: Evaluating LLM Agent Robustness under Controlled Interaction Perturbations." arXiv — https://arxiv.org/abs/2610.21624

## Also published

- Hao Zhang (First Institute of Oceanography, Ministry of Natural Resources, Qingdao, China), Hengrui Liu (First Institute of Oceanography, Ministry of Natural Resources, Qingdao, China), Lina Sun (First Institute of Oceanography, Ministry of Natural Resources, Qingdao, China), Junmin Meng (First Institute of Oceanography, Ministry of Natural Resources, Qingdao, China). "ISW-Agent: Integrating LLM-Driven Dialogue with n8n Workflow for Internal Solitary Wave Remote Sensing Image Processing." arXiv — https://arxiv.org/abs/2610.21502
- Shuoran Jiang, Wentao Zhu, Yang Xiang, Dongfeng Li, Yunan Zhang, Mengchen Zhao, Yuhui Guo, Kai Chen, Youcheng Pan, Xiangping Wu, Qingcai Chen. "Functional Subnetwork Localization for Efficient Continual Learning in Large Language Models." arXiv — https://arxiv.org/abs/2610.21537
- Zhiyuan Ma, Jiabao Wei, Tianyu Wang, Hanqing Wang, Jiadong Pan, Haowen Xu, Liangliang Zhao, Ruixun Liu, Yuhan Wang, Yuwei Zhang, Liang Feng, Junhao Xiao, Kaiyan Zhang, Xuekai Zhu, Daizong Liu, Biqing Qi, Yihao Liu, Ganqu Cui, Ning Ding, Linfeng Zhang, Jianjun Li, Kun He, Xiang Bai, Bowen Zhou. "Reinforcement Learning-driven Diffusion Models: Language, Vision, and Beyond." arXiv — https://arxiv.org/abs/2610.21539
- Dixi Yao, Tahseen Rabbani, Tian Li. "Private Retrieval Augmented Generation via Random Projection." arXiv — https://arxiv.org/abs/2610.22297
- Han Shen, Qifu Tyler Sun, Fanyang Meng, Ye Wang, Yongsheng Liang. "PriorityFEC: Deadline-Aware Streaming FEC for KV-Cache Handoff in Edge Multi-Agent Systems." arXiv — https://arxiv.org/abs/2610.21390
