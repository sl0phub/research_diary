+++
title = "arXiv Brief — 2026-09-29"
date = 2026-09-29T06:00:00Z
type = "arxiv"
tags = ["cs.CR", "llm-security", "side-channel", "privacy"]
summary = "Agent control boundaries under stress: vault-mediated credentials, spoofed subagent identities, and backchain memory attacks; plus traffic analysis and privacy-preserving cloud consultation."
+++

## In brief

- Agent architectures continue to struggle with control boundaries. Evaluated frameworks trust the harness's own self-reported execution record over independent verification, allow spoofed subagent identities to hijack orchestration control, and consolidate low-trust episodic observations into action-driving procedural memory. A vault-mediated connector architecture limits credential exposure but requires strong action authorization.
- Remote LLM inference leaves practical signatures in encrypted network traffic. Both the target model and the prompt category can be fingerprinted from packet timings and sizes, and collaborative multi-agent tasks remain detectable even when the observer can see only one agent's traffic.
- To protect task intent during local-cloud LLM consultation, one framework mathematically reformulates the reasoning requirement before sending it to the cloud, reducing intent inference to near zero without relying on decoy queries.



## A Large-Scale Benchmark and Risk Assessment of Traffic Analysis Attacks on Cloud LLM Services

- A unified traffic-analysis benchmark measures leakage across both direct user-LLM interactions and collaborative multi-agent executions, containing 60,000 interactions across 10 models and 6 prompt categories, plus 2,838 multi-agent executions covering 10 tasks.
- A passive on-path observer using only encrypted packet metadata (timing, sizes, burst structure) can classify the serving model at 97.7% balanced accuracy, the prompt category at 76.7% mean accuracy, and the multi-agent task at up to 90.7% accuracy.
- Multi-agent task fingerprints remain detectable even when the observer has partial visibility and can see only a single agent's traffic, because task workflows create distinct packet counts, sizes, and burst timing patterns.

Pouryousef, S., Lopez, J., Nowmi, S. R., Kamol, M. M., Hossain, M., Tran, M., Rahman, M. S. "A Large-Scale Benchmark and Risk Assessment of Traffic Analysis Attacks on Cloud LLM Services." arXiv, 2026.
arXiv:2609.31877 — https://arxiv.org/abs/2609.31877

## CyberClear: A Benchmark for LLM Agent Systems on APT Attack Chain Provenance

- Existing agent benchmarks focus on CTF problem-solving, vulnerability discovery, or code repair. CyberClear evaluates APT attack chain provenance: reasoning over raw, noisy, long-context defender logs to extract a complete attack graph without prior attack clues.
- The benchmark contains 450 instances averaging 531,000 characters of security logs per instance. It covers 318 single-step attacks and 132 multi-stage attack chains, derived from the PROVCON and CAM-LDS datasets and verified by Claude Opus and GPT-4o.
- An LLM-as-a-judge method compares generated DOT provenance graphs against the ground truth on five semantic dimensions: single-step correctness, multi-step identification, temporal and causal consistency, entity and relationship fidelity, and attack narrative consistency. Identifiers and visual styling are ignored.
- The paper also proposes CyberProvenance, a multi-agent harness with evidence accumulation, execution validation, and feedback-guided refinement, demonstrating that current agents fail on this task because they lack iterative evidence refinement rather than just long-context reasoning.

Chen, Q., Huo, F., Shen, H., Guo, J., Li, S., Cheng, G. "CyberClear: A Benchmark for LLM Agent Systems on APT Attack Chain Provenance." arXiv, 2026.
arXiv:2609.32424 — https://arxiv.org/abs/2609.32424

## Ask Without Telling: Local SLMs Consult Cloud LLMs Without Revealing Task Intent

- Hiding sensitive names and values in an LLM query still leaves the task's context and operation visible: allocating generic supplies across generic nodes still signals a supply shortage, which can be sensitive.
- The PriCon framework instead hides task intent by having a local Small Language Model (SLM) convert the core reasoning requirement into a generalized mathematical or abstract query. The cloud LLM solves the abstraction, and the local SLM grounds the response back into the sensitive context.
- Evaluated on 100 tasks on medical and legal reasoning benchmarks, the protocol reduces an observer's ability to infer the original task intent to 4% (Hit@1 close to 0%), compared to 98% under direct queries and 93–99% under sensitive-value removal.
- The cloud-assisted local SLM retains 89% of the performance of querying the cloud LLM directly, demonstrating that reasoning capacity can be cleanly separated from data exposure without relying on decoy queries.

