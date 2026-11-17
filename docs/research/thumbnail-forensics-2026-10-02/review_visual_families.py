"""Record the manual side-by-side review of all 176 perceptual-hash candidates (reviewed 2026-10-04).

Default verdict after viewing every pair: TEMPLATE_FAMILY (same layout/portrait/character, different text or
object). Overrides below are the pairs where the images are the same creative, a text/overlay variant, or
not related (pillarboxed vertical-Shorts thumbnails whose blurred side bars drive the hash).
"""
import csv
from collections import defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent
SAME = {'VFC-005': 'Identical artwork on two different videos of the same channel', 'VFC-163': 'Near-identical artwork on videos of two different channels'}
VARIANT = {'VFC-042': 'Overlay text added ($500 EVERY MONTH) on otherwise same scene', 'VFC-064': 'Same scene; label/arrow and cap marking differ',
           'VFC-114': 'Same scene, animals reordered and headline reworded'}
NOT_SAME = {'VFC-041': 'pillarboxed Shorts; hash driven by blurred side bars', 'VFC-067': 'pillarboxed Shorts; blurred bars', 'VFC-083': 'pillarboxed Shorts; blurred bars',
            'VFC-084': 'pillarboxed Shorts; blurred bars', 'VFC-086': 'pillarboxed Shorts; blurred bars', 'VFC-145': 'pillarboxed Shorts; blurred bars'}
rows = list(csv.DictReader((HERE / 'visual-family-candidates.csv').open()))
par = {}
def find(x):
    par.setdefault(x, x)
    while par[x] != x: par[x] = par[par[x]]; x = par[x]
    return x
for r in rows:
    k = r['Candidate_ID']
    if k in SAME: st, note, typ = 'VERIFIED_SAME_CREATIVE', SAME[k], 'SAME_CREATIVE_DIFFERENT_VIDEO'
    elif k in VARIANT: st, note, typ = 'VERIFIED_VARIANT', VARIANT[k], 'TEXT_VARIANT'
    elif k in NOT_SAME: st, note, typ = 'NOT_SAME', NOT_SAME[k], 'OTHER_SIMILARITY'
    else: st, note, typ = 'TEMPLATE_FAMILY', 'Same template/character/portrait layout; text or hero object differs', 'SAME_TEMPLATE'
    r.update(Reviewer_Status=st, Review_Notes=note, Candidate_Type=typ)
    if st != 'NOT_SAME': par[find(r['Thumbnail_ID_A'])] = find(r['Thumbnail_ID_B'])
fam = defaultdict(set)
for r in rows:
    if r['Reviewer_Status'] != 'NOT_SAME': fam[find(r['Thumbnail_ID_A'])] |= {r['Thumbnail_ID_A'], r['Thumbnail_ID_B']}
fid = {}
for n, (root, mem) in enumerate(sorted(fam.items(), key=lambda kv: sorted(kv[1])[0]), 1):
    for m in mem: fid[m] = f'VF-{n:03d}'
for r in rows: r['Visual_Family_ID'] = fid.get(r['Thumbnail_ID_A'], '') if r['Reviewer_Status'] != 'NOT_SAME' else ''
with (HERE / 'visual-family-candidates.csv').open('w', newline='') as f:
    w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
U = {r['Thumbnail_ID']: r for r in csv.DictReader((HERE / 'thumbnail-universe.csv').open()) if r['Thumbnail_ID']}
status = defaultdict(set)
for r in rows:
    if r['Reviewer_Status'] != 'NOT_SAME':
        for t in (r['Thumbnail_ID_A'], r['Thumbnail_ID_B']): status[t].add(r['Reviewer_Status'])
rank = ['VERIFIED_SAME_CREATIVE', 'VERIFIED_VARIANT', 'TEMPLATE_FAMILY']
reg = [dict(Visual_Family_ID=fid[t], Thumbnail_ID=t, Video_ID=U[t]['Video_ID'], Channel_ID=U[t]['Channel_ID'], Title=U[t]['Title'],
            Member_Evidence=sorted(status[t], key=rank.index)[0], Reviewer_Status='MANUALLY_REVIEWED', Scope='perceptual-hash candidates only (pHash<=10, dHash<=14)')
       for t in sorted(fid, key=lambda t: (fid[t], t))]
with (HERE / 'visual-family-register.csv').open('w', newline='') as f:
    w = csv.DictWriter(f, list(reg[0])); w.writeheader(); w.writerows(reg)
from collections import Counter
print(Counter(r['Reviewer_Status'] for r in rows), len(set(fid.values())), 'families', len(fid), 'members')
