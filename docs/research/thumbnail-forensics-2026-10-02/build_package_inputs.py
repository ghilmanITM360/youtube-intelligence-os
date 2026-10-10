"""Plan package-audit batches (PK-NN, 24 packages each) over videos whose thumbnail audit is VERIFIED, and write reviewer inputs to the scratchpad.

Eligible = master-packages rows with a verified thumbnail audit (batches listed in package-batch-plan.json `verified_thumbnail_batches`; edit that list only after a wave clears QA).
Existing PK batches are never reshuffled; new eligible packages are appended as new PK-NN. Reviewer inputs are BLIND to views/performance. Usage: build_package_inputs.py [add_batch ...]
"""
import csv, glob, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCR = Path('/private/tmp/claude-501/-Users-ghilmankhan-workprojects-youtube-intelligence-os/e9d5fa3f-9fa3-4acc-b7cf-207755ab01a1/scratchpad')
PLAN = HERE / 'package-batch-plan.json'
SIZE = 24
TH = ['text', 'scene', 'partnership', 'mechanism', 'hierarchy_clear', 'mobile_readability_160', 'text_density', 'face_visible', 'face_scale', 'art_style', 'title_relation', 'reveal_too_much_risk', 'medical_label', 'score_100']
TT = ['core_topic', 'exact_promise', 'intended_viewer', 'unanswered_question', 'orientation', 'overpromise_risk', 'medical_title_flag', 'ANALYST_TITLE_DIAGNOSTIC_SCORE']


def thumb_rows():
    from packaging_audit_records import verified_records
    return verified_records(HERE)[0]


def view_path(tid, batch):
    if batch == 'B001': return None
    inp = SCR / 'audit' / batch / 'input.json'
    for i in json.load(inp.open()):
        if i['Thumbnail_ID'] == tid: return i['View_Path']


def main():
    plan = json.load(PLAN.open()) if PLAN.exists() else dict(verified_thumbnail_batches=['B001'] + [f'B002-{n:02d}' for n in range(1, 13)], batches={})
    for b in sys.argv[1:]:
        if b not in plan['verified_thumbnail_batches']: plan['verified_thumbnail_batches'].append(b)
    mp = {r['Thumbnail_ID']: r for r in csv.DictReader((HERE / 'master-packages.csv').open()) if r['Thumbnail_ID']}
    ta = {r['Video_ID']: r for r in csv.DictReader((HERE / 'title-analyst-audit.csv').open())}
    uni = {r['Thumbnail_ID']: r for r in csv.DictReader((HERE / 'thumbnail-universe.csv').open()) if r['Thumbnail_ID']}
    tr = thumb_rows()
    planned = {p for v in plan['batches'].values() for p in v}
    elig = [(b, r['Thumbnail_ID'], r.get('seq', 0)) for t, (b, r) in tr.items() if b in plan['verified_thumbnail_batches'] and t in mp and mp[t]['Package_ID'] not in planned for r in [r]]
    elig.sort(key=lambda x: (x[0], x[2]))
    ids = [mp[t]['Package_ID'] for _, t, _ in elig]
    n0 = len(plan['batches'])
    for k in range(0, len(ids), SIZE):
        plan['batches'][f'PK-{n0 + k // SIZE + 1:02d}'] = ids[k:k + SIZE]
    PLAN.write_text(json.dumps(plan, indent=1))
    by_pkg = {m['Package_ID']: m for m in mp.values()}
    (SCR / 'packages').mkdir(exist_ok=True)
    for pk, pids in plan['batches'].items():
        items = []
        for j, pid in enumerate(pids, 1):
            m = by_pkg[pid]; b, r = tr[m['Thumbnail_ID']]; a = ta[m['Video_ID']]
            vp = view_path(m['Thumbnail_ID'], b) or str(HERE.parents[2] / uni[m['Thumbnail_ID']]['Source_Path'])
            items.append(dict(seq=j, Package_ID=pid, Video_ID=m['Video_ID'], Thumbnail_ID=m['Thumbnail_ID'], Title=m['Title_Current'], Channel_Name=m['Channel_Name'], Niche=m['Niche'], Format=m['Format'],
                              Creative_Temporal_Alignment=m['Creative_Temporal_Alignment'], Image_Path=vp, Thumbnail_Batch=b, thumbnail_audit={k: r.get(k) for k in TH}, title_audit={k: a.get(k) for k in TT}))
        (SCR / 'packages' / f'{pk}.json').write_text(json.dumps(items, indent=1))
    print(len(ids), 'new packages;', len(plan['batches']), 'PK batches;', 'verified thumbnail batches', len(plan['verified_thumbnail_batches']))


if __name__ == '__main__': main()
