+++
title = "arXiv Brief — 2026-09-16"
date = 2026-09-16T06:00:00Z
type = "arxiv"
tags = ["cs.CR", "llm-security", "hardware", "exploitation", "mobile", "binary-analysis"]
summary = "LLM agents are central today, revealing new architectural risks like capability laundering and the stochastic deputy problem, while hardware vulnerabilities expand into GPU memory architectures."
+++

## In brief

* LLM agent capabilities present new structural threats. The "capability laundering" paper shows how a weaker orchestrator model can bypass safety boundaries by breaking tasks down and feeding benign sub-tasks to aligned frontier models. Similarly, the "stochastic deputy" problem highlights the risk of relying on LLM-supplied parameters for multi-tenant isolation.
* GPU Rowhammer is becoming practical. "GPUThor" bypasses ECC-protected GPUs by exploiting non-uniform memory-access patterns, significantly increasing bit flip rates and demonstrating privilege escalation on modern NVIDIA architectures.

## Divide, Consult, Conquer: Capability Laundering Through Aligned LLMs

* A weaker, unaligned model can orchestrate a harmful task by decomposing it into benign sub-tasks, querying an aligned, stronger model for each sub-task independently, and then locally reassembling the results.
* This "capability laundering" attack completely avoids triggering standard safety classifiers and jailbreak detectors since no single query violates safety policies.
* In tests, the Gemma-4-31B orchestrator bypassed GPT-5.5's safeguards on the CyBench and CBRN attack chain datasets, resulting in a score uplift from 62.3 to 83.1 on a 100-point bioweapon rubric.
* Refusing harmful queries in aligned models does not prevent their capabilities from being effectively utilized to compose larger malicious attacks.

Mark Russinovich, Blake Bullwinkel, Giorgio Severi, Cristian Ovadiuc, Ahmed Salem. "Divide, Consult, Conquer: Capability Laundering Through Aligned LLMs". arXiv, 2026. https://arxiv.org/abs/2609.15383

## GPUThor: Amplifying Rowhammer Attacks via Non-Uniform Patterns to Exploit ECC-Protected GPUs

* Traditional GPU Rowhammer attacks are limited by uniform hammering patterns, causing low bit flip rates that limit practical exploitation.
* GPUThor introduces a high-intensity non-uniform hammering technique by reverse-engineering memory-access coalescing on NVIDIA GPUs to prioritize aggressor rows over decoy rows.
* The attack successfully navigates in-DRAM mitigations by crafting specific patterns across refresh intervals, boosting bit flip rates by up to 23,500 more than previous GPU attacks.
* This allows practical Rowhammer exploitation on ECC-protected GPUs (such as A4000, A5000, A6000), achieving uncorrectable double and triple bit flips to enable privilege escalation.

Chris S. Lin, Joyce Qu, Aditya Rajeev, Gururaj Saileshwar. "GPUThor: Amplifying Rowhammer Attacks via Non-Uniform Patterns to Exploit ECC-Protected GPUs". arXiv, 2026. https://arxiv.org/abs/2609.16546

## The Stochastic Deputy: Structural Tenant Isolation for Tool-Using LLM Agents

* LLM agents handling tool access often use the "stochastic deputy" pattern where the LLM's output determines the tenant identifier, opening it up to prompt injection risks that can lead to cross-tenant data access.
* Relying on model compliance for tenant isolation is structurally flawed; an ablation study showed that properly formatted but malicious out-of-scope read requests were honored 26 out of 26 times.
* A structural defense is proposed: eliminating the tenant identity from the Model Context Protocol (MCP) schema, forcing the underlying interface to derive access from verified, out-of-band credentials.
* Implementing cryptographically protected context binding at the interface level caused a latency increase, but a JSON_TABLE lateral join strategy can restore index access and performance.

Mirza Samad Ahmed Baig, Syeda Anshrah Gillani, Asher Ali, Muhammad Hamzah Siddiqui. "The Stochastic Deputy: Structural Tenant Isolation for Tool-Using LLM Agents". arXiv, 2026. https://arxiv.org/abs/2609.14780

## InceptionRAG: Stealthy Poisoning Attack Against Retrieval-Augmented Generation

