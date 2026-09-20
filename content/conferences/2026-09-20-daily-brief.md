+++
title = "Conference Brief — 2026-09-20"
date = 2026-09-20T06:00:00Z
type = "conferences"
tags = ["ndss", "fuzzing", "protocol-analysis", "llm-security", "cloud", "binary-analysis"]
summary = "New findings spanning library fuzzing, BACnet protocol vulnerabilities, OLE document security, backdoors in machine learning, risks in AI character platforms, and cloud app-in-app resource isolation."
+++

## In brief

- **BACnet vulnerabilities:** Implicitly reserved fields in BACnet protocols present systemic risks to building automation, emphasizing the challenge of securing industrial control networks.
- **AI safety and model poisoning:** Extensive benchmarking of AI character platforms reveals significant safety deficits, while new methods such as BARBIE identify subtle model backdoors via latent separability.
- **Ecosystem isolation risks:** Both OLE specifications and App-in-App cloud services highlight how blurred trust boundaries between nested environments can lead to robust exploits.

## Automatic Library Fuzzing through API Relation Evolvement

- Software libraries pose significant security threats, but fuzzing them automatically is hard due to the need for drivers that reflect correct API usage without causing misuses or missing deep logic flaws.
- NEXZZER uses hybrid relation learning to continuously infer and evolve API relations, combined with a novel driver architecture for better library code coverage.
- Evaluated on 18 libraries and Google's Fuzzer Test Suite, the fuzzer identified and filtered out API misuse crashes while discovering 27 zero-day vulnerabilities in targets like OpenSSL and libpcre2.
- Lin, Jiayi et al. "Automatic Library Fuzzing through API Relation Evolvement." NDSS (2026) — https://www.ndss-symposium.org/ndss-paper/automatic-library-fuzzing-through-api-relation-evolvement/

## BACnet or “BADnet”? On the (In)Security of Implicitly Reserved Fields in BACnet

- The Building Automation and Control Networks (BACnet) protocol, a leading standard in the building automation sector, is known for lacking intrinsic encryption, but other structural weaknesses remain under-explored.
- The research examines the security implications of implicitly reserved fields within the protocol standard, which can be manipulated by attackers despite the specification's expectations.
- As the global market for building automation scales, addressing these implicit flaws is necessary for ensuring long-term safety and operational resilience of smart facilities.
- Zhang, Qiguang et al. "BACnet or “BADnet”? On the (In)Security of Implicitly Reserved Fields in BACnet." NDSS (2026) — https://www.ndss-symposium.org/ndss-paper/bacnet-or-badnet-on-the-insecurity-of-implicitly-reserved-fields-in-bacnet/

## BARBIE: Robust Backdoor Detection Based on Latent Separability

- Shared deep learning models face substantial backdoor risks, but previous methods attempting to detect backdoors by clustering or measuring distance between latent representations often fail against adaptive attacks.
- BARBIE introduces a relative competition score (RCS) that pinpoints latent separability by evaluating how strongly latent representations dominate the model's final output.
- This approach makes backdoor detection highly robust against adaptive attacks that intentionally obfuscate representational differences between benign and poisoned models.
- Zhang, Hanlei et al. "BARBIE: Robust Backdoor Detection Based on Latent Separability." NDSS (2026) — https://www.ndss-symposium.org/ndss-paper/barbie-robust-backdoor-detection-based-on-latent-separability/

## Be Careful of What You Embed: Demystifying OLE Vulnerabilities

- Object Linking & Embedding (OLE) allows composite documents across Microsoft Office (such as an Excel sheet inside a Word file), which streamlines interchange but complicates security.
- The fundamental design of OLE blurs the trust boundary between the host document and the embedded object, exposing structural weaknesses that can be weaponized.
- The work dissects these inherent OLE vulnerabilities, demonstrating how adversaries leverage the specification to bypass traditional document security filters.
- Tian, Yunpeng et al. "Be Careful of What You Embed: Demystifying OLE Vulnerabilities." NDSS (2026) — https://www.ndss-symposium.org/ndss-paper/be-careful-of-what-you-embed-demystifying-ole-vulnerabilities/

## Benchmarking and Understanding Safety Risks in AI Character Platforms

- Platforms providing conversations with personalized AI personas are widely adopted, but their immersive nature paired with technical vulnerabilities introduces significant risks to end users.
- A large-scale evaluation using 5,000 questions across 16 safety categories measured the safety performance across 16 different popular AI character platforms.
- AI character platforms demonstrated a 65.1% unsafe response rate—markedly higher than the 17.7% baseline for standard LLM interfaces—showing a vast disparity in safety across different personas.
- Wei, Yiluo et al. "Benchmarking and Understanding Safety Risks in AI Character Platforms." NDSS (2026) — https://www.ndss-symposium.org/ndss-paper/benchmarking-and-understanding-safety-risks-in-ai-character-platforms/

## Better Safe than Sorry: Uncovering the Insecure Resource Management in App-in-App Cloud Services

- Modern super-apps offer cloud spaces and identity management for embedded mini-apps, removing the need for third-party developers to operate their own backend servers.
- This app-in-app architecture frequently mishandles resource management and authorization checks when mini-apps attempt to store and access sensitive user information like home addresses and medical records.
- The research uncovers systemic insecurities in how super-apps partition cloud resources, allowing malicious or compromised mini-apps to potentially breach broader user data stored in the super-app ecosystem.
- Shi, Yizhe et al. "Better Safe than Sorry: Uncovering the Insecure Resource Management in App-in-App Cloud Services." NDSS (2026) — https://www.ndss-symposium.org/ndss-paper/better-safe-than-sorry-uncovering-the-insecure-resource-management-in-app-in-app-cloud-services/
