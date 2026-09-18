+++
title = "arXiv Brief — 2026-09-17"
date = 2026-09-17T06:00:00Z
type = "arxiv"
tags = ["cs.CR", "cs.AI", "llm-security"]
summary = "New findings on the attack surface of LLM agents, from cross-channel fragmentation in tool-calling pipelines to adversarial task contamination and supply chain poisoning of self-modifying code."
+++

## In brief

- Multiple papers address the trust boundaries of LLM agents: tool-calling pipelines can be exploited by fragmenting payloads across channels, and task environments themselves can deceive agents with adversarial artifacts.
- The boundary between visual rendering and physical collision meshes in robotics simulators introduces a new poisoning vector that survives visual inspection but fails in deployment.
- Structural containment and explicit architectural boundaries, rather than relying solely on LLM judgment, are increasingly necessary to isolate compromised agents and restrict prompt lifetimes.

## Measuring and Exploiting Implicit Trust in LLM Tool-Calling Pipelines

- Evaluates the Model Context Protocol (MCP), showing that sharing a single context window across tool descriptions, results, and sampling messages allows attackers to bypass single-channel injection defences.
- Develops cross-channel fragmentation attacks that distribute a payload across two or three channels, resulting in up to 100% credential exfiltration compliance on models like GPT-4o and Llama 70B.
- Demonstrates that current prompt-based defences and third-party MCP security tools fail to detect fragmented payloads, highlighting an unexplored attack surface in agent tool invocation.

Ediga, M., Chattopadhyay, S. "Measuring and Exploiting Implicit Trust in LLM Tool-Calling Pipelines." arXiv, 2026.
arXiv:2609.18217 — https://arxiv.org/abs/2609.18217

## PentestChain: A Cost-Aware, MCP-Orchestrated Framework for Automated Penetration Testing with Free-Tier LLMs

- Presents a ten-phase automated penetration testing framework that orchestrates a local 7B model and free-tier APIs via the Model Context Protocol to execute offensive security tasks.
- Treats US-dollar cost as a primary metric, sustaining end-to-end operation with zero measured paid-API cost by keeping the local model off the critical path via a deterministic backbone.
- Analyses the attack surface of an MCP-exposed offensive engine, grounding the threat model in recent 2025 MCP incidents, and introduces a reproducible evaluation protocol aligned with standardized testbeds.

Patel, R.V., et al. "PentestChain: A Cost-Aware, MCP-Orchestrated Framework for Automated Penetration Testing with Free-Tier LLMs." arXiv, 2026.
arXiv:2609.18120 — https://arxiv.org/abs/2609.18120

## "Your Robot Was Trained on a Lie": Collision Mesh Poisoning Attacks on Robotic Manipulation

- Identifies the Visual-Collision Gap in 3D simulator assets, where the coarse collision mesh used for physical interaction can be modified independently of the visual mesh.
- Proposes Collision Mesh Poisoning (CMP), an attack delivered through the 3D asset supply chain that behaves normally in simulation but degrades or creates safety risks during real-world physical deployment.
- Shows that current asset review practices, which cover malware and format compliance but not visual-collision consistency, fail to defend against CMP.

Xu, G., et al. ""Your Robot Was Trained on a Lie": Collision Mesh Poisoning Attacks on Robotic Manipulation." arXiv, 2026.
arXiv:2609.18122 — https://arxiv.org/abs/2609.18122

## AgentLSD: Evaluating AI Security Agents Under Adversarial Task Contamination

- Introduces adversarial task contamination, where non-instructional evidence like fake results and decoy endpoints in the environment influences agent behaviour.
- Uses a Capture the Flag framework to inject trap artifacts into web challenges, finding that even when agents succeed, traps increase the number of reasoning tokens and turns required.
- Demonstrates that clean CTF performance understates an agent's vulnerability to deceptive evidence, as some model-challenge pairs consistently follow decoys or submit incorrect flags.

Golinelli, M., et al. "AgentLSD: Evaluating AI Security Agents Under Adversarial Task Contamination." arXiv, 2026.
arXiv:2609.19140 — https://arxiv.org/abs/2609.19140

## The Illusion of Local Privacy: Confidentiality Boundary Failures in Consumer LLM Serving Systems

