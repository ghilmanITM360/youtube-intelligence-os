"""Append-only continuation from frozen receipts; no transfer or source mutation."""
from pathlib import Path
import datetime, hashlib, json, subprocess, sys

R = Path(__file__).parent
a = json.loads(sys.argv[1])
d = Path(a['control']['checkpoint_dir'])
assert d.parent == R and not (d / 'CONTINUATION.json').exists()
previous = max(R.glob('checkpoint-*/CONTINUATION.json'), key=lambda p: p.parent.name)
v = json.loads(previous.read_text())
s = json.loads(subprocess.check_output(['python3', str(R/'continue_backup.py'), 'state', '{}'], text=True))
assert s['uploaded_bytes_including_controls'] == s['verified_bytes_including_controls']
latest = max(int(p.name.split('-')[1]) for p in R.glob('batch-*'))
for n in range(v['latest_verified_batch'] + 1, latest + 1):
    b = json.loads((R/('batch-%04d' % n)/'RECEIPT.json').read_text())
    assert b['status'] == 'VERIFIED'
    v['source_remote_objects'] += sum(not z.get('duplicate_of_verified', False) for z in b['files'])
    for z in b['files']:
        if z.get('package_manifest'):
            m = json.loads(Path(z['package_manifest']).read_text())
            assert z['retrieval']['package_source_members_verified'] == len(m['members'])
            v['verified_archive_members'] += len(m['members'])
            v['logical_archive_member_bytes'] += sum(q['bytes'] for q in m['members'])
            v['covered_original_source_paths'] += len(m['members']) + len(m.get('duplicate_aliases', []))
        else:
            v['covered_original_source_paths'] += 1
controls = 183330 + sum(json.loads(p.read_text())['uploaded_bytes'] for p in R.glob('CONTROL-UPLOAD-*.json'))
total = s['uploaded_bytes_including_controls']
assert total <= 12000000000 and a['gate']['conservative_free_bytes'] >= 2000000000
source = total - controls
plan_path = max(R.glob('ORDERED_PLAN_V[0-9]*.json'), key=lambda p: int(p.stem.rsplit('_V', 1)[1]))
plan = json.loads(plan_path.read_text())
base = json.loads((R/'recovery-20261026-machine-b-handoff/SOURCE_TO_DRIVE_INVENTORY.json').read_text())
done = {z['source'] for z in base['files']}
for p in R.glob('batch-*/RECEIPT.json'):
    if int(p.parent.name.split('-')[1]) >= 10:
        done.update(z['source_absolute'] for z in json.loads(p.read_text())['files'])
pending = [z for z in plan['files'] if z['source_absolute'] not in done]
v.update(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    status='PILOT_AND_BATCHES1_%d_AND_ALL_MD_CONTROLS_VERIFIED' % latest,
    latest_verified_batch=latest, actual_uploaded_bytes_including_controls=total,
    independently_retrieved_sha256_verified_unique_bytes_including_controls=s['verified_bytes_including_controls'],
    source_payload_uploaded_bytes=source, source_payload_independently_verified_bytes=source,
    control_uploaded_bytes=controls, control_independently_verified_bytes=controls,
    control_remote_files=1+len(list(R.glob('CONTROL-UPLOAD-*.json'))), mapped_source_paths=s['mapped_source_paths'],
    remaining_payload_cap_bytes=12000000000-total, remaining_plan_objects=len(pending),
    newest_plan=plan_path.name, next_sequence=pending[0]['sequence'] if pending else None,
    latest_compact_receipt=a['control'], gate=a['gate'],
    helper_sha256=hashlib.sha256((R/'continue_backup.py').read_bytes()).hexdigest(),
    previous_immutable_checkpoint=str(previous.parent),
    coverage_count_basis='Direct path mappings plus archive member paths and explicit aliases; may include a path represented directly and in an archive. This is not a deduplicated unique-file/content count.',
    next_action='Fresh usage/owner/privacy/quota/disk/ownership gates then next ordered unique-basename bounded batch. No incomplete batch or unknown upload remains. Do not repeat verified uploads or inventory. After the selected plan continue approved unique recovery/LFS scope within cap/reserve.')
with (d/'CONTINUATION.json').open('x') as f:
    json.dump(v, f, indent=2, ensure_ascii=False)
(d/'CONTINUATION.json').chmod(0o400)
with (d/'SHA256SUMS').open('x') as f:
    for p in sorted(d.iterdir()):
        if p.name != 'SHA256SUMS' and p.is_file():
            f.write(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name+'\n')
(d/'SHA256SUMS').chmod(0o400)
for line in (d/'SHA256SUMS').read_text().splitlines():
    h, n = line.split('  ', 1)
    assert hashlib.sha256((d/n).read_bytes()).hexdigest() == h
print(json.dumps({k:v[k] for k in ['status','actual_uploaded_bytes_including_controls',
    'independently_retrieved_sha256_verified_unique_bytes_including_controls',
    'source_payload_uploaded_bytes','control_uploaded_bytes','source_remote_objects',
    'remaining_plan_objects','next_sequence']}, indent=2))
