import re
import json

with open("content/arxiv/2026-09-25-arxiv-brief.md", "r") as f:
    lines = f.readlines()

new_lines = []
in_also_published = False
seen_brfid = False

for line in lines:
    if line.startswith('## Also published'):
        in_also_published = True
        new_lines.append(line)
        continue

    if in_also_published and line.startswith('- ') and ' — https://arxiv.org/abs/' in line:
        # If it's BRFID, skip it because it shouldn't be in Also published
        if 'BRFID' in line:
            continue

        # Parse it properly to avoid quote parity issues
        match = re.search(r'^(- .*?)[ \.]?["\'](.*?)["\']\.? arXiv:(.*?) — (.*)$', line)
        if match:
            authors = match.group(1).strip()
            title = match.group(2).strip()
            arxiv_id = match.group(3).strip()
            url = match.group(4).strip()

            if authors.endswith('.'):
                authors = authors[:-1]

            # If the title still has internal double quotes, replace them with single quotes
            title = title.replace('"', "'")

            # ensure no nested quotes at the boundary
            while title.startswith("'") or title.startswith('"'):
                title = title[1:]
            while title.endswith("'") or title.endswith('"'):
                title = title[:-1]

            new_line = f'{authors}. "{title}." arXiv:{arxiv_id} — {url}\n'
            new_lines.append(new_line)
        else:
            # simple fallback
            parts = line.split('"')
            if len(parts) >= 3:
                authors = parts[0].strip()
                if authors.endswith('.'):
                    authors = authors[:-1]
                title = "".join(parts[1:-1]).replace('"', "'")
                tail = parts[-1].strip()
                if tail.startswith('.'):
                    tail = tail[1:].strip()
                new_line = f'{authors}. "{title}." {tail}\n'
                new_lines.append(new_line)
            else:
                new_lines.append(line.replace('"', "'")) # just replace all to be safe
    else:
        new_lines.append(line)

with open("content/arxiv/2026-09-25-arxiv-brief.md", "w") as f:
    f.writelines(new_lines)