- Examines the persistence of prompt data in local LLM serving systems, finding that plaintext representations survive in allocator-managed memory even after sanitization.
- Recovers prompts after inference and shows that consumer wrappers can extend prompt lifetimes through plaintext persistence.
- Uncovers an authorization flaw in llama.cpp that allows cross-tenant conversation state restoration, and a remote timing oracle exposed by shared prompt-prefix caching.

Ibrahim, Y.H.Z., Ikram, M., Salama, M.K. "The Illusion of Local Privacy: Confidentiality Boundary Failures in Consumer LLM Serving Systems." arXiv, 2026.
arXiv:2609.18526 — https://arxiv.org/abs/2609.18526

## Reflections on Trusting Trust, Revisited: Contaminating Self-Modifying AI Coding Agents with Poisoned Benchmarks

- Applies the "Trusting Trust" compiler backdoor concept to self-modifying AI coding agents, where an adversary supplies a poisoned benchmark to the self-evaluation process.
- Demonstrates that poisoned benchmarks induce agents to self-evolve instructions that write vulnerable code (e.g., disabling HTTPS validation) on clean, held-out tasks.
- Shows that this contamination often persists even when the poisoned agent is later evolved against clean benchmarks, highlighting a critical vulnerability in autonomous self-improvement.

Roesner, F., Kohno, T. "Reflections on Trusting Trust, Revisited: Contaminating Self-Modifying AI Coding Agents with Poisoned Benchmarks." arXiv, 2026.
arXiv:2609.17817 — https://arxiv.org/abs/2609.17817

## Autonomy in Check: Governor-Mediated Adaptive Security at the Edge

- Addresses the risk of edge security planners (like LLM-assisted agents) executing semantically wrong actions based on manipulated observations.
- Proposes a split-control architecture where an untrusted planner emits security intents, and a deterministic governor checks each intent against safety, resource, and proportionality invariants.
- Reports that the governor bounds and admits intents at microsecond costs without disrupting regular operations, showing that security relies on a mediation boundary rather than trusting the planner's action.

Ahmad, I., et al. "Autonomy in Check: Governor-Mediated Adaptive Security at the Edge." arXiv, 2026.
arXiv:2609.18338 — https://arxiv.org/abs/2609.18338

## ASLEval: Measuring Privacy Exposure Displacement in LLM Agent Sessions

- Argues that local proxies for evaluating privacy in tool-using agents often miss unauthorized exposure in multi-step sessions.
- Introduces ASLEval, a framework that pre-registers a hidden target set and measures all visible exits, revealing that expected-outlet-only views miss 46.9% of exposure.
- Finds that schema-aligned internal evidence usually precedes visible exposure, and that relying solely on attacker self-reports combines omissions with high false discovery.

Wu, G., et al. "ASLEval: Measuring Privacy Exposure Displacement in LLM Agent Sessions." arXiv, 2026.
arXiv:2609.18864 — https://arxiv.org/abs/2609.18864

## Also published

- Wu, X., et al. "Collective Loss of Control in LLM Agent Systems: An Epidemic Account of Mutation, Contagion, and Recovery." arXiv:2609.18460 — https://arxiv.org/abs/2609.18460
- Safin, T.H., et al. "Trust propagation and structural containment in Multi-agent LLM pipelines." arXiv:2609.17648 — https://arxiv.org/abs/2609.17648
- Ovadia, O., et al. "MiST: Mid-Training LLMs for Cybersecurity." arXiv:2609.18496 — https://arxiv.org/abs/2609.18496
- Duesterwald, L., et al. "Evaluating the Impact of Personalization in Conversational Cybersecurity Assistants." arXiv:2609.17839 — https://arxiv.org/abs/2609.17839
- Qi, M., et al. "Detecting Logic Vulnerabilities Across the Contract and Device Layers of Blockchain-Enabled IoT With Multi-Agent Heterogeneous Graph Attention." arXiv:2609.18344 — https://arxiv.org/abs/2609.18344
- Irshad, H., et al. "The Verifiable Action Card: Trustworthy Human-in-the-Loop Control for Secure Autonomous Agents." arXiv:2609.18411 — https://arxiv.org/abs/2609.18411
- Vadayath, J., et al. "AIJon: Automated Generation of Annotations for Fuzzing." arXiv:2609.18457 — https://arxiv.org/abs/2609.18457
- Bouke, M. "A Global Readiness and Sovereignty Capability Model for Post-Quantum Cryptography Migration." arXiv:2609.18477 — https://arxiv.org/abs/2609.18477
