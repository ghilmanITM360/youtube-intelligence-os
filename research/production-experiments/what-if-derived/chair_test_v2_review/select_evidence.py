from pathlib import Path
import csv,json,re
from study import sheet
r=Path('chair_test_v2_review'); ss=json.loads((r/'evidence/sources.json').read_text());states=list(csv.DictReader(open('production_intelligence_brain/01_master_data/MASTER_STATES.csv')));sync=list(csv.DictReader(open('production_intelligence_brain/01_master_data/MASTER_AUDIO_VISUAL_SYNC.csv')))
choices={'R02':[0,2,4,5,7],'R03':[1,3,4,6],'R04':[0,1,2,7],'R05':[2,4,5,6],'R06':[0,2,4,7],'R07':[1,3,5,6],'R08':[1,3,4,5],'R09':[0,1,3,5,7],'R10':[1,3,5,6],'R11':[0,2,4,7],'R12':[1,2,4,5],'R13':[0,2,3,5,7],'R14':[1,4,5,6],'R15':[0,2,4,7]};evidence=[]
for s in ss:
 d=Path('video_forensics_output')/s['slug']; sent=list(csv.DictReader((d/'05_audio/semantic/TRANSCRIPT_SENTENCES.csv').open())); sel=[]
 print('\n##',s['id'],s['slug'])
 for k in choices[s['id']]:
  t=s['times'][k];state=next((x for x in states if x['VIDEO_SLUG']==s['slug'] and float(x['START_SEC'])<=t<float(x['END_SEC'])),None);speech=[x for x in sent if float(x['START_SEC'])<=t<float(x['END_SEC'])];f=next((r/'evidence'/s['id']).glob(f'overview_{k+1:02}_*'));sid=state['STATE_ID'] if state else 'UNMAPPED';eid=f'{s["id"]}-{k+1:02}'
  print(eid,t,sid, 'FRAME:',(state or {}).get('LITERAL_FRAME_DESCRIPTION','')[:1000], '\nMOTION:',(state or {}).get('TRANSITION_IN',''), '|',(state or {}).get('TRANSITION_OUT',''),'\nNARRATION:',[x['TEXT'] for x in speech])
  evidence.append(dict(id=eid,reference=s['id'],timestamp=t,state=sid,file=str(f),source=s['source'],slug=s['slug'],record=state,speech=speech));sel.append((f,f'{eid} {t:.3f}s'))
 sheet(sel,r/'evidence'/f'{s["id"]}_selected.jpg',3,340,640 if s['height']>s['width'] else 240)
 # Each source's reconstruction and prompts: selected excerpts, subordinate to image.
 for rel in ['03_capcut/CAPCUT_REBUILD.md','04_image_to_video/IMAGE_PROMPTS.md','04_image_to_video/ANIMATION_PROMPTS.md']:
  txt=(d/rel).read_text(); paras=[x for x in txt.split('\n\n') if any(w in x.lower() for w in ['stick','figure','character','pose','replace','caption','hand-drawn'])]; print(rel, '\n'.join(paras[:2])[:1600])
(r/'evidence/selected_evidence.json').write_text(json.dumps(evidence,indent=2))
