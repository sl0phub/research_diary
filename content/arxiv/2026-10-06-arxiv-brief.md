+++
title = "arXiv Brief — 2026-10-06"
date = 2026-10-06T06:00:00Z
type = "arxiv"
tags = ["cs.CR", "cs.AI", "cs.SE", "llm-security", "vulnerability-discovery"]
summary = "An attack injecting vulnerabilities via AI coding assistants, task-level poisoning detection in instruction-tuned LLMs, and fingerprinting black-box dense retrievers."
+++

## In brief

- AI models can be compromised at different stages to undermine security: malicious coding assistants passively inserting vulnerabilities, poisoned instruction data targeting specific tasks, and distinct embeddings leaking through retriever outputs.
- Detection systems face unique challenges, with task-level poisoning requiring conditional output auditing without a clean model, and retriever fingerprinting bypassing even reranked end-to-end RAG environments.

## Beware EviLLM: Enabling Vulnerability Injection via Large Language Models

- Evaluates an attack model where an AI coding assistant covertly injects software vulnerabilities that are hard for developers to detect, simulating a compromised backend.
- A user study found that under the Custom Instructions condition, 7 out of 8 participants submitted code containing vulnerabilities.
- Detection was notably poor, with 13 out of 21 participants (61.9%) reporting that they rarely thought about the security threat, highlighting the risk of passive acceptance in AI-assisted development.

Zeezoo Ryu, Simon Chung, Muhammad Faraz Karim, Anna Raymaker, Karan Singh Jodha, Yash Chaturvedi, Sukarno Mertoguno. "Beware EviLLM: Enabling Vulnerability Injection via Large Language Models." arXiv, 2026.
arXiv:2610.03857 — https://arxiv.org/abs/2610.03857
## Localize-and-Detect: Auditing Task-Level Poisoning in Instruction-Tuned Models

- Investigates auditing LLMs for task-level poisoning where instruction tuning data is manipulated to inject a backdoor on a specific target task.
- The two-stage auditing method ranks suspect tasks based on conditional model behavior (Stage A) and evaluates task-conditioned generation (Stage B), identifying poisoned tasks without requiring a clean reference model.
- Out of 108 poisoned Llama models trained with varied parameters including budgets like 10, 30 and 50 examples, correct target-task reports fall from 65 to 30 over the tested range, demonstrating reliable extraction but dropping at lower poisoning configurations.

Luze Sun, Cristina Nita-Rotaru, Alina Oprea. "Localize-and-Detect: Auditing Task-Level Poisoning in Instruction-Tuned Models." arXiv, 2026.
arXiv:2610.03960 — https://arxiv.org/abs/2610.03960
## The TellTail of Embeddings: Fingerprinting Retrievers in Black-Box Systems

- Introduces a fingerprinting method for black-box dense retrievers, optimizing an adversarial suffix to induce a model-specific retrieval behavior when appended to queries.
- Tested across multiple interfaces, the targeted adversarial queries consistently achieved a high Attack Success Rate (ASR) of identifying the correct retriever under full-rank and response-only configurations.
- The approach was validated in an end-to-end RAG system (OpenWebUI) with reranking, where 14 of the 19 candidates had at least 6 of their 10 optimized queries achieve all target-topic retrieved chunks, demonstrating that distinct representation topologies leak through retrieval outputs even under strong filtering.

Abdullah Garra, Matan Ben-Tov, Mahmood Sharif. "The TellTail of Embeddings: Fingerprinting Retrievers in Black-Box Systems." arXiv, 2026.
arXiv:2610.04026 — https://arxiv.org/abs/2610.04026
## Also published

- Maria Sanchez del Rio, Mikhail Terekhov. "Control OSWorld: An AI Control Environment for GUI Computer Use Agents." arXiv:2610.03818 — https://arxiv.org/abs/2610.03818
- Akash Iyer, Taha Demirkan, Keerthi Koneru, Aaryan Siddharthan, Sheethal Kumar, Ramesh Radhakrishnan. "From Requirements to Attack Trees: Grounded LLM Agents for Design-Time Security Review." arXiv:2610.03820 — https://arxiv.org/abs/2610.03820
- Kieu Dang, Phung Lai, Ching-Yun Ko, Pin-Yu Chen. "Adaptive Co-Serving LLM Watermarking on Modern Inference Engines." arXiv:2610.03955 — https://arxiv.org/abs/2610.03955
- Ekzhin Ear, Caleb Chang, Shouhuai Xu. "SCRM: An Actionable Framework for Space Cyber Risk Management." arXiv:2610.03970 — https://arxiv.org/abs/2610.03970
- Md Shamimul Islam, Ayesha S. Dina. "SERA-IDS: Structured Experience Retrieval-Augmented Intrusion Detection with Small Language Models." arXiv:2610.03999 — https://arxiv.org/abs/2610.03999
