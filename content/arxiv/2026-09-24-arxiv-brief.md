+++
title = "arXiv Brief — 2026-09-24"
date = 2026-09-24T06:00:00Z
type = "arxiv"
tags = ["cs.CR", "llm-security", "fuzzing", "memory-safety", "cloud"]
summary = "New perspectives on LLM cryptographic capabilities, agent oversight bypasses, and hardware fuzzing paradigms."
+++

## In brief

- Multi-agent and tool-using LLM workflows are proving vulnerable to architectural oversights, with attacks demonstrating bypasses of reasoning-based oversight via token injection, and agent routing failures via name collisions.
- Hardware fuzzing is undergoing systematization, distinguishing it from software fuzzing, with new frameworks addressing the unique constraints of bounded search, oracles, and target abstractions in hardware designs.
- Blind cipher identification by LLMs is heavily dependent on metadata, with capability collapsing dramatically when metadata is removed, emphasizing structural heuristics over genuine statistical cryptanalysis.

## ACTS: A multi-tier benchmark evaluating LLM cipher identification under controlled blind conditions

- Introduces ACTS, a benchmark isolating LLM cryptanalytic ability by progressively depriving metadata, evaluating whether models genuinely perform statistical cryptanalysis on ciphertexts or merely exploit contextual hints.
- Extensive evaluation on 7,000 files reveals a 40.9 percentage point drop in capability when shifting from full metadata (Tier-1: 71.7% accuracy) to completely blind ciphertext-only conditions (Tier-3: 30.8% accuracy), demonstrating a massive reliance on metadata.
- Demonstrates that forced reasoning techniques like chain-of-thought and code-as-reasoning fail to recover accuracy under blind conditions, concluding that observed capabilities are primarily structural heuristics rather than robust statistical inference.

Y. H. Z. Ibrahim, M. K. Salama. "ACTS: A multi-tier benchmark evaluating LLM cipher identification under controlled blind conditions." arXiv, 2026.
arXiv:2609.26893 — https://arxiv.org/abs/2609.26893

## Ajar: Measuring Open Privilege in Agent Defenses

