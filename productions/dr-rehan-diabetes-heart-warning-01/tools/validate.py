"""Focused delivery integrity checks; no medical or artistic sign-off implied."""
from pathlib import Path
import csv,json,hashlib,re,xml.etree.ElementTree as ET
from PIL import Image
p=Path(__file__).resolve().parents[1]
reg=list(csv.DictReader((p/'ASSET_REGISTER.csv').open()));ids={r['asset_id'] for r in reg};assert len(ids)==len(reg)
for r in reg:
 f=p/r['source'];assert f.exists(),f
 assert hashlib.sha256(f.read_bytes()).hexdigest()==r['source_sha256']
 root=ET.parse(f).getroot();Image.open(p/r['png']).verify()
 im=Image.open(p/r['png']);assert im.size==(int(r['width']),int(r['height']))
 assert im.mode=='RGBA', (f,im.mode)
 if r['transparency']=='alpha':assert im.getextrema()[3][0]==0,(f,'missing transparency')
for st in json.loads((p/'KEYFRAME_HANDOFF.json').read_text())['states']:
 f=p/'scenes'/f'{st["state_id"]}.svg';root=ET.parse(f).getroot()
 nodeids=[e.attrib['id'] for e in root.iter() if 'id' in e.attrib];assert len(nodeids)==len(set(nodeids))
 for layer in st['layers']:
  assert layer['asset_id'] in ids;assert layer['layer_id'] in nodeids
 assert (p/'exports/scenes'/f'{st["state_id"]}.png').exists()
for f in p.rglob('*'):
 if f.is_file():
  assert f.stat().st_size<20_000_000,(f,'oversize')
  assert f.suffix.lower() not in ('.mp4','.mp3','.mov','.wav'),f
  if f.suffix in ('.md','.json','.csv','.py','.mjs','.txt','.svg'):
   s=f.read_text();assert not re.search(r'\b(?:ghp_[A-Za-z0-9]{30,}|sk-proj-[A-Za-z0-9_-]{30,}|AKIA[A-Z0-9]{16})',s),f
maps=list(csv.DictReader((p/'SCENE_ASSET_MAP.csv').open()))
board=list(csv.DictReader((p/'FULL_STORYBOARD.csv').open()))
for st in json.loads((p/'KEYFRAME_HANDOFF.json').read_text())['states']:
 expected={x['layer_id'] for x in st['layers']}
 assert expected=={r['layer_id'] for r in maps if r['state_id']==st['state_id']}
 assert expected==set(next(r['layer_ids'] for r in board if r['state_id']==st['state_id']).split(';'))
assert (p/'PROVISIONAL_STORYBOARD.csv').read_bytes()==(p/'FULL_STORYBOARD.csv').read_bytes()
print(f'PASS: {len(reg)} asset sources, {len(maps)} scene layers; PNG dimensions/alpha, hashes, IDs, map/storyboard agreement, file sizes and focused secret scan')
if (p/'PART_REGISTER.csv').exists():
 for r in csv.DictReader((p/'PART_REGISTER.csv').open()):
  assert r['parent_asset_id'] in ids
  for name,key in [('source','source_sha256'),('png','png_sha256')]:assert hashlib.sha256((p/r[name]).read_bytes()).hexdigest()==r[key],r['part_id']
  im=Image.open(p/r['png']);assert im.size==(600,900) and im.mode=='RGBA'
 h=json.loads((p/'KEYFRAME_HANDOFF.json').read_text());script=(p/'ORIGINAL_TRANSCRIPT.txt').read_text();covered=set()
 for st in h['states']:
  span=st['script_span'];a,b=span['start_char'],span['end_char_exclusive'];assert script[a:b]==st['script_words'];covered.update(range(a,b))
  present={i['asset_id'] for i in st['layers']}
  for layer in st['layers']:assert set(layer['dependencies'])<=present
 assert all(c.isspace() or i in covered for i,c in enumerate(script)), 'unmapped narration'
 assert h['original_transcript_sha256']==hashlib.sha256((p/'ORIGINAL_TRANSCRIPT.txt').read_bytes()).hexdigest()
 manifest=json.loads((p/'SOURCE_MANIFEST.json').read_text())
 for r in manifest['files']:assert hashlib.sha256((p/r['path']).read_bytes()).hexdigest()==r['sha256'],r['path']
 actual={str(f.relative_to(p)) for f in p.rglob('*') if f.is_file() and f.name!='SOURCE_MANIFEST.json' and '__pycache__' not in f.parts}
 assert actual=={r['path'] for r in manifest['files']},'unmanifested file'
 print(f'PASS: all {len(manifest["files"])} payload hashes; part parents; dependency closure; 100% non-whitespace transcript coverage')
# Character identity invariant: pose changes cannot silently change head shell or clothes.
families={}
for r in reg:
 if r['kind']=='character_variant':
  root=ET.parse(p/r['source']).getroot();fixed=tuple(ET.tostring(next(e for e in root if e.attrib.get('id')==name)) for name in ['head','torso'])
  family=r['authored_design_family']
  if family in families:assert fixed==families[family],f'identity drift: {r["asset_id"]}'
  else:families[family]=fixed
required=['README.md','ORIGINAL_TRANSCRIPT.txt','SCRIPT_ISSUES.md','MEDICAL_CLAIMS_QA.md','REFERENCE_EVIDENCE.md','STYLE_GUIDE.md','CHARACTER_BIBLE.md','FULL_STORYBOARD.csv','PROVISIONAL_STORYBOARD.csv','ASSET_REGISTER.csv','SCENE_ASSET_MAP.csv','KEYFRAME_HANDOFF.json','FULL_ASSET_CONTACT_SHEET.png','ASSET_QA.md','PRODUCTION_PROGRESS.json','CLAUDE_ANIMATION_HANDOFF.md','RESUME_HERE.md']
assert all((p/f).exists() for f in required),'missing required deliverable'
print(f'PASS: {len(families)} consistent character identities and all required deliverables')
