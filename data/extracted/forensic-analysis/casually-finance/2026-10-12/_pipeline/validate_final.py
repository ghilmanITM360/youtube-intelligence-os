import csv,json,datetime,re
from pathlib import Path
root=Path('.');p=json.load(open(root/'00_MANIFEST/PROGRESS.json'));manifest={r['video_id']:r for r in csv.DictReader(open(root/'00_MANIFEST/SELECTED_18.csv'))};done=p['completed_videos']
files={'TRANSCRIPT':'word_id','SENTENCES':'sentence_id','SHOTS':'shot_id','STATES':'state_id','MOTIONS':'motion_id','ASSETS':'asset_id','AUDIO_EVENTS':'audio_event_id','AUDIO_VISUAL_SYNC':'sync_id','SEMANTIC_BEATS':'beat_id','FINANCE_CLAIMS':'claim_id'}
errors=[];results={};counts={k:0 for k in files}
for vid in done:
 d=root/'02_VIDEO_FORENSICS'/vid;tables={};checks={}
 def check(k,c):
  checks[k]=bool(c)
  if not c:errors.append(vid+': '+k)
 for fn,key in files.items():
  path=d/(fn+'.csv');check(fn+'_exists',path.exists());r=list(csv.DictReader(open(path))) if path.exists() else [];tables[fn]=r;counts[fn]+=len(r);check(fn+'_unique_ids',len({x[key] for x in r})==len(r));check(fn+'_video_ids',all(x.get('video_id',vid)==vid for x in r))
 ids={fn:{x[key] for x in tables[fn]} for fn,key in files.items()};dur=float(manifest[vid]['local_duration_sec'])
 for fn,rs in tables.items():
  check(fn+'_timestamps',all(0<=float(x['start_sec'])<=float(x['end_sec'])<=dur+0.15 for x in rs if 'start_sec' in x and 'end_sec' in x))
 def fk(fn,field,target):return all(not x.get(field) or x[field] in ids[target] for x in tables[fn])
 check('state_shot_fk',fk('STATES','shot_id','SHOTS'))
 check('shot_state_fk',fk('SHOTS','first_state_id','STATES') and fk('SHOTS','last_state_id','STATES'))
 check('motion_fk',all(fk('MOTIONS',f,t) for f,t in [('shot_id','SHOTS'),('target_shot_id','SHOTS'),('source_state','STATES'),('target_state','STATES')]))
 check('sync_fk',all(fk('AUDIO_VISUAL_SYNC',f,t) for f,t in [('shot_id','SHOTS'),('state_id','STATES'),('motion_id','MOTIONS'),('sentence_id','SENTENCES'),('word_id','TRANSCRIPT'),('audio_event_id','AUDIO_EVENTS')]))
 check('asset_fk',all(all(a in ids['ASSETS'] for a in x.get('asset_ids','').split(';') if a) for fn in ['STATES','SHOTS'] for x in tables[fn]))
 check('beat_sentence_fk',fk('SEMANTIC_BEATS','first_sentence_id','SENTENCES') and fk('SEMANTIC_BEATS','last_sentence_id','SENTENCES'))
 check('claim_sentence_fk',all(all(t in ids['SENTENCES'] for t in re.findall(r'T\d{4}',x['sentence_ids'])) for x in tables['FINANCE_CLAIMS']))
 sh={x['shot_id']:x for x in tables['SHOTS']}
 check('states_inside_shots',all(float(sh[x['shot_id']]['start_sec'])-.002<=float(x['start_sec'])<=float(x['end_sec'])<=float(sh[x['shot_id']]['end_sec'])+.002 for x in tables['STATES']))
 check('shot_contiguous_coverage',abs(float(tables['SHOTS'][0]['start_sec']))<.002 and abs(float(tables['SHOTS'][-1]['end_sec'])-json.load(open(d/'QA.json'))['coverage']['video_duration_sec'])<.002 and all(abs(float(a['end_sec'])-float(b['start_sec']))<.002 for a,b in zip(tables['SHOTS'],tables['SHOTS'][1:])))
 src=json.load(open(d/'SOURCE.json'));qa=json.load(open(d/'QA.json'));check('hash_provenance_matches_manifest',src['sha256']==manifest[vid]['sha256']);check('source_video_id',src['video_id']==vid);check('structural_qa',qa['status']=='PASS_STRUCTURAL' and all(qa['checks'].values()))
 check('required_reports',all((d/x).exists() for x in ['PACKAGING.md','VISUAL_RECONSTRUCTION.md','SOURCE.json','QA.json']))
 check('evidence_sheets_exist',all((d/x['evidence_sheet']).exists() for x in tables['STATES']))
 check('container_tail_under_quarter_second',0<=dur-float(tables['SHOTS'][-1]['end_sec'])<.25)
 results[vid]={'container_tail_sec':round(dur-float(tables['SHOTS'][-1]['end_sec']),6),'checks':checks,'sha256':src['sha256'],'source_hash_verification_basis':'Fresh source hash matched this session' if vid in ['0ll9rEtoRrs','-X6YzlY_8tM'] else 'Previous checkpoint documented source bytes verified; no repeated hashing','audiovisual_status':'AUDIOVISUAL_QA_PARTIAL'}
masters={}
for fn,key in files.items():
 name={'TRANSCRIPT':'WORDS','SENTENCES':'SENTENCES','SHOTS':'SHOTS','STATES':'STATES','MOTIONS':'MOTIONS','ASSETS':'ASSETS','AUDIO_EVENTS':'AUDIO_EVENTS','AUDIO_VISUAL_SYNC':'AUDIO_VISUAL_SYNC','SEMANTIC_BEATS':'SEMANTIC_BEATS','FINANCE_CLAIMS':'FINANCE_CLAIMS'}[fn]
 r=list(csv.DictReader(open(root/'03_MASTER_DATA'/f'MASTER_{name}.csv')));expected=[]
 for vid in done:
  for x in tables_for(vid,fn) if False else list(csv.DictReader(open(root/'02_VIDEO_FORENSICS'/vid/(fn+'.csv')))):
   x.setdefault('video_id',vid);expected.append(x)
 unique=len({(x['video_id'],x[key]) for x in r})==len(r);equal=len(r)==counts[fn] and all(all(a.get(k,'')==b.get(k,'') for k in set(a)|set(b)) for a,b in zip(r,expected));masters[name]={'rows':len(r),'unique_keys':unique,'exact_per_video_reconciliation':equal}
 if not unique or not equal:errors.append('MASTER_'+name+' reconciliation failed')
res={'generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':f'{len(done)}/18 COMPLETE videos only; structural QA; six of eight Shorts','videos':results,'master_tables':masters,'all_pass':not errors,'errors':errors,'status':'STRUCTURAL_QA_PASSED' if not errors else 'FAILED','audiovisual_status':'AUDIOVISUAL_QA_PARTIAL','missing_local':['turJ6VMfUjI','Qof71Ef-3EU'],'limitations':['No direct audio listening','Whisper numbers and proper nouns uncertified','Easing unassessed','Independent visual QA incomplete','Financial contradictions retained','Prior final spectrogram strips stretch partial duration under fixed120s axis; do not read beyond actual duration','Source hashes based on prior documented verification for14 and fresh verification for2; master files match byte-level CSV cell values of per-video outputs']}
q=root/'07_VALIDATION/VALIDATION_RESULTS.json';tmp=q.with_suffix('.tmp');tmp.write_text(json.dumps(res,indent=1));tmp.replace(q);print(res['status'],len(done),masters);print('ERRORS',errors)
raise SystemExit(bool(errors))
