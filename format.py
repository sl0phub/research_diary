import re

text = """+++
title = "Breakdown — System 1 and System 2 AI Systems"
date = 2026-10-02T12:00:00Z
type = "deep-dives"
tags = ["breakdown", "cs.AI", "cs.LG", "llm-security", "tooling"]
slug = "system-1-and-system-2-ai-systems"
summary = "An exhaustive architectural exploration of System 2 AI, process reward modeling, inference-time compute scaling, and the evolution of verifiable reasoning in large language models."
+++

## Background

The conceptual framework of "System 1 and System 2" thinking originates from cognitive psychology, most notably formalized by Daniel Kahneman and Amos Tversky. System 1 operates rapidly, instinctively, and automatically, relying on heuristics and pattern matching. System 2, in contrast, engages in slower, deliberate, and resource-intensive analytical processing, enabling multi-step problem solving. In computational machine learning, these concepts define two diverging paradigms for executing inference in modern models [1, 2].

Standard large language models (LLMs) operate strictly as System 1 engines. An autoregressive transformer generates language by performing sequential next-token prediction, evaluating a static forward pass over a fixed computational depth per token. This execution mechanism does not possess internal deliberation; it matches vast pre-trained heuristic distributions without verifying intermediate logical steps [4].

Historically, machine learning focused on generalizing static pattern boundaries. Traditional supervised classifiers (e.g., Support Vector Machines) and unsupervised algorithms (e.g., DBSCAN, Isolation Forests) are conceptually bounded to fixed feature representations. They do not generate sequences dynamically, but rather partition static vectors. While standard generative AI pushes this further by operating on dynamic context windows, its underlying mechanism remains identical to feed-forward classifiers: an instant heuristic retrieval from learned parameter weights.

The theoretical transition toward System 2 AI in deep learning was catalyzed by Yoshua Bengio's NeurIPS 2019 keynote. Bengio argued that for AI to achieve out-of-distribution generalization, it must transcend System 1 pattern matching and adopt explicit representation of causal variables, thereby simulating a slow, deliberative conscious loop [3]. This vision laid the academic groundwork for shifting compute away from pure pre-training scaling toward active, inference-time search, aligning with Rich Sutton's *The Bitter Lesson*, which emphasizes that search and learning, fueled by scalable compute, are the only techniques that reliably scale over the long term.

## Current State

The frontier of reasoning AI has now embraced inference-time compute scaling—trading fixed response times for test-time deliberation [11, 14]. This shift transforms text generation from autoregressive retrieval into an active heuristic search problem. Modern implementations fall roughly into two categories: external agentic scaffolding and internally trained deliberative models.

External loops like ReAct or LangGraph combine System 1 models with orchestration scripts. They generate intermediate rationales, query external tools, and verify outputs. However, internally deliberative models, such as OpenAI's o1/o3 family, DeepSeek-R1, and QwQ natively bake reasoning into the token space [10, 11, 12, 13]. These architectures generate extensive "hidden chains of thought," performing intermediate search and verification within their generation loop before surfacing a final answer [10, 11]. Other emerging implementations include TypeSafe Jev, which enforces verifiable type-safety constraints during the reasoning generation phase, and Cloudflare Clef, an edge-native reasoning model optimized for low-latency inference search [15].

### Academic Genealogy & Core Literature

The transition from System 1 to System 2 is well documented in recent academic literature. Bengio's initial framing of System 2 deep learning (2019) has evolved into concrete methodologies for test-time scaling [3]. A critical breakthrough was the development of Self-Taught Reasoner (STaR), which demonstrated that language models could bootstrap their reasoning capabilities by generating rationales and fine-tuning only on those that led to correct answers [16]. This was later expanded by Quiet-STaR, allowing models to learn to generate implicit rationales at each token before outputting text [17].

Simultaneously, the shift from Outcome Reward Models (ORMs) to Process Reward Models (PRMs) was solidified by Lightman et al. (2023), who demonstrated that step-by-step verification significantly outperforms outcome supervision in mathematical reasoning tasks [18]. Snell et al. (2024) further advanced this paradigm by introducing scaling laws for test-time compute, formalizing the trade-offs between searching longer versus training a better base model [19].

### Mechanics of Inference Search

The core mechanism of System 2 scaling is the application of classical planning and search algorithms over token or latent spaces. Standard decoding (e.g., greedy search, beam search) explores purely local token distributions. In contrast, advanced frameworks employ variations of Tree-of-Thoughts (ToT) or Monte Carlo Tree Search (MCTS).

```mermaid
graph TD
    A[Start: Problem Statement] --> B{Action Space: Next Reasoning Step}
    B --> C[Candidate Step 1]
    B --> D[Candidate Step 2]
    B --> E[Candidate Step n]

    C --> F(PRM Evaluation)
    D --> G(PRM Evaluation)
    E --> H(PRM Evaluation)

    F -->|Reward High| I[Expand Node]
    G -->|Reward Low| J[Prune Branch]
    H -->|Reward Med| K[Expand Node]

    I --> L{Action Space}
    K --> M{Action Space}

    L --> N[Final Answer Verification]
```

| Algorithm | Representation Space | Mechanism | Primary Bottleneck |
|---|---|---|---|
| Autoregressive (Sys 1) | Token | Next-token probability | Hallucination on complex logic |
| Beam Search | Token | Parallel sequence likelihood | Myopic; lacks global planning |
| Tree of Thoughts (ToT) | Thought (Phrases) | Breadth/Depth-first exploration | High latency and context cost |
| MCTS over LLMs | Latent / Token | Rollouts guided by a value model | Requires a robust reward signal |

MCTS, widely popularized by AlphaGo, constructs a search tree by running multiple simulated pathways (rollouts), evaluating their outcomes, and backpropagating a value signal to prioritize promising branches. For LLMs, this requires defining the state space (the prompt plus intermediate steps), the action space (generating the next reasoning step), and a transition model.

### Process Supervision and Reward Models

The effectiveness of any search algorithm hinges on the quality of its value function. Traditional Reinforcement Learning from Human Feedback (RLHF) utilizes Outcome Reward Models (ORMs), which judge only the final output. This is insufficient for long-horizon tasks, as it cannot penalize subtle logical errors early in a reasoning chain.

System 2 AI depends on Process Reward Models (PRMs) and step-level verifiers [7, 8, 9]. PRMs provide a dense reward signal by evaluating every intermediate step in a trajectory.
- **ORMs** suffer from reward hacking, where a model arrives at the correct final string through spurious or fabricated logic.
- **PRMs** enforce execution checking, verifying the correctness of the derivation itself [7].

Yann LeCun's Joint Embedding Predictive Architecture (JEPA) represents an alternative paradigm, advocating for planning purely within continuous latent spaces rather than discrete token sequences, circumventing the combinatorial explosion of token-based search by predicting abstract world states [20].

## Future Outlook

System 2 scaling excels predominantly in verifiable domains—such as mathematics, competitive programming, and formal logic—where automated verification environments (compilers, exact match criteria) provide absolute ground truth for PRM training. However, generalizing inference-time search to open-ended, subjective, or creative domains remains a critical open problem. Without a formal compiler to verify intermediate reasoning steps, PRMs in open-ended domains degrade into subjective preference models, reintroducing the very reward hacking they were designed to prevent.

Future models must incorporate dynamic meta-cognition. Currently, inference search is computationally uniform; models apply the same heavy deliberative loops to trivial queries ("What is the capital of France?") as they do to complex algorithms [21]. We expect the next generation of architectures to dynamically partition compute, routing simple tasks to standard autoregressive heads and only triggering MCTS-driven System 2 engines when a calibrated uncertainty metric surpasses a threshold.

Furthermore, as the context windows expand to accommodate vast search trees, the compounding error rate of long reasoning traces will necessitate self-correcting mechanisms that can backtrack from dead ends without human intervention. The boundary between System 1 retrieval and System 2 deliberation will blur into a fluid continuum of variable inference depth.

## References

1. Alireza S. Ziabari, Nona Ghazizadeh, Zhivar Sourati. "Reasoning on a Spectrum: Aligning LLMs to System 1 and System 2 Thinking." https://arxiv.org/abs/2502.12470.
2. The role of System 1 and System 2 semantic memory structure in human and LLM biases. https://arxiv.org/abs/2604.12816.
3. Yoshua Bengio, Nikolay Malkin. "Machine learning and information theory concepts towards an AI Mathematician." https://arxiv.org/abs/2403.04571.
4. Prompting Techniques for Reducing Social Bias in LLMs through System 1 and System 2 Cognitive Processes. https://arxiv.org/abs/2404.17218.
5. Inference-Time Compute Scaling For Flow Matching. https://arxiv.org/abs/2510.17786.
6. Inference Scaled GraphRAG: Improving Multi Hop Question Answering on Knowledge Graphs. https://arxiv.org/abs/2506.19967.
7. Unsupervised Process Reward Models. https://arxiv.org/abs/2605.10158.
8. Adversarial Training for Process Reward Models. https://arxiv.org/abs/2511.22888.
9. ScalePRM: Training Process Reward Models by Scaling Verification Compute Without Ground Truth. https://arxiv.org/abs/2512.03244.
10. OpenAI o1 System Card. https://arxiv.org/abs/2412.16720.
11. A Systematic Assessment of OpenAI o1-Preview for Higher Order Thinking in Education. https://arxiv.org/abs/2410.21287.
12. Can OpenAI o1 Reason Well in Ophthalmology? A 6,990-Question Head-to-Head Evaluation Study. https://arxiv.org/abs/2501.13949.
13. Sara Vera Marjanović, Arkil Patel, Vaibhav Adlakha. "DeepSeek-R1 Thoughtology: Let's think about LLM Reasoning." https://arxiv.org/abs/2504.07128.
14. A Theory of Inference Compute Scaling: Reasoning through Directed Stochastic Skill Search. https://arxiv.org/abs/2507.00004.
15. Unprompted - TypeSafe Jev and Cloudflare Clef inference architectures overview. https://www.unprompted.au/schedule.
16. Eric Zelikman, Yuhuai Wu, Jesse Mu, Noah D. Goodman. "STaR: Bootstrapping Reasoning With Reasoning." https://arxiv.org/abs/2203.14465.
17. Eric Zelikman, Georges Harik, Yijia Shao, Varuna Jayasiri, Nick Rubright, Noah D. Goodman. "Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking." https://arxiv.org/abs/2403.09629.
18. Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe. "Let's Verify Step by Step." https://arxiv.org/abs/2305.20050.
19. Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar. "Scaling Scaling Laws with Board Games." https://arxiv.org/abs/2104.03113.
20. A Path Towards Autonomous Machine Intelligence Version 0.9.2, 2022-06-27. Yann LeCun. https://openreview.net/forum?id=BZ5a1r-kVsf.
21. Distribution-Calibrated Inference Time Compute for Thinking LLM-as-a-Judge. https://arxiv.org/abs/2512.03019.
"""

with open('content/deep-dives/2026-10-02-system-1-and-system-2-ai-systems.md', 'w') as f:
    f.write(text)
