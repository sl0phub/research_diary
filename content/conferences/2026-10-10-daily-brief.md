+++
title = "Conference Brief — 2026-10-10"
date = 2026-10-10T07:33:29Z
type = "conferences"
tags = ["ndss", "malware", "vulnerability-discovery", "kernel", "llm-security", "network-security", "privacy", "protocol-analysis"]
summary = "New papers from NDSS on multimodal model security, IoT vulnerability detection, RTOS double-fetch bugs, malicious domain detection, and LLM agent isolation."
+++

## In brief

## InverTune: A Backdoor Defense Method for Multimodal Contrastive Learning via Backdoor-Adversarial Correlation Analysis

- Multimodal contrastive learning models like CLIP have demonstrated remarkable vision-language alignment capabilities and now serve as foundational components in many largescale multimodal systems.
- Experimental results show that InverTune reduces the average attack success rate (ASR) by 97.87% against the state-of-the-art (SOTA) attacks while limiting clean accuracy (CA) degradation to just 3.07%.
- Recently, many approaches have been proposed to detect or purify backdoors in MCL models.

- Mengyuan Sun (Wuhan University), Yu Li (Wuhan University), Yunjie Ge (Wuhan University), Yuchen Liu (Wuhan University), Bo Du (Wuhan University), Qian Wang (Wuhan University). "InverTune: A Backdoor Defense Method for Multimodal Contrastive Learning via Backdoor-Adversarial Correlation Analysis." NDSS — https://www.ndss-symposium.org/ndss-paper/invertune-a-backdoor-defense-method-for-multimodal-contrastive-learning-via-backdoor-adversarial-correlation-analysis/

## IoTBec: An Accurate and Efficient Recurring Vulnerability Detection Framework for Black Box IoT devices

- The proliferation of IoT devices has driven a rise in vulnerability exploits.
- To address this limitation, we propose IoTBec, a novel firmware and source-code independent framework for recurring vulnerability detection.
- Results show that IoTBec discovers over 7 times more vulnerabilities than the current state-of-the-art (SOTA) black-box fuzzing methods, with 100% precision and 93.37% recall.

- Haoran Yang (Institute of Information Engineering, Chinese Academy of Sciences, China and School of Cyber Security, University of Chinese Academy of Sciences, China), Jiaming Guo (Institute of Information Engineering, Chinese Academy of Sciences, China and School of Cyber Security, University of Chinese Academy of Sciences, China), Shuangning Yang (School of Internet, Anhui University, China), Guoli Zhao (Institute of Information Engineering, Chinese Academy of Sciences, China and School of Cyber Security, University of Chinese Academy of Sciences, China), Qingqi Liu (Institute of Information Engineering, Chinese Academy of Sciences, China and School of Cyber Security, University of Chinese Academy of Sciences, China), Chi Zhang (Institute of Information Engineering, Chinese Academy of Sciences, China and School of Cyber Security, University of Chinese Academy of Sciences, China), Zhenlu Tan (Institute of Information Engineering, Chinese Academy of Sciences, China and School of Cyber Security, University of Chinese Academy of Sciences, China), Lixiao Shan (Institute of Information Engineering, Chinese Academy of Sciences, China and School of Cyber Security, University of Chinese Academy of Sciences, China), Qihang Zhou (Institute of Information Engineering, Chinese Academy of Sciences, China and School of Cyber Security, University of Chinese Academy of Sciences, China), Mengting Zhou (Institute of Information Engineering, Chinese Academy of Sciences, China), Jianwei Tai (School of Internet, Anhui University, China), Xiaoqi Jia (Institute of Information Engineering, Chinese Academy of Sciences, China and School of Cyber Security, University of Chinese Academy of Sciences, China). "IoTBec: An Accurate and Efficient Recurring Vulnerability Detection Framework for Black Box IoT devices." NDSS — https://www.ndss-symposium.org/ndss-paper/iotbec-an-accurate-and-efficient-recurring-vulnerability-detection-framework-for-black-box-iot-devices/

## IsolatOS: Detecting Double Fetch Bugs in COTS RTOS by Re-enabling Kernel Isolation

- Real-time operating systems (RTOS) often expose double-fetch vulnerabilities when the kernel reads the same userspace memory location multiple times without ensuring consistency between fetches.
- Conventional static analysis cannot inspect proprietary, commercial off-the-shelf (COTS) RTOS kernels, and dynamic heuristics, which rely on broad time-window thresholds, suffer from high false positive rates and heavy emulation overhead.
- To address these challenges, we present ISOLAT OS, the first hardware-supported framework for detecting doublefetch bugs in COTS RTOS.

- Yingjie Cao (Sun Yat-sen University and The Hong Kong Polytechnic University), Xiaogang Zhu (Adelaide University), Dean Sullivan (University of New Hampshire, US), Haowei Yang, Lei Xue (Sun Yat-sen University), Xian Li (Swinburne University of Technology, Australia), Chenxiong Qian (University of Hong Kong, China), Minrui Yan (Swinburne University of Technology, Australia), Xiapu Luo (The Hong Kong Polytechnic University). "IsolatOS: Detecting Double Fetch Bugs in COTS RTOS by Re-enabling Kernel Isolation." NDSS — https://www.ndss-symposium.org/ndss-paper/isolatos-detecting-double-fetch-bugs-in-cots-rtos-by-re-enabling-kernel-isolation/

