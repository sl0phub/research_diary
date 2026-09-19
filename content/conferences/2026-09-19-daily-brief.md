+++
title = "Conference Brief — 2026-09-19"
date = 2026-09-19T06:00:00Z
type = "conferences"
tags = ["web-security", "protocol-analysis", "supply-chain", "malware", "mobile", "llm-security", "tooling", "ndss"]
summary = "Misconfigured email auto-configuration globally, manipulating GitHub contribution histories to infiltrate supply chains, and adversarial Android malware factories."
+++

## In brief

- Defective and misconfigured email auto-configuration mechanisms allow for credential theft and attacker-controlled server connections in the wild.
- Attackers can trivially spoof Git commit authorship to build deceptive GitHub profiles and build trust before launching supply-chain attacks.
- Adversarial perturbations can be tailored to malicious code segments and injected into various Android carriers to generate evasion-resistant piggybacked malware at scale.

## Automatic Insecurity: Exploring Email Auto-configuration in the Wild

- Email auto-configuration mechanisms, meant to simplify setup, introduce critical security risks in client implementations and server deployments.
- An analysis of 29 clients and over a million domains found 17 defects—8 previously unknown—and misconfigurations in 49,013 domains (including 19 of the top 1K), putting credentials at risk via insecure connections or attacker-controlled servers.
- The vulnerabilities allow attackers to intercept connections silently, aided by inadequate UI notifications in 27 out of the 29 tested clients.

Wen, S., Zhang, Y., Shen, Y., Li, B., Duan, H., Lin, J. "Automatic Insecurity: Exploring Email Auto-configuration in the Wild." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/automatic-insecurity-exploring-email-auto-configuration-in-the-wild/

## Attributing Open-Source Contributions is Critical but Difficult: A Systematic Analysis of GitHub Practices and Their Impact on Software Supply Chain Security

- Git's design allows arbitrary configuration of author details, which GitHub uses to link commits to user profiles, creating a gap between actual and claimed contributions.
- A large-scale analysis of 50,328 critical open-source projects revealed that 85.9% are susceptible to contribution hijacking, exposing over 573,043 unclaimed email addresses that attackers can use to spoof historic trust.
- Despite the severity, defensive adoption remains low: 95.4% of users have never signed a commit, and online security advice overwhelmingly focuses on credential protection rather than preventing contributor spoofing.

Holtgrave, J.-U., Friedrich, K., Fischer, F., Huaman, N., Busch, N., Klemmer, J. H., Fourné, M., Wiese, O., Wermke, D., Fahl, S. "Attributing Open-Source Contributions is Critical but Difficult: A Systematic Analysis of GitHub Practices and Their Impact on Software Supply Chain Security." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/attributing-open-source-contributions-is-critical-but-difficult-a-systematic-analysis-of-github-practices-and-their-impact-on-software-supply-chain-security/

## Automated Mass Malware Factory: The Convergence of Piggybacking and Adversarial Example in Android Malicious Software Generation

- Combining piggybacking with adversarial examples allows attackers to generate thousands of evasive Android malware variants by inserting a tailored, adversarial malicious code segment into benign carrier apps.
- The perturbation is generated specifically for the malicious rider, preventing misuse and minimizing the attack footprint across different carriers.
- Against machine learning models like DREBIN and MaMaDroid, the generated malware achieves an average attack success rate of 88.3%, and significantly bypasses commercial antivirus engines.

Li, H., Yao, Z., Wu, B., Gao, C., Xu, T., Yuan, W., Luo, X. "Automated Mass Malware Factory: The Convergence of Piggybacking and Adversarial Example in Android Malicious Software Generation." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/automated-mass-malware-factory-the-convergence-of-piggybacking-and-adversarial-example-in-android-malicious-software-generation/

## Automated Code Annotation with LLMs for Establishing TEE Boundaries

- Identifying precise regions of security-sensitive code, particularly cryptography, for isolation within Trusted Execution Environments (TEEs) traditionally requires deep manual inspection.
- The LLM-CAL tool fine-tunes models using quantized LoRA on a dataset of 4,000 C source files, encoding local context, global semantic data, and structural metadata to automate code annotation.
- Evaluation on models like Gemma-2B and Llama-7B demonstrates that the tool can identify cryptographic code lines with a 98.40% F1 score, reducing the manual effort needed to minimize the Trusted Computing Base (TCB).

Gadey, V., Götz, M., Sendner, C., Sovio, S., Dmitrienko, A. "Automated Code Annotation with LLMs for Establishing TEE Boundaries." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/automated-code-annotation-with-llms-for-establishing-tee-boundaries/

## Also published

- Zhong, Y. et al. "Attention is All You Need to Defend Against Indirect Prompt Injection Attacks in LLMs." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/attention-is-all-you-need-to-defend-against-indirect-prompt-injection-attacks-in-llms/
- Murakami, T. et al. "Augmented Shuffle Differential Privacy Protocols for Large-Domain Categorical and Key-Value Data." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/augmented-shuffle-differential-privacy-protocols-for-large-domain-categorical-and-key-value-data/
