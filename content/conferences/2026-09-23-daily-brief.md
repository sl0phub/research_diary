+++
title = "Conference Brief — 2026-09-23"
date = 2026-09-23T06:00:00Z
type = "conferences"
tags = ["cloud", "fuzzing", "kernel", "llm-security", "mitigations", "supply-chain", "web-security", "ndss"]
summary = "New findings spanning LLM cache poisoning, npm prototype pollution, and kernel compartmentalization with PKS."
+++

## In brief

- A broad range of findings across different abstraction layers, highlighting systemic weaknesses in both emerging technologies and established infrastructure.
- At the infrastructure level, misaligned abstractions enable cross-namespace attacks in Kubernetes operators, while new approaches to kernel compartmentalization use Intel PKS for bi-directional isolation.
- On the application and model side, prototype pollution in npm packages is scaled through an exploitation-driven framework, and LLM serving caches introduce new poisoning and side-channel threats.

## Cache Me, Catch You: Cache Related Security Threats in LLM Serving Frameworks

- Caching mechanisms in LLM serving engines—prefix cache, multimodal cache, and semantic cache—improve efficiency by reusing intermediate computational states, but they also introduce shared-state vulnerabilities across different requests.
- The analysis demonstrates side-channel attacks for data extraction and cache poisoning attacks that can manipulate model outputs, bypassing alignment safeguards or causing denial of service.
- The root cause is the lack of strict isolation in multi-tenant LLM serving frameworks, treating the cache as trusted data without verifying its context or source.

Wu, X., Ying, L., Chen, G., Gu, Y., Qu, H. "Cache Me, Catch You: Cache Related Security Threats in LLM Serving Frameworks." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/cache-me-catch-you-cache-related-security-threats-in-llm-serving-frameworks/

## Bullseye: Detecting Prototype Pollution in NPM Packages with Proof of Concept Exploits

- Static analysis of prototype pollution in JavaScript often suffers from high false-positive rates or fails to scale due to the dynamic nature of the language.
- This approach uses an exploit-generation framework that pairs static tracking of property assignments with dynamic verification, constructing concrete proof-of-concept exploits to confirm reachability and impact.
- Evaluated on popular npm packages, it uncovered new, actionable vulnerabilities that previous static-only tools missed, providing a clearer view of the supply-chain risk posed by prototype pollution.

Houis, T., Jiang, S., Mannan, M., Youssef, A. "Bullseye: Detecting Prototype Pollution in NPM Packages with Proof of Concept Exploits." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/bullseye-detecting-prototype-pollution-in-npm-packages-with-proof-of-concept-exploits/

## BSFuzzer: Context-Aware Semantic Fuzzing for BLE Logic Flaw Detection

- Bluetooth Low Energy (BLE) protocol stacks frequently contain logic flaws—such as incorrect state transitions or misinterpreted fields—that enable authentication bypasses and DoS, yet these evade conventional fuzzing due to deep semantic constraints.
- A black-box, context-aware fuzzing approach is introduced to actively infer the target's state machine and generate semantically valid but logically flawed test cases.
- By maintaining state awareness during the fuzzing loop, the tool reaches deeper logic paths in BLE implementations, discovering flaws that standard syntax-based or stateless fuzzers miss.

Yang, T., Qin, Y., Zhang, L., Fu, Z., Chen, J., Wang, J., Zhao, S., Li, Q., Li, R., Wang, H., Zhang, Y. "BSFuzzer: Context-Aware Semantic Fuzzing for BLE Logic Flaw Detection." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/bsfuzzer-context-aware-semantic-fuzzing-for-ble-logic-flaw-detection/

## BULKHEAD: Secure, Scalable, and Efficient Kernel Compartmentalization with PKS

- Kernel compartmentalization follows the principle of least privilege, but existing mechanisms struggle with performance overhead and scalability when trying to isolate numerous kernel components.
- The design leverages Intel Protection Keys for Supervisor (PKS) to provide bi-directional isolation, isolating code and data into mutually untrusted compartments with fast switching.
- A lightweight in-kernel monitor enforces data integrity, execute-only memory, and interface integrity, demonstrating that hardware-assisted compartmentalization can achieve strong security guarantees without incurring prohibitive costs.

Guo, Y., Wang, Z., Bai, W., Zeng, Q., Lu, K. "BULKHEAD: Secure, Scalable, and Efficient Kernel Compartmentalization with PKS." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/bulkhead-secure-scalable-and-efficient-kernel-compartmentalization-with-pks/

## Breaking the Bulkhead: Demystifying Cross-Namespace Reference Vulnerabilities in Kubernetes Operators

- Kubernetes relies on namespace isolation to separate workloads, but Operators often require elevated privileges that transcend these boundaries, introducing a vulnerability class where the Operator’s implemented logic mismatches its declared scope.
- An attacker with access to a single namespace can exploit these cross-namespace reference vulnerabilities to manipulate resources in unauthorized namespaces, leading to privilege escalation.
- A static analysis of Kubernetes Operators reveals the widespread nature of this flaw, showing that operators frequently fail to validate the namespace context of the resources they interact with.

Chen, A., Guo, Z., Jin, Z., Li, Z., Chen, Y. "Breaking the Bulkhead: Demystifying Cross-Namespace Reference Vulnerabilities in Kubernetes Operators." NDSS 2025.
https://www.ndss-symposium.org/ndss-paper/breaking-the-bulkhead-demystifying-cross-namespace-reference-vulnerabilities-in-kubernetes-operators/
