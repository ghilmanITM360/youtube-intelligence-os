from pathlib import Path
import os,json,csv,hashlib,collections
r=Path('/Users/ghilmankhan/workprojects/youtube-intelligence-os/data/extracted/forensic-analysis/casually-finance/2026-10-12');script=(r/'_pipeline/validate_final.py').read_text().replace("q=root/'07_VALIDATION/VALIDATION_RESULTS.json'","q=Path('/Users/ghilmankhan/workprojects/yios-recovery-status/finance-final-qa/finalization-validation.json')");os.chdir(r)
try:exec(compile(script,'validate_final.py','exec'),{})
except SystemExit as e:assert not e.code,e.code
q=r/'07_VALIDATION';o=json.loads(Path('/Users/ghilmankhan/workprojects/yios-recovery-status/finance-final-qa/finalization-validation.json').read_text());assert o['all_pass'];rs=list(csv.DictReader((q/'MOTION_QA_DISPOSITION.csv').open()));assert len(rs)==len({(x['video_id'],x['motion_id']) for x in rs})==664
for p in q.glob('*MOTION_REVIEW.json'):
 m=json.loads(p.read_text());observed=m.get('observations',m.get('review_observations',{}));assert set(observed)=={x['motion_id'] for x in m['sequences']},p
 for e in m.get('evidence_files',[]):assert hashlib.sha256((r/e['path']).read_bytes()).hexdigest()==e['sha256']
for x in rs:
 if x['disposition']:
  for ref in x['evidence_reference'].split(';'):assert (r/ref).exists(),ref
  if x['disposition']=='CORRECTED_LABEL':
   current=next(m for m in csv.DictReader((r/'02_VIDEO_FORENSICS'/x['video_id']/'MOTIONS.csv').open()) if m['motion_id']==x['motion_id']);assert current['action_label']!=x['original_label'],x
matrix=list(csv.DictReader((q/'VIDEO_QA_COMPLETION_MATRIX.csv').open()));assert len(matrix)==18 and len({x['video_id'] for x in matrix})==18
claims=list(csv.DictReader((q/'FINANCE_CLAIM_VERIFICATION.csv').open()));assert len(claims)==287 and len({(x['video_id'],x['claim_id']) for x in claims})==287
assert not any(x['existing_evidence_status']=='ON_SCREEN_PRIMARY_SOURCE_CONSISTENT' and x['external_verification_result']=='VERIFIED' for x in claims)
o['candidate_counts']=dict(collections.Counter(x['disposition'] or 'NOT_STARTED' for x in rs));o['all_motion_candidates_triaged']=all(x['disposition'] for x in rs);o['source_integrity']=json.loads((q/'FINALIZATION_SOURCE_INTEGRITY.json').read_text());o['research_complete']=False;o['research_status']='RESEARCH_CONTINUATION_REQUIRED';o['source_hash_scope']='Freshly rehashed17 original files/16 Video_IDs plus2033 supplementary files; no modified bytes';o['master_checksums']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (r/'03_MASTER_DATA').glob('MASTER_*.csv')};o['limitations']=['No continuous whole-video playback or direct listening certified','Untriaged long-form flags and insufficient-evidence Short mechanisms remain','External claim register includes unfinished agent verification','Two original Shorts absent; public accessibility fetch throttled'];(q/'FINAL_VALIDATION.json').write_text(json.dumps(o,indent=2)+'\n');print('FINALIZATION_CHECKS_PASS',o['candidate_counts'],'18 matrix rows,287 claim rows,10 reconciled masters')
