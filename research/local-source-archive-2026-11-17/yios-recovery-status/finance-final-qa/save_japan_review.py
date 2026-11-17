from pathlib import Path
import csv,json,hashlib
from PIL import Image
r=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os/data/extracted/forensic-analysis/casually-finance/2026-10-12');v='rSa2aziEsAI';d=r/'02_VIDEO_FORENSICS'/v;o=Path('/Users/ghilmankhan/workprojects/yios-recovery-status/finance-final-qa/rSa2aziEsAI-motion')
for i in [1,2,3]:
 with Image.open(o/f'review-{i}.png') as im:im.save(d/'evidence'/f'finalization-motion-{i}.jpg',quality=88)
obs={
'M0001':('REVEAL_MOVE','Japan map character moves downward across debt-note composition between 1.8337 and 2.017s; bubble changes separately. No whole-scene cut in sampled progression.'),
'M0003':('CUT','Abrupt monster scene at 3.6s; character/background motion continues, then interest-rate screenshot by 8.733s. CUT is valid at scene-replacement scope; interval is not purely instantaneous.'),
'M0005':('TRANSFER_MOVE','Bank building remains while yen bag moves downward toward notes and notes rise toward bank over 10.8667–11.7s. Scene replacement is not observed.'),
'M0006':('CUT_THEN_SCALE_THEN_CUT','Bank composition replaces with Japan/debt-note composition at 12.6663s; latter enlarges over 13.608–15.558s; bond-holder table replaces scene by 16.533s. Object scale versus camera zoom unverified.'),
'M0007':('POP_IN_THEN_REVEAL_MOVE','Table remains: debt note appears between 17.0 and 17.0333s, Japan character rises from lower edge over 17.1833–17.733s. Not a whole-scene cut.'),
'M0010':('REVEAL_MOVE','Character progressively enters from below screenshot over 20.7165–21.1s. Entry is visibly progressive, not instantaneous.'),
'M0011':('','Coin graphics are absent at 21.4337s, first present at 21.6502s, and second appears later. Nine samples establish sequential occurrence but do not establish each coin entry mechanism; retain label pending denser review.'),
'M0012':('','Screenshot replaces with yen banknote at 22.8s; additional banknotes accumulate, then businessman scene appears by 24.167s. Sparse samples do not establish every build mechanism; retain existing label and explicit incomplete mechanism review.'),
'M0017':('REVEAL_MOVE_THEN_POP_IN','Top-hat character progressively rises from bottom over 29.3337–29.8918s; speech bubble appears by 30.1s. Distinct entrance and subsequent bubble phases.'),
'M0020':('SWAP_THEN_NUMBER_BUILD','Speech bubble contents replace between 33.6 and 33.6333s; visible rate changes 1%, 2%, 3% across 33.750–34.200s. Character and bubble remain.'),
'M0023':('CUT','Embedded reaction clip visibly changes over 35.8–36.6167s; bank illustration appears abruptly by 36.9s. CUT describes final replacement, not every active frame.'),
'M0027':('TRANSFER_MOVE','Banknotes move upward from lower commercial-bank icons toward Bank of Japan over 38.867–39.4285s, with lower notes disappearing. Existing POP_IN misses spatial transfer.'),
'M0031':('','Arrow appears above bank, percent icon subsequently rises, then numerical comparison appears. Multiple phases observed; nine samples insufficient to distinguish all entrances and replacements. Retain existing label pending denser review.'),
'M0037':('TEXT_SWAP','Caption changes to red that is a horrible deal by 54.5998s; host expression and lower reaction figure also change. Existing text event label valid; not a description of all concurrent activity.'),
'M0038':('CUT','CFI/host composition persists through 55.7082s; Japan character composition appears by 55.8s. Existing CUT valid at scene-replacement scope.')}
cor={m:l for m,(l,_) in obs.items() if l and m not in ['M0003','M0023','M0037','M0038']}
unknown={'M0011','M0012','M0031'}
def write(p,rows):
 with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
for p in [d/'MOTIONS.csv',r/'03_MASTER_DATA/MASTER_MOTIONS.csv']:
 rows=list(csv.DictReader(p.open()))
 for x in rows:
  if x['video_id']==v and x['motion_id'] in obs and x['motion_id'] not in unknown:
   mid=x['motion_id'];label,note=obs[mid];x['action_label']=label;x['observed_action']=note;x['label_vs_measure_check']='INDEPENDENT_SEQUENCE_REVIEW: '+('CORRECTED_MULTIPHASE_OR_MOVE_LABEL' if mid in cor else 'CONFIRMED_EVENT_LABEL_WITH_CONCURRENT_ACTIVITY');x['confidence']='HIGH for stated sampled visual changes; continuous playback, easing and narration not verified'
   if mid in cor:x['tool_agnostic_reconstruction_method']='Reconstruct the observed phase order: '+note+' Use independently designed assets; easing unassessed.'
 write(p,rows)
rows=list(csv.DictReader((r/'07_VALIDATION/MOTION_QA_DISPOSITION.csv').open()));order=list(obs)
for x in rows:
 if x['video_id']==v:
  mid=x['motion_id'];x.update(review_status='PARTIAL' if mid in unknown else 'COMPLETE_WITH_DOCUMENTED_LIMITATIONS',disposition='INSUFFICIENT_EVIDENCE' if mid in unknown else ('CORRECTED_LABEL' if mid in cor else 'CONFIRMED_EXISTING_LABEL'),evidence_reference=f'02_VIDEO_FORENSICS/{v}/evidence/finalization-motion-{order.index(mid)//5+1}.jpg',observed_behavior=obs[mid][1],confidence='HIGH for stated sampled observations; phase mechanism incomplete for insufficient-evidence rows',remaining_dependency='Denser native-frame entrance review' if mid in unknown else 'Audio synchronization/easing remain uncertified')
write(r/'07_VALIDATION/MOTION_QA_DISPOSITION.csv',rows)
qa=json.loads((d/'QA.json').read_text());qa['counts']['label_vs_measure_conflicts']=3;qa['independent_motion_review']={'original_candidates':15,'reviewed':15,'confirmed_existing_labels':4,'corrected_labels':8,'insufficient_evidence':3,'scope':'Nine source-frame samples per candidate, not continuous playback; three require denser entrance review','decoder_note':'Two ffmpeg seek extractions emitted nonfatal h264 mmco unref-short warnings. Saved images inspected; no source bytes altered.'};(d/'QA.json').write_text(json.dumps(qa,indent=1)+'\n')
meta=json.loads((o/'metadata.json').read_text());meta['observations']=obs;meta['corrections']=cor;meta['insufficient_evidence']=sorted(unknown);meta['evidence_files']=[{'path':str(p.relative_to(r)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in (d/'evidence').glob('finalization-motion-*.jpg')];(r/'07_VALIDATION/JAPAN_MOTION_REVIEW.json').write_text(json.dumps(meta,indent=2)+'\n');print('15 reviewed: 8 corrected,4 confirmed,3 insufficient evidence')
