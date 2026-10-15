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