Wang, Y., Li, Y., Fan, S., Zheng, Y., Chang, T.-H. "Ask Without Telling: Local SLMs Consult Cloud LLMs Without Revealing Task Intent." arXiv, 2026.
arXiv:2609.32642 — https://arxiv.org/abs/2609.32642

## Hearsay: Can an Auditor Trust the Record a Deployed Agent Harness Writes?

- An agent harness writes its own execution record, which is all a later auditor has. Across 16 deployed agent frameworks, none currently writes a record that an absent reader can verify without trusting the harness itself.
- Evaluated on 140 runs across five harnesses and 14 tasks, a native execution record allows examiners to name the right fault in 74–91% of cases. However, fewer than 10% of citations for these verdicts point to anything the harness did not write itself (i.e. independent evidence), and examiners missed half of all entries manually deleted or fabricated by the researchers.
- A cryptographic hash chain over the harness's own record passes all omissions and fabrications, because it merely seals what the harness chose to write.
- The proposed remedy is a second author: an append-only log kept outside the harness that records what passes between the harness and the model. A reverse check between the two records caught 28 of 28 run-time fabrications and 98 of 115 post-run edits, showing that evidence relies on who writes it, not just what it contains.

Dai, J., Yang, Z., Shao, P., Ng, K., Liu, Z., Ju, C., He, Y., Hu, B. "Hearsay: Can an Auditor Trust the Record a Deployed Agent Harness Writes?" arXiv, 2026.
arXiv:2609.32495 — https://arxiv.org/abs/2609.32495

## API Secrets Should Never Become Tokens in the LLM's Vocabulary: A Threat Analysis of API Credential Handling in LLM Agent Systems and an Empirical Evaluation of a Vault-Mediated Execution Boundary

- Passing an API key in an LLM prompt or tool configuration moves credential hygiene from a storage problem to an execution-security problem. Once in the model's context, the key can be retained in conversation history, logs, memory stores, and generated code, where prompt injection or excessive agency can exploit it.
- A vault-mediated execution architecture solves this by having the model select a connector identifier rather than handling the raw key, while a trusted boundary injects the authentication header during the actual request.
- Black-box evaluation of a production implementation (Corvic Security Vault) confirmed the boundary holds: across 16 probes, an authenticated GitHub API request succeeded while the credential itself remained absent from process environment values, caller-visible headers, the filesystem, and third-party echo services.
- Centralized custody does not guarantee correct usage: one tested connector failed because its stored header mapping did not meet the provider's authentication contract, highlighting that mediation must be paired with strict least privilege and deterministic action authorization.

Kenney, P., Ahmadi, H., Lusson, D., Nguyen, D., Gill, G. "API Secrets Should Never Become Tokens in the LLM's Vocabulary: A Threat Analysis of API Credential Handling in LLM Agent Systems and an Empirical Evaluation of a Vault-Mediated Execution Boundary." arXiv, 2026.
arXiv:2609.33371 — https://arxiv.org/abs/2609.33371

## Trust the Brand, Lose Control: How Identity Hijacks LLM Agent Orchestration

