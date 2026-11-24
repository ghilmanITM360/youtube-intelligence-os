"""Phase 5: recompute families, Short->long reuse and per-script metrics from the raw 83 transcripts.
Read-only on the repo. Run: python3 -I phase5_corpus.py
"""
import csv, json, re, statistics as st
from pathlib import Path
R = Path('/Users/ghilmanislam360/Documents/youtube-intelligence-os/research/what-if-scripts')
OUT = Path(__file__).resolve().parent.parent
inv = json.loads((R / 'analysis/inventory.json').read_text())
census = {r['video_id']: r for r in csv.DictReader(open('/Users/ghilmanislam360/Documents/youtube-intelligence-os/research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/census/census.csv'))}

def body(r):
    t = (R / r['script']).read_text().split('## Script\n', 1)[1]
    return t
def toks(t): return re.findall(r"[a-z0-9']+", t.lower())
def grams(w, n=8): return {tuple(w[i:i+n]) for i in range(len(w)-n+1)}

V = {}
for r in inv:
    t = body(r); w = toks(t)
    V[r['vid']] = dict(r=r, text=t, w=w, g=grams(w), paras=[p for p in t.split('\n\n') if p.strip()])

# containment of each Short in every other video (8-gram), best parent
rows = []; link = {}
for vid, d in V.items():
    best = (0, None)
    for o, e in V.items():
        if o == vid or not d['g']: continue
        if d['r']['format'] != 'long' and e['r']['format'] != 'long': continue  # parents are long videos
        if d['r']['format'] == 'long' and e['r']['format'] != 'long': continue
        c = len(d['g'] & e['g']) / len(d['g'])
        if c > best[0]: best = (c, o)
    rows.append((vid, d['r']['format'], best[1], round(best[0], 3)))
    if best[0] >= 0.30: link[vid] = best[1]

# union-find families
par = {v: v for v in V}
def f(x):
    while par[x] != x: par[x] = par[par[x]]; x = par[x]
    return x
for a, b in link.items(): par[f(a)] = f(b)
fam = {}
for v in V: fam.setdefault(f(v), []).append(v)
fam_id = {}
for i, (k, vs) in enumerate(sorted(fam.items(), key=lambda kv: min(kv[1])), 1):
    for v in vs: fam_id[v] = f'F{i:02d}'

with open(OUT / '05_FAMILY_AND_REUSE_TABLE.csv', 'w', newline='') as fh:
    w = csv.writer(fh); w.writerow(['vid', 'video_id', 'format', 'family', 'best_parent', 'containment_8gram', 'role'])
    for vid, fmt, p, c in rows:
        role = 'LONG_ROOT' if fmt == 'long' and c < .30 else ('LONG_OVERLAPS_LONG' if fmt == 'long' else ('DERIVED_SHORT' if c >= .30 else 'INDEPENDENT_SHORT'))
        w.writerow([vid, V[vid]['r']['id'], fmt, fam_id[vid], p if c >= .30 else '', c, role])

# per-script metrics
mrows = []
unit = re.compile(r"\b(km|kilomet|meter|metre|mile|kilogram|tons?|joules?|watts?|megaton|degrees|percent|miles per hour|mph|seconds?|hours?|years?)\w*", re.I)
for vid, d in V.items():
    r = d['r']; w = d['w']; t = d['text']; n = len(t.split())  # whitespace words = inventory definition
    first = re.split(r'(?<=[.?!])\s', d['paras'][0].strip())[0] if d['paras'] else ''
    dur = r['duration']; h, m_, s = map(int, dur.split(':')); secs = h*3600+m_*60+s
    cen = census.get(r['id'], {})
    mrows.append(dict(vid=vid, video_id=r['id'], format=r['format'], words=n, duration_s=secs, wps=round(n/secs, 2) if secs else '',
        paragraphs=len(d['paras']), question_marks=t.count('?'), numerals_per_100w=round(100*len(re.findall(r'\d', t))/max(n, 1), 1),
        you_per_100w=round(100*sum(1 for x in w if x in ('you', "you'd", "you're", "you'll", 'your'))/max(n, 1), 1),
        opens_attributed=int(bool(re.search(r"(question|asks?|asked|writes?|wants to know)\b.{0,40}\b(from|by)\b|comes from|\bfrom [A-Z][a-z]+", ' '.join(d['paras'][:2])))),
        has_technically=int('technically' in w), has_unfortunately=int('unfortunately' in w),
        family=fam_id[vid], views_2026_11_04=cen.get('views_player', '')))
with open(OUT / '05_SCRIPT_METRICS.csv', 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(mrows[0])); w.writeheader(); w.writerows(mrows)

# summary
L = [m for m in mrows if m['format'] == 'long']; S = [m for m in mrows if m['format'] != 'long']
def s(x): return f"n={len(x)} median={st.median(x)} min={min(x)} max={max(x)}"
print('families', len(fam), 'multi-member', sum(len(v) > 1 for v in fam.values()))
print('roles', {k: sum(1 for r in csv.DictReader(open(OUT/'05_FAMILY_AND_REUSE_TABLE.csv')) if r['role']==k) for k in ('LONG_ROOT','LONG_OVERLAPS_LONG','DERIVED_SHORT','INDEPENDENT_SHORT')})
print('LONG words', s([m['words'] for m in L]), 'dur', s([m['duration_s'] for m in L]), 'wps', s([m['wps'] for m in L]))
print('SHORT words', s([m['words'] for m in S]), 'dur', s([m['duration_s'] for m in S]), 'wps', s([m['wps'] for m in S]))
print('paras long', s([m['paragraphs'] for m in L]), 'qmarks long', s([m['question_marks'] for m in L]), 'numerals/100w', s([m['numerals_per_100w'] for m in L]))
print('you/100w long', s([m['you_per_100w'] for m in L]))
print('attributed regex long', sum(m['opens_attributed'] for m in L), 'of', len(L), '| short', sum(m['opens_attributed'] for m in S), 'of', len(S))
print('technically in long', sum(m['has_technically'] for m in L), 'unfortunately', sum(m['has_unfortunately'] for m in L))
shorts_by_parent = {}
for vid, fmt, p, c in rows:
    if fmt != 'long' and c >= .30: shorts_by_parent.setdefault(p, []).append((vid, c))
print('shorts per parent', sorted(((p, len(v)) for p, v in shorts_by_parent.items()), key=lambda x: -x[1])[:10], 'parents', len(shorts_by_parent))
print('containment of derived shorts: ', s([round(c, 2) for vid, fmt, p, c in rows if fmt != 'long' and c >= .3]))
print('indep shorts', [(vid, c) for vid, fmt, p, c in rows if fmt != 'long' and c < .30])
print('long overlapping long', [(vid, p, c) for vid, fmt, p, c in rows if fmt == 'long' and c >= .30])
print('longs with no short', len([m for m in L if m['vid'] not in shorts_by_parent]))
