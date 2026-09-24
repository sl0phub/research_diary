+++
title = "Conference Brief — 2026-09-24"
date = 2026-09-24T06:00:00Z
type = "conferences"
tags = ["ndss", "malware", "privacy", "web-security"]
summary = "New findings on app promotion malware, membership inference attacks, and CSS-based browser fingerprinting."
+++

## In brief

- Malware operators are exploiting app promotion advertisements to distribute payloads outside official app store scrutiny.
- Cascading and proxy techniques significantly amplify the success rate of membership inference attacks against machine learning models.
- Modern CSS features can be weaponised to fingerprint browsers even when JavaScript is completely disabled, compromising privacy in restricted environments like email clients.

## Careful About What App Promotion Ads Recommend! Detecting and Explaining Malware Promotion via App Promotion Graph

- Demonstrates that malware authors use app promotion ads to bypass app store vetting processes, acting as a new distribution vector.
- Introduces ADGPE, a tool integrating UI exploration with graph learning to automatically detect and explain malware promotion.
- The method identifies complex promotion graphs and highlights structural differences between benign and malicious app promotions.

Ma, S., Chen, C., Yang, S., Hou, S., Li, T. J.-J., Xiao, X., Xie, T., Ye, Y. "Careful About What App Promotion Ads Recommend! Detecting and Explaining Malware Promotion via App Promotion Graph." NDSS 2024.
https://www.ndss-symposium.org/ndss-paper/careful-about-what-app-promotion-ads-recommend-detecting-and-explaining-malware-promotion-via-app-promotion-graph/

## Cascading and Proxy Membership Inference Attacks

- Evaluates membership inference attacks (MIAs) against machine learning models, distinguishing between adaptive and non-adaptive adversary models.
- Proposes a Cascading MIA framework that improves attack performance by exploiting membership dependencies via conditional shadow training.
- Highlights that existing defenses may need re-evaluation when adversaries can adaptively query and train shadow models.

Du, Y., Li, J., Chen, Y., Zhang, K., Yuan, Z., Xiao, H., Ribeiro, B., Li, N. "Cascading and Proxy Membership Inference Attacks." NDSS 2024.
https://www.ndss-symposium.org/ndss-paper/cascading-and-proxy-membership-inference-attacks/

## Cascading Spy Sheets: Exploiting the Complexity of Modern CSS for Email and Browser Fingerprinting

- Systematically investigates modern CSS features for fingerprinting capabilities without relying on JavaScript.
- Presents three novel techniques that bypass state-of-the-art scriptless tracking mitigations in privacy-aware browsers and email clients.
- Emphasizes the tension between rich styling features and privacy, showing CSS alone can leak substantial fingerprinting data.

Trampert, L., Weber, D., Gerlach, L., Rossow, C., Schwarz, M. "Cascading Spy Sheets: Exploiting the Complexity of Modern CSS for Email and Browser Fingerprinting." NDSS 2024.
https://www.ndss-symposium.org/ndss-paper/cascading-spy-sheets-exploiting-the-complexity-of-modern-css-for-email-and-browser-fingerprinting/

## Also published

- Xiao, L., Wang, H., Yu, A., Zhao, L., Meng, D.. "CASPR: Context-Aware Security Policy Recommendation." NDSS 2024 — https://www.ndss-symposium.org/ndss-paper/caspr-context-aware-security-policy-recommendation/
- Wang, J., Yan, Z., Lan, J., Li, X., Bertino, E.. "CAT: Can Trust be Predicted with Context-Awareness in Dynamic Heterogeneous Networks?." NDSS 2024 — https://www.ndss-symposium.org/ndss-paper/cat-can-trust-be-predicted-with-context-awareness-in-dynamic-heterogeneous-networks/
- Tajalli, B., Koffas, S., Picek, S.. "CatBack: Universal Backdoor Attacks on Tabular Data via Categorical Encoding." NDSS 2024 — https://www.ndss-symposium.org/ndss-paper/catback-universal-backdoor-attacks-on-tabular-data-via-categorical-encoding/
- Chen, L., Sun, Y., Wei, H., Chen, Y.. "Causal-Guided Detoxify Backdoor Attack of Open-Weight LoRA Models." NDSS 2024 — https://www.ndss-symposium.org/ndss-paper/causal-guided-detoxify-backdoor-attack-of-open-weight-lora-models/
- Liu, Z., Rong, Y., Li, C., Tan, W., Li, Y., Han, X., Yang, S., Zhang, C.. "CCTAG: Configurable and Combinable Tagged Architecture." NDSS 2024 — https://www.ndss-symposium.org/ndss-paper/cctag-configurable-and-combinable-tagged-architecture/
