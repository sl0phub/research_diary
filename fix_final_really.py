import re
import subprocess
import json

res = subprocess.run(["python3", "automation/scripts/linkcheck.py", "--files", "content/arxiv/2026-09-25-arxiv-brief.md"], capture_output=True, text=True)
errors = res.stderr.split('\n')

id_to_true_title = {}
for err in errors:
    match = re.search(r'FAIL.*?arXiv:(.*?) is "(.*?)", not ', err)
    if match:
        arxiv_id = match.group(1).strip()
        true_title = match.group(2).strip()
        id_to_true_title[arxiv_id] = true_title

with open("content/arxiv/2026-09-25-arxiv-brief.md", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.startswith('- ') and 'arXiv:' in line:
        for arxiv_id, true_title in id_to_true_title.items():
            if f'arXiv:{arxiv_id} —' in line:
                # The line format is:
                # - Authors. "Title." arXiv:ID — URL
                parts = line.split('. "')
                if len(parts) >= 2:
                    authors_part = parts[0]
                    # We rebuild the entire line using the true_title
                    # The true_title might contain quotes, we must escape them.
                    safe_title = true_title.replace('"', '\\"')
                    lines[i] = f'{authors_part}. "{safe_title}." arXiv:{arxiv_id} — https://arxiv.org/abs/{arxiv_id}\n'
                    break

with open("content/arxiv/2026-09-25-arxiv-brief.md", "w") as f:
    f.writelines(lines)
