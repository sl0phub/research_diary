import re
import subprocess
import json

with open("overflow.json", "r") as f:
    overflow = json.load(f)

# we map id to true title from original JSON fetched
id_to_true_title = {sc['cand']['url'].split('/')[-1]: sc['cand']['title'] for sc in overflow}

with open("content/arxiv/2026-09-25-arxiv-brief.md", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.startswith('- ') and ' — https://arxiv.org/abs/' in line:
        arxiv_id = line.split(' — https://arxiv.org/abs/')[1].strip()
        if arxiv_id in id_to_true_title:
            true_title = id_to_true_title[arxiv_id]
            # Replace exactly the WRONG string "BRFID: Toward Byzantine-Robust Federated Intrusion Detection"
            # It's currently in all of these overflow items. Let's just find and replace it.
            wrong_title = "BRFID: Toward Byzantine-Robust Federated Intrusion Detection"
            # Wait, the wrong title could be anything.
            # I will just write a simple parsing based on the file formatting.
            parts = line.split('. "')
            if len(parts) >= 2:
                # the first part is `- Authors`
                authors = parts[0]
                lines[i] = f'{authors}. "{true_title.strip()}." arXiv:{arxiv_id} — https://arxiv.org/abs/{arxiv_id}\n'
            else:
                parts = line.split(' "')
                if len(parts) >= 2:
                    authors = parts[0]
                    lines[i] = f'{authors} "{true_title.strip()}." arXiv:{arxiv_id} — https://arxiv.org/abs/{arxiv_id}\n'

with open("content/arxiv/2026-09-25-arxiv-brief.md", "w") as f:
    f.writelines(lines)
