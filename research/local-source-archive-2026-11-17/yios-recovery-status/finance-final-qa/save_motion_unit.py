from pathlib import Path
import csv,json,hashlib,sys
from PIL import Image
v=sys.argv[1];r=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os/data/extracted/forensic-analysis/casually-finance/2026-10-12');d=r/'02_VIDEO_FORENSICS'/v;o=Path('/Users/ghilmankhan/workprojects/yios-recovery-status/finance-final-qa')/(v+'-motion');obs=json.loads(Path(sys.argv[2]).read_text());meta=json.loads((o/'metadata.json').read_text());assert meta['video_id']==v
review_confidence='MODERATE for broad motion in192x108 recovered grayscale; color/fine text/audio/easing unverified' if 'gray.u8' in meta.get('method','') else 'HIGH for stated sampled observations; easing/audio/continuous playback not certified'
for p in sorted(o.glob('landscape-*.png') if list(o.glob('landscape-*.png')) else o.glob('review-*.png')):
 with Image.open(p) as im:im.save(d/'evidence'/('finalization-motion-'+p.stem.split('-')[-1]+'.jpg'),quality=88)
def write(p,rows):
 with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
old={x['motion_id']:x['original_label'] for x in csv.DictReader((r/'07_VALIDATION/MOTION_QA_DISPOSITION.csv').open()) if x['video_id']==v};cor={m:l for m,(l,n) in obs.items() if l and l!=old[m]};unknown={m for m,(l,n) in obs.items() if not l}
for p in [d/'MOTIONS.csv',r/'03_MASTER_DATA/MASTER_MOTIONS.csv']:
 rows=list(csv.DictReader(p.open()))
 for x in rows:
  if x['video_id']==v and x['motion_id'] in obs and x['motion_id'] not in unknown:
   mid=x['motion_id'];label,note=obs[mid];x['action_label']=label;x['observed_action']=note;x['label_vs_measure_check']='INDEPENDENT_SEQUENCE_REVIEW: '+('CORRECTED_LABEL' if mid in cor else 'CONFIRMED_EVENT_SCOPE');x['confidence']=review_confidence
   if mid in cor:x['tool_agnostic_reconstruction_method']='Recreate observed phases with original assets: '+note
 write(p,rows)
rows=list(csv.DictReader((r/'07_VALIDATION/MOTION_QA_DISPOSITION.csv').open()));order=list(obs)
for x in rows:
 if x['video_id']==v and x['motion_id'] in obs:
  mid=x['motion_id'];x.update(review_status='PARTIAL' if mid in unknown else 'COMPLETE_WITH_DOCUMENTED_LIMITATIONS',disposition='INSUFFICIENT_EVIDENCE' if mid in unknown else ('CORRECTED_LABEL' if mid in cor else 'CONFIRMED_EXISTING_LABEL'),evidence_reference=f'02_VIDEO_FORENSICS/{v}/evidence/finalization-motion-{order.index(mid)//5+1}.jpg',observed_behavior=obs[mid][1],confidence=review_confidence,remaining_dependency='Denser source sequence / earlier adjacent state review' if mid in unknown else 'Audio synchronization and easing uncertified')
write(r/'07_VALIDATION/MOTION_QA_DISPOSITION.csv',rows)
qa=json.loads((d/'QA.json').read_text());qa['counts']['label_vs_measure_conflicts']=sum(x['label_vs_measure_check'].startswith('LABEL_IMPLIES_') for x in csv.DictReader((d/'MOTIONS.csv').open()));qa['independent_motion_review']={'original_candidates':sum(x['video_id']==v for x in rows),'reviewed':sum(x['video_id']==v and bool(x['disposition']) for x in rows),'confirmed_existing_labels':sum(x['video_id']==v and x['disposition']=='CONFIRMED_EXISTING_LABEL' for x in rows),'corrected_labels':sum(x['video_id']==v and x['disposition']=='CORRECTED_LABEL' for x in rows),'insufficient_evidence':sum(x['video_id']==v and x['disposition']=='INSUFFICIENT_EVIDENCE' for x in rows),'scope':'Nine source samples per candidate at native-frame-adjacent start and distributed follow-on points; not continuous playback'};(d/'QA.json').write_text(json.dumps(qa,indent=1)+'\n')
meta['observations']=obs;meta['corrections']=cor;meta['insufficient_evidence']=sorted(unknown);meta['evidence_files']=[{'path':str(p.relative_to(r)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in (d/'evidence').glob('finalization-motion-*.jpg')];(r/'07_VALIDATION'/f'{v}_MOTION_REVIEW.json').write_text(json.dumps(meta,indent=2)+'\n');print(qa['independent_motion_review'])
