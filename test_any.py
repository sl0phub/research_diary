import sys
import os
import json
sys.path.append(os.path.join(os.getcwd(), 'automation/scripts'))
import linkcheck
import re
import postparse

ident = "2609.28488"
with open("content/arxiv/2026-09-25-arxiv-brief.md", "r") as f:
    body = f.read()

sections = postparse.split_sections(body)
entries = {str(i): t for i, (_, t) in enumerate(sections)}

wanted = {}
for label, entry in entries.items():
    for m in postparse.ARXIV_ID.finditer(entry):
        wanted.setdefault(m.group(1), []).append(entry)

contexts = wanted[ident]
quoted = [q for c in contexts for q in re.findall(r'"([^"]{8,})"', c)]

# wait, does quoted have the exact title?
print(f"Number of quoted items: {len(quoted)}")
print(f"Quoted[0]: {quoted[0]}")
# Is the actual title of 28488 in quoted?
found = False
for q in quoted:
    if "IaC" in q:
        print("FOUND IAC IN QUOTED: ", q)
        found = True

print("Was it found?", found)
