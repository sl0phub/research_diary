import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'automation/scripts'))
import re
import postparse

with open("content/arxiv/2026-09-25-arxiv-brief.md", "r") as f:
    body = f.read()

sections = postparse.split_sections(body)
entries = {str(i): t for i, (_, t) in enumerate(sections)}
also_published_text = entries['9']

print("All quoted items:")
for q in re.findall(r'"([^"]{8,})"', also_published_text):
    print("  ", q)
