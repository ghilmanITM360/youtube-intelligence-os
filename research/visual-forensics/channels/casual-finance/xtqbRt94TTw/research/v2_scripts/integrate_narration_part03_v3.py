"""Independent saved-output validation/read audit, then a versioned sampled crosswalk."""
import base64
import collections
import copy
import csv
import hashlib
import json
from pathlib import Path

R = Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
C = Path('/Users/ghilmankhan/YIOS-local-audits/CASUALLY_FINANCE_35_VIDEO_TARGET_20261104')
S = R / 'session_20261104'
D = R / 'agents/narration_visual_review_03'
expected = json.loads((D / 'items.json').read_text())
output = json.loads((D / 'OUT_narration_visual_review_03.json').read_text())
assert hashlib.sha256((D / 'OUT_narration_visual_review_03.json').read_bytes()).hexdigest() == '41a2b1465819135484a315e6a179d898f63209cb4fe18466a903e64df5b81a3b'
labels = {'LITERAL', 'METAPHOR', 'DATA', 'CONTRAST', 'HUMOR', 'DECORATIVE', 'UNDETERMINED', 'POTENTIAL_MISMATCH'}
inputs = {x['asr_id']: x for x in expected}

def validate(data):
    ids = [x['asr_id'] for x in data['items']]
    pending = data['pending_asr_ids']
    assert len(ids) == len(set(ids)) and len(pending) == len(set(pending))
    assert set(ids).isdisjoint(pending) and set(ids) | set(pending) == set(inputs)
    assert ids == [x['asr_id'] for x in expected if x['asr_id'] in set(ids)]
    reads = {x['path']: x for x in data['evidence_reads']}
    assert len(reads) == len(data['evidence_reads'])
    for x in data['items']:
        supplied = inputs[x['asr_id']]
        assert x['relation'] in labels and x['description'].strip()
        assert x['asr_text_status'] == 'UNCERTIFIED' and x['actual_listening'] is False
        assert x['input_asr_text_uncertified'] == supplied['text_ASR_uncertified']
        assert x['input_asr_interval_s'] == [supplied['start_s'], supplied['end_s']]
        assert x['evidence_paths'] and set(x['evidence_paths']) <= set(reads)
        assert set(x['evidence_paths']) <= {y['path'] for y in supplied['images']}
        assert set(x['sampled_source_frames']) <= {y['frame'] for y in supplied['images']}
    for x in reads.values():
        assert x['successful'] and x['witness'].strip()
        assert hashlib.sha256(Path(x['path']).read_bytes()).hexdigest() == x['sha256']
    return reads

reads = validate(output)
assert not output['pending_asr_ids'] and len(output['items']) == 33
negative_checks = []
for name, mutate in [('duplicate_id', lambda d: d['items'].append(copy.deepcopy(d['items'][0]))),
                     ('unknown_relation', lambda d: d['items'][0].update(relation='FULL_AV_PASS')),
                     ('unprovided_evidence', lambda d: d['items'][0].update(evidence_paths=['/not/supplied.jpg']))]:
    tampered = copy.deepcopy(output)
    mutate(tampered)
    try:
        validate(tampered)
    except AssertionError:
        negative_checks.append(name)
    else:
        raise AssertionError('Validator failed to reject ' + name)

oldcalls = set()
for rel, key in [('session_20261103/narration_visual_review_01_validation.json', 'actual_returns'),
                 ('session_20261103/narration_part02_new_read_audit.json', 'actual_returns')]:
    oldcalls.update(x['call_id'] for x in json.loads((R / rel).read_text())[key])
logs = []
for p in Path('/Users/ghilmankhan/.codex/sessions/2026/11').glob('*/*.jsonl'):
    with p.open() as f:
        first = json.loads(f.readline())
    if first.get('payload', {}).get('agent_path') == '/root/narration_review_01':
        logs.append(p)
