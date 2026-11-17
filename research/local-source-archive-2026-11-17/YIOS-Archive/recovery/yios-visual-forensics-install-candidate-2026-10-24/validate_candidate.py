#!/usr/bin/env python3
"""Validate an installed/candidate visual-ct-scan tree. Usage: validate_candidate.py <root containing .claude/>"""
import csv, hashlib, json, re, sys
from pathlib import Path
R = Path(sys.argv[1]); S = R/'.claude/skills/visual-ct-scan'; err = []
M = json.loads((S/'SOURCE_PROMPT_MANIFEST.json').read_text())
for i in M['sources']:
    p = S/i['bundled_path']
    if not p.exists() or p.stat().st_size != i['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest() != i['sha256']:
        err.append('prompt hash mismatch: '+i['bundled_path'])
raw = (S/'SKILL.md').read_text()
if not re.match(r'---\nname: visual-ct-scan\ndescription: "[^"]+"\n---\n', raw): err.append('frontmatter')
for n in range(1, 15):
    if len(list((S/'references').glob(f'{n:02d}_*.md'))) != 1: err.append(f'reference {n}')
for ref in re.findall(r'\]\((references/[^)]+)\)', raw):
    if not (S/ref).exists(): err.append('dead link '+ref)
for m in ['INVENTORY','STRUCTURAL','DEEP','CT_SCAN','RECONSTRUCTION','CHANNEL_DNA']:
    if m not in raw: err.append('mode '+m)
for f in (S/'templates').iterdir():
    if not f.stat().st_size: err.append('empty '+f.name)
    if f.suffix == '.json': json.loads(f.read_text())
    if f.suffix == '.csv': list(csv.reader(f.open()))
if len(list((S/'templates').iterdir())) != 7: err.append('template count')
cm = R/'CLAUDE.md'
if not cm.exists() or '.claude/skills/visual-ct-scan/SKILL.md' not in cm.read_text(): err.append('CLAUDE.md pointer')
idx = R/'docs/research/README.md'
if not idx.exists() or 'visual-ct-scan/SKILL.md' not in idx.read_text(): err.append('index link')
print(json.dumps({'status': 'FAIL' if err else 'PASS', 'errors': err}, indent=1)); sys.exit(bool(err))
