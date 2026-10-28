+++
title = "Conference Brief — 2026-09-15"
date = 2026-09-15T06:00:00Z
type = "conferences"
tags = ["side-channel", "exploitation", "ndss"]
summary = "Extracting DNN architectures through walls using GPU EM emissions, and bypassing CPU defenses via GPU memory mapping vulnerabilities."
+++

## In brief

- Both items highlight the security implications of hardware components that act as black boxes or bypass standard CPU protections.
- ModelSpy demonstrates that GPU electromagnetic emissions during inference leak enough architecture-specific information to reconstruct complete deep neural networks from several meters away.
- PhantomMap shows that vulnerabilities in the GPU's memory mapping can be weaponized to achieve arbitrary physical memory read/write access, bypassing mature CPU-side kernel defenses.

## Peering Inside the Black-Box: Long-Range and Scalable Model Architecture Snooping via GPU Electromagnetic Side-Channel

- Proposes ModelSpy, a stealthy DNN architecture snooping attack based on GPU electromagnetic (EM) leakage.
- Capable of extracting complete architecture from several meters away, even through walls, by observing that GPUs emanate far-field EM signals exhibiting architecture-specific amplitude modulation during DNN inference.
- Achieves 97.6% accuracy in layer segmentation and 94.0% in hyperparameter estimation, with a working distance of up to 6 meters on five high-end consumer GPUs.

- Rui Xiao, Sibo Feng, Soundarya Ramesh, Jun Han, and Jinsong Han. "Peering Inside the Black-Box: Long-Range and Scalable Model Architecture Snooping via GPU Electromagnetic Side-Channel." NDSS — https://www.ndss-symposium.org/ndss-paper/peering-inside-the-black-box-long-range-and-scalable-model-architecture-snooping-via-gpu-electromagnetic-side-channel/

## PhantomMap: GPU-Assisted Kernel Exploitation

- Conducts the first in-depth security analysis of the Mali GPU's memory mapping mechanism, uncovering allocation-mapping decoupling and missing physical address validation.
- Introduces PhantomMap, a GPU-assisted exploitation technique that transforms limited heap vulnerabilities into powerful physical memory read/write primitives to bypass mainstream kernel defenses.
- Develops 15 end-to-end exploits based on real-world CVEs across two Mali driver architectures, including the first public exploit for CVE-2025-21836.

- Jiayi Hu, Qi Tang, Xingkai Wang, Jinmeng Zhou, Rui Chang, and Wenbo Shen. "PhantomMap: GPU-Assisted Kernel Exploitation." NDSS — https://www.ndss-symposium.org/ndss-paper/phantommap-gpu-assisted-kernel-exploitation/
