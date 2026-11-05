"""Independent saved-output/schema and actual returned-image-byte audit."""
from pathlib import Path
import base64
import collections
import datetime
import hashlib
import io
import json
import sys
from PIL import Image

R = Path('/Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan')
out_path, label = R / sys.argv[1], sys.argv[2]
o = json.loads(out_path.read_text())
manifest = json.loads((out_path.parent / 'items.json').read_text())
requested = manifest['new_view_requests']
requested_by_path = {r['path']: r for r in requested}
expected_ids = {r.get('id', r.get('event', {}).get('event_id')) for r in manifest['items']}
assert len(expected_ids) == len(manifest['items'])
assert len(o['items']) == len(expected_ids)
assert set(r['id'] for r in o['items']) == expected_ids
assert o['source_sha256'] == manifest['source_sha256']
assert o['actual_listening_seconds'] == 0 and o['CT_SCAN_COMPLETE'] is False
reads = o['new_evidence_reads']
assert len({r['path'] for r in reads}) == len(reads)
pending = o['pending_new_image_paths']
assert not set(pending) & {r['path'] for r in reads}
assert set(pending) | {r['path'] for r in reads} == set(requested_by_path)
for read in reads:
    assert read['successful'] is True
    assert hashlib.sha256(Path(read['path']).read_bytes()).hexdigest() == read['sha256'] == requested_by_path[read['path']]['sha256']
    assert 'NATIVE' in read['scale']
for item in o['items']:
    assert item['shot_boundary'] in {'YES', 'NO', 'UNDETERMINED'}
    assert item['description'] and item['confidence'] and item['limitations']
    source_item = next(r for r in manifest['items'] if r.get('id', r.get('event', {}).get('event_id')) == item['id'])
    if item['id'] not in o['pending_case_ids']:
        assert {str(out_path.parent / f'f{n:05d}_native.png') for n in source_item['frames']} == set(item['evidence_paths'])
    if item['shot_boundary'] == 'YES':
        onset = item['onset_frame_or_bracket']['frame']
        assert item['onset_frame_or_bracket']['before_frame'] == onset - 1
        assert onset in source_item['frames']

log = Path('/Users/ghilmankhan/.codex/sessions/2026/11/03/rollout-2026-11-03T23-56-51-01a1a2c5-7474-7bb0-8347-8cf541ba6fad.jsonl')
first_utc = '2026-11-05T03:11:42'
hashes = {r['sha256'] for r in requested}
returns = []
for line in log.open():
    row = json.loads(line)
    if row.get('timestamp', '') < first_utc:
        continue
    payload = row.get('payload', {})
    if row.get('type') != 'response_item' or payload.get('type') != 'custom_tool_call_output' or not isinstance(payload.get('output'), list):
        continue
    for block in payload['output']:
        if block.get('type') != 'input_image':
            continue
        url = block.get('image_url')
        url = url.get('url') if isinstance(url, dict) else url
        if not isinstance(url, str) or not url.startswith('data:'):
            continue
        data = base64.b64decode(url.split(',', 1)[1])
        h = hashlib.sha256(data).hexdigest()
        if h in hashes:
            dimensions = list(Image.open(io.BytesIO(data)).size)
            assert dimensions == [1920, 1080]
            returns.append(dict(call_id=payload['call_id'], timestamp=row['timestamp'], sha256=h, dimensions=dimensions))
expected = collections.Counter(r['sha256'] for r in reads)
actual = collections.Counter(r['sha256'] for r in returns)
assert actual == expected, dict(expected=expected, actual=actual)
assert [r['sha256'] for r in returns] == [r['sha256'] for r in reads], 'Actual returned-byte order differs from claimed saved receipt order'
audit = dict(recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), saved_output=str(out_path.relative_to(R)),
             saved_output_sha256=hashlib.sha256(out_path.read_bytes()).hexdigest(), rollout_log=str(log), earliest_scope_utc=first_utc,
             requested_cases=len(expected_ids), requested_paths=len(requested), completed_case_ids=[r['id'] for r in o['items'] if r['id'] not in o['pending_case_ids']],
             pending_case_ids=o['pending_case_ids'], pending_paths=pending, actual_native_fullframe_returns=len(returns), actual_scaled_returns=0,
             schema_ids_fields_request_coverage='PASS', actual_bytehash_order_multiplicity_and_1920x1080='PASS', returns=returns,
             method='Compare actual image dataURL bytes from saved custom_tool_call_output input_image blocks to saved request/receipt SHA256, exact order and multiplicity. PNG file presence alone is not a successful image read.',
             semantic_review_scope='Independent delegated native-pair review; root integration validates taxonomy/limits and separately records any repeat visual spots. No global semantic/all-frame certification.',
             actual_listening_seconds=0, CT_SCAN_COMPLETE=False)
dest = R / 'session_20261105' / (label + '_independent_return_audit_v1.json')
assert not dest.exists()
dest.write_text(json.dumps(audit, indent=2)+'\n')
print('PASS', label, 'cases', len(audit['completed_case_ids']), 'native actual returns', len(returns), 'pending', len(pending))
