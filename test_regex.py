import re

text = """- Ayush Jain, Sreeharsha Paruchuri, Ishita Gupta, Fan Zhang, Tanner Schmidt, Jakob Engel, Katerina Fragkiadaki, Adam W. Harley. "TrackEverything: Long Horizon Dense Tracking via De-Duplicating 3D Scene Representations." arXiv:2609.30222 — https://arxiv.org/abs/2609.30222
- Lokesh Chauhan. "IaC-Guard-V: A Verification Framework for LLM-Generated Infrastructure-as-Code Repairs." arXiv:2609.28488 — https://arxiv.org/abs/2609.28488"""

print(re.findall(r'"([^"]{8,})"', text))
