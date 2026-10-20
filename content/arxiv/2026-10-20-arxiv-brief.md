+++
title = "arXiv Brief — 2026-10-20"
date = 2026-10-20T00:00:00Z
type = "arxiv"
tags = ["arxiv", "cs.CR", "llm-security"]
summary = "New research on LLM jailbreak evaluation, prompt injection taxonomy, federated learning for malware, and coding agents for kernel vulnerabilities."
+++

## In brief

- **LLM security evaluation challenges:** Two papers highlight flaws in current evaluation metrics. One demonstrates how changing the grader model collapses jailbreak attack success rates, while another systematizes prompt injection techniques to show how widely used benchmarks test only part of the attack space and adaptive attackers favor mechanisms that curated benchmarks underrepresent.
- **Agentic vulnerability detection falls short:** An evaluation of Claude Code on Linux kernel bugs finds that agents identify the correct vulnerability class and location in only 15.7% of attempts, highlighting the gap between basic coding assistance and security auditing.

## The Missing Compliance Class: LLM Graders That Collapse Jailbreak Success, and a Free Check

- Evaluates the effect of changing the LLM grader while keeping the target model, prompts, and responses fixed when assessing jailbreak attack success rates.
- Measures that on two corpora of 900 responses and eight graders, the compliance rate differs by a factor of 22 to 25, while the non-refusal rate differs by 18 to 23 percentage points.
- Proposes a reporting minimum that requires publishing the per-class label counts and the named grader alongside the compliance rate to expose this collapse without human labeling costs.
- Ruqiya Bin Safi. "The Missing Compliance Class: LLM Graders That Collapse Jailbreak Success, and a Free Check." arXiv — https://arxiv.org/abs/2610.24872

## SoK: PIAtlas: Decomposing the Unbounded Prompt Injection Attack Space

- Systematizes the prompt injection attack space by proposing PIAtlas, a taxonomy organized around how injected instructions are constructed to subvert underlying models, unifying incompatible vocabularies from over twenty public datasets.
- Maps thousands of records from a newly released, license-clean prompt-injection dataset (PICorpus) to PIAtlas under a human-verified protocol, showing that attacks typically combine techniques from only a few mechanisms.
- Demonstrates that widely used agent benchmarks test only part of the attack space, and adaptive attackers favor mechanisms that curated benchmarks underrepresent.
- Stavros Damianakis, Konstantinos Psounis. "SoK: PIAtlas: Decomposing the Unbounded Prompt Injection Attack Space." arXiv — https://arxiv.org/abs/2610.24999

## Federated Learning for Malware Image Classification under Data Heterogeneity

- Evaluates federated learning for malware image classification under varying degrees of data heterogeneity across the MalImg, Virus-MNIST, and MalNet datasets.
- Shows that while federated learning achieves strong accuracy under IID conditions, both accuracy and training stability degrade as data becomes increasingly non-IID.
- Demonstrates that class entropy (diversity of class labels present in a given round) exhibits strong positive correlation with global model accuracy, and proposes an entropy-aware client selection strategy that filters candidate client subsets based on class entropy to outperform standard random selection.
- Victor Taiwo, Cemal Nisan, Muhammad Athallah, M. Emre Gursoy, Oznur Ozkasap. "Federated Learning for Malware Image Classification under Data Heterogeneity." arXiv — https://arxiv.org/abs/2610.25264

## How Effectively Do Security Skills Guide Coding Agents in Vulnerability Detection in Linux Kernel?

- Evaluates Claude Code and four underlying LLMs on 100 real Linux kernel vulnerabilities across ten classes to measure the effectiveness of 37 task-specific security skills in vulnerability analysis, resulting in 14,800 skill-LLM-vulnerability runs.
- Measures that across all runs, 24.4% locate the correct vulnerable function, 18.3% identify both the function and responsible statement, and 15.7% identify the correct vulnerable class.
- Proposes SKILL-SIF, an iterative self-improving framework that automatically evolves vulnerability detection skills by learning from previously missed vulnerabilities and their associated failure patterns, which improves fully correct vulnerability detection by up to 8 percentage points (from 2% to 16%) on unseen vulnerabilities.
- Haoran Xue, Nikta Akbarpour, Gias Uddin, Song Wang. "How Effectively Do Security Skills Guide Coding Agents in Vulnerability Detection in Linux Kernel?." arXiv — https://arxiv.org/abs/2610.25705

## Also published

- Walid El Maouaki, Mohammad Izen, Nouhaila Innan, Alberto Marchisio, Muhammad Shafique. "Q-MALDetect: Quantum Image-Based Malware Detection and Adversarial Robustness Analysis." arXiv — https://arxiv.org/abs/2610.26240
- Nam Hoang Thanh, Trung Pham Duy, Lam Bui Thu. "Mal-AAEGAN: Adversarial Autoencoder with Double-Critic WGAN-GP for Malware Generation." arXiv — https://arxiv.org/abs/2610.26488
- Ashok Subbabhatta Gopalakrishna. "Connection Escrow: Holding AI-Agent Pod Egress in the Kernel Until an Isolated Verifier Rules." arXiv — https://arxiv.org/abs/2610.26501
- Rohan Menon, Chih-Hong Cheng. "Beyond Attack Success Rate: Cost-Aware Metric for Evaluating Iterative LLM Jailbreaks." arXiv — https://arxiv.org/abs/2610.26589
