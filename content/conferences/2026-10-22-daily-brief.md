+++
title = "Conference Brief — 2026-10-22"
date = 2026-10-22T06:00:00Z
type = "conferences"
tags = ["hardware", "side-channel", "fuzzing", "ndss"]
summary = "Laser-based phantom motion injection attacks, security pitfalls in multi-CPU systems, and side-channel vulnerabilities from write port contention."
+++

## In brief

- Physical and hardware interfaces continue to be a fertile ground for attacks: one paper highlights how laser beams can bypass motion detection systems, while another discovers write port contention side-channel vulnerabilities via hardware fuzzing.
- The integration of multiple CPUs in embedded systems without adapting security boundaries uncovers new attack vectors, allowing code execution across components.

## PhantomMotion: Laser-Based Motion Injection Attacks on Wireless Security Surveillance Systems

- PhantomMotion is an attack framework that aims to fool wireless security surveillance systems by generating fake motion stimuli stealthily by aiming laser beams into the motion detection range.
- The mechanism works stealthily from a distance of up to 120 meters and validates the response by sniffing wireless traffic, without needing physical motion within the monitored area.
- Experimental results against 18 popular wireless motion-activated security systems showed it can always generate fake motion successfully within an average of 12.8 seconds and via moving the laser spot for a mean distance of 1.1 m.

- Yan He, Guanchong Huang, Song Fang. "PhantomMotion: Laser-Based Motion Injection Attacks on Wireless Security Surveillance Systems." NDSS — https://www.ndss-symposium.org/ndss-paper/phantommotion-laser-based-motion-injection-attacks-on-wireless-security-surveillance-systems/

## Pitfalls for Security Isolation in Multi-CPU Systems

- The research systematically identifies security issues resulting from the integration of multiple CPUs into one SoC, finding four major attack vectors related to memory and peripheral access control.
- These issues stem from the re-use of single-CPU security mechanisms such as memory protection units (MPUs), which can lead to arbitrary read and write in protected memory of the other CPU, and even to code execution.
- The study also reveals that the communication mechanism of a popular open source RTOS, FreeRTOS, introduces code execution vulnerabilities in the multi-CPU scenario, which may lead to the compromise of a custom trusted execution environment (TEE).

- Simeon Hoffmann, Nils Ole Tippenhauer. "Pitfalls for Security Isolation in Multi-CPU Systems." NDSS — https://www.ndss-symposium.org/ndss-paper/pitfalls-for-security-isolation-in-multi-cpu-systems/

## PortRush: Detect Write Port Contention Side-Channel Vulnerabilities via Hardware Fuzzing

- PORTRUSH is a novel register-transfer level (RTL) fuzzing framework designed to detect write port contention side-channel vulnerabilities caused by multiple functional modules simultaneously competing for a limited number of shared write ports.
- The framework statically constructs a Write Request Graph (WRG) and implements a Hierarchical Aggregation and Decoding method to efficiently detect contention by monitoring relevant hardware signals.
- Evaluated on three RISC-V CPUs (BOOM, NutShell, and Rocket Core), it uncovered exploitable vulnerabilities leading to two novel attack vectors: Birgus-variant, exploiting contention at the physical register file in the Reorder Buffer, and MSHRush, leveraging contention between the LSU and MSHR at the L1 data cache.

- Peihong Lin, Pengfei Wang, Lei Zhou, Gen Zhang, Xu Zhou, Wei Xie, Zhiyuan Jiang, Kai Lu. "PortRush: Detect Write Port Contention Side-Channel Vulnerabilities via Hardware Fuzzing." NDSS — https://www.ndss-symposium.org/ndss-paper/portrush-detect-write-port-contention-side-channel-vulnerabilities-via-hardware-fuzzing/

## Also published

- Ahod Alghuried, David Mohaisen. "Phishing in Wonderland: Evaluating Learning-Based Ethereum Phishing Transaction Detection and Pitfalls." NDSS — https://www.ndss-symposium.org/ndss-paper/phishing-in-wonderland-evaluating-learning-based-ethereum-phishing-transaction-detection-and-pitfalls/
- Sayak Saha Roy, Shirin Nilizadeh. "PhishLang: A Real-Time, Fully Client-Side Phishing Detection Framework Using MobileBERT." NDSS — https://www.ndss-symposium.org/ndss-paper/phishlang-a-real-time-fully-client-side-phishing-detection-framework-using-mobilebert/
- Jonas Hofmann, Philipp-Florens Lehwalder, Shahriar Ebrahimi, Parisa Hassanizadeh, Sebastian Faust. "PIRANHAS: PrIvacy-Preserving Remote Attestation in Non-Hierarchical Asynchronous Swarms." NDSS — https://www.ndss-symposium.org/ndss-paper/piranhas-privacy-preserving-remote-attestation-in-non-hierarchical-asynchronous-swarms/
- Andrick Adhikari, Sanchari Das, Rinku Dewri. "PolicyPulse: Precision Semantic Role Extraction for Enhanced Privacy Policy Comprehension." NDSS — https://www.ndss-symposium.org/ndss-paper/policypulse-precision-semantic-role-extraction-for-enhanced-privacy-policy-comprehension/
