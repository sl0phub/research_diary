import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'automation/scripts'))
import linkcheck

with open("content/arxiv/2026-09-25-arxiv-brief.md", "r") as f:
    for line in f:
        if 'BRFID' in line:
            print("FOUND BRFID:", line.strip())
