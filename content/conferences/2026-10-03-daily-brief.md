+++
title = "Conference Brief — 2026-10-03"
date = 2026-10-03T06:00:00Z
type = "conferences"
tags = ["fuzzing", "hardware", "side-channel", "supply-chain", "binary-analysis", "network-security", "privacy", "malware", "ndss"]
summary = "NDSS papers covering hardware side-channels, 1-day vulnerability tracking, binary diffing, website fingerprinting, network intrusion, and evasive ransomware detection."
+++

## In brief

- Side channels and website fingerprinting reveal how deeply embedded hardware and traffic patterns expose sensitive data.
- Analysis of third-party library dependencies uncovers significant unpatched 1-day vulnerabilities, highlighting supply chain risks.
- Fuzzing and binary diffing techniques continue to advance, utilizing dynamic instruction alignment to locate evasive vulnerabilities.

## Efficiently Detecting DBMS Bugs through Bottom-up Syntax-based SQL Generation

- Demonstrates a bottom-up fuzzing technique that prioritizes exploring feature-rich grammar rules before backtracking to the root of the syntax tree to create diverse queries.
- Detects recursive grammar dynamically, falling back to a more conservative top-down forward traversal to prevent path explosion and maintain generation performance.
- Discovered 63 unique zero-day bugs across MySQL, MariaDB, CockroachDB, DuckDB, and PostgreSQL, outperforming traditional top-down and bit-flip mutation fuzzers.

Liang, Y., Liu, P. "Efficiently Detecting DBMS Bugs through Bottom-up Syntax-based SQL Generation." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/efficiently-detecting-dbms-bugs-through-bottom-up-syntax-based-sql-generation/

## EMIRIS: Eavesdropping on Iris Information via Electromagnetic Side Channel

- Captures electromagnetic signals emitted by commercial iris recognition devices during the scanning process to reconstruct iris images.
- Uses a tailored diffusion model to denoise and restore iris texture details, framing the reconstruction as a linear inverse problem.
- Achieved a 53.47% average spoofing success rate against classical iris recognition models across more than 3,000 samples from 50 different users.

Li, W. et al. "EMIRIS: Eavesdropping on Iris Information via Electromagnetic Side Channel." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/emiris-eavesdropping-on-iris-information-via-electromagnetic-side-channel/

## Enhancing Security in Third-Party Library Reuse - Comprehensive Detection of 1-day Vulnerability through Code Patch Analysis

- Introduces VULTURE, a tool that identifies 1-day vulnerabilities in third-party libraries (TPLs) by using hashing-based comparisons instead of pure code-level similarity.
- Conducts version-based and chunk-based analysis separately to capture fine-grained semantic features, accommodating both exact and custom TPL reuse scenarios.
- Identified 175 vulnerabilities across 10 real-world projects, noting that custom adaptations account for roughly 55% of all TPL reuses.

Xu, S. et al. "Enhancing Security in Third-Party Library Reuse - Comprehensive Detection of 1-day Vulnerability through Code Patch Analysis." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/enhancing-security-in-third-party-library-reuse-comprehensive-detection-of-1-day-vulnerability-through-code-patch-analysis/

## Enhancing Semantic-Aware Binary Diffing with High-Confidence Dynamic Instruction Alignment

- Proposes BARRACUDA, an instruction alignment technique that samples execution paths based on instruction value-set sizes to partially reveal runtime values.
- Extracts instruction semantics through forced execution without requiring specific input, maintaining a mapping from intermediate representation values to abstract memory addresses.
- Generated 24.0% more instruction alignment anchor points with 92.1% precision, improving F1 scores for DeepBinDiff by 12.3 to 42.7 percentage points.

Ye, C., Zhou, A., Zhang, C. "Enhancing Semantic-Aware Binary Diffing with High-Confidence Dynamic Instruction Alignment." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/enhancing-semantic-aware-binary-diffing-with-high-confidence-dynamic-instruction-alignment/

## Enhancing Website Fingerprinting Attacks against Traffic Drift

- Mitigates the performance degradation of website fingerprinting models caused by temporal and network traffic drift by introducing contrastive learning and data augmentation strategies.
- Uses data augmentation to simulate drifted traffic patterns, which allows the Deep Learning model to retain high accuracy without needing continuous real-time labeled data collection.
- Demonstrates significant resilience over time, maintaining an F1-score of 82.27% under 270 days of real-world traffic drift.

Deng, X. et al. "Enhancing Website Fingerprinting Attacks against Traffic Drift." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/enhancing-website-fingerprinting-attacks-against-traffic-drift/

## ENTENTE: Cross-silo Intrusion Detection on Network Log Graphs with Federated Learning

- Evaluates a graph-based network intrusion detection system under federated learning poisoning attacks, bounding the attack strategy to test robustness.
- Demonstrated capabilities of detecting sophisticated lateral movement attacks using advanced graph models like graph autoencoders over distributed logs without centralizing data.
- Reached an area under the curve (AUC) metric of over 0.9 across most tested models.

Xu, J. et al. "ENTENTE: Cross-silo Intrusion Detection on Network Log Graphs with Federated Learning." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/entente-cross-silo-intrusion-detection-on-network-log-graphs-with-federated-learning/

## ERW-Radar: An Adaptive Detection System against Evasive Ransomware by Contextual Behavior Detection and Fine-grained Content Analysis

- Uses contextual correlation and fine-grained content analysis, checking byte stream probability distributions and the chi-squared test, to distinguish encrypted files from benign modifications.
- Identifies unique I/O repetitiveness exhibited by evasive ransomware during the encryption phase, a pattern rarely observed in benign programs.
- Reached a detection accuracy of 96.18% with a 5.36% false positive rate, consuming an average of 5.09% CPU utilization and 3.80% memory utilization.

Zhao, L. et al. "ERW-Radar: An Adaptive Detection System against Evasive Ransomware by Contextual Behavior Detection and Fine-grained Content Analysis." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/erw-radar-an-adaptive-detection-system-against-evasive-ransomware-by-contextual-behavior-detection-and-fine-grained-content-analysis/
