import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'automation/scripts'))
import linkcheck
import pathlib

findings = linkcheck.check_file(pathlib.Path("content/arxiv/2026-09-25-arxiv-brief.md"))
count = 0
for f in findings:
    if f.gating and count < 3:
        print("FAIL:", f.message)
        count += 1
