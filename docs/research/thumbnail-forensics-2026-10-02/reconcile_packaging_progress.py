"""Rebuild current rollups from exact-ID verified records; preserve research history."""
import csv
import hashlib
import json
from pathlib import Path

from packaging_audit_records import verified_records

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def read_csv(path):
    return list(csv.DictReader(path.open()))


def write_csv(path, rows):
    with path.open('w', newline='') as file:
        writer = csv.DictWriter(file, list(rows[0]), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


def qa_video_ids(root=HERE):
    ids = set()
    def walk(value):
        if isinstance(value, dict):
            if value.get('verdict') in ('PASS', 'PASS_WITH_CORRECTIONS') and value.get('Package_ID'):
                ids.add(value['Package_ID'].removeprefix('PKG-'))
            if value.get('result') in ('PASS', 'PASS_WITH_CORRECTIONS') and value.get('Video_ID'):
                ids.add(value['Video_ID'])
            for item in value.values():
                walk(item)
        elif isinstance(value, list):
            for item in value:
                walk(item)
    for file in sorted(root.glob('package-qa-review-*.json')) + sorted(root.glob('channels/*/qa.json')):
        walk(json.loads(file.read_text()))
    return ids


def rebuild(root=HERE, repo=ROOT):
    root, repo = Path(root), Path(repo)
    thumbs, packages = verified_records(root)
    master = read_csv(root / 'master-packages.csv')
    video_map = {row['Video_ID']: row for row in master}
    assert len(video_map) == len(master)
    qa = qa_video_ids(root)
    assert qa <= {row['Video_ID'] for row in packages.values()}
    queue = read_csv(root / 'channel-processing-queue.csv')
    for row in queue:
        channel = row['Channel_ID']
        videos = [v for v in master if v['Channel_ID'] == channel]
        row['Existing_Verified_Thumbnail_Audits'] = str(sum(v['Thumbnail_ID'] in thumbs for v in videos))
        row['Existing_Package_Audits'] = str(sum(v['Package_ID'] in packages for v in videos))
        row['Existing_Package_QA'] = str(sum(v['Video_ID'] in qa for v in videos))
        if row['Channel_Status'] == 'COMPLETE':
            assert videos and all(v['Thumbnail_ID'] in thumbs and v['Package_ID'] in packages and v['Video_ID'] in qa for v in videos)
    write_csv(root / 'channel-processing-queue.csv', queue)
    summary = json.loads((root / 'packaging-progress-summary.json').read_text())
    summary['titles']['done'] = len(read_csv(root / 'title-analyst-audit.csv'))
    summary['thumbnails']['verified'] = len(thumbs)
    summary['packages'].update(audited=len(packages), qa_sampled=len(qa))
    summary['thumbnails']['remaining'] = summary['thumbnails']['eligible'] - len(thumbs)
    summary['packages']['remaining'] = summary['packages']['eligible'] - len(packages)
    summary['channels']['complete'] = sum(row['Channel_Status'] == 'COMPLETE' for row in queue)
    summary['reconciliation_basis'] = 'Exact-ID QA-gated legacy and channel union; drafts preserved separately; no new visual review'
    progress = summary['progress']
    progress.update(title=summary['titles']['done']/summary['titles']['eligible'], thumbnail=len(thumbs)/summary['thumbnails']['eligible'], package=len(packages)/summary['packages']['eligible'], qa=len(qa)/summary['packages']['eligible'])
    progress['composite'] = sum(progress[k] for k in ('title', 'thumbnail', 'package', 'qa')) / 4
    delta = []
    for file in sorted(root.glob('channels/*/package-audits.json')):
        for item in json.loads(file.read_text()):
            video = video_map[item['Video_ID']]
            delta.append(dict(Video_ID=item['Video_ID'], Thumbnail_ID=item['Thumbnail_ID'], Channel_ID=video['Channel_ID'], audit_source=str(file.with_name('thumbnail-audits.json').relative_to(root)), package_source=str(file.relative_to(root)), QA_state='PASS_WITH_CORRECTIONS' if next(r for r in json.loads(file.with_name('qa.json').read_text())['reviews'] if r['Video_ID']==item['Video_ID'])['result']=='PASS_WITH_CORRECTIONS' else 'PASS', included_in_518=True, included_in_legacy_510=False, reason='Legacy generators globbed top-level wave files only; channel overlay omitted'))
    write_csv(root / 'rollup-reconciliation.csv', delta)
    # Hash registry describes current bytes, not historical snapshots. Changes require
    # the separate hash-reconciliation record, including the committed LFS object.
    derived = {'master-packages.csv', 'channel-coverage.csv', 'channel-packaging-profiles.csv', 'package-forensics.json', 'packaging-quadrants.csv'}
    approvals = {r['path']: r['approved_sha256'] for r in json.loads((root / 'hash-reconciliation.json').read_text())['approved_source_corrections']}
    for path, old_hash in summary['source_SHA256'].items():
        actual = hashlib.sha256((repo / path).read_bytes()).hexdigest()
        if actual != old_hash and Path(path).name not in derived and approvals.get(path) != actual:
            raise ValueError('Unexplained dashboard hash drift: ' + path)
        summary['source_SHA256'][path] = actual
    (root / 'packaging-progress-summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps({'titles': summary['titles']['done'], 'thumbnails':len(thumbs), 'packages':len(packages), 'qa':len(qa), 'delta':len(delta), 'hashes':len(summary['source_SHA256'])}))


if __name__ == '__main__':
    rebuild()
