"""Recover this channel's existing work; validate new rows without rewriting legacy research."""
import csv, hashlib, importlib.util, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESEARCH = HERE.parents[1]
ROOT = RESEARCH.parents[2]
CHANNEL = HERE.name

def readcsv(name):
    return list(csv.DictReader((RESEARCH / name).open()))

def load_validator(name):
    spec = importlib.util.spec_from_file_location(name, RESEARCH / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    videos = sorted((r for r in readcsv('master-packages.csv') if r['Channel_ID'] == CHANNEL), key=lambda r: r['Video_ID'])
    universe = {r['Thumbnail_ID']: r for r in readcsv('thumbnail-universe.csv')}
    crosswalk = {r['Thumbnail_ID']: r for r in readcsv('legacy-batch-to-channel.csv')}
    oldthumb = {}
    oldpkg = {}
    for file in sorted(RESEARCH.glob('audit-batch-B002-*.json')):
        for row in json.loads(file.read_text()):
            oldthumb[row['Thumbnail_ID']] = row
    for file in sorted(RESEARCH.glob('package-audit-PK-*.json')):
        for row in json.loads(file.read_text()):
            oldpkg[row['Video_ID']] = row
    qa_ids = set()
    for file in RESEARCH.glob('package-qa-review-*.json'):
        data = json.loads(file.read_text())
        def walk(obj):
            if isinstance(obj, dict):
                if obj.get('Video_ID'): qa_ids.add(obj['Video_ID'])
                if obj.get('Package_ID') and ('verdict' in obj or 'image_matches_thumbnail_description' in obj):
                    qa_ids.add(obj['Package_ID'].removeprefix('PKG-'))
                for value in obj.values(): walk(value)
            elif isinstance(obj, list):
                for value in obj: walk(value)
        walk(data)
    newthumb = json.loads((HERE / 'thumbnail-audits.json').read_text())
    newpkg = json.loads((HERE / 'package-audits.json').read_text())
    qa = json.loads((HERE / 'qa.json').read_text()) if (HERE / 'qa.json').exists() else {'reviews': []}
    reviewed = {r['Video_ID'] for r in qa['reviews'] if r['result'] in ('PASS', 'PASS_WITH_CORRECTIONS')}
    nt = {r['Thumbnail_ID']: r for r in newthumb}
    np = {r['Video_ID']: r for r in newpkg}
    errors = []
    assert len(videos) == 10 and len({r['Video_ID'] for r in videos}) == 10
    assert len(nt) == len(newthumb) and len(np) == len(newpkg)
    superseded = set(nt) & set(oldthumb)
    provenance = {r['Thumbnail_ID'] for r in qa['reviews'] if r.get('legacy_draft_preserved') and r.get('legacy_draft_source') and r['result'] in ('PASS', 'PASS_WITH_CORRECTIONS')}
    assert superseded <= provenance, 'Legacy successors require explicit preserved-draft QA provenance'
    assert not set(np) & set(oldpkg), 'Never duplicate a legacy package'
    vmap = {r['Video_ID']: r for r in videos}
    for row in newthumb:
        u = universe[row['Thumbnail_ID']]
        assert u['Channel_ID'] == CHANNEL and u['Video_ID'] in vmap
        path = ROOT / u['Source_Path']
        assert path.exists() and hashlib.sha256(path.read_bytes()).hexdigest() == u['SHA256'] == row['Thumbnail_ID'][4:]
    te, tf = load_validator('validate_audit_batch').validate(newthumb)
    pe, pf = load_validator('validate_package_audit').validate(newpkg, [vmap[r['Video_ID']] for r in newpkg])
    errors += te + pe
    adjudicated={r['Thumbnail_ID'][:16]+' '+w['code'] for r in qa['reviews'] for w in r.get('warnings',[]) if w['disposition'] in ('RESOLVED','EXPLICITLY_ACCEPTED_WITH_REASON')}
    unresolved=[w for w in tf['consistency_warnings'] if w not in adjudicated]
    errors += ['UNRESOLVED_WARNING '+w for w in unresolved]
    manifest = []
    for order, v in enumerate(videos, 1):
        tid, vid = v['Thumbnail_ID'], v['Video_ID']
        legacy = crosswalk.get(tid, {})
        verified = legacy.get('Legacy_Status') == 'VERIFIED' or vid in reviewed
        thumb = nt.get(tid, oldthumb.get(tid))
        package = np.get(vid, oldpkg.get(vid))
        sampled = vid in qa_ids or vid in reviewed
        ts = 'THUMBNAIL_VERIFIED' if verified else 'THUMBNAIL_DRAFT' if thumb else 'NOT_STARTED'
        ps = 'PACKAGE_AUDITED' if package else 'NOT_STARTED'
        qs = 'PASS' if vid in reviewed else 'HISTORICAL_SAMPLE' if sampled else 'QA_PENDING' if package else 'NOT_STARTED'
        complete = verified and package is not None and sampled
        manifest.append(dict(Video_Order=order, Video_ID=vid, Title=v['Title_Current'], Title_Status='TITLE_DONE', Thumbnail_ID=tid,
            Thumbnail_Status=ts, Package_Status=ps, QA_Status=qs, Legacy_B002_Batch=legacy.get('B002_Batch',''),
            Legacy_B002_Seq=legacy.get('Seq',''), Needs_Work='NONE' if complete else '|'.join(x for x,b in [('THUMBNAIL',not verified),('PACKAGE',package is None),('QA',not sampled)] if b),
            Source_Path=universe[tid]['Source_Path'], Source_SHA=universe[tid]['SHA256'], Title_Score=v['ANALYST_TITLE_DIAGNOSTIC_SCORE'],
            Thumbnail_Score=thumb['score_100'] if thumb else '', Package_Score=package['score_100'] if package else '',
            Performance_Class=v['Relative_Performance_Class'], Evidence_Tier=v['Evidence_Tier'], Perf_Percentile_Age_Matched=v['Perf_Percentile_Age_Matched'],
            Creative_Temporal_Alignment=v['Creative_Temporal_Alignment'], Medical_Packaging_Status=package.get('medical_package_label','NOT_ASSESSED') if package else 'NOT_ASSESSED',
            Current_Status='COMPLETE' if complete else 'QA_PENDING' if package else ts if thumb else 'TITLE_DONE'))
    with (HERE / 'packaging-progress.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(manifest[0]), lineterminator='\n'); writer.writeheader(); writer.writerows(manifest)
    result = dict(channel=CHANNEL, videos=10, new_thumbnail_rows=len(newthumb), new_package_rows=len(newpkg), reviewed=len(reviewed), errors=errors, unresolved_warnings=unresolved, thumbnail_flags=tf, package_flags=pf,
                  source_hashes='PASS', mappings='PASS', legacy_preserved='PASS', result='PASS' if not errors else 'FAIL')
    (HERE / 'validation.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=1))
    if errors: raise SystemExit(1)

if __name__ == '__main__': main()
