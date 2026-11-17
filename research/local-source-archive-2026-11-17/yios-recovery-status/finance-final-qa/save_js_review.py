from pathlib import Path
import csv,json,hashlib
from PIL import Image
r=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os/data/extracted/forensic-analysis/casually-finance/2026-10-12');v='JsK53moCyZA';out=Path('/Users/ghilmankhan/workprojects/yios-recovery-status/finance-final-qa/JsK53moCyZA-motion');d=r/'02_VIDEO_FORENSICS'/v
for name in ['review','M0018-detail','M0032-detail','M0023-detail','M0034-detail']:
 with Image.open(out/(name+'.png')) as im: im.save(d/'evidence'/('finalization-'+name+'.jpg'),quality=85)
obs={
'M0015':'Caption changes from target valuation to SpaceX would be worth while character arms move; chart remains in place. TEXT_SWAP describes the text event, not the whole active-pixel interval.',
'M0017':'Caption changes from SpaceX would be worth to more than while character arms move. Existing text-swap label is valid at event scope.',
'M0018':'Second comparison bar is absent at 9.00000s and present at 9.03333s. Later character and caption changes explain extended activity; progressive left-to-right bar draw is not supported by adjacent native frames.',
'M0020':'Caption changes from every American to defense contractor combined while character arms move; bar layout persists. Existing text-swap label is valid at event scope.',
'M0023':'Native frames show abrupt replacement of bar layout and character placement between 11.70000 and 11.73333s. Subsequent caption replacement is included in the active interval.',
'M0032':'Abrupt replacement of consumer-brand comparison with London-listed company comparison between 17.23333 and 17.26667s; a head subsequently enters progressively from below. Label must include both phases. No chart draw-on or easing is certified.',
'M0034':'Chart composition persists through 21.46667s, then abruptly replaces with stick-figure host at 21.50000s; caption appears later. Existing CUT describes the scene reset.',
'M0046':'Host/angel/devil composition changes to 401k paper between 30.4333 and 30.4667s; paper subsequently enlarges through 32.9337s. Object enlargement is observed; camera movement and easing are not established.'}
cor={'M0032':'CUT_THEN_REVEAL_MOVE','M0046':'CUT_THEN_SCALE'}
def write(path,rows):
 with path.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
for path in [d/'MOTIONS.csv',r/'03_MASTER_DATA/MASTER_MOTIONS.csv']:
 rows=list(csv.DictReader(path.open()))
 for x in rows:
  if x['video_id']==v and x['motion_id'] in obs:
   mid=x['motion_id'];x['label_vs_measure_check']='INDEPENDENT_SEQUENCE_REVIEW: '+('CORRECTED_MULTIPHASE_LABEL' if mid in cor else 'CONFIRMED_EVENT_LABEL_WITH_CONCURRENT_ACTIVITY')
   x['observed_action']=obs[mid];x['confidence']='HIGH for sampled scene/text changes; continuous playback, narration and easing not verified'
   if mid in cor:
    x['action_label']=cor[mid];x['tool_agnostic_reconstruction_method']='Separate initial scene replacement from subsequent '+('head entrance from below.' if mid=='M0032' else 'paper enlargement.')
 write(path,rows)
rows=list(csv.DictReader((r/'07_VALIDATION/MOTION_QA_DISPOSITION.csv').open()))
for x in rows:
 if x['video_id']==v:
  mid=x['motion_id'];x.update(review_status='COMPLETE_WITH_DOCUMENTED_LIMITATIONS',disposition='CORRECTED_LABEL' if mid in cor else 'CONFIRMED_EXISTING_LABEL',evidence_reference=f'02_VIDEO_FORENSICS/{v}/evidence/finalization-review.jpg'+(f';02_VIDEO_FORENSICS/{v}/evidence/finalization-{mid}-detail.jpg' if mid in ['M0018','M0032','M0023','M0034'] else ''),observed_behavior=obs[mid],confidence='HIGH for stated visual observation',remaining_dependency='Narration alignment and easing remain uncertified; isolated adjacent samples do not certify full playback')
write(r/'07_VALIDATION/MOTION_QA_DISPOSITION.csv',rows)
qa=json.loads((d/'QA.json').read_text());qa['counts']['label_vs_measure_conflicts']=0;qa['independent_motion_review']={'original_candidates':8,'reviewed':8,'confirmed_existing_labels':6,'corrected_labels':2,'scope':'Source-hash-verified narrow native-frame sequences; no auditory or whole-duration playback sign-off','evidence':'evidence/finalization-review.jpg'};(d/'QA.json').write_text(json.dumps(qa,indent=1)+'\n')
meta=json.loads((out/'metadata.json').read_text());meta['review_observations']=obs;meta['corrections']=cor;meta['evidence_files']=[{'path':str(p.relative_to(r)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in (d/'evidence').glob('finalization-*.jpg')];(r/'07_VALIDATION/JSK53_MOTION_REVIEW.json').write_text(json.dumps(meta,indent=2)+'\n')
print('8 reviewed, 6 confirmed, 2 corrected; 656 unreviewed')
