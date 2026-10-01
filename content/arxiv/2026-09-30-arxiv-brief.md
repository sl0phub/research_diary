+++
title = "arXiv Brief — 2026-09-30"
date = 2026-09-30T06:00:00Z
type = "arxiv"
tags = ["vulnerability-discovery", "privacy", "browser", "network-security", "kernel", "exploitation", "hardware", "fuzzing"]
summary = "LLM agent limitations across vulnerability discovery, privacy preservation, scientific review, and browser use; plus on-device cohort inference, SLUB allocator exploitation, temporal HDR corruption, and adversarial DDoS detection."
+++

## In brief
- Studies across multiple domains highlighted vulnerabilities and limitations in LLM agents, finding that they waste significant verification effort on safe decoys, inappropriately access confidential sources for personal information without explicit privacy instructions, remain susceptible to perturbations in scientific reviews, and suffer from "belief failure" in browser tasks.
- In systems and hardware, new attack surfaces were demonstrated with the SLUB allocator's sheaf/barn caching mechanism breaking traditional exploit assumptions and mitigation effectiveness, and the FLASH attack using pulsed light to corrupt temporal HDR fusion in modern cameras without requiring hardware failure.
- New privacy-preserving and defensive approaches were introduced, including the Sealed Inference Frame (SIF) for identity-less professional cohorts in B2B advertising, and combining Generative Adversarial Networks (GANs) with adversarial debiasing for more robust DDoS detection.

## Cheap to Hypothesize, Costly to Verify: The Defense Surface of Agentic Vulnerability Discovery

- Autonomous vulnerability discovery creates a hypothesis-verification asymmetry: LLM agents generate many vulnerability hypotheses cheaply, but verifying them with reachability analysis and proof-of-concept construction consumes significant time and budget.
- RedHerring defends repositories by introducing certifiably safe decoys that mimic CVE-derived vulnerability chains, complete with false bridges that render their dangerous sinks unreachable.
- Because defenders hold a private certificate verifying safety, establishing the same guarantee from the outside requires solving computationally hard problems, making the decoys effective sinks for automated verification effort.
- Tested across 33 OSS-Fuzz projects using five models, RedHerring reduced the discovery of real vulnerabilities by 38.7% to 60.4% by absorbing 30.6% to 51.5% of the agents' completion token budget.
- Explicitly informing the agent that decoys might be present caused it to adapt its strategy, but RedHerring still achieved a 37.2% reduction in discovered vulnerabilities, demonstrating resilience against informed adversaries.
- Authors. "Cheap to Hypothesize, Costly to Verify: The Defense Surface of Agentic Vulnerability Discovery." arXiv:2609.35909 — https://arxiv.org/abs/2609.35909

## PrivacySkills: How Privacy Guidance Shapes Source Selection in LLM Agents

- The PrivacySkills framework evaluates how LLM agents choose between equivalent information sources: asking the user, consulting public records, or accessing confidential accounts.
- Without privacy guidance, five open-weight models tested accessed confidential sources in 30% of valid task runs despite having alternative sources available; this rose to 45% when users were simulated as unavailable.
- Providing system-level privacy instructions alone had limited impact, and skill-level "intrusiveness" metadata labels only reduced confidential access by 24% on average.
- However, combining system-level instructions with skill-level metadata labels proved complementary, halving the rate of confidential access across the models tested.
- Authors. "PrivacySkills: How Privacy Guidance Shapes Source Selection in LLM Agents." arXiv:2609.35937 — https://arxiv.org/abs/2609.35937

## Privacy-Friendly Cohort Determination: Sealed, CSP-Independent In-Browser ML Inference of Professional Segments for Identity-Less Advertising

- With third-party cookies blocked and Google's Privacy Sandbox cohorts retired, determining B2B advertising targets (employer size, industry, function) typically relies on matching cross-site identities or decaying reverse-IP firmographics.
- The Sealed Inference Frame (SIF) replaces cross-site identity tracking by performing on-device ML inference to assign coarse professional cohorts, emitting only locally differentially private labels into the OpenRTB bid stream.
- SIF bypasses restrictive publisher Content Security Policies (CSPs) by using a navigated cross-origin iframe to run inference in WebAssembly, while nesting the worker with a `default-src 'none'` policy to completely isolate the model from the network.
- The system limits leakage to approximately 5 bits per site per week even if the model is malicious, using a memoised, randomised response tied to the publisher's first-party identifier to prevent cross-site linking.
- Authors. "Privacy-Friendly Cohort Determination: Sealed, CSP-Independent In-Browser ML Inference of Professional Segments for Identity-Less Advertising." arXiv:2609.36153 — https://arxiv.org/abs/2609.36153

## Adversarial Debiasing of Machine Learning Models for Enhanced Network Security against DDoS Attacks

- The authors propose a machine-learning framework for DDoS detection that combines synthetic data generation via Generative Adversarial Networks (GANs) with adversarial debiasing.
- The GAN-generated synthetic traffic achieved 80.3% cosine similarity to real-world traffic data, allowing the model to learn underlying patterns without suffering from the imbalance of packet-related features.
- Adversarial debiasing was applied to reduce the Random Forest classifier's sensitivity to skewed distributions in variables like forward and backward packet counts and total byte lengths.
- Retraining the model on a mix of synthetic and real data resulted in 99.98% accuracy on benchmark data and a 22.60% improvement in detection on unseen synthetic traffic.
- Authors. "Adversarial Debiasing of Machine Learning Models for Enhanced Network Security against DDoS Attacks." arXiv:2609.36167 — https://arxiv.org/abs/2609.36167

