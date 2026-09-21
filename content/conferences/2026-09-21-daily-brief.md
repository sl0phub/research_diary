+++
title = "Conference Brief — 2026-09-21"
date = 2026-09-21T06:00:00Z
type = "conferences"
tags = ["ndss", "mobile", "llm-security", "cloud", "reverse-engineering", "binary-analysis"]
summary = "New findings covering auto-contextualized mobile logic bombs, blurred capability boundaries in LLM applications, side-channel attacks on serverless cloud functions, cross-compilation binary alignment, and function name inference in stripped binaries."
+++

## In brief

- **Mobile and LLM security:** New research highlights the risk of covert logic bombs on Android and previously underexplored capability downgrades/upgrades in customized LLM applications.
- **Serverless infrastructure:** Co-location attacks are shown to be viable in serverless clouds, demonstrating vulnerabilities in scheduling algorithms that allow adversaries to share physical instances with victims.
- **Binary analysis:** Advancements in reverse-engineering techniques use domain-adapted language models to accurately infer function names in stripped binaries and improve binary diffing across different architectures and compilation environments.

## Beyond Conventional Triggers: Auto-Contextualized Covert Triggers for Android Logic Bombs

- SensorBomb is a novel logic bomb framework that exploits legitimate sensor usage, actuator behaviors, and functional contexts to hide trigger conditions in Android apps.
- The framework automatically analyzes a host app to construct covert trigger channels that blend with its natural behaviors, evading state-of-the-art static analysis and fuzzing techniques.
- Experimental evaluation showed high trigger reliability and zero false positives across diverse environments, while large-scale injections proved SensorBomb could be deployed without disrupting normal app functionality.
- Wang, Ye et al. "Beyond Conventional Triggers: Auto-Contextualized Covert Triggers for Android Logic Bombs." NDSS (2026) — https://www.ndss-symposium.org/ndss-paper/beyond-conventional-triggers-auto-contextualized-covert-triggers-for-android-logic-bombs/

## Beyond Jailbreak: Unveiling Risks in LLM Applications Arising from Blurred Capability Boundaries

- The study systematically analyzes the capability boundaries of Large Language Model (LLM) applications, uncovering risks where capabilities are inadvertently downgraded or maliciously upgraded without adversarial rewriting.
- LLMApp-Eval, a newly developed framework, was used to evaluate 199 popular applications across 4 platforms and 6 open-source models, revealing that 89.45% of tested applications are potentially affected.
- Testing showed that 17 applications could execute malicious tasks directly due to poorly designed prompts, demonstrating that prompt quality is highly correlated with application robustness and security.
- Zhang, Yunyi et al. "Beyond Jailbreak: Unveiling Risks in LLM Applications Arising from Blurred Capability Boundaries." NDSS (2026) — https://www.ndss-symposium.org/ndss-paper/beyond-jailbreak-unveiling-risks-in-llm-applications-arising-from-blurred-capability-boundaries/

## Bit of a Close Talker: A Practical Guide to Serverless Cloud Co-Location Attacks

- The research presents a methodology for exploiting serverless cloud schedulers to achieve physical co-location with a victim instance, a prerequisite for micro-architectural side-channel attacks.
- Exploitable features in scheduling algorithms were uncovered and used to successfully achieve instance co-location on prevalent open-source infrastructures and Microsoft Azure Functions.
- To defend against these attacks, a mitigation strategy named the Double-Dip scheduler was proposed to enhance security in serverless computing environments.
- Shao, Wei et al. "Bit of a Close Talker: A Practical Guide to Serverless Cloud Co-Location Attacks." NDSS (2026) — https://www.ndss-symposium.org/ndss-paper/bit-of-a-close-talker-a-practical-guide-to-serverless-cloud-co-location-attacks/

## BINALIGNER: Aligning Binary Code for Cross-Compilation Environment Diffing

- BINALIGNER is a binary diffing approach that addresses limitations in cross-compilation scenarios by using instruction-independent basic block features for subgraph embedding generation.
- The method uses conditional relaxation strategies to identify candidate subgraph pairs, significantly reducing the false and missed match rates between control flow graphs from identical source code snippets.
- In cross-architecture evaluations and mixed compilation environments, BINALIGNER achieved F1-scores averaging 65% higher than baseline state-of-the-art methods.
- Zhu, Yiran et al. "BINALIGNER: Aligning Binary Code for Cross-Compilation Environment Diffing." NDSS (2026) — https://www.ndss-symposium.org/ndss-paper/binaligner-aligning-binary-code-for-cross-compilation-environment-diffing/

## Beyond Classification: Inferring Function Names in Stripped Binaries via Domain Adapted LLMs

- SYMGEN is a framework that employs domain-adapted generative Large Language Models to interpret binary code semantics and infer function names in stripped binaries.
- The system was evaluated on a dataset of over 2.2 million binary functions spanning four architectures and four optimization levels, demonstrating superior generalizability over vocabulary-based classifiers.
- Experimental results showed advancements in precision, recall, and F1 score by up to 409.3%, 553.5%, and 489.4% respectively, proving practical utility against obfuscated binaries and malware.
- Jiang, Linxi et al. "Beyond Classification: Inferring Function Names in Stripped Binaries via Domain Adapted LLMs." NDSS (2026) — https://www.ndss-symposium.org/ndss-paper/beyond-classification-inferring-function-names-in-stripped-binaries-via-domain-adapted-llms/

## Also published

- Wang, Yongpan et al. "BinEnhance: An Enhancement Framework Based on External Environment Semantics for Binary Code Search." NDSS (2026) — https://www.ndss-symposium.org/ndss-paper/binenhance-an-enhancement-framework-based-on-external-environment-semantics-for-binary-code-search/
