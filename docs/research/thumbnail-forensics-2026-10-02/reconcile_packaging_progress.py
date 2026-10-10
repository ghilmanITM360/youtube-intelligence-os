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


def dashboard_payload(root=HERE):
    """Derive current dashboard from the exact-ID audit union, never cached totals."""
    root = Path(root)
    thumbs, packages = verified_records(root)
    master = read_csv(root / 'master-packages.csv')
    assert len({row['Video_ID'] for row in master}) == len(master)
    qa = qa_video_ids(root)
    assert qa <= {row['Video_ID'] for row in packages.values()}
    titles = {row['Video_ID'] for row in read_csv(root / 'title-analyst-audit.csv')}
    queue = read_csv(root / 'channel-processing-queue.csv')
    for video in master:
        thumb = thumbs.get(video['Thumbnail_ID'])
        package = packages.get(video['Package_ID'])
        video['Thumbnail_Audit_Status'] = 'AUDITED' if thumb else 'NOT_AUDITED'
        video['Packaging_Audit_Status'] = 'AUDITED' if package else 'NOT_AUDITED'
        if thumb:
            video['Thumbnail_Diagnostic_Score'] = thumb[1]['score_100']
        if package:
            video['EXPERT_PACKAGING_DIAGNOSTIC_SCORE'] = package['score_100']
        video['QA_Status'] = 'PASS' if video['Video_ID'] in qa else 'QA_PENDING'
        video['Title_Status'] = 'TITLE_DONE' if video['Video_ID'] in titles else 'NOT_STARTED'
        video['Current_Status'] = 'COMPLETE' if thumb and package and video['Video_ID'] in qa else 'QA_PENDING' if package else 'NOT_STARTED'
    for row in queue:
        videos = [v for v in master if v['Channel_ID'] == row['Channel_ID']]
        row['Existing_Title_Audits'] = str(sum(v['Video_ID'] in titles for v in videos))
        row['Existing_Verified_Thumbnail_Audits'] = str(sum(v['Thumbnail_ID'] in thumbs for v in videos))
        row['Existing_Package_Audits'] = str(sum(v['Package_ID'] in packages for v in videos))
        done = sum(v['Current_Status'] == 'COMPLETE' for v in videos)
        row['Existing_Package_QA'] = str(done)
        row['Videos_Remaining'] = str(len(videos) - done)
        if videos and done == len(videos):
            row['Channel_Status'] = 'COMPLETE'
        elif row['Channel_Status'] == 'COMPLETE':
            row['Channel_Status'] = 'IN_PROGRESS'
    active = sorted((row for row in queue if int(row['Videos_Remaining']) > 0 and row['Channel_Status'] not in ('IDENTITY_ONLY', 'INSUFFICIENT_DATA')), key=lambda row: int(row['Channel_Order']))
    current = {}
    if active:
        row = active[0]
        videos = [v for v in master if v['Channel_ID'] == row['Channel_ID']]
        remaining = [v for v in videos if v['Current_Status'] != 'COMPLETE']
        # QA of existing packages first, then verified thumbnails, then new work.
        remaining.sort(key=lambda v: (0 if v['Package_ID'] in packages else 1 if v['Thumbnail_ID'] in thumbs else 2, v['Video_ID']))
        next_video = remaining[0]
        current = dict(order=int(row['Channel_Order']), Channel_ID=row['Channel_ID'], name=row['Channel_Name'], videos=len(videos), next_Video_ID=next_video['Video_ID'], next_Thumbnail_ID=next_video['Thumbnail_ID'], completed_videos=int(row['Existing_Package_QA']), remaining_videos=len(remaining), progress=sum(float(row[key]) / len(videos) for key in ('Existing_Title_Audits', 'Existing_Verified_Thumbnail_Audits', 'Existing_Package_Audits', 'Existing_Package_QA')) / 4, status=row['Channel_Status'])
    return dict(research_root=str(root.resolve()), queue=queue, master=master, qa_ids=sorted(qa), current_channel=current, totals=dict(titles=len(titles), thumbnails=len(thumbs), packages=len(packages), qa=len(qa), channels_complete=sum(row['Channel_Status'] == 'COMPLETE' for row in queue)))


def rebuild(root=HERE, repo=ROOT):
    root, repo = Path(root), Path(repo)
    thumbs, packages = verified_records(root)
    master = read_csv(root / 'master-packages.csv')
    video_map = {row['Video_ID']: row for row in master}
    assert len(video_map) == len(master)
    qa = qa_video_ids(root)
    assert qa <= {row['Video_ID'] for row in packages.values()}
    data = dashboard_payload(root)
    queue = data['queue']
    write_csv(root / 'channel-processing-queue.csv', queue)
    summary = json.loads((root / 'packaging-progress-summary.json').read_text())
    summary['titles']['done'] = data['totals']['titles']
    summary['thumbnails']['verified'] = len(thumbs)
    summary['packages'].update(audited=len(packages), qa_sampled=len(qa))
    summary['thumbnails']['remaining'] = summary['thumbnails']['eligible'] - len(thumbs)
    summary['packages']['remaining'] = summary['packages']['eligible'] - len(packages)
    summary['channels']['complete'] = sum(row['Channel_Status'] == 'COMPLETE' for row in queue)
    summary['current_channel'] = data['current_channel']
    summary['next_channel'] = next((row for row in queue if row['Channel_ID'] == data['current_channel'].get('Channel_ID')), {})
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
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--payload', type=Path)
    args = parser.parse_args()
    rebuild()
    if args.payload:
        args.payload.parent.mkdir(parents=True, exist_ok=True)
        args.payload.write_text(json.dumps(dashboard_payload(), indent=2) + '\n')
