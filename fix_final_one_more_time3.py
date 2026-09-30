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
            true_title = id_to_true_title[arxiv_id].replace('\n', ' ').strip()

            # Since linkcheck expects EXACT title matching, let's look at what's between `"` and `." arXiv`
            # And replace whatever is inside with `true_title`. Wait, `true_title` might contain internal quotes!
            # Linkcheck literally expects `true_title` directly from the API. We have that in `sc['cand']['title']`.
            # Let's completely recreate the line and explicitly not strip double quotes.
            # But the overall format is: `- Authors. "Title." arXiv:ID — URL`

            parts = line.split(' "')
            if len(parts) >= 2:
                authors = parts[0]
                lines[i] = f'{authors} "{true_title}." arXiv:{arxiv_id} — https://arxiv.org/abs/{arxiv_id}\n'

with open("content/arxiv/2026-09-25-arxiv-brief.md", "w") as f:
    f.writelines(lines)
