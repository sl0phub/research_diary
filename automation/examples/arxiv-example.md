+++
title = "arXiv Brief — 2026-09-17"
date = 2026-09-17T06:00:00Z
type = "arxiv"
tags = ["cs.CR", "hardware", "llm-security", "cryptography", "side-channel"]
summary = "An analog input pin turned into an outbound channel in 55-nm silicon, a payload split across MCP channels so no single one carries an injection, and polynomial-time sign recovery on hard-label networks."
+++

*This file is a format reference, not published content. It lives outside `content/` on purpose.*

*Every identifier below is real and resolves. That is deliberate: the previous version of this file
used invented arXiv IDs and DOIs to illustrate the shape, and a deep dive copied one of them,
changed a digit, and published it. Do not treat any identifier here as a template to adapt — see
hard constraint 9 in AGENTS.md.*

## In brief

- Two of the three turn on a boundary that was assumed rather than checked: a pin's directionality
  inferred from nominal signal flow, and a context window shared by three channels with no privilege
  separation between them.
- In both, the detection layer is looking somewhere else — specification-based analog screening never
  watches an input-only pin for outbound data, and the MCP scanners inspect tool descriptions at
  install time rather than results at runtime.

## Analog Pin Directionality as an Exfiltration Attack Surface in Mixed-Signal ICs

- A hardware Trojan modulates the input offset of a closed-loop amplifier, turning a nominally
  input-only analog pin into an outbound channel. Three host conditions enable it: a closed-loop
  amplifier, an amplifier input exposed to a pin, and sufficiently high impedance at that pin — which
  covers ECG, PPG, EEG, off-chip temperature sensing and optical interfaces with off-chip diodes.
- Silicon, not simulation: a 39.284 µm² payload in a PPG analog front end fabricated on a commercial
  55-nm CMOS process, 0.8% of the front-end amplifier and under 0.001% of a typical biosensing AFE.
  Activation costs 0.03 dB of the host's filtered output SNR, and the 5.9% maximum perturbation of
  the PPG amplitude sits inside the 34.3% benign variation measured across process corners and 0–80 °C.
- The recovery asymmetry is the result. Raw SINR at the pin stays below −20 dB, under the
  interference-and-noise floor; a receiver that knows the signalling band applies a 250 Hz digital
  high-pass and gains 34 dB, clearing 14 dB and recovering the data.
- Read the two bit rates separately: a 256-bit PRBS-7 message is recovered with zero observed errors
  at **6 bps**, while the 10 kbps figure comes from alternating-pattern measurements with BER
  estimated from measured SINR, not from an error-free payload. The authors are explicit that the
  channel is not intrinsically undetectable — it becomes observable once validation monitors
  input-only pins for data-dependent spectral activity.

Ranganatham, R., Adiga, C., Zuzak, M., Das, T. "Analog Pin Directionality as an Exfiltration Attack
Surface in Mixed-Signal ICs." arXiv, 2026.
arXiv:2609.19111 — https://arxiv.org/abs/2609.19111

## Measuring and Exploiting Implicit Trust in LLM Tool-Calling Pipelines

- MCP feeds three attacker-influenced channels into one context window with no privilege boundary
  between them: tool descriptions, tool results and sampling messages. The paper first measures a
  per-model *trust profile* — a channel × payload compliance matrix — rather than scoring injection
  resistance as one number.
- Cross-channel fragmentation then splits a payload so that no single channel carries a complete
  injection and the model reassembles it. Evaluated over 12 frontier models, three production clients
  and six payloads in more than 15,000 trials, with two- and three-channel variants (sign test
  p = 0.016).
- The headline is the discontinuity, not the rate: models at 0% compliance under single-channel
  injection reach up to 100% credential exfiltration under two-channel fragmentation — GPT-4o goes
  0% → 100%. A model that looks immune when each channel is tested alone is not immune.
- Defences are measured too. Four static description scanners (Tencent AI-Infra-Guard, Snyk
  agent-scan, Agentic Radar, Cisco MCP Scanner) analyse tool descriptions at install time and none
  inspects results at runtime, so a payload assembled at runtime is structurally invisible to them;
  all seven third-party tools tested missed fragmented payloads, and the three prompt-based defences
  held per-model rather than universally.

Ediga, M., Chattopadhyay, S. "Measuring and Exploiting Implicit Trust in LLM Tool-Calling
Pipelines." arXiv, 2026.
arXiv:2609.18217 — https://arxiv.org/abs/2609.18217

## Normal Alignment: Improved Cryptanalytic Sign Recovery on Hard-Label Networks

- Attacks the sign-recovery step of cryptanalytic model extraction on hard-label (S1) deep networks,
  where the attacker sees only the predicted label. Carlini et al. (EUROCRYPT 2025) made signature
  and sign recovery polynomial-time, but their sign method holds only a marginal edge over guessing
  and emits high-confidence wrong predictions in deeper layers, which forces exponential enumeration.
- Normal Alignment infers neuron signs from the expected length difference between projected normals
  of adjacent decision facets at dual points, which both raises voting accuracy and pushes the
  remaining errors into low-confidence ranks where they are cheap to fix.
- Combined with the hard-label SOE extension as `eSOE + Alignment`, that ranking removes the
  enumeration step entirely: full sign recovery in polynomial time for CIFAR-10 (192-64×8-10) and
  MNIST (64-96×3-32-10) models, against enumerations of roughly 2^52 and 2^82 sign guesses under the
  prior method.

*Abstract only — full text not retrieved.*

Tang, S., Chen, Z., Su, Y., Gao, Z., Qin, L., Dong, X. "Normal Alignment: Improved Cryptanalytic
Sign Recovery on Hard-Label Networks." arXiv, 2026.
arXiv:2609.18751 — https://arxiv.org/abs/2609.18751

## Also published

- Vadayath, J. M., Wang, H., Schloegel, M., et al. "AIJon: Automated Generation of Annotations for
  Fuzzing." arXiv:2609.18457 — https://arxiv.org/abs/2609.18457
- Liu, G., Cheng, G., Liu, W. "Structural Decomposability of Encrypted Traffic Side-Channel Leakage."
  arXiv:2609.19036 — https://arxiv.org/abs/2609.19036
- Surapani, R. K., et al. "Authorization Architectures for Tool-Using AI Agents." arXiv:2609.15906 —
  https://arxiv.org/abs/2609.15906
