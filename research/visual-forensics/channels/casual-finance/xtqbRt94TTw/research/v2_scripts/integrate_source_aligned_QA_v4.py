"""Audit actual native image returns and update only sixteen targeted crosswalk rows."""
from pathlib import Path
import base64
import collections
import csv
import hashlib
import json

R=Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
D=R/'narration_source_aligned_QA_v1';S=R/'session_20261104'
raw=D/'OUT_narration_source_aligned_QA_v1.json'
assert hashlib.sha256(raw.read_bytes()).hexdigest()=='056839bcb933c5b758c6dae2c799038541a633b2677aade730d1db51d4471e3a'
expected=json.loads((D/'items.json').read_text());output=json.loads(raw.read_text());given={x['asr_id']:x for x in expected['items']}
ids=[x['asr_id'] for x in output['items']]
assert ids==list(given) and len(ids)==len(set(ids))==16 and not output['pending_asr_ids']
labels={'LITERAL','METAPHOR','DATA','CONTRAST','HUMOR','DECORATIVE','UNDETERMINED','POTENTIAL_MISMATCH'}
reads={x['path']:x for x in output['evidence_reads']};assert len(reads)==len(output['evidence_reads'])==48
for path,x in reads.items():
    assert x['successful'] and x['witness'] and x['scale']=='NATIVE_FULLFRAME1920x1080'
    assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==x['sha256']
for x in output['items']:
    item=given[x['asr_id']]
    assert x['relation'] in labels and x['asr_text_status']=='UNCERTIFIED' and x['actual_listening'] is False
    assert set(x['evidence_paths'])=={y['path'] for y in item['images']}<=set(reads)
    assert set(x['sampled_source_frames'])=={y['frame'] for y in item['images']}
    assert x['source_vs_ASR_note'] and x['description'] and x['change_reason']
    for image in item['images']:
        assert image['width']==1920 and image['height']==1080
        assert item['start_s']-1e-8<=image['source_pts_s']<item['end_s']+1e-8
        assert image['sha256']==reads[image['path']]['sha256']
oldcalls=set()
for rel in ['session_20261103/narration_visual_review_01_validation.json','session_20261103/narration_part02_new_read_audit.json','session_20261104/narration_part03_independent_validation_v1.json']:
    oldcalls.update(x['call_id'] for x in json.loads((R/rel).read_text())['actual_returns'])
logs=[]
for p in Path('/Users/ghilmankhan/.codex/sessions/2026/11').glob('*/*.jsonl'):
    with p.open() as f:meta=json.loads(f.readline())
    if meta.get('payload',{}).get('agent_path')=='/root/narration_review_01':logs.append(p)
assert len(logs)==1
actual=[]
for line in logs[0].open():
    x=json.loads(line).get('payload',{})
    if x.get('type')!='custom_tool_call_output' or x.get('call_id') in oldcalls or not isinstance(x.get('output'),list):continue
    for b in x['output']:
        if b.get('type')!='input_image':continue
        url=b.get('image_url');url=url.get('url') if isinstance(url,dict) else url
        if isinstance(url,str) and url.startswith('data:'):
            actual.append({'call_id':x['call_id'],'sha256':hashlib.sha256(base64.b64decode(url.split(',',1)[1])).hexdigest()})
assert collections.Counter(x['sha256'] for x in reads.values())==collections.Counter(x['sha256'] for x in actual)
assert len(actual)==48
integrity=json.loads((S/'sequential_same_decoder_seek_integrity_audit_v1.json').read_text())
assert integrity['mismatches']==0 and integrity['exact_matches']==88
proof={'cases':16,'pending':0,'native_fullframe_returns':48,'scaled_returns':0,'actual_returns':actual,'image_bytehash_multiplicity':'PASS',
       'sample_locations_strictly_inside_uncertified_ASR_intervals':'PASS_ALL48','nonseeking_source_decode_identity':'PASS_ALL88_DERIVATIVES',
       'audio_alignment':'NOT_VERIFIED','actual_listening_seconds':0}
(S/'source_aligned_QA_independent_validation_v1.json').write_text(json.dumps(proof,indent=2)+'\n')
with (R/'production_v1/narration_visual_alignment_v3.csv').open() as f:rows=list(csv.DictReader(f))
by={x['asr_id']:x for x in output['items']}
for row in rows:
    x=by.get(int(row['asr_id']));row['native_followup_source_vs_ASR_note']='';row['sample_location_check']=''
    if x:
        row.update(review_status='SOURCE_ALIGNED_NATIVE_SAMPLED_ASR_RELATION_REVIEWED',relation=x['relation'],description=x['description'],
                   visible_text=x['visible_text_only_if_readable'],evidence_paths=json.dumps(x['evidence_paths']),sampled_frames=json.dumps(x['sampled_source_frames']),
                   confidence=x['confidence'],limitations=json.dumps(x['limitations']),row_review_source='narration_source_aligned_QA_v1/OUT_narration_source_aligned_QA_v1.json',
                   native_followup_source_vs_ASR_note=x['source_vs_ASR_note'])
    frames=json.loads(row['sampled_frames']);start=float(row['start_s']);end=float(row['end_s'])
    assert frames and all(start-1e-8<=(n+1)/24<end+1e-8 for n in frames),(row['asr_id'],frames,start,end)
    row['sample_location_check']='ALL_USED_SAMPLES_INSIDE_PROVISIONAL_ASR_INTERVAL;NOT_AUDIO_TIMING_CERTIFICATION'
p=R/'production_v1/narration_visual_alignment_v4.csv';assert not p.exists()
with p.open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
stats={'ASR_segments_total':199,'sampled_relation_rows_reviewed':199,'pending_unreviewed':0,'source_aligned_native_QA_cases':16,
       'prior_outside_interval_cases_fixed':[56,57,74,120,121,133,136,152,162,166,171],'current_used_sample_locations_outside_ASR_interval':0,
       'relation_counts':dict(collections.Counter(x['relation'] for x in rows)),
       'undetermined_ids':[int(x['asr_id']) for x in rows if x['relation']=='UNDETERMINED'],
       'potential_mismatch_ids':[int(x['asr_id']) for x in rows if x['relation']=='POTENTIAL_MISMATCH'],
       'actual_listening_seconds':0,'speech_certified':False,'continuous_sync_verified':False,'status':'199SAMPLED_ROWS_REVIEWED_16SOURCE_ALIGNED_QA_NOT_FULL_AV'}
(R/'production_v1/narration_visual_alignment_stats_v4.json').write_text(json.dumps(stats,indent=2)+'\n');print(json.dumps(stats))
