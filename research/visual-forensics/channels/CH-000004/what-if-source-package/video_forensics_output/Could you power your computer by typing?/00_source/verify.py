"""Run with python3; checks the saved forensic package without decoding again."""
from pathlib import Path
import csv,json,re
R=Path(__file__).resolve().parents[1]
def rows(p):return list(csv.DictReader((R/p).open()))
def frame(t):
 m,s=t.split(':');return round((int(m)*60+float(s))*24)
t=rows('02_analysis/TIMELINE.csv');a=rows('02_analysis/ASSET_MANIFEST.csv');m=rows('02_analysis/MOTION_EVENTS.csv')
states={x['STATE_ID']:x for x in t};assets={x['ASSET_ID'] for x in a};motions={x['MOTION_ID'] for x in m};shots=list(dict.fromkeys(x['SHOT_ID'] for x in t))
assert len(states)==len(t) and len(assets)==len(a) and len(motions)==len(m)
assert frame(t[0]['IN'])==0 and frame(t[-1]['OUT'])==2419
for i,r in enumerate(t):
 assert frame(r['IN'])<frame(r['OUT']),r
 assert abs(float(r['DURATION'])-(frame(r['OUT'])-frame(r['IN']))/24)<0.00001
 if i:assert r['IN']==t[i-1]['OUT'],r['STATE_ID']
 assert set(r['ASSET_IDS'].split(';'))<=assets
 assert set(filter(None,r['MOTION_IDS'].split(';')))<=motions
 assert list((R/'01_evidence/frames').glob(f'f{frame(r["IN"]):04d}_*.png')),r['STATE_ID']
valid={'SEQUENTIAL','SIMULTANEOUS_COUPLED','SIMULTANEOUS_INDEPENDENT','PERSISTENT_LOOP','CAMERA_SUBJECT_COUPLED','STATE_REPLACEMENT'}
for r in m:
 assert r['SOURCE_STATE'] in states and r['TARGET_STATE'] in states
 assert states[r['SOURCE_STATE']]['SHOT_ID']==r['SHOT_ID']==states[r['TARGET_STATE']]['SHOT_ID']
 assert r['RELATIONSHIP'] in valid and frame(r['IN'])<frame(r['OUT'])
 assert frame(states[r['SOURCE_STATE']]['IN'])<=frame(r['IN'])
 assert frame(states[r['TARGET_STATE']]['IN'])<frame(r['OUT'])
 assert any(r['MOTION_ID'] in x['MOTION_IDS'].split(';') for x in t),r['MOTION_ID']
 required=[x for x in t if x['SHOT_ID']==r['SHOT_ID']]
 assert frame(required[0]['IN'])<=frame(r['IN'])<frame(r['OUT'])<=frame(required[-1]['OUT'])
for p in ['03_capcut/CAPCUT_REBUILD.md','04_image_to_video/I2V_REBUILD.md']:
 text=(R/p).read_text();assert re.findall(r'^## (S\d+) —',text,re.M)==shots
cap=(R/'03_capcut/CAPCUT_REBUILD.md').read_text()
for aid in motions:assert re.search(r'\b'+aid+r'\b',cap),aid
anim=(R/'04_image_to_video/ANIMATION_PROMPTS.md').read_text()
blocks=re.split(r'^## (A\d+)\n',anim,flags=re.M)[1:]
assert set(blocks[0::2])==motions
for aid,block in zip(blocks[0::2],blocks[1::2]):
 p=block.split('ANIMATION PROMPT:\n',1)[1].strip();assert 0<len(p)<=500,(aid,len(p))
images=(R/'04_image_to_video/IMAGE_PROMPTS.md').read_text();imgids=set(re.findall(r'^## (IMG\d+)$',images,re.M));assert len(imgids)==18
assert images.count('TEXT BAKED: NO')==len(imgids)
# Check relative Markdown links, including every indexed evidence frame.
for p in R.rglob('*.md'):
 for dest in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if '://' not in dest and not dest.startswith('#'):
   assert (p.parent/dest.split('#')[0]).exists(),(str(p),dest)
metadata=json.loads((R/'00_source/metadata.json').read_text());assert len(metadata['streams'])==1 and metadata['streams'][0]['codec_type']=='video'
run=json.loads((R/'RUN_STATE.json').read_text());expected={'shots':len(shots),'visual_states':len(t),'unique_assets':len(a),'motion_events':len(m),'unique_images':len(imgids),'audio_assets':0};assert run['counts']==expected
print('PASS: timeline coverage, IDs, state evidence, both shot guides, all event recipes, prompt limits, file links, source stream facts and counts.')
