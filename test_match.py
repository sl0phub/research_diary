import sys
import os
import json
sys.path.append(os.path.join(os.getcwd(), 'automation/scripts'))
import linkcheck
import re

# `overflow.json` was deleted. I'll just use the arxiv API to fetch the real title.
ident = "2609.28488"
real_titles = linkcheck.arxiv_titles([ident])
real_title = real_titles.get(ident)

with open("content/arxiv/2026-09-25-arxiv-brief.md", "r") as f:
    body = f.read()

import postparse
sections = postparse.split_sections(body)

contexts = re.findall(rf"(?m)^.*{ident}.*$", body)
print(f"Contexts for {ident}: {contexts}")
quoted = [q for c in contexts for q in re.findall(r'"([^"]{8,})"', c)]
print(f"Extracted quotes: {quoted}")
quoted += [h for h, t in sections if ident in t]
print(f"Final quoted list: {quoted}")
print(f"Real title: {real_title}")

for q in quoted:
    match = linkcheck.titles_match(q.rstrip("."), real_title)
    print(f"Checking '{q}' vs '{real_title}': {match}")
