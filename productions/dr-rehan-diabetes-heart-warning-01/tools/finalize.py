"""Index existing deliverables, keeping design counts distinct from derivatives."""
from pathlib import Path
import json,csv,hashlib,xml.etree.ElementTree as ET,platform
from PIL import Image, __version__ as pillow_version
p=Path(__file__).resolve().parents[1]
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def write_csv(name,rows):
 with (p/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
reg=list(csv.DictReader((p/'ASSET_REGISTER.csv').open()))
for r in reg:r['png_sha256']=sha(p/r['png'])
write_csv('ASSET_REGISTER.csv',reg)
lookup={r['asset_id']:r for r in reg};parts=[]
pivots={'legs':[285,649],'torso':[285,445],'arm-left':[200,470],'arm-right':[365,470],'head':[285,425],'eyes-brows':[285,278],'mouth':[284,354]}
for f in sorted((p/'assets/parts').glob('*.svg')):
 parent,part=f.stem.split('--');order=['legs','torso','arm-left','arm-right','head','eyes-brows','mouth'].index(part)
 png=p/'exports/assets/parts'/f.with_suffix('.png').name
 parts.append(dict(part_id=f.stem,parent_asset_id=parent,part=part,width=600,height=900,x=0,y=0,z=order,anchor=json.dumps(pivots[part]),transparency='alpha',source=str(f.relative_to(p)),png=str(png.relative_to(p)),source_sha256=sha(f),png_sha256=sha(png),dependencies=parent,variant=lookup[parent]['variant'],interaction='Preserve parent pose; do not detach hand from sleeve',design_count=0))
write_csv('PART_REGISTER.csv',parts)
h=json.loads((p/'KEYFRAME_HANDOFF.json').read_text());script=(p/'ORIGINAL_TRANSCRIPT.txt').read_text()
prev=None
for st in h['states']:
 phrase=st['script_words'];start=script.index(phrase);st['script_span']={'start_char':start,'end_char_exclusive':start+len(phrase),'unit':'Unicode code points; not audio timestamps'}
 st['narration_status']='OWNER_TRANSCRIPT_UNVERIFIED_AUDIO'
 st['minimum_hold_frames_at_30fps']=round(st['minimum_hold_seconds']*30)
 st['source']='scenes/'+st['state_id']+'.svg';st['source_sha256']=sha(p/st['source'])
 st['preview']='exports/scenes/'+st['state_id']+'.png';st['preview_sha256']=sha(p/st['preview'])
 prior={i['asset_id'] for i in prev['layers']} if prev and prev['scene_id']==st['scene_id'] else set()
 diagram=0
 for i in st['layers']:
  r=lookup[i['asset_id']];i['source']=r['source'];i['png']=r['png'];i['source_sha256']=r['source_sha256'];i['png_sha256']=r['png_sha256'];i['contact_points_local']=json.loads(r['contact_points']);i['transparency']=r['transparency']
  i['reuse_from_previous_state']=i['asset_id'] in prior
  i['suggested_entry_frame']=0
  if i['operation']=='DIAGRAM_BUILD':diagram+=1;i['suggested_entry_frame']=18*diagram
  elif i['operation'] in ('SLIDE_IN','POP_IN'):i['suggested_entry_frame']=12
  i['transition_duration_frames']=h['recipes'][i['operation']]['frames']
  i['dependencies']=[]
  if i['asset_id']=='MED-coronary-overlay':i['dependencies']=['MED-heart-anterior']
  if i['asset_id'] in ('MED-plaque','MED-flow'):i['dependencies']=['MED-artery-wall']
  if i['asset_id']=='PROP-glucose-kit':i['dependencies']=['CH-diabetes-hold-neutral-front'];i['interaction_parent']='CH-diabetes-hold-neutral-front'
  if i['asset_id']=='CH-diabetes-sit-concerned-front':i['dependencies']=['PROP-chair'];i['interaction_parent']='PROP-chair'
 prev=st
h['parts_register']='PART_REGISTER.csv';h['original_transcript_sha256']=sha(p/'ORIGINAL_TRANSCRIPT.txt')
(p/'KEYFRAME_HANDOFF.json').write_text(json.dumps(h,indent=2)+'\n')
# Synchronize placement map with dependency contract, preserving exact fields and hashes.
rows=[]
for st in h['states']:
 for i in st['layers']:
  rows.append(dict(scene_id=st['scene_id'],state_id=st['state_id'],**{k:json.dumps(v) if isinstance(v,(list,dict)) else v for k,v in i.items()}))
# union fields permits interaction_parent only on contacted assets
fields=list(dict.fromkeys(k for r in rows for k in r));rows=[{k:r.get(k,'') for k in fields} for r in rows];write_csv('SCENE_ASSET_MAP.csv',rows)
counts={'character_identities':len({r['authored_design_family'] for r in reg if r['kind']=='character_variant'}),'character_pose_expression_composites':sum(r['kind']=='character_variant' for r in reg),'environment_designs':len({r['authored_design_family'] for r in reg if r['kind']=='environment_layer'}),'environment_layer_files':sum(r['kind']=='environment_layer' for r in reg),'medical_designs':len({r['authored_design_family'] for r in reg if r['kind'].startswith('medical')}),'medical_layer_files':sum(r['kind'].startswith('medical') for r in reg),'prop_designs':sum(r['kind']=='prop' for r in reg),'emphasis_designs':sum(r['kind']=='emphasis' for r in reg),'text_layouts':sum(r['kind']=='text' for r in reg),'stage_fields':sum(r['kind']=='stage' for r in reg),'primary_asset_sources':len(reg),'derived_character_parts':len(parts),'scene_groups':len({s['scene_id'] for s in h['states']}),'composed_visual_states':len(h['states']),'svg_files_total':len(list(p.rglob('*.svg'))),'png_asset_exports':len(list((p/'exports/assets').rglob('*.png'))),'png_scene_exports':len(list((p/'exports/scenes').glob('*.png'))),'scene_review_sheets':len(list((p/'reviews').glob('S*.png')))}
counts['original_illustration_designs_excluding_text_stages_poses_and_parts']=sum(counts[k] for k in ['character_identities','environment_designs','medical_designs','prop_designs','emphasis_designs'])
(p/'DELIVERY_COUNTS.json').write_text(json.dumps(counts,indent=2)+'\n')
progress=json.loads((p/'PRODUCTION_PROGRESS.json').read_text());progress.update(status='ASSET_PACKAGE_READY_FOR_OWNER_REVIEW',publication_status='SCRIPT_APPROVAL_REQUIRED',clinical_status='SOURCE_REVIEWED_CLINICIAN_APPROVAL_PENDING',native_qa='SAMPLED_NATIVE_REVIEW',mobile_qa='ALL_18_STATES_REVIEWED_AT_360x640',ending_status='EDITORIAL_PLACEHOLDER_NOT_PUBLISHABLE',counts=counts)
(p/'PRODUCTION_PROGRESS.json').write_text(json.dumps(progress,indent=2)+'\n')
# No timestamps in integrity hashes: byte changes, not wall time, drive revisions.
files=[]
for f in sorted(p.rglob('*')):
 if f.is_file() and f.name!='SOURCE_MANIFEST.json' and '__pycache__' not in f.parts:
  files.append(dict(path=str(f.relative_to(p)),bytes=f.stat().st_size,sha256=sha(f)))
(p/'SOURCE_MANIFEST.json').write_text(json.dumps({'scope':'all delivery files except this manifest; no competitor imagery','files':files},indent=2)+'\n')
print(json.dumps(counts,indent=2))
