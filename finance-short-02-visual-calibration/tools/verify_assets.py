"""Meaningful source/dependency/semantic validation; art approval remains human."""
from pathlib import Path
import argparse,base64,csv,hashlib,json,re,subprocess,xml.etree.ElementTree as ET
from decimal import Decimal
from PIL import Image
R=Path(__file__).resolve().parents[1];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();NS='{http://www.w3.org/2000/svg}'
def verify(require_complete=False):
 approved=R/'editable_sources/original/APPROVED_NARRATION.txt';assert sha(approved)=='a43916ce5eed6eacd1fbc1ce49bcf0c0143e165521303e12f0fdb203b2d3be0b';assert len(approved.read_text().split())==147
 assert Decimal('3000000000000')*Decimal('0.0025')==Decimal('7500000000')
 states=list(csv.DictReader((R/'FULL_STORYBOARD.csv').open()));assert len(states)==36 and len({s['scene_id'] for s in states})==7
 assert float(states[0]['provisional_start_sec'])==0 and float(states[-1]['provisional_end_sec'])==53
 for x,y in zip(states,states[1:]):assert float(x['provisional_end_sec'])==float(y['provisional_start_sec'])
 assert sum(s['cut_at_start']=='True' for s in states)==5
 assets=list(csv.DictReader((R/'ASSET_REGISTER.csv').open()));ids={r['asset_id'] for r in assets};assert len(ids)==len(assets)
 maps=list(csv.DictReader((R/'SCENE_ASSET_MAP.csv').open()));exports=json.loads((R/'manifests/EXPORT_HASHES.json').read_text());crop_hashes={x['sha256'] for x in json.loads((R/'ARTICLE_EVIDENCE/CROP_MANIFEST.json').read_text())}
 parsed=0;decoded=0;embedded=0
 for r in assets:
  f=R/r['filename'];assert f.exists() and sha(f)==r['sha256'];root=ET.parse(f).getroot();allids=[e.get('id') for e in root.iter()];assert len(allids)==len(set(allids)) and None not in allids
  assert root.get('data-asset-id')==r['asset_id'];assert not root.findall('.//'+NS+'text'),'Production artwork must use portable original lettering'
  image=R/r['png_export'];assert image.exists() and sha(image)==r['png_sha256']==exports[r['asset_id']]['png_sha256'];assert sha(f)==exports[r['asset_id']]['source_sha256']
  with Image.open(image) as im:
   im.verify()
  im=Image.open(image);assert im.size==(round(float(r['width'])),round(float(r['height'])))
  if r['transparency']=='transparent_background' and r['classification']!='DOCUMENTARY_CROP':assert im.mode=='RGBA' and im.getchannel('A').getextrema()==(0,255),r['asset_id']
  for img in root.iter(NS+'image'):
   href=img.get('href') or img.get('{http://www.w3.org/1999/xlink}href');assert href.startswith('data:image/png;base64,');assert hashlib.sha256(base64.b64decode(href.split(',',1)[1])).hexdigest() in crop_hashes;embedded+=1
  if r['classification'] not in ['DOCUMENTARY_CROP','CANVAS']:
   box=im.getchannel('A').getbbox();assert box[0]>0 and box[1]>0 and box[2]<im.width and box[3]<im.height,('edge clipping',r['asset_id'],box)
  parsed+=1;decoded+=1
 authored=[s for s in states if s['art_status']=='AUTHORED']
 for s in authored:
  assert set(s['required_asset_ids'].split(';'))<=ids
  root=ET.parse(R/'assets/scene_compositions'/ (s['state_id']+'.svg')).getroot();actual={n.get('id'):n.get('data-asset-id') for n in root};mapped={x['layer_id']:x['asset_id'] for x in maps if x['state_id']==s['state_id']};assert actual==mapped
  assert all(float(x['scale'])>0 and 0<=float(x['x_normalized'])<=1 and 0<=float(x['y_normalized'])<=1 for x in maps if x['state_id']==s['state_id'])
  assert len([x for x in maps if x['state_id']==s['state_id']])==len(root)
  with Image.open(R/'assets/exports'/ (s['state_id']+'_320.png')) as im:assert im.size==(320,569);im.verify()
  parsed+=1;decoded+=1
 # Semantic constraints survive source edits because relevant phrases are actual assets.
 txt=' '.join((ET.parse(R/r['filename']).getroot().get('data-text') or '') for r in assets)
 for scene in [3,5,6,7]:
  if any(s['scene_id']==f'SCENE_{scene:02d}' for s in authored):
   phrase={3:'IF RESERVES STAY THE SAME',5:'NOT CREATED BY THIS HIKE ALONE',6:'UNTIL EARNINGS COVER THE BALANCE',7:'CAN MAKE REPAIR HARDER'}[scene];assert phrase in txt,phrase
 if require_complete:assert len(authored)==36;assert len(list((R/'manifests').glob('SCENE_??.json')))==7
 # Actual metadata/raw pixels remain unchanged; never certify a fake source crop.
 from PIL import ImageChops
 crops=json.loads((R/'ARTICLE_EVIDENCE/CROP_MANIFEST.json').read_text())
 for c in crops:
  assert sha(R/c['file'])==c['sha256'] and sha(R/c['source'])==c['source_sha256']
  assert Image.open(R/c['source']).crop(c['box_xyxy']).convert('RGB').tobytes()==Image.open(R/c['file']).convert('RGB').tobytes()
 git_result=subprocess.run(['git','ls-files','-z','--',str(R)],cwd=R.parent,capture_output=True)
 tracked=git_result.stdout.decode().split('\0') if git_result.returncode==0 else [str(f.relative_to(R)) for f in R.rglob('*') if f.is_file()]
 assert not any('/references/' in f or 'VISUAL_COMPARISON' in f or 'HOST_CONCEPT' in f or f.endswith(('.zip','.mp4','.mp3','.mov')) for f in tracked)
 # Interaction anchor and consistent anatomy checks, independent of source generation.
 data={r['asset_id']:r for r in json.loads((R/'manifests/ASSET_DATA.json').read_text())}
 def world(layer,anchor):
  point=data[layer['asset_id']]['anchors'][anchor]
  return (float(layer['x'])+float(layer['scale'])*point[0],float(layer['y'])+float(layer['scale'])*point[1])
 contact_checks=0
 for state in ['S07_01','S07_02','S07_03','S07_04']:
  if any(x['state_id']==state for x in maps):
   layer={x['layer_id'].replace('SCENE_07_',''):x for x in maps if x['state_id']==state}
   host=world(layer['HOST'],'near_hand')
   for key,anchor in ([('SHIELD_GRIP','wrist'),('SHIELD','grip')] if state in ['S07_01','S07_02'] else [('TOOL_GRIP','wrist'),('WRENCH','handle')]):
    point=world(layer[key],anchor);assert sum((x-y)**2 for x,y in zip(point,host))**.5<2.5,(state,key,host,point);contact_checks+=1
 def signature(node):return [(e.tag,{k:v for k,v in e.attrib.items() if k!='id'}) for e in node.iter()]
 reference=None
 for r in assets:
  if r['classification']=='POSE_EXPRESSION_VARIANT':
   root=ET.parse(R/r['filename']).getroot(); anatomy=[signature(root[0]),signature(root[1]),*[signature(e) for e in list(root[3])[:3]]]
   if reference is None:reference=anatomy
   else:assert anatomy==reference,('anatomy drift',r['asset_id'])
  parts=json.loads(r['editable_subparts_json']);flat=[]
  for value in parts.values():flat.extend(value if isinstance(value,list) else [value])
  assert set(flat)<={e.get('id') for e in ET.parse(R/r['filename']).getroot().iter()}
 if require_complete:
  for n in ['FULL_ASSET_CONTACT_SHEET.png','PRODUCTION_CHARACTER_SHEET.png','ANIMATION_HANDOFF.md','CHARACTER_BIBLE.md','STYLE_GUIDE.md','RESUME_HERE.md']:
   assert (R/n).exists(),n
 report={'result':'PASS','approved_words':147,'script_sha256':sha(approved),'states_authored':len(authored),'states_planned':36,'scenes_authored':len({s['scene_id'] for s in authored}),'assets':len(assets),'actual_scene_layers':len(maps),'contact_anchor_checks':contact_checks,'host_anatomy_consistent':True,'transparent_asset_edges_unclipped':True,'SVGs_checked':parsed,'PNG_decodes_checked':decoded,'embedded_evidence_hashes_checked':embedded,'exact_pixel_crops':len(crops),'financial_decimal_calculation':'3000000000000 * 0.0025 = 7500000000','timing':'53 seconds PROVISIONAL','planned_cuts':5,'competitor_pixels_tracked':False,'human_art_approval':'PENDING','automated_tests_do_not_certify_art':True}
 (R/'manifests/VALIDATION.json').write_text(json.dumps(report,indent=2));print(json.dumps(report))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--complete',action='store_true');verify(p.parse_args().complete)
