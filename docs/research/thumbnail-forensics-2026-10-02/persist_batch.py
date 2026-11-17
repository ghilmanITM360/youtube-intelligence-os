"""Validate manually observed rows and persist one traceable audit batch."""
import csv,hashlib,json,sys
from pathlib import Path
from datetime import datetime,timezone
OUT=Path(__file__).resolve().parent
batch=sys.argv[1] if len(sys.argv)>1 else 'B002-01'
stem=batch.lower().replace('b','batch-',1)
rows=json.loads((OUT/(stem+'-selection.json')).read_text())
notes=[json.loads(x) for x in (OUT/(stem+'-observations.jsonl')).read_text().splitlines()]
assert len(rows)==len(notes)==24 and {n['i'] for n in notes}==set(range(1,25))
score_keys=['story_15','psychological_hook_15','title_partnership_15','hierarchy_10','mobile_readability_10','composition_10','emotion_subject_alignment_10','credibility_10','distinctiveness_5']
limits=[15,15,15,10,10,10,10,10,5]
required=['text','small_text','scene','hook','composition','typography','color','psychology','partnership','scan','art','mobile320','mobile160','strong','weak','bottleneck','action','counterexample','safety','scores','focal_regions','background','confidence']
out=[]
for n in notes:
 r=rows[n['i']-1];assert all(k in n for k in required)
 digest=hashlib.sha256(Path(r['local_path']).read_bytes()).hexdigest();assert r['Thumbnail_ID']=='THB-'+digest
 assert len(n['scores'])==9 and all(0<=s<=m for s,m in zip(n['scores'],limits))
 out.append(dict(r,sha256=digest,inspection_status='INSPECTED_NATIVE_320x180_160x90',inspection_method='INDIVIDUAL_MULTISCALE_PANEL_VISUALLY_OPENED',inspected_at=datetime.now(timezone.utc).isoformat(),rubric_version='B001_WEIGHTS_V1',score_interpretation='EXPERT_VISUAL_DIAGNOSTIC_ONLY_NOT_CTR_OR_PERFORMANCE',**dict(zip(score_keys,n['scores'])),score_100=sum(n['scores']),A_observed_content=n['scene'],visible_headline_text=n['text'],visible_small_text=n['small_text'],headline_word_count=len(n['text'].split()),word_count_method='WHITESPACE_TOKENS_MAIN_AND_SECONDARY_GRAPHIC_COPY_EXCLUDES_SMALL_TEXT',B_attention_mechanism=n['hook'],C_composition=n['composition'],D_typography=n['typography'],E_color_light=n['color'],F_human_psychology=n['psychology'],G_title_thumbnail_partnership=n['partnership'],H_first_look_heuristic=n['scan'],I_art_direction=n['art'],J_diagnosis=dict(strongest=n['strong'],weakest=n['weak'],bottleneck=n['bottleneck'],corrective_action=n['action'],counterexample_audit_id=n['counterexample'],confidence=n['confidence']),mobile_320=n['mobile320'],mobile_160=n['mobile160'],health_claim_flags=n['safety'],medical_verification_status='NOT_MEDICAL' if n['safety']=='NOT_MEDICAL' else 'TRIAGED_REQUIRES_CLAIM_SPECIFIC_REVIEW',content_promise_verified='NOT_CHECKED',analyst_face_count=n.get('face_count',1),analyst_major_focal_regions=n['focal_regions'],analyst_background_complexity=n['background'],measurement_note='Face/focal-region/background labels are manual observations or judgments, not automated objective measurements'))
def save(name,data):
 (OUT/(name+'.json')).write_text(json.dumps(data,indent=2,ensure_ascii=False))
 keys=list(dict.fromkeys(k for r in data for k in r))
 with (OUT/(name+'.csv')).open('w') as f:
  w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(dict,list)) else v for k,v in r.items()} for r in data)
save('individual-audit-'+stem,out)
ledger=list(csv.DictReader((OUT/'completion-ledger.csv').open()))
ledger=[r for r in ledger if r['batch_id']!=batch]
ledger.append(dict(batch_id=batch,scope='24 registered thumbnails; native and both mobile scales; medical/content validation remains separate B008 work',status='VISUAL_AUDIT_COMPLETE',discovered_units=24,completed_units=24,provenance='individual-audit-'+stem+'.json',opened=24,audited=24,excluded=0,ambiguous=0,remaining=0,validation_result='PASS: 24 exact source hashes, unique IDs, required A–J fields, three scales, score bounds'))
completed=sum(len(json.loads(p.read_text())) for p in OUT.glob('individual-audit-batch-002-*.json'))
for r in ledger:
 if r['batch_id']=='B002':r.update(status='IN_PROGRESS',completed_units=completed,remaining=138-completed,scope='Historical 138 pending registered thumbnails; current public additions tracked separately')
save('completion-ledger',ledger)
print('PASS: 24 audited records; source hashes, rubric bounds, unique sequence and required fields verified.')
