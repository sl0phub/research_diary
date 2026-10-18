+++
title = "Conference Brief — 2026-10-18"
date = 2026-10-18T07:00:00Z
type = "conferences"
tags = ["llm-security", "network-security", "hardware", "mitigations", "web-security", "ndss"]
summary = "New papers on MLLM jailbreaks, TCP side-channels, LiDAR spoofing, DoS memory risks, and email aliasing."
+++

## In brief

- Multi-modal LLMs present new attack surface by letting attackers conceal malicious intent through dual steganography across image and text modalities, bypassing text-only filters.
- Off-path attackers can hijack TCP connections over Wi-Fi by observing encrypted frame sizes to deduce ACK and RST responses.
- Memory adaptation in switch-based DoS mitigations creates new resource contention vulnerabilities that can disable the defense.

## Odysseus: Jailbreaking Commercial Multimodal LLM-integrated Systems via Dual Steganography

- Introduces a dual steganography jailbreak paradigm targeting multimodal large language models (MLLMs) by concealing adversarial intent across modalities.
- Exploits the assumption that safety filters require explicitly visible malicious content in input or output to function.
- Demonstrates effectiveness against commercial MLLM-integrated systems, which often use filters tailored for text-only interactions.
- Songze Li, Jiameng Cheng, Yiming Li, Xiaojun Jia, Dacheng Tao. "Odysseus: Jailbreaking Commercial Multimodal LLM-integrated Systems via Dual Steganography." NDSS — https://www.ndss-symposium.org/ndss-paper/odysseus-jailbreaking-commercial-multimodal-llm-integrated-systems-via-dual-steganography/

## Off-Path TCP Hijacking in Wi-Fi Networks: A Packet-Size Side Channel Attack

- Reveals a side channel in Wi-Fi networks where the size of encrypted frames reliably leaks the size of underlying TCP response packets (ACK and RST).
- Allows off-path attackers to detect and hijack a victim's TCP connection, bypassing WEP, WPA2, and WPA3 security.
- Tested against 30 popular wireless routers from 9 vendors; none protected victims from the attack, which successfully hijacked connections in 93.75% of 80 real-world Wi-Fi networks.
- Ziqiang Wang, Xuewei Feng, Qi Li, Kun Sun, Yuxiang Yang, Mengyuan Li, Ganqiu Du, Ke Xu, Jianping Wu. "Off-Path TCP Hijacking in Wi-Fi Networks: A Packet-Size Side Channel Attack." NDSS — https://www.ndss-symposium.org/ndss-paper/off-path-tcp-hijacking-in-wi-fi-networks-a-packet-size-side-channel-attack/

## On the Realism of LiDAR Spoofing Attacks against Autonomous Driving Vehicle at High Speed and Long Distance

- Presents a Moving Vehicle Spoofing (MVS) system to demonstrate LiDAR spoofing at high speeds (60 km/h) and long distances (110 meters).
- Introduces an adaptive high-frequency removal (AHFR) attack that removes points even against recent LiDARs with pulse fingerprinting by leveraging scan timing knowledge.
- Achieves 96% attack success rate against vehicles driving at high speeds in realistic autonomous driving scenarios.
- Takami Sato, Ryo Suzuki, Yuki Hayakawa, Kazuma Ikeda, Ozora Sako, Rokuto Nagata, Ryo Yoshida, Qi Alfred Chen, Kentaro Yoshioka. "On the Realism of LiDAR Spoofing Attacks against Autonomous Driving Vehicle at High Speed and Long Distance." NDSS — https://www.ndss-symposium.org/ndss-paper/on-the-realism-of-lidar-spoofing-attacks-against-autonomous-driving-vehicle-at-high-speed-and-long-distance/

## On the Security Risks of Memory Adaptation and Augmentation in Data-plane DoS Mitigation

- Identifies a vulnerability in line-rate DoS mitigation systems that adaptively augment switch memory using the control plane.
- Presents Heracles, an attack that exploits hardware constraints to orchestrate resource contention across data-plane and control-plane memory via timing side channels.
- Disrupts DoS defenses by triggering synchronized augmentation, memory squeezing, and time-window exploitation using loosely synchronized (1-2 seconds) attack sources.
- Hocheol Nam, Daehyun Lim, Huancheng Zhou, Guofei Gu, Min Suk Kang. "On the Security Risks of Memory Adaptation and Augmentation in Data-plane DoS Mitigation." NDSS — https://www.ndss-symposium.org/ndss-paper/on-the-security-risks-of-memory-adaptation-and-augmentation-in-data-plane-dos-mitigation/

## One Email, Many Faces: A Deep Dive into Identity Confusion in Email Aliases

- Analyzes the identity confusion arising from email aliasing, where providers treat aliases as the same identity but platforms treat them as distinct.
- Finds that 11 of 28 analyzed providers support undocumented alias behaviors, leading to account multiplication abuse (e.g., up to 139 npm accounts from one base email).
- Reports that 31.65% of surveyed users with alias knowledge misidentified phishing emails as legitimate aliases due to inconsistent provider implementations.
- Mengying Wu, Geng Hong, Jiatao Chen, Baojun Liu, Mingxuan Liu, Min Yang. "One Email, Many Faces: A Deep Dive into Identity Confusion in Email Aliases." NDSS — https://www.ndss-symposium.org/ndss-paper/one-email-many-faces-a-deep-dive-into-identity-confusion-in-email-aliases/
