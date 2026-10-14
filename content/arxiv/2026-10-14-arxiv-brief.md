+++
title = "arXiv Brief — 2026-10-14"
date = "2026-10-14T00:00:00Z"
type = "arxiv"
tags = ["arxiv", "vulnerability-discovery", "llm-security", "browser", "privacy", "malware"]
summary = "Browser agent confused deputy vulnerabilities, LLM retrieval access controls, and new defense benchmarks."
+++

## In brief

## The Agent Clicks Approve: Injected Page Text Makes Browser Agents Authorize Access the Task Never Named

- Browser agents can be steered by a two-sentence note on a page into approving a third party’s access to the user’s account.
- The agent acts as a confused deputy, where the user's session supplies the authority but the page dictates the access request or webhook URL, without any cross-verification at the point of action.
- Without a defense the unauthorized action completed in all 73 attack runs.
- Testing an authority envelope gate successfully rejected the requests, as the service accepted a request only when it matched the task's envelope. With the gate, the agent still sent the request in every one of 70 attack runs, but the service rejected each.
- Md Imran Hossen. "The Agent Clicks Approve: Injected Page Text Makes Browser Agents Authorize Access the Task Never Named." arXiv — https://arxiv.org/abs/2610.15138

## Privacy Conductor: An Architectural Enforcement of Contextual Integrity in LLM-Based Document Retrieval

- Large language models (LLMs) used for document retrieval struggle to reliably enforce access controls based on contextual integrity, as they depend on probabilistic reasoning.
- Privacy Conductor introduces a deterministic gate that enforces policies authored by an authority, restricting the model to receive only documents the requester is authorized to see.
- Across seven configurations of six models, LLMs correctly reproduce access-control lists on as few as 23% of documents. On 214 flows from HIPAA court cases, the most accurate configuration (87.8%) still permits 11 of the 20 disclosures the law prohibits.
- Ryan Thornton, Mir Mehedi A. Pritom, Maanak Gupta, Jessee Roberts. "Privacy Conductor: An Architectural Enforcement of Contextual Integrity in LLM-Based Document Retrieval." arXiv — https://arxiv.org/abs/2610.15804

## Purpose IR: Compiling User Purpose for Privacy-Preserving Agent Workflow State

- LLM-agent workflows often transform observations into reusable states like plans and summaries, creating a mismatch where evidence needed for a task might not be authorized for persistent storage.
- Purpose IR introduces a bounded typed intermediate representation that compiles user purpose into an executable semantic boundary. A Purpose program is an acyclic semantic dataflow graph where evidence leaves specify semantics and declared sinks determine what values cross the reusable-state boundary.
- Evaluated across 1,200 cases in frameworks like LangGraph and CrewAI, Purpose IR achieved 99.6% Privacy, 83.3% Task, and 83.3% Privacy-Compliant Success (PCS).
- Dongsheng Chen, Xiangyu Zhao, Lei Ma, Xin Yao, Xuetao Wei. "Purpose IR: Compiling User Purpose for Privacy-Preserving Agent Workflow State." arXiv — https://arxiv.org/abs/2610.16414

## CWE-bench: Refocusing Agentic Security from Exploitation to Defense

- AI cybersecurity evaluations heavily favor offensive tasks, but fixing vulnerabilities is harder, as defenders must find and patch all flaws without breaking functionality.
- CWE-bench is a private benchmark of 120 held-out repository audit-and-repair tasks spanning 73 CWE types, eight languages, and all OWASP Top 10 2025 categories. Agents receive the repository and a threat model, but must independently locate and patch the weaknesses.
- Evaluated agents reached a peak of 68% pass@1 and 81% pass@4, showing performance varies significantly by vulnerability category rather than programming language.
- Gonzalo Gonzalez-Pumariega, Ajay Jagannath, Adit Jain, Guram Gogia, Soumyadeep Bakshi, Nazneen Rajani. "CWE-bench: Refocusing Agentic Security from Exploitation to Defense." arXiv — https://arxiv.org/abs/2610.17020

## BrowseSafe++: Benchmarking Prompt Injection Detection Across Web Contexts, Languages, and Browser Views

- Browser agents are vulnerable to malicious instructions embedded in untrusted webpages, which can redirect legitimate user tasks.
- BrowseSafe++ expands on the BrowseSafe benchmark by providing 38,675 attack/control page pairs, including 32,187 built from injections observed on production webpages.
- The benchmark is used to train BrowseSafe-Guard, two 0.8B-parameter detectors for text and screenshots, which achieved higher F1 scores than frontier-model detectors while maintaining low false-positive rates on benign pages.
- Yuetian Chen, Kaiyuan Zhang, Yuntao Du, Thomas Li, Mark Tenenholtz, Kyle Polley, Jerry Ma, Denis Yarats, Ninghui Li. "BrowseSafe++: Benchmarking Prompt Injection Detection Across Web Contexts, Languages, and Browser Views." arXiv — https://arxiv.org/abs/2610.17457

## Also published

- Tao Ni, Zehua Sun, Yihe Zhou, Yuefeng Du, Qingchuan Zhao, Cong Wang. "Penetrating the Reality Wall: Long-Range and Through-Wall AR/VR Privacy Eavesdropping via Wireless Power Side Channel." arXiv — https://arxiv.org/abs/2610.15865
- Zian Yuan, Wei Li. "PrivacyGuard: Source-Linked Sanitization and Locally Resolvable PII References for Cloud GUI Agents." arXiv — https://arxiv.org/abs/2610.16778
- Salma Aboelmagd, Md. Rakibul Ahasan, Zhixin Pan, Abdulrahman Takiddin, Ziyu Shu. "Hardware-Assisted Multi-Stage Ransomware Detection with Adaptive Machine Learning." arXiv — https://arxiv.org/abs/2610.15951
- Hongzhen Xiang, Chenxu Wang, Yumeng Song, Tao Qin, Yushuai Li, Pinghui Wang, Wei Wang. "Risk-aware Road-network Trajectory Synthesis under Local Differential Privacy." arXiv — https://arxiv.org/abs/2610.16384
- Xiuyuan Qi, Yi Wang, Wenjie Wang. "Differential Privacy Protected Preference Alignment on Survey Derived Data." arXiv — https://arxiv.org/abs/2610.16458
- Assunta Imperatrice, Luigi ROmano. "Toward Realistic Privacy Risk in FL-Enabled OT Intrusion Detection Systems." arXiv — https://arxiv.org/abs/2610.16872
