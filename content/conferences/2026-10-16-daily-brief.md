+++
title = "Conference Brief — 2026-10-16"
date = 2026-10-16T06:00:00Z
type = "conferences"
tags = ["ndss", "vulnerability-discovery", "fuzzing", "tooling"]
summary = "A batch of NDSS papers covering URL shortening service abuse, GPU driver fuzzing, ZK compiler testing, and latency improvements for DAG-based consensus."
+++

## In brief

- **Misdirection attacks on URL shorteners** exploit implicit trust, extending consequences to phishing and code injection, with researchers finding a quarter of the DUSSs are susceptible.
- **Fuzzing and testing tools tackle complex targets:** Moneta addresses the costs of physical GPU driver testing via an ex-vivo approach, while MTZK pioneers metamorphic testing for ZK compilers to uncover 21 logic bugs.
- **Consensus protocol latency is pushed to theoretical lower bounds** by Mysticeti-C, an uncertified DAG-based design reaching 3 message rounds.

- Dedicated URL Shortening Services (DUSSs) are designed to transform trusted long URLs into shortened links, but attackers exploit these to misdirect implicit trust from both users and domain-based checkers.
- The researchers introduced Ditto to test mobile-centric DUSSs, discovering that a quarter of the DUSSs are susceptible to Misdirection Attack.
- The consequences extend beyond simple redirection, enabling stealthy phishing attacks and code injection on users' mobile phones.
- Zhibo Zhang, Lei Zhang, Zhangyue Zhang, Geng Hong, Yuan Zhang, Min Yang. "Misdirection of Trust: Demystifying the Abuse of Dedicated URL Shortening Service." NDSS — https://www.ndss-symposium.org/ndss-paper/misdirection-of-trust-demystifying-the-abuse-of-dedicated-url-shortening-service/

- Ex-vivo driver fuzzing approaches mitigate the hardware requirement imposed by in-vivo approaches, but existing ex-vivo approaches face challenges.
- Moneta bypasses these limitations through an "ex-vivo" fuzzing methodology, which models and recalls "in-vivo" execution states to test GPU drivers.
- The tool enables stateful GPU driver fuzzing by using snapshots and recordings, and large-scale fuzzing by duplicating snapshots and recordings.
- Joonkyo Jung, Jisoo Jang, Yongwan Jo, Jonas Vinck, Alexios Voulimeneas, Stijn Volckaert, Dokyung Song. "Moneta: Ex-Vivo GPU Driver Fuzzing by Recalling In-Vivo Execution States." NDSS — https://www.ndss-symposium.org/ndss-paper/moneta-ex-vivo-gpu-driver-fuzzing-by-recalling-in-vivo-execution-states/

- MTZK is a metamorphic testing framework designed to test Zero-Knowledge (ZK) compilers for compilation correctness and uncover logic bugs.
- The framework leverages deliberately designed metamorphic relations (MRs) to mutate ZK compiler inputs, allowing for automated testing without requiring manual intervention.
- In an evaluation of four industrial ZK compilers, MTZK successfully uncovered 21 logic bugs, out of which the developers have promptly patched 15.
- Dongwei Xiao, Zhibo Liu, Yiteng Peng, Shuai Wang. "MTZK: Testing and Exploring Bugs in Zero-Knowledge (ZK) Compilers." NDSS — https://www.ndss-symposium.org/ndss-paper/mtzk-testing-and-exploring-bugs-in-zero-knowledge-zk-compilers/

- Mysticeti-C is a DAG-based Byzantine consensus protocol designed to achieve the lower bounds of latency of 3 message rounds.
- The protocol achieves this latency improvement by avoiding explicit certification of DAG blocks and using a novel commit rule, ensuring blocks can be committed without delays.
- At a steady state of 50k to 400k TPS for both network sizes, Mysticeti-C exhibits sub-second latency.
- Kushal Babel, Andrey Chursin, George Danezis, Anastasios Kichidis, Lefteris Kokoris-Kogias, Arun Koshy, Alberto Sonnino, Mingwei Tian. "Mysticeti: Reaching the Latency Limits with Uncertified DAGs." NDSS — https://www.ndss-symposium.org/ndss-paper/mysticeti-reaching-the-latency-limits-with-uncertified-dags/

- Shuangxiang Kan, Xiao Cheng, Yuekang Li. "MUTATO: Enhancing Fuzz Drivers with Adaptive API Option Mutation." NDSS — https://www.ndss-symposium.org/ndss-paper/mutato-enhancing-fuzz-drivers-with-adaptive-api-option-mutation/
- Robin Vassantlal, Hasan Heydari, Bernardo Ferreira, Alysson Bessani. "MVP-ORAM: a Wait-free Concurrent ORAM for Confidential BFT Storage." NDSS — https://www.ndss-symposium.org/ndss-paper/mvp-oram-a-wait-free-concurrent-oram-for-confidential-bft-storage/
- Wayne Wang, Aaron Ortwein, Enrique Sobrados, Robert Stanley, Piyush Kumar Sharma, Afsah Anwar, Roya Ensafi. "MVPNalyzer: An Investigative Framework for Auditing the Security & Privacy of Mobile VPNs." NDSS — https://www.ndss-symposium.org/ndss-paper/mvpnalyzer-an-investigative-framework-for-auditing-the-security-privacy-of-mobile-vpns/
- Hanyue Dou, Peifang Ni, Yingzi Gao, Jing Xu. "Mobius: Enabling Byzantine-Resilient Single Secret Leader Election with Uniquely Verifiable State." NDSS — https://www.ndss-symposium.org/ndss-paper/mobius-enabling-byzantine-resilient-single-secret-leader-election-with-uniquely-verifiable-state/
