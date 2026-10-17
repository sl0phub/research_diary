+++
title = "Conference Brief — 2026-10-17"
date = 2026-10-17T06:00:00Z
type = "conferences"
tags = ["ndss", "llm-security", "exploitation", "side-channel", "vulnerability-discovery"]
summary = "New attacks against aligned LLMs, automatic exploit generation for Node.js, mapping CVEs to MITRE ATT&CK, and cross-privilege BTB side channels."
+++

## In brief

* **LLM safety mechanisms bypassed:** Attackers can identify and prune a small number of "safety neurons" in aligned language models to disable their protections, achieving high success rates even with vanilla malicious prompts.
* **Instruction-level side channels:** New cross-privilege Branch Target Buffer (BTB) attacks allow user-mode attackers to leak kernel control-flow information at high resolution without requiring shared entries.
* **Automated Node.js exploitation:** A new tool successfully synthesizes working exploits for arbitrary code execution and command injection vulnerabilities in hundreds of npm packages.

## NeuroStrike: Neuron-Level Attacks on Aligned LLMs

* Introduces an attack framework that targets the specialized "safety neurons" responsible for detecting and suppressing harmful inputs in aligned large language models.
* In white-box scenarios, the attack identifies these neurons via feedforward activation analysis and prunes them during inference to disable safety mechanisms.
* For black-box targets, adversarial prompt generators are trained on open-weight surrogate models and deployed against proprietary models, demonstrating the transferability of safety neurons.
* Removing less than 0.6% of neurons in targeted layers achieves an average attack success rate of 76.9% across over 20 open-weight models from major developers.
- Lichao Wu, Sasha Behrouzi, Mohamadreza Rostami, Maximilian Thang, Stjepan Picek, Ahmad-Reza Sadeghi. "NeuroStrike: Neuron-Level Attacks on Aligned LLMs." NDSS — https://www.ndss-symposium.org/ndss-paper/neurostrike-neuron-level-attacks-on-aligned-llms/

## NEXUS: Towards Accurate and Scalable Mapping between Vulnerabilities and Attack Techniques

* Addresses the gap between unstructured CVE descriptions and the MITRE ATT&CK framework by automatically mapping vulnerabilities to specific Tactics, Techniques, and Procedures (TTPs).
* Evaluated on a newly constructed dataset encompassing 208 TTPs and over 92,000 CVEs, overcoming the lack of large-scale, high-quality datasets linking the two.
* Achieves a maximum F1-score of 97.94% in CVE-to-TTP mapping, significantly outperforming existing methods which reached a maximum of 67.68%.
- Ehsan Khodayarseresht, Suryadipta Majumdar, Serguei Mokhov, Mourad Debbabi. "NEXUS: Towards Accurate and Scalable Mapping between Vulnerabilities and Attack Techniques." NDSS — https://www.ndss-symposium.org/ndss-paper/nexus-towards-accurate-and-scalable-mapping-between-vulnerabilities-and-attack-techniques/

## NodeMedic-FINE: Automatic Detection and Exploit Synthesis for Node.js Vulnerabilities

* Employs a type and object-structure aware fuzzer to explore execution paths during dynamic taint analysis, improving the detection of vulnerabilities in Node.js packages.
* Leverages taint analysis data to infer input types and structures, guiding an exploit synthesis engine to automatically generate proof-of-concept payloads for arbitrary code execution and command injection.
* Evaluated against 33,011 npm packages, identifying 2,257 potential flows and successfully synthesizing working exploits for 766 packages.
- Darion Cassel, Nuno Sabino, Min-Chien Hsu, Ruben Martins, Limin Jia. "NodeMedic-FINE: Automatic Detection and Exploit Synthesis for Node.js Vulnerabilities." NDSS — https://www.ndss-symposium.org/ndss-paper/nodemedic-fine-automatic-detection-and-exploit-synthesis-for-node-js-vulnerabilities/

## Non-intrusive and Unconstrained Keystroke Inference in VR Platforms via Infrared Side Channel

* Discloses a side-channel vulnerability in the constellation tracking systems of mainstream Virtual Reality platforms, exploiting infrared signals emitted by VR controllers.
* Introduces VRecKey, an attack that intercepts ambient IR signals using a customized 2D IR sensor array to non-intrusively infer unconstrained keystrokes on virtual keyboards.
* Capable of inferring both character-level key presses and word-level keystrokes along with their typing trajectories.
* Achieves over 94.2% top-3 accuracy for character-level inference and 90.5% top-3 accuracy for word-level inference across different keystroke lengths on two commercial VR devices.
- Tao Ni, Yuefeng Du, Qingchuan Zhao, Cong Wang. "Non-intrusive and Unconstrained Keystroke Inference in VR Platforms via Infrared Side Channel." NDSS — https://www.ndss-symposium.org/ndss-paper/non-intrusive-and-unconstrained-keystroke-inference-in-vr-platforms-via-infrared-side-channel/

## ObliInjection: Order-Oblivious Prompt Injection Attack to LLM Agents with Multi-source Data

* Targets LLM applications and agents that process input data from multiple sources, where the attacker controls only a subset of the sources and does not know their final ordering.
* Introduces an "order-oblivious loss" metric to quantify the likelihood of an LLM completing a malicious task regardless of the arrangement of clean and contaminated segments.
* Utilizes a tailored algorithm, orderGCG, to minimize this loss and optimize the contaminated segments for successful prompt injection.
* Experiments across 12 LLMs show the attack remains highly effective even when only one out of 6 to 100 segments is contaminated.
- Reachal Wang, Yuqi Jia, Neil Zhenqiang Gong. "ObliInjection: Order-Oblivious Prompt Injection Attack to LLM Agents with Multi-source Data." NDSS — https://www.ndss-symposium.org/ndss-paper/obliinjection-order-oblivious-prompt-injection-attack-to-llm-agents-with-multi-source-data/

## OCCUPY+PROBE: Cross-Privilege Branch Target Buffer Side-Channel Attacks at Instruction Granularity

* Presents an eviction-based Branch Target Buffer (BTB) side-channel attack that allows user-mode processes to leak kernel control-flow behaviors without requiring shared entries.
* Exploits an offset-related BTB update mechanism on Intel processors, revealing that kernel-mode entries can directly replace user-mode entries regardless of replacement policies or hardware isolation.
* Achieves instruction-level granularity in branch monitoring, providing higher spatial resolution than existing eviction-based BTB attacks.
* Successfully demonstrates the leakage of control-flow information across privilege boundaries.
- Kaiyuan Rong, Junqi Fang, Haixia Wang, Dapeng Ju, Dongsheng Wang. "OCCUPY+PROBE: Cross-Privilege Branch Target Buffer Side-Channel Attacks at Instruction Granularity." NDSS — https://www.ndss-symposium.org/ndss-paper/occupyprobe-cross-privilege-branch-target-buffer-side-channel-attacks-at-instruction-granularity/
