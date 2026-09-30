import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'automation/scripts'))
import postparse
import re

with open("content/arxiv/2026-09-25-arxiv-brief.md", "r") as f:
    body = f.read()

sections = postparse.split_sections(body)
for h, t in sections:
    print(f"Heading: {h}")
    # print arxiv ids in this section
    ids = re.findall(r'2609\.\d{5}', t)
    print(f"  Contains {len(ids)} IDs")
