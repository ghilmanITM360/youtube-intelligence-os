#!/usr/bin/env python3
"""Static demo: parse the SKILL.md routing table and show which mode each owner phrase selects."""
import re, sys
from pathlib import Path
raw = (Path(sys.argv[1])/'.claude/skills/visual-ct-scan/SKILL.md').read_text()
desc = re.search(r'description: "([^"]+)"', raw).group(1).lower()
rows = re.findall(r'^\| (.+?) \| (.+?) \|$', raw.split('## Trigger')[1], re.M)[1:]
table = [([q.strip('" ').lower() for q in a.split('", "')], b) for a, b in rows]
tests = ['visual forensics', 'CT scan', 'deeper visual analysis', 'motion reconstruction', 'frame-by-frame investigation', 'channel visual DNA']
ok = True
for t in tests:
    hit = [(k, m) for ks, m in table for k in ks if k.strip('"') in t.lower() or t.lower() in k]
    print(f'{t!r:40} -> {hit[0][1] if hit else "NO MATCH"}'); ok &= bool(hit)
for kw in ['forensic', 'ct scan', 'deep visual', 'frame by frame', 'scene by scene']:
    print(f'description trigger {kw!r}:', kw in desc); ok &= kw in desc
sys.exit(not ok)
