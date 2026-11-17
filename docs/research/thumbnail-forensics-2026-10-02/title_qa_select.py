"""Deterministic stratified sample for manual QA of the analyst title audit; writes title-qa-selection.json and reviewer packets.

Greedy coverage: hash-ordered candidates, each round picks the row that fills the most unmet stratum quotas. Usage: title_qa_select.py [N=144]
"""
import csv, hashlib, json, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCR = Path('/private/tmp/claude-501/-Users-ghilmankhan-workprojects-youtube-intelligence-os/e9d5fa3f-9fa3-4acc-b7cf-207755ab01a1/scratchpad/titleqa')
rd = lambda f: {r['Video_ID']: r for r in csv.DictReader(open(HERE / f))}


def build(n=144):
    tf, an, mp = rd('title-forensics.csv'), rd('title-analyst-audit.csv'), rd('master-packages.csv')
    sc = sorted(int(a['ANALYST_TITLE_DIAGNOSTIC_SCORE']) for a in an.values()); lo, hi = sc[len(sc) // 3], sc[2 * len(sc) // 3]
    ch = sorted(int(t['Character_Count']) for t in tf.values()); short_c, long_c = ch[len(ch) // 20], ch[-len(ch) // 20]
    chan_n = Counter(t['Channel_ID'] for t in tf.values())

    def labels(v):
        t, a, m = tf[v], an[v], mp[v]; s = int(a['ANALYST_TITLE_DIAGNOSTIC_SCORE'])
        L = ['CH:' + t['Channel_ID'], 'FMT:' + t['Format'], 'PERF:' + m['Relative_Performance_Class'], 'ARCH:' + t['Title_Archetype'],
             'TIER:' + ('LOW' if s <= lo else 'HIGH' if s >= hi else 'MID'), 'NUM:' + t['Number_Present'], 'MED:' + a['medical_title_flag']]
        if t['Authority_Cue'] != 'NONE': L.append('AUTH:Y')
        if int(t['Character_Count']) <= short_c: L.append('LEN:VERY_SHORT')
        if int(t['Character_Count']) >= long_c: L.append('LEN:VERY_LONG')
        return L
    quota = {}
    for v in tf:
        for l in labels(v): quota.setdefault(l, 0)
    for l in quota:
        quota[l] = (2 if chan_n[l[3:]] >= 25 else 1) if l.startswith('CH:') else 12 if l == 'FMT:SHORT' else 8 if l.startswith(('ARCH:', 'LEN:', 'MED:', 'AUTH:')) else 20
    quota['PERF:INSUFFICIENT_COHORT'] = 3
    order = sorted(tf, key=lambda v: hashlib.sha256(('titleqa' + v).encode()).hexdigest())
    have, chosen = Counter(), []
    while len(chosen) < n:
        best = max((v for v in order if v not in chosen), key=lambda v: sum(have[l] < quota[l] for l in labels(v)))
        chosen.append(best); have.update(labels(best))
    unmet = {l: (have[l], q) for l, q in quota.items() if have[l] < q}
    return chosen, dict(tf=tf, an=an, mp=mp), unmet, dict(lo=lo, hi=hi, short_c=short_c, long_c=long_c)


if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 144
    chosen, d, unmet, th = build(n)
    SCR.mkdir(exist_ok=True)
    (HERE / 'title-qa-selection.json').write_text(json.dumps(dict(n=n, thresholds=th, unmet_quota=unmet, video_ids=chosen), indent=1))
    per = n // 6
    for k in range(6):
        ids = chosen[k * per:(k + 1) * per]
        blind = [dict(i=j + 1, Video_ID=v, title=d['tf'][v]['Exact_Title'], channel=d['tf'][v]['Channel_Name'], niche=d['tf'][v]['Niche'], format=d['tf'][v]['Format']) for j, v in enumerate(ids)]
        full = [dict(i=j + 1, Video_ID=v, programmatic={k2: x for k2, x in d['tf'][v].items() if k2 not in ('Channel_ID', 'Channel_Name', 'Niche', 'Format', 'Published_At', 'Title_Observation', 'Title_Observed_At', 'Classification_Method')},
                     analyst={k2: x for k2, x in d['an'][v].items() if k2 not in ('Channel_ID', 'batch', 'qa_status')}) for j, v in enumerate(ids)]
        (SCR / f'blind_{k + 1}.json').write_text(json.dumps(blind, indent=1)); (SCR / f'full_{k + 1}.json').write_text(json.dumps(full, indent=1))
    print(len(chosen), 'channels', len({d['tf'][v]['Channel_ID'] for v in chosen}), 'unmet', unmet, th)