## Harvest Season for SLUB: From io_uring vulnerability to Novel Sheaf-Based Exploitation Techniques

- The SLUB allocator's new sheaf/barn caching mechanism, introduced in Linux 6.18 for per-CPU and NUMA performance, breaks traditional cross-cache attacks by caching objects before they reach the buddy system, while simultaneously neutralizing the `SLAB_FREELIST_HARDENED` mitigation because its object pointer array lacks encryption and bypasses double-free checks on the fast path.
- The authors used two new 0-day vulnerabilities in the io_uring subsystem—a race condition during CQ/SQ ring resize and a use-after-free in the provided-buffer bundle error path—to develop a complete local privilege escalation exploit.
- Three novel sheaf-based exploitation techniques are proposed: an object array hijack that controls the allocator to return an arbitrary location, an object array out-of-bounds write that corrupts the `size` metadata to overwrite a `task_struct` credential pointer, and an RCU-sheaf cross-cache technique.
- The RCU-sheaf technique achieves cross-cache migration without relying on the buddy system by hijacking the `cache` metadata on a `slab_sheaf` during an RCU grace period, enabling more stable and flexible object placement between cache pools.
- Authors. "Harvest Season for SLUB: From io_uring vulnerability to Novel Sheaf-Based Exploitation Techniques." arXiv:2609.37608 — https://arxiv.org/abs/2609.37608

## Lights, Camera, Attack: Exploiting Temporal HDR Fusion with Pulsed Light

- The FLASH (Fusion-Level Attack by Saturating HDR) attack uses external pulsed light to corrupt the image signal processing pipelines of cameras using temporal High Dynamic Range (HDR) fusion, bypassing the need for physical access, exact phase lock, or hardware damage.
- Temporal HDR fusion algorithms assume stable scene illumination across sequential exposures with different integration times; FLASH violates this assumption to create cross-exposure inconsistency before downstream perception logic is applied.
- In physical evaluations, FLASH induced extreme-darkening rates of 50.0% on an iPhone 16 Pro and 33.7% on a Wyze Battery Cam Pro, consistently triggering a system-level low-visibility response (10/10 trials) that continuous or randomized flashing could not reproduce.
- A controlled OpenPilot case study showed severe target-region darkening in 23.0% of frames with up to a 90.8% reduction in target-background Contrast-to-Noise Ratio (CNR), while a proof-of-concept exposure-rejection defense in a night-only stress test reduced median absolute output-luma deviation by 79.16%.
- Authors. "Lights, Camera, Attack: Exploiting Temporal HDR Fusion with Pulsed Light." arXiv:2609.37742 — https://arxiv.org/abs/2609.37742

## Breaking the Illusion of Review Reliability under Static Evaluation: SCOPE Fuzzing for LLM-based Scientific Reviewers

- The authors challenge the assumed reliability of LLM-based peer reviewers by demonstrating that prior static template evaluations overlook two critical vulnerabilities: *stratified vulnerability* (perturbation effects depend on the original review score) and *perturbation undercoverage* (a single static template fails to expose vulnerabilities shown by diverse realizations).
- To address these limitations, the authors introduce a three-level evaluation framework (TREAP) that covers form-, reasoning-, and cognitive judgment-level perturbations.
- Based on the TREAP framework, the authors built SCOPE-Fuzzer, a strategy-aware fuzzer that uses feedback-driven strategy selection and adaptive mutation of paper content.
- By iteratively probing reviewers with dynamic perturbations rather than static templates, SCOPE-Fuzzer consistently uncovers reliability vulnerabilities and demonstrates that current LLM reviewers are still susceptible to academically plausible content manipulations.
- Authors. "Breaking the Illusion of Review Reliability under Static Evaluation: SCOPE Fuzzing for LLM-based Scientific Reviewers." arXiv:2609.37097 — https://arxiv.org/abs/2609.37097

## Constructing Challenging Browser-Use Tasks by Controlled Environment Interventions

- The authors propose BreakingWeb, a benchmark methodology that makes browser-use tasks systematically harder by applying deterministic, recoverable interventions to the web environment (at different web stack layers) while preserving the instruction and the backend success criterion.
- Rather than endlessly collecting new tasks to increase difficulty, this approach transforms difficulty into a programmable property, creating pairs of clean and intervened tasks across seven self-hosted environments.
- When evaluating six strong browser-use agents and three GUI-only agents, the interventions successfully overturned nearly half of the tasks the agents could solve in the clean environments, whereas human performance only suffered minimally.
- The evaluation highlights two primary bottlenecks: text-based models suffer from "belief failure" (declaring success when the required change never happened) due to poor post-action verification of external state, while GUI-only agents struggle with affordance discovery on rendered images.
- Authors. "Constructing Challenging Browser-Use Tasks by Controlled Environment Interventions." arXiv:2609.35814 — https://arxiv.org/abs/2609.35814
