"""One exact-ID, QA-gated union for legacy waves and channel audit overlays.

Raw images are not read by derived rollup generation. Revalidation is separate.
Channel successors may replace a preserved legacy draft only with explicit QA.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def verified_records(root=HERE):
    root = Path(root)
    allowed = set(json.loads((root / 'package-batch-plan.json').read_text())['verified_thumbnail_batches'])
    thumbs, packages = {}, {}
    files = [root / 'individual-audit-batch-001.json'] + sorted(root.glob('audit-batch-B002-*.json'))
    for file in files:
        batch = file.stem.replace('audit-batch-', '') if file.name != 'individual-audit-batch-001.json' else 'B001'
        if batch not in allowed:
            continue
        for row in json.loads(file.read_text()):
            key = row['Thumbnail_ID']
            if key in thumbs:
                raise ValueError('Duplicate verified thumbnail: ' + key)
            thumbs[key] = (batch, row)
    for file in sorted(root.glob('package-audit-PK-*.json')):
        for row in json.loads(file.read_text()):
            key = row['Package_ID']
            if key in packages:
                raise ValueError('Duplicate verified package: ' + key)
            if row['Thumbnail_ID'] not in thumbs:
                raise ValueError('Package lacks verified thumbnail: ' + key)
            packages[key] = row
    for file in sorted(root.glob('channels/*/thumbnail-audits.json')):
        reviews = json.loads(file.with_name('qa.json').read_text())['reviews']
        reviewed = {r['Thumbnail_ID']: r for r in reviews if r.get('result') in ('PASS', 'PASS_WITH_CORRECTIONS')}
        for row in json.loads(file.read_text()):
            key = row['Thumbnail_ID']
            review = reviewed.get(key)
            if not review or row.get('qa_status') not in ('PRIMARY_SEQUENTIAL_QA_PASS', 'PRIMARY_SEQUENTIAL_QA_PASS_WITH_CORRECTIONS'):
                raise ValueError('Channel overlay lacks explicit QA: ' + key)
            if key in thumbs and not (review.get('legacy_draft_preserved') and review.get('legacy_draft_source')):
                raise ValueError('Unexplained verified-thumbnail successor: ' + key)
            thumbs[key] = (row['batch_id'], row)
        for row in json.loads(file.with_name('package-audits.json').read_text()):
            key = row['Package_ID']
            review = reviewed.get(row['Thumbnail_ID'])
            if not review or review['Video_ID'] != row['Video_ID'] or key != 'PKG-' + row['Video_ID']:
                raise ValueError('Channel package identity/QA mismatch: ' + key)
            if key in packages:
                raise ValueError('Duplicate verified package: ' + key)
            if row['Thumbnail_ID'] not in thumbs:
                raise ValueError('Channel package lacks verified thumbnail: ' + key)
            packages[key] = row
    return thumbs, packages
