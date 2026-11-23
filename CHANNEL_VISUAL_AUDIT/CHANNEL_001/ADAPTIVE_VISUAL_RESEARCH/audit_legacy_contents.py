"""Compare archived receipts and state timelines. Run beside the research CSVs."""
import collections
import csv
import hashlib
import json
from pathlib import Path

def rows(path):
    with open(path, newline='', encoding='utf-8-sig') as stream:
        return list(csv.DictReader(stream))

corpus = {r['sha256']: r for r in rows('FULL_CORPUS_VISUAL_CLASSIFICATION.csv')}
groups = collections.defaultdict(dict)
for receipt in rows('LEGACY_RESEARCH_INTEGRATION_REGISTER.csv'):
    path = Path(receipt['original_path'])
    content = path.read_bytes()
    if hashlib.sha256(content).hexdigest() != receipt['sha256']:
        raise ValueError(f'Changed legacy receipt: {path}')
    if not receipt['video_id']:
        continue
    entry = groups[receipt['video_id']]
    if receipt['scope'] == 'Historical Shorts ASR receipt':
        segments = json.loads(content)['segments']
        entry['asr_segments'] = len(segments)
        entry['asr_last_end'] = max((s['end'] for s in segments), default=0)
    elif path.name in {'SOURCE_IDENTITY_AND_MANIFEST.json', 'source_manifest.json'}:
        datum = json.loads(content)
        entry['source_sha256'] = datum.get('source_sha256', datum.get('sha256', ''))
    elif path.name == 'quality_gate.json':
        gate = json.loads(content)
        entry['gate_summary'] = gate.get('verdict', gate.get('overall_verdict', gate.get('overall_status', '')))
        entry['gate_fields'] = json.dumps(gate.get('gates', {}), sort_keys=True)
    elif path.name.lower() == 'visual_states.csv':
        entry[path.name] = rows(path)

fields = ['video_id','source_sha256','inventory_tier','inventory_id','state_count','state_copy_changed_rows','state_copy_frame_changes','asr_segments','asr_last_end','gate_summary','gate_fields']
with open('LEGACY_CONTENT_RECONCILIATION.csv', 'w', newline='') as output:
    writer = csv.DictWriter(output, fields, extrasaction='ignore')
    writer.writeheader()
    for video_id, entry in sorted(groups.items()):
        source = corpus.get(entry.get('source_sha256'), {})
        upper = entry.get('VISUAL_STATES.csv', [])
        lower = entry.get('visual_states.csv', [])
        entry.update(video_id=video_id, inventory_tier=source.get('tier',''), inventory_id=source.get('reconciled_video_id',''), state_count=len(upper))
        if upper and lower:
            differences = sum(a != b for a,b in zip(upper, lower))
            frame_changes = sum(any(a.get(k) != b.get(k) for k in ('start_frame', 'end_frame')) for a,b in zip(upper,lower))
            entry.update(state_copy_changed_rows=differences + abs(len(upper)-len(lower)), state_copy_frame_changes=frame_changes + abs(len(upper)-len(lower)))
        writer.writerow(entry)
