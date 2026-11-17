#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,re,sys,csv
R=Path(__file__).resolve().parent
M=json.loads((R/'SOURCE_PROMPT_MANIFEST.json').read_text())
errors=[]
for item in M['sources']:
 p=R/item['bundled_path']
 if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=item['sha256'] or p.stat().st_size!=item['bytes']:
  errors.append('Original uploaded prompt mismatch: '+str(p))
assert len(M['sources'])==4
S=R/'.claude/skills/visual-ct-scan/SKILL.md'
raw=S.read_text()
if not re.search(r'^---\nname: visual-ct-scan\ndescription: ',raw): errors.append('Invalid skill frontmatter')
for i in range(1,15):
 refs=list((R/'.claude/skills/visual-ct-scan/references').glob(f'{i:02d}_*.md'))
 if len(refs)!=1 or refs[0].stat().st_size<150:errors.append('Missing reference '+str(i))
for f in (R/'.claude/skills/visual-ct-scan/templates').iterdir():
 if not f.stat().st_size:errors.append('Empty template '+str(f))
 if f.suffix=='.json':json.loads(f.read_text())
 if f.suffix=='.csv': list(csv.reader(f.open()))
for trigger in ['CT_SCAN','DEEP','INVENTORY','STRUCTURAL','RECONSTRUCTION','CHANNEL_DNA']:
 if trigger not in raw:errors.append('Missing mode '+trigger)
for f in [R/'INSTALL_README.md',R/'MASTER_INSTALL_PROMPT_FOR_CLAUDE.md',R/'SKILL_INVOCATION_EXAMPLES.md']:
 if not f.exists() or f.stat().st_size<100: errors.append('Missing install document '+str(f))
print(json.dumps({'status':'PASS' if not errors else 'FAIL','four_uploaded_source_prompts_hash_verified':len(M['sources']),'reference_modules':14,'template_files':len(list((R/'.claude/skills/visual-ct-scan/templates').iterdir())),'errors':errors},indent=2))
sys.exit(1 if errors else 0)