- Proposes Ajar, a framework to empirically measure open privilege—the excess authority left unprotected—in agent defenses by testing whether defenses block unneeded, extraneous tool calls.
- Evaluates five defenses (Progent, CaMeL, AC4A, Permission Assistant, and Claude Code's Auto mode) on the AgentDojo benchmark by intentionally proposing benign tool calls that the task does not actually require, measuring whether the defense permits them.
- Reveals large disparities in open privilege among defenses that exhibit similar levels of benign utility and attack mitigation, demonstrating that current evaluation metrics mask significant variations in excessive privilege granting.

R. K. Sharma, L. Jiang, S. Chen, Z. Lin. "Ajar: Measuring Open Privilege in Agent Defenses." arXiv, 2026.
arXiv:2609.26900 — https://arxiv.org/abs/2609.26900

## Improving Service Availability in KubeEdge-Based Architectures Using Lightweight Intrusion Detection

- Evaluates the resilience of KubeEdge container orchestrations under attack, finding that native failover mechanisms actually amplify system degradation during malicious pod deployments by repeatedly rescheduling the malicious workload across the cluster.
- Proposes RIDRS (Recommended Intrusion Detection Rule Set), a lightweight detection mechanism optimized for resource-constrained edge devices (like Raspberry Pi), offering an alternative to heavier cloud-native solutions like Falco.
- Experimental results show RIDRS reduces outage time to zero for code injection and malicious pod attacks by detecting them in 1.33 and 30.12 seconds respectively, but fails to mitigate large-scale network DoS attacks, demonstrating the limits of node-level detection.

H. N. Kuibou, M. A. Ghorab, M. A. Saied. "Improving Service Availability in KubeEdge-Based Architectures Using Lightweight Intrusion Detection." arXiv, 2026.
arXiv:2609.27052 — https://arxiv.org/abs/2609.27052

## SoK: You Find What You Seek: Rethinking Oracles, Guidance, and Input Generation in Hardware Fuzzing

- Systematizes knowledge on hardware fuzzing through a comprehensive analysis of 52 fuzzers spanning RTL/IP, CPU, NoC, and SoC designs, mapping verification into a bounded search framework defined by objective, oracle, guidance, and input generation.
- Delineates a sharp contrast between constrained-random verification (CRV) augmentation and directed adversarial testing, highlighting that the majority of required user effort goes into adapting target-specific artifacts, simulation infrastructure, and security specifications rather than the fuzzer engines themselves.
- Concludes that industrial adoption of hardware fuzzing is blocked by a lack of reproducible benchmarks and stable interfaces to standard workflows (e.g., UVM), urging a shift toward releasing complete verification and fuzzing collateral to support continuous fuzzing and failure triage.

G. Abarajithan, Z. Ma, C. Tirelli, A. Meza, F. Restuccia, C. Sturton, R. Kastner. "SoK: You Find What You Seek: Rethinking Oracles, Guidance, and Input Generation in Hardware Fuzzing." arXiv, 2026.
arXiv:2609.27300 — https://arxiv.org/abs/2609.27300

## Extracting CNNs in the Unknown-Architecture and Feedback-Agnostic Setting

- Analyzes cryptanalytic extraction of convolutional neural networks (CNNs), proving that the typical assumption of a known architecture is unnecessary for networks employing max and average pooling.
- Demonstrates that the spatial geometry of weight vectors, recovered via existing parameter-recovery attacks, inherently leaks the architectural specifications: sparsity consistency reveals layer type, kernel size, and stride, while numerical consistency exposes padding mode and output channels.
- Combines these geometric insights with parameter-recovery techniques to create a feedback-agnostic extraction framework, successfully demonstrating simultaneous recovery of both network architecture and model parameters in black-box settings.

J. Liu, R. Ma, M. Li, Y. Chen, S. Chen. "Extracting CNNs in the Unknown-Architecture and Feedback-Agnostic Setting." arXiv, 2026.
arXiv:2609.27427 — https://arxiv.org/abs/2609.27427

## Control-Token Injection Suppresses Chain-of-Thought and Defeats Reasoning-Based Oversight in Tool-Using Agents

- Demonstrates that the safety of tool-using agents is jointly dependent on the model and its decoding harness (chat template renderers and tool parsers), and that untrusted input can attack this interface to bypass oversight.
- By appending channel-control tokens to a user message, attackers can trick the tokenizer into rendering a completed reasoning turn, suppressing the model's chain-of-thought (reducing it from a mean of 52.5 tokens to zero across 40 tasks) and forcing immediate tool execution.
- This token injection attack bypassed rule monitors and cross-family LM monitors entirely, successfully converting 39.6% of the model's refusals on malicious requests into completed exfiltrations using the `gpt-oss-20b` reasoning model.

M. Usama, K. U. Nisa, S. Y. Jung. "Control-Token Injection Suppresses Chain-of-Thought and Defeats Reasoning-Based Oversight in Tool-Using Agents." arXiv, 2026.
arXiv:2609.27542 — https://arxiv.org/abs/2609.27542

## Agent Name Collision Attacks in Multi-Agent Systems

- Identifies a recurring implementation vulnerability class in multi-agent hosts where human-readable agent names, rather than origin-bound stable identities, are incorrectly used as local routing identifiers.
- Tracing registration through dispatch across seven pinned open-source revisions revealed that six client-style integrations routed requests addressed to a trusted peer's name to an attacker-controlled endpoint. A brokered implementation collapsed both peers onto one route, resulting in interception or denial-of-service depending on access control states.
- The outcome is primarily wrong-peer dispatch rather than universal privilege inheritance; synthetic tests found no direct transfer of specific credentials or owned tools, although caller-configuration objects and delegated tokens can be forwarded if the attacker consumes the route.

A. A. Kumar. "Agent Name Collision Attacks in Multi-Agent Systems." arXiv, 2026.
arXiv:2609.27624 — https://arxiv.org/abs/2609.27624

## Also published

- L. Hernandez, S. Bratus. "Trouble at the top: can Python extend the chains of trust in infrastructure firmware?" arXiv:2609.27802 — https://arxiv.org/abs/2609.27802
- J. Liu, et al. "GUIAuditor: Enabling Post-hoc Child Safety Forensics via Action-Guided GUI Provenance on Mobile Devices." arXiv:2609.28205 — https://arxiv.org/abs/2609.28205
- L. Brito, et al. "Do Electromagnetic Side-Channel Attacks Threaten Electronic Polling Stations? Scenarios and Recommendations." arXiv:2609.28209 — https://arxiv.org/abs/2609.28209