## Indicator of Benignity: An Industry View of False Positive in Malicious Domain Detection and its Mitigation

- Malicious domain detection serves as a critical technique to keep users safe against cyber attacks.
- To address these challenges, we propose a transitive trust model for IOB and implement it in a system called IOBHunter.
- Our evaluation using a dataset that contains verified FPs shows that IOBHunter can achieve 99.22% precision and 68.6% recall.

- Daiping Liu (Palo Alto Networks, Inc.), Danyu Sun (University of California, Irvine), Zhenhua Chen (Palo Alto Networks, Inc.), Shu Wang (Palo Alto Networks, Inc.), Zhou Li (University of California, Irvine). "Indicator of Benignity: An Industry View of False Positive in Malicious Domain Detection and its Mitigation." NDSS — https://www.ndss-symposium.org/ndss-paper/indicator-of-benignity-an-industry-view-of-false-positive-in-malicious-domain-detection-and-its-mitigation/

## Iris: Dynamic Privacy Preserving Search in Authenticated Chord Peer-to-Peer Networks

- In structured peer-to-peer networks, like Chord, users ﬁnd data by asking a number of intermediate nodes in the network.
- In order to better capture the privacy achieved by the iterative nature of the search we propose a new privacy notion, inspired byk-anonymity.
- We present a security analysis of the proposed algorithm based on the privacy notion we introduce.

- Angeliki Aktypi (University of Oxford), Kasper Rasmussen (University of Oxford). "Iris: Dynamic Privacy Preserving Search in Authenticated Chord Peer-to-Peer Networks." NDSS — https://www.ndss-symposium.org/ndss-paper/iris-dynamic-privacy-preserving-search-in-authenticated-chord-peer-to-peer-networks/

## IsolateGPT: An Execution Isolation Architecture for LLM-Based Agentic Systems

- Large language models (LLMs) extended as systems, such as ChatGPT, have begun supporting third-party applications.
- To that end, we propose I SOLA TEGPT, a design architecture that demonstrates the feasibility of execution isolation and provides a blueprint for implementing isolation, in LLM-based systems.
- The performance overhead incurred by I SOLATE GPT to improve security is under 30% for three-quarters of tested queries.

- Yuhao Wu (Washington University in St. Louis), Franziska Roesner (University of Washington), Tadayoshi Kohno (University of Washington), Ning Zhang (Washington University in St. Louis), Umar Iqbal (Washington University in St. Louis). "IsolateGPT: An Execution Isolation Architecture for LLM-Based Agentic Systems." NDSS — https://www.ndss-symposium.org/ndss-paper/isolategpt-an-execution-isolation-architecture-for-llm-based-agentic-systems/

## Ipotane: Balancing the Good and Bad Cases of Asynchronous BFT

- State-of-the-art asynchronous Byzantine Fault Tolerance (BFT) protocols integrate a partially-synchronous optimistic path.
- Another recent work, ParBFT (CCS'23) ensures good latency in all situations but suffers from reduced throughput in unfavorable situations due to the use of extra Asynchronous Binary Agreement (ABA) instances.
- We propose Ipotane, a protocol that attains performance comparable to partially-synchronous protocols in favorable situations and to purely asynchronous ones in unfavorable situations, in terms of both throughput and latency.

- Xiaohai Dai (Huazhong University of Science and Technology), Chaozheng Ding (Huazhong University of Science and Technology), Hai Jin (Huazhong University of Science and Technology), Julian Loss (CISPA Helmholtz Center for Information Security), Ling Ren (University of Illinois at Urbana-Champaign). "Ipotane: Balancing the Good and Bad Cases of Asynchronous BFT." NDSS — https://www.ndss-symposium.org/ndss-paper/ipotane-balancing-the-good-and-bad-cases-of-asynchronous-bft/

## Interventional Root Cause Analysis of Failures in Multi-Sensor Fusion Perception Systems

- Autonomous driving systems (ADS) heavily depend on multi-sensor fusion (MSF) perception systems to process sensor data and improve the accuracy of environmental perception.
- To overcome these limitations, we propose a novel approach called interventional root cause analysis (IRCA).
- The average F1-score of IRCA in real fault scenarios is over 95%.

- Shuguang Wang (City University of Hong Kong), Qian Zhou (City University of Hong Kong), Kui Wu (University of Victoria), Jinghuai Deng (City University of Hong Kong), Dapeng Wu (City University of Hong Kong), Wei-Bin Lee (Information Security Center, Hon Hai Research Institute), Jianping Wang (City University of Hong Kong). "Interventional Root Cause Analysis of Failures in Multi-Sensor Fusion Perception Systems." NDSS — https://www.ndss-symposium.org/ndss-paper/interventional-root-cause-analysis-of-failures-in-multi-sensor-fusion-perception-systems/