assert len(logs) == 1, logs
actual = []
for line in logs[0].open():
    x = json.loads(line).get('payload', {})
    if x.get('type') != 'custom_tool_call_output' or x.get('call_id') in oldcalls or not isinstance(x.get('output'), list):
        continue
    for block in x['output']:
        if block.get('type') != 'input_image':
            continue
        url = block.get('image_url')
        url = url.get('url') if isinstance(url, dict) else url
        if isinstance(url, str) and url.startswith('data:'):
            actual.append({'call_id': x['call_id'], 'sha256': hashlib.sha256(base64.b64decode(url.split(',', 1)[1])).hexdigest()})
need = collections.Counter(x['sha256'] for x in reads.values())
have = collections.Counter(x['sha256'] for x in actual)
assert not need - have
assert len(actual) == len(reads) == 56
proof = dict(completed_rows=33, pending_rows=0, actual_new_image_returns=len(actual),
             successful_unique_path_receipts=len(reads), native_fullframes=0, scaled960x540=len(reads),
             old_part01_part02_call_ids_excluded=len(oldcalls), image_bytehash_multiplicity='PASS',
             negative_checks_rejected=negative_checks, actual_returns=actual, actual_listening_seconds=0)
(S / 'narration_part03_independent_validation_v1.json').write_text(json.dumps(proof, indent=2) + '\n')

root = json.loads((C / 'ASR156_supplemental_review_v1.json').read_text())
rootproof = json.loads((S / 'ASR156_independent_image_return_audit_v1.json').read_text())
assert rootproof['status'] == 'PASS_ACTUAL_IMAGE_BYTE_RETURN_AUDIT'
assert rootproof['source_review_sha256'] == hashlib.sha256((C / 'ASR156_supplemental_review_v1.json').read_bytes()).hexdigest()
rootrow = dict(asr_id=156, relation=root['relation'], description=' '.join(x['observed'] for x in root['observations']) + ' ' + root['relation_reasoning'],
               visible_text_only_if_readable='United States Treasury; %; BIG BUSINESS; DEBT',
               evidence_paths=[x['path'] for x in root['evidence_images']], sampled_source_frames=[x['frame'] for x in root['evidence_images']],
               confidence='medium', limitations=root['limitations'])
new = {x['asr_id']: x for x in output['items'] + [rootrow]}
assert len(new) == 34
with (R / 'production_v1/narration_visual_alignment_v2.csv').open() as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 199 and {int(x['asr_id']) for x in rows if x['review_status'] == 'PENDING'} == set(new)
for row in rows:
    ident = int(row['asr_id'])
    x = new.get(ident)
    if x:
        row.update(review_status='SAMPLED_ASR_VISUAL_RELATION_REVIEWED', relation=x['relation'], description=x['description'],
                   visible_text=x['visible_text_only_if_readable'], evidence_paths=json.dumps(x['evidence_paths']),
                   sampled_frames=json.dumps(x['sampled_source_frames']), confidence=x['confidence'], limitations=json.dumps(x['limitations']))
    row['row_review_source'] = ('ASR156 root supplement + independent byte-return audit' if ident == 156 else
                                'agents/narration_visual_review_03/OUT_narration_visual_review_03.json' if x else 'immutable checkpointO/v2')
    row['scope'] = 'Sampled relation to uncertified ASR; not verified speech, continuous synchronization, financial fact-check or listening'
dest = R / 'production_v1/narration_visual_alignment_v3.csv'
assert not dest.exists()
with dest.open('w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
stats = dict(ASR_segments_total=199, visually_sampled_relation_rows_reviewed=199, pending_count=0, pending_ids=[],
             newly_integrated_rows=34, preserved_prior_rows=165, new_root_scaled_image_returns=2,
             new_agent_scaled_image_returns=56, relation_counts=dict(collections.Counter(x['relation'] for x in rows)),
             actual_listening_seconds=0, continuous_sync_verified=False, speech_certified=False,
             status='ALL199_SAMPLED_ASR_RELATION_ROWS_REVIEWED_NOT_FULL_AV',
             undetermined_ids=[int(x['asr_id']) for x in rows if x['relation']=='UNDETERMINED'],
             potential_mismatch_ids=[int(x['asr_id']) for x in rows if x['relation']=='POTENTIAL_MISMATCH'])
(R / 'production_v1/narration_visual_alignment_stats_v3.json').write_text(json.dumps(stats, indent=2) + '\n')
print(json.dumps(stats))