- In multi-agent orchestration, the orchestrator delegates tasks based on the displayed identities of subagents. This paper demonstrates that these labels decide operational authority: who is trusted to check work and who is allowed to change it.
- TrustFork, a new safety benchmark with 1,890 tasks and 27,826 trajectories across 16 systems, tests this by giving one subagent a risky goal (e.g., executing a poisoned cleaner) while keeping three aligned, allowing contradictory evidence to emerge. Crucially, the benchmark can spoof the identity labels shown to the orchestrator without changing the underlying subagent models.
- Even when another subagent explicitly contradicts the risky response, the orchestrator still acts on the risky advice in 72.0% of cases. Swapping model family labels (e.g., spoofing a subagent as being from the orchestrator's own family) nearly triples how often the orchestrator adopts the risky response.
- A safe alternative is available in 84.0% of tasks, but orchestrators select it only 25.0% of the time. Runtime defenses show that hiding identity cues entirely is the most consistent mitigation, whereas relying on pre-action verification works only if the harness surfaces enough contradicting evidence.

Mao, X., Qian, R., Chen, L., Gao, Y., Liao, J., Cai, J., Zhao, J., Wang, C. "Trust the Brand, Lose Control: How Identity Hijacks LLM Agent Orchestration." arXiv, 2026.
arXiv:2609.32635 — https://arxiv.org/abs/2609.32635

## REFINE: A Resilient Evolution Framework for Intelligent Enterprise Alert Triage in Security Operations Centers

- Security Operations Centers (SOCs) need alert triage models that evolve with changing asset priorities and threat landscapes, but standard LLM-agent self-evolution optimizes a single scalar objective, failing to enforce the asymmetric cost of false positives (a time penalty) vs. missed threats (a security failure).
- REFINE introduces a skill-evolution framework that treats 100% recall as a hard, inviolable constraint. An agent starts with a globally inferred initial skill instead of an empty or manual seed, then iteratively improves accuracy (expanding false-positive auto-closure) over a batch of boundary samples.
- The constraint is enforced hierarchically: a batch-level gate rejects inner-loop revisions that drop recall before they waste evaluation budget, and a global-level gate outputs only the highest-accuracy skill that still retains 100% recall. If no such skill is found, the system explicitly falls back to human triage.
- Evaluated on four alert scenarios from a real industrial SOC, REFINE reaches 1.0 recall across all evolution sets. On future test windows, it retains 1.0 recall in three of four scenarios; in the one case where performance degraded (0.807 recall), it still outperformed generic self-evolution baselines (0.49–0.58).

Chen, H., Long, Q., Wang, Y. "REFINE: A Resilient Evolution Framework for Intelligent Enterprise Alert Triage in Security Operations Centers." arXiv, 2026.
arXiv:2609.32516 — https://arxiv.org/abs/2609.32516

## BMA: Backchain Memory Attacks Create Unauthorized Control Paths in LLM Agents

- Agent persistent memory introduces an authority-control mismatch: an agent may consolidate observations from a low-trust source into reusable rules that later bypass security checks on clean tasks. For example, a low-trust report about a specific cancellation episode is generalized by the agent into a rule to "cancel before verifying identity."
- The Backchain Memory Attack (BMA) is a grey-box, inverse-planning attack that reasons backward from a target action to the memory that would trigger it, and finally to the declarative edit of low-trust evidence that would form that memory. The adversary only edits the low-trust evidence; they do not write memory or alter the future task directly.
- The paper introduces Pathway-Certified Attack Success Rate (Path-CASR) to ensure hits are genuinely memory-mediated: the registered memory must form, be retrieved, drive the target behavior, and pass matched-intervention checks. BMA achieves 18.8% Macro Path-CASR across four substrates and three decision backbones, compared to 13.4% for the baseline.
- Typical memory-side controls still leave 11.0% Path-CASR. Provenance-bound authorization, which links the consolidated rule back to the authority of its source, reduces the attack success rate to 2.0% while preserving 92.1% legitimate-action success.

Fan, K., Gao, Y., Tang, X., Bissyandé, T. F., Zhang, W. "BMA: Backchain Memory Attacks Create Unauthorized Control Paths in LLM Agents." arXiv, 2026.
arXiv:2609.32186 — https://arxiv.org/abs/2609.32186

## Also published

- Kweon, S., Chung, P., Straw, I., Dameff, C. J., Tully, J. L., Savage, S., Voelker, G. M., Kumar, D. "Something to Talk About: Social Media as a Lens on Healthcare Ransomware Events." arXiv:2609.31984 — https://arxiv.org/abs/2609.31984
- Shaw, A. "Silent Failures in Agentic Security Evaluation: A Validated Harness for Tool-Call Mediation Under Indirect Prompt Injection." arXiv:2609.32691 — https://arxiv.org/abs/2609.32691
- Shahriar, A., Rahman, M. N., Ahmed, S., Sadeque, F., Parvez, M. R. "AgentTell: Behavioural Side-Channel Leakage in Browser-Use Agents." arXiv:2609.32915 — https://arxiv.org/abs/2609.32915
- Zhu, P., Yang, J., Liu, Y., Sun, L., Su, S. "SkillDRE: Dual-Stage Red-Team Evolution of Agent Skills via Pre-Execution and Runtime Feedback." arXiv:2609.32400 — https://arxiv.org/abs/2609.32400
