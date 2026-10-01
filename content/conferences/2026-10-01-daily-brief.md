+++
title = "Conference Brief — 2026-10-01"
date = 2026-10-01T06:00:00Z
type = "conferences"
tags = ["web-security", "side-channel", "hardware", "ndss"]
summary = "A taxonomy of Ethereum transaction phishing, a single-stepping attack extracting DNN architectures from SGX, and a large-scale evaluation of client-side open redirect impact."
+++

## In brief

- The Ethereum ecosystem is seeing a shift towards payload-based transaction phishing, resulting in significant financial losses.
- Hardware enclaves like Intel SGX remain vulnerable to side-channel attacks that can reconstruct the architecture of protected deep neural networks.
- Client-side open redirections are significantly more prevalent and exploitable than their server-side counterparts, enabling cross-site scripting and other critical threats.

## Dissecting Payload-based Transaction Phishing on Ethereum

- Scammers are increasingly utilizing payload-based transaction phishing (PTXPHISH) on Ethereum, which involves executing malicious payloads to deceive users into authorizing harmful interactions.
- A long-term measurement study identified 130,637 phishing transactions across 300 days, accounting for over $341.9 million in losses.
- Scammers consume roughly 13.4 ETH daily to broadcast these malicious transactions, highlighting the scale and profitability of the campaigns.

Chen, Z., Luo, D., Hu, Y., Wu, L., He, B., Zhou, Y., Zhejiang University. "Dissecting Payload-based Transaction Phishing on Ethereum." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/dissecting-payload-based-transaction-phishing-on-ethereum/

## DNN Latency Sequencing: Extracting DNN Architectures from Intel SGX Enclaves with Single-Stepping Attacks

- The DNN Latency Sequencing (DLS) attack demonstrates that side-channel leakage from Intel SGX can be used to extract the complete architecture of a protected deep neural network.
- The attack uses SGX-Step to perform single-stepping execution and collect fine-grained latency traces, analyzing them at both the function and basic block levels to reconstruct the model.
- Evaluated against models running in Darknet, TensorFlow Lite, and ONNX Runtime, DLS can successfully infer layer types and configurations based solely on execution latency patterns.

Park, M., Kong, Z., Kim, C. H., University of Texas at Dallas; Tian, D., Celik, Z. B., Purdue University. "DNN Latency Sequencing: Extracting DNN Architectures from Intel SGX Enclaves with Single-Stepping Attacks." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/dnn-latency-sequencing-extracting-dnn-architectures-from-intel-sgx-enclaves-with-single-stepping-attacks/

## Do (Not) Follow the White Rabbit: Challenging the Myth of Harmless Open Redirection

- Client-side open redirection vulnerabilities are often dismissed as low impact, but the shift to JavaScript-based redirections has introduced severe risks, such as cross-site scripting.
- A large-scale measurement of the Tranco top 10K sites utilizing a static-dynamic tool named STORK uncovered 20,800 open redirect vulnerabilities across 623 websites.
- Over 11.5% of the discovered open redirect vulnerabilities could be escalated into more critical threats, demonstrating that these client-side flaws are substantially more dangerous than traditional server-side redirects.

Khodayari, S., Pellegrino, G., CISPA Helmholtz Center for Information Security; Glauber, K., Saarland University. "Do (Not) Follow the White Rabbit: Challenging the Myth of Harmless Open Redirection." NDSS 2026.
https://www.ndss-symposium.org/ndss-paper/do-not-follow-the-white-rabbit-challenging-the-myth-of-harmless-open-redirection/
