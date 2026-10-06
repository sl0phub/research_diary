+++
title = "Conference Brief — 2026-10-06"
date = 2026-10-06T00:00:00Z
type = "conferences"
tags = ["vulnerability-discovery", "llm-security", "supply-chain", "reverse-engineering", "web-security", "privacy", "fuzzing", "hardware", "firmware", "exploitation", "ndss"]
summary = "A batch of papers from NDSS."
+++

## In brief

- Evaluates LLMs (LLaMA-2, GPT-4, etc.) on vulnerability detection in Java and C/C++, testing zero-shot and few-shot capabilities.
- Finds Gemma and LLaMA-2 perform strongly in identifying specific vulnerability types.
- Jie Lin, David Mohaisen. "From Large to Mammoth: A Comparative Evaluation of Large Language Models in Vulnerability Detection." NDSS — https://ndss-symposium.org/ndss-paper/from-large-to-mammoth-a-comparative-evaluation-of-large-language-models-in-vulnerability-detection

- Proposes VulTracer, a framework for function-level vulnerability propagation analysis in the npm ecosystem.
- Builds semantic graphs for packages and stitches them together to trace precise propagation paths.
- Yingyuan Pu, Lingyun Ying, Yacong Gu. "From Noise to Signal: Precisely Identify Affected Packages of Known Vulnerabilities in npm Ecosystem." NDSS — https://ndss-symposium.org/ndss-paper/from-noise-to-signal-precisely-identify-affected-packages-of-known-vulnerabilities-in-npm-ecosystem

- Presents JSIMPLIFIER, a multi-stage deobfuscation tool using AST static analysis, dynamic execution tracing, and LLM-enhanced identifier renaming.
- Introduces a dataset of 44,421 real-world obfuscated JavaScript samples.
- Dongchao Zhou, Lingyun Ying, Huajun Chai, Dongbin Wang. "From Obfuscated to Obvious: A Comprehensive JavaScript Deobfuscation Tool for Security Analysis." NDSS — https://ndss-symposium.org/ndss-paper/from-obfuscated-to-obvious-a-comprehensive-javascript-deobfuscation-tool-for-security-analysis

- Studies how XR developers perceive and respond to security and privacy threats.
- Highlights the unprecedented data collection and user interactions that create novel challenges in immersive environments.
- Kunlin Cai, Jinghuai Zhang, Ying Li, Zhiyuan Wang, Xun Chen, Tianshi Li, Yuan Tian. "From Perception to Protection: A Developer-Centered Study of Security and Privacy Threats in Extended Reality (XR)." NDSS — https://ndss-symposium.org/ndss-paper/from-perception-to-protection-a-developer-centered-study-of-security-and-privacy-threats-in-extended-reality-xr

- Introduces Fuzzilicon, a post-silicon microcode-guided fuzzing framework for x86 CPUs.
- Extracts feedback directly from the processor's microarchitecture by reverse-engineering Intel's proprietary microcode.
- Johannes Lenzen, Lichao Wu, Mohamadreza Rostami, Ahmad-Reza Sadeghi. "Fuzzilicon: A Post-Silicon Microcode-Guided x86 CPU Fuzzer." NDSS — https://ndss-symposium.org/ndss-paper/fuzzilicon-a-post-silicon-microcode-guided-x86-cpu-fuzzer

- Presents FUZZUER, a feedback-guided fuzzer for UEFI interfaces on EDK-2.
- Uses FIRNESS to statically analyze and automatically generate fuzzing harnesses for interface functions.
- Connor Glosner, Aravind Machiry. "FUZZUER: Enabling Fuzzing of UEFI Interfaces on EDK-2." NDSS — https://ndss-symposium.org/ndss-paper/fuzzuer-enabling-fuzzing-of-uefi-interfaces-on-edk-2

- Proposes GadgetMeter to quantitatively evaluate the exploitability of speculative execution gadgets.
- Aims to help prioritize and guide mitigations, addressing the performance overhead of full prevention.
- Qi Ling, Yujun Liang, Yi Ren, Baris Kasikci, Shuwen Deng. "GadgetMeter: Quantitatively and Accurately Gauging the Exploitability of Speculative Gadgets." NDSS — https://ndss-symposium.org/ndss-paper/gadgetmeter-quantitatively-and-accurately-gauging-the-exploitability-of-speculative-gadgets

- Introduces GAP-Diff to protect JPEG-compressed images from unauthorized fine-tuning by text-to-image diffusion models.
- Adds protective noise to disrupt facial customization while remaining robust against simple pre-processing techniques.
- Haotian Zhu, Shuchao Pang, Zhigang Lu, Yongbin Zhou, Minhui Xue. "GAP-Diff: Protecting JPEG-Compressed Images from Diffusion-based Facial Customization." NDSS — https://ndss-symposium.org/ndss-paper/gap-diff-protecting-jpeg-compressed-images-from-diffusion-based-facial-customization
