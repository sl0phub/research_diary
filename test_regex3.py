import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'automation/scripts'))
import re
import postparse

with open("content/arxiv/2026-09-25-arxiv-brief.md", "r") as f:
    body = f.read()

sections = postparse.split_sections(body)
entries = {str(i): t for i, (_, t) in enumerate(sections)}

also_published_text = entries['9'] # Assuming index 9 is also published
quoted = re.findall(r'"([^"]{8,})"', also_published_text)

import linkcheck
ident = "2609.28488"
real_titles = linkcheck.arxiv_titles([ident])
real_title = real_titles.get(ident)

for q in quoted:
    match = linkcheck.titles_match(q.rstrip("."), real_title)
    if match:
        print(f"FOUND MATCH! '{q}' vs '{real_title}'")
