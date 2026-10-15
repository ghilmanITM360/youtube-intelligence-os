"""Focused artifact integrity checks; never certifies clinical truth or human listening."""
from pathlib import Path
import json,hashlib,xml.etree.ElementTree as ET,math,subprocess
from PIL import Image
R=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,d):p.write_text(json.dumps(d,indent=2))
errors=[];results=[]
def check(test,msg):
 if not test:errors.append(msg)
manifest=json.loads((R/'INPUT_MANIFEST.json').read_text())
for m in manifest:check(Path(m['path']).is_file() and sha(Path(m['path']))==m['sha256'],'Source changed/missing: '+m['path'])
z=json.loads((R/'ZIP_MANIFEST.json').read_text());check(len(z)==24,'ZIP disposition count');check(all(x['disposition'] in ('REFERENCE_ONLY','NOISE') for x in z),'ZIP unsafe/disposition')
for P in sorted(R.glob('0*')):
 before=len(errors);plan=json.loads((P/'animation_plan/KEYFRAME_PLAN.json').read_text());reg=json.loads((P/'assets/ASSET_REGISTER.json').read_text());ids={a['asset_id'] for a in reg};check(len(ids)==len(reg),P.name+' duplicate assets')
 previous=0;allwords=[];count_obj=0
 for s in plan['scenes']:
  check(s['in_frame']==previous,P.name+' frame gap '+s['scene_id']);check(s['out_frame_exclusive']>s['in_frame'],P.name+' empty scene');previous=s['out_frame_exclusive'];allwords.append(s['narration_verbatim_asr'])
  for o in s['objects']:
   count_obj+=1;check(o['asset_id'] in ids,'Missing asset '+o['asset_id']);ks=o['keyframes'];check(all(s['in_frame']<=k['frame']<s['out_frame_exclusive'] for k in ks),'Keyframe bounds');check(all(a['frame']<=b['frame'] for a,b in zip(ks,ks[1:])),'Keyframe order');check(ks[-1]['opacity']==1,'No visible end')
   a=next(a for a in reg if a['asset_id']==o['asset_id']);k=ks[-1];check(k['x']>=0 and k['y']>=0 and k['x']+a['width']*k['scale']<=1080 and k['y']+a['height']*k['scale']<=1920,'Canvas bounds '+P.name+' '+s['scene_id']+' '+o['asset_id'])
  for t in s['fixed_text_layers']:check(t['asset_id'] in ids,'Missing label')
 check(previous==plan['duration_frames'],'Tail coverage')
 asr=json.loads((P/'script/ASR_SMALL_EN.json').read_text());words=[w for seg in asr['segments'] for w in seg['words']]
 check(' '.join(' '.join(allwords).split())==' '.join(''.join(w['word'] for w in words).split()),P.name+' ASR narration omitted/reordered')
 hashes=[];pngs=0;parts=0
 for a in reg:
  files=[a]+a['layers'];parts+=len(a['layers'])
  for item in files:
   p=P/item['svg'];node=ET.parse(p).getroot();xmlids=[n.attrib['id'] for n in node.iter() if 'id' in n.attrib];check(len(xmlids)==len(set(xmlids)),'Duplicate SVG IDs '+str(p));check(not any('href' in k for n in node.iter() for k in n.attrib),'External asset link '+str(p))
   q=P/item['png'];im=Image.open(q);im.load();pngs+=1;check(im.size==(a['width'],a['height']),'PNG dimensions '+str(q));check(im.mode=='RGBA','PNG not RGBA '+str(q));check(im.getchannel('A').getextrema()==(0,255),'No transparent margin '+str(q));check(im.getbbox() is not None,'Empty image '+str(q))
   for f in [p,q]:hashes.append({'path':str(f.relative_to(P)),'bytes':f.stat().st_size,'sha256':sha(f)})
 for s in plan['scenes']:
  for state in ('start','mid','end'):
   for ext in ('svg','png'):
    p=P/'scene_states'/f'{s["scene_id"]}_{state}.{ext}';check(p.is_file(),'Missing state '+str(p))
    if ext=='png':im=Image.open(p);im.load();check(im.size==(1080,1920),'Scene dimensions')
    else:ET.parse(p)
    hashes.append({'path':str(p.relative_to(P)),'bytes':p.stat().st_size,'sha256':sha(p)})
 dump(P/'assets/FILE_HASHES.json',hashes)
 source=next(m for m in manifest if m.get('package')==P.name)
 # Both streams decoded to the same signed 24-bit PCM; confirms no duration/speed/voice edits.
 dig=[]
 for f in [source['path'],str(P/'source_audio/narration_mix.wav')]:
  dig.append(subprocess.check_output(['ffmpeg','-v','error','-i',f,'-map','0:a:0','-c:a','pcm_s24le','-f','hash','-hash','sha256','-'],text=True).strip())
 check(dig[0]==dig[1],P.name+' audio PCM mismatch')
 result={'package':P.name,'structural_status':'PASS' if len(errors)==before else 'FAIL','publication_status':'QA_BLOCKED','scenes':len(plan['scenes']),'source_duration_seconds':plan['duration_seconds'],'full_assets_including_labels':len(reg),'unique_base_design_ids_excluding_text':len({a['design_id'] for a in reg if a['category']!='label'}),'character_pose_variants':len([a for a in reg if a['category']=='character']),'label_exports':len([a for a in reg if a['category']=='label']),'component_exports_per_format':parts,'png_exports_assets_and_parts':pngs,'svg_exports_assets_and_parts':pngs,'scene_states_per_format':len(plan['scenes'])*3,'asset_instances':count_obj,'source_words_machine_aligned':len(words),'decoded_pcm_sha256_match':dig[0]==dig[1],'errors':errors[before:],'limits':['No human listening certification','No clinician signoff','Static scene/asset review only; no final animation rendered','Original style adaptation, not competitor parity certification']}
 dump(P/'qa/VALIDATION.json',result);results.append(result)
status={'status':'QA_BLOCKED','artifact_stage':'THREE_DRAFT_ASSET_PACKAGES_BUILT','source_integrity':'PASS' if not any('Source changed' in e for e in errors) else 'FAIL','structural_status':'PASS' if not errors else 'FAIL','packages':results,'errors':errors}
dump(R/'PRODUCTION_STATUS.json',status)
print(json.dumps({'structural_status':status['structural_status'],'publication_status':status['status'],'packages':[{k:r[k] for k in ['package','scenes','full_assets_including_labels','component_exports_per_format','source_words_machine_aligned']} for r in results],'errors':errors},indent=2))
raise SystemExit(bool(errors))