* InceptionRAG outlines a stealthy poisoning strategy against Retrieval-Augmented Generation (RAG) models, moving beyond traditional single-document explicit injection attacks.
* The payload is fragmented into a chain of dormant, seemingly harmless passages designed to evade standard mitigation mechanisms during independent examination.
* When these passages are collectively retrieved, they induce the LLM to self-deduce misinformation through multi-hop reasoning, showing over 80% attack success rates against black-box models.
* The attack implies that stronger reasoning capabilities in LLMs ironically exacerbate their vulnerability to reasoning-based poisoning.

Jiachang Zhang, Min Chen, Xiao Ren, Zhenyong Zhang, Yuanchao Shu, Yunjun Gao, Zhikun Zhang. "InceptionRAG: Stealthy Poisoning Attack Against Retrieval-Augmented Generation". arXiv, 2026. https://arxiv.org/abs/2609.16818

## Universal Defenses for Tool-Integrated LLM Agents Against Adversarial Attacks

* Tool-integrated LLM agents face significant adversarial risks from direct and indirect prompt injection, memory poisoning, and backdoor attacks.
* The paper evaluates universal defenses, focusing on Attacker Tool Filtering via anomaly detection (e.g., Isolation Forest) and Normal Tool Recalling which restores the initial toolset prior to planning.
* Additional prompt-based defense techniques, such as Chain-of-Thought reasoning and task paraphrasing, were used to mitigate these vulnerabilities.
* Experiments over multiple open-source and proprietary models demonstrated a reduction in Attack Success Rates (ASR), often down to 0%, while maintaining normal task performance.

Xiaoyan Li, Yunli Wang. "Universal Defenses for Tool-Integrated LLM Agents Against Adversarial Attacks". arXiv, 2026. https://arxiv.org/abs/2609.16098

## SEMA-GUARD: Semantic and Graph-Based Vulnerability Detection in Assembly Code

* SEMA-GUARD introduces a graph neural network-based approach to detect vulnerabilities in compiled assembly code, eliminating the reliance on source code availability.
* It augments conventional control flow graphs with deeper semantic information, integrating stack manipulations, memory accesses, and data flow.
* The framework analyzes code by translating it to assembly and chunking at the function level.
* Testing on the Juliet Test Suite yielded an 85.1% accuracy and an F1 score of 0.801, demonstrating that semantic context significantly improves structural anomaly detection in binaries.

Halil Dursunoglu, Kaan Sulkalar. "SEMA-GUARD: Semantic and Graph-Based Vulnerability Detection in Assembly Code". arXiv, 2026. https://arxiv.org/abs/2609.17254

## Toward Secure AI-Powered Penetration Testing Agents: Security Threats, Guardrails, and Architectural Perspectives

* AI-powered penetration testing agents introduce unique risks, particularly regarding autonomous adversarial actions and unintended side effects.
* The paper outlines architectural guardrails required to safely deploy LLMs for automated security testing.
* *Abstract only — full text not retrieved.*

Rahul Dev T Y, Hiran V Nath. "Toward Secure AI-Powered Penetration Testing Agents: Security Threats, Guardrails, and Architectural Perspectives". arXiv, 2026. https://arxiv.org/abs/2609.16694

## When Agents See Differently: Exposing UI Desynchronization Threats in Mobile Agents

* Mobile agents rely on UI consistency, but UI desynchronization threats allow applications to deceive the agent with a layout that differs from what human users observe.
* Attackers can build Android applications (APKs) that present physical visual elements to a user while feeding contradictory view hierarchies to the agent model.
* Evaluations across five frameworks demonstrated an average 77.9% misleading rate on agents without arousing suspicion in human studies.

Heng Li, Fulin Zhao, Zhe Geng, Zhiyuan Yao, Wei Yuan, Xiapu Luo. "When Agents See Differently: Exposing UI Desynchronization Threats in Mobile Agents". arXiv, 2026. https://arxiv.org/abs/2609.16732

## Also published

* "Permutation-Based Stegomalware in Large Language Models: Threats and Countermeasures", arXiv. https://arxiv.org/abs/2609.16193
