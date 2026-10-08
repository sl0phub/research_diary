+++
title = "Conference Brief — 2026-10-08"
date = 2026-10-08T06:00:00Z
type = "conferences"
tags = ["malware", "vulnerability-discovery", "hardware", "network-security", "cryptography", "privacy", "fuzzing", "cloud", "llm-security", "ndss"]
summary = "New papers on botnet remediation, satellite honeypots, Payment Channel Networks, censorship circumvention, hypervisor fuzzing, and LLM prompt leakage."
+++

## In brief

- A batch of papers from NDSS 2026 detailing new methods for taking down botnets using their own update mechanisms, a high-interaction satellite honeypot, improved virtual channel protocols for blockchain networks, web protocol tunneling for censorship circumvention, hybrid fuzzing for virtual CPUs, and a prompt leakage vulnerability in multi-tenant LLM serving frameworks.

- Proposes ECHO, an automated malware forensics pipeline that extracts payload deployment routines to generate remediation payloads, disabling or removing frontend bots from infected devices.
- Reuses the malware's built-in update mechanism to distribute crafted payloads, turning the botnet's infrastructure against itself.
- Bypasses the need for traditional botnet cleanup which often leaves infected machines intact, preventing operators from pushing updates to re-establish control.

- Runze Zhang, Mingxuan Yao, Haichuan Xu, Omar Alrawi, Jeman Park, Brendan Saltaformaggio. "Hitchhiking Vaccine: Enhancing Botnet Remediation With Remote Code Deployment Reuse." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/hitchhiking-vaccine-enhancing-botnet-remediation-with-remote-code-deployment-reuse/

- Presents HoneySat, a high-interaction satellite honeypot framework capable of convincingly simulating a real-world CubeSat, a type of Small Satellite (SmallSat).
- Addresses the challenge of collecting data on satellite adversarial techniques by providing a realistic target for attackers.
- Overcomes the historical reliance on security by obscurity for satellite systems, moving towards proactive threat intelligence generation.

- Efrén López-Morales, Ulysse Planta, Gabriele Marra, Carlos González, Jacob Hopkins, Majid Garoosi, Elías Obreque, Carlos Rubio-Medrano, Ali Abbasi. "HoneySat: A Network-based Satellite Honeypot Framework." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/honeysat-a-network-based-satellite-honeypot-framework/

- Introduces Horcrux, a universal and efficient multi-party virtual channel protocol for Payment Channel Networks (PCNs) that does not rely on extra trust assumptions or scripting languages.
- Prevents channel depletion caused by extensive reuse of multi-hop routes, which can make channels unidirectional or force them to close.
- Synthesizes and splits payments to enhance sustainability and scalability of off-chain transactions without compromising universality.

- Anqi Tian, Peifang Ni, Yingzi Gao, Jing Xu. "Horcrux: Synthesize, Split, Shift and Stay Alive; Preventing Channel Depletion via Universal and Enhanced Multi-hop Payments." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/horcrux-synthesize-split-shift-and-stay-alive-preventing-channel-depletion-via-universal-and-enhanced-multi-hop-payments/

- Proposes Huma, a web protocol tunneling tool that evades detection by deferring covert data transmissions, allowing the participating website to first respond with unmodified content.
- Mitigates traffic analysis and fingerprinting attacks that easily detect existing tunneling tools due to their abnormal browsing patterns.
- Encapsulates covert data within standard web protocols to blend with legitimate traffic and bypass Internet censorship.

- Sina Kamali, Diogo Barradas. "Huma: Censorship Circumvention via Web Protocol Tunneling with Deferred Traffic Replacement." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/huma-censorship-circumvention-via-web-protocol-tunneling-with-deferred-traffic-replacement/

- Introduces HyperMirage, a hybrid fuzzing framework that directly manipulates state to scrutinize the complex and security-sensitive virtual CPU components of hypervisors.
- Addresses the challenge of exposing a large virtualization interface to guest VMs, which adversaries can exploit to trigger faults or security bugs and break out of the sandbox.
- Enhances the detection of vulnerabilities in hypervisor virtual CPU implementations that run at the highest privilege levels.

- Manuel Andreas, Fabian Specht, Marius Momeu. "HyperMirage: Direct State Manipulation in Hybrid Virtual CPU Fuzzing." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/hypermirage-direct-state-manipulation-in-hybrid-virtual-cpu-fuzzing/

- Discovers a prompt leakage vulnerability in multi-tenant Large Language Model (LLM) serving frameworks, such as SGLang and vLLM, caused by sharing the Key-Value (KV) cache.
- Demonstrates that the mechanism intended for scalable applications and efficient resource management can inadvertently expose prompts across different tenants.
- Highlights the security risks of shared infrastructure in AGI foundational technologies, specifically focusing on the isolation of tenant data.

- Guanlong Wu, Zheng Zhang, Yao Zhang, Weili Wang, Jianyu Niu, Ye Wu. "I Know What You Asked: Prompt Leakage via KV-Cache Sharing in Multi-Tenant LLM Serving." NDSS 2026 — https://www.ndss-symposium.org/ndss-paper/i-know-what-you-asked-prompt-leakage-via-kv-cache-sharing-in-multi-tenant-llm-serving/
