"""Phase 14 (reconciliation 2026-11-23): descriptive + design-aware presentation of the 156-shot boundary review.
Sample design known from scripts/review_sample*.py: strata = format x boundary strength (<0.3, >=0.3); inside a stratum videos with the fewest
already-sampled shots first, then random; batch sizes 24/36/48/48 with different per-stratum allocation. So selection is NOT simple random within strata.
This script reports (1) raw counts, (2) population stratum sizes and sample allocation, (3) clustering by video, (4) a post-stratified estimate with a
video-cluster bootstrap and leave-one-video-out sensitivity. These are SENSITIVITY analyses conditional on stated assumptions, not channel-wide intervals.
usage: uv run --no-project python scripts/phase14_sample_design.py"""
import csv, json, os, random, collections
A = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pop = list(csv.DictReader(open(A + '/ledgers_measured/ALL_SHOT_LEDGER.csv')))
smp = list(csv.DictReader(open(A + '/review_sample/REVIEWED_SAMPLE.csv')))
inv = {r['video_id']: r['format'] for r in csv.DictReader(open(A + '/03_CHANNEL_MASTER_INVENTORY.csv'))}
def fmt(v): return 'LONG' if inv[v].upper().startswith('LONG') else 'SHORT'
def strat(f, s): return f + ('_lt0.3' if s < 0.3 else '_ge0.3')
elig = [r for r in pop if r['boundary_strength'] not in ('', None)]
P = collections.Counter(strat(fmt(r['video_id']), float(r['boundary_strength'])) for r in elig)
key = lambda r: (r['video_id'], r['shot_id'])
assert len({key(r) for r in smp}) == len(smp) == 156 and all(key(r) in {key(p) for p in pop} for r in smp)
for r in smp: r['stratum'] = strat(r['fmt'], float(r['boundary_strength'])); r['cut'] = 1 if r['boundary_check'] == 'TRUE_CUT' else 0
S = collections.Counter(r['stratum'] for r in smp); T = collections.defaultdict(int)
for r in smp: T[r['stratum']] += r['cut']
def west(rows):
    n = collections.Counter(r['stratum'] for r in rows); c = collections.Counter(r['stratum'] for r in rows if r['cut'])
    tot = sum(P[s] for s in n); return sum(P[s] * c[s] / n[s] for s in n) / tot
def vest(rows):  # each video weight 1 (selection equalised videos)
    g = collections.defaultdict(list)
    for r in rows: g[r['video_id']].append(r['cut'])
    return sum(sum(v) / len(v) for v in g.values()) / len(g)
raw = sum(r['cut'] for r in smp) / len(smp); w = west(smp); v = vest(smp)
byv = collections.defaultdict(list)
for r in smp: byv[r['video_id']].append(r)
random.seed(14); boots = []
vids = list(byv)
for _ in range(4000):
    rows = [x for vid in random.choices(vids, k=len(vids)) for x in byv[vid]]
    n = collections.Counter(x['stratum'] for x in rows)
    if len(n) < 4: continue
    boots.append(west(rows))
boots.sort(); lo, hi = boots[int(.025 * len(boots))], boots[int(.975 * len(boots))]
loo = {vid: west([x for x in smp if x['video_id'] != vid]) for vid in vids}
worst = sorted(loo.items(), key=lambda kv: kv[1])
sizes = sorted(((len(x), k) for k, x in byv.items()), reverse=True)
out = dict(sample_n=len(smp), population_eligible_shots=len(elig), videos=len(vids),
           population_by_stratum=dict(P), sample_by_stratum=dict(S), true_cut_by_stratum=dict(T),
           sampling_fraction_by_stratum={s: round(S[s] / P[s], 3) for s in P},
           raw_true_cut_share=round(raw, 3), poststratified_true_cut_share=round(w, 3), video_equal_weight_true_cut_share=round(v, 3),
           video_cluster_bootstrap_95=[round(lo, 3), round(hi, 3)], bootstrap_n=len(boots),
           leave_one_video_out_min_max=[round(worst[0][1], 3), round(worst[-1][1], 3)], leave_one_out_most_influential=worst[0][0],
           cluster_size_top5=sizes[:5], cluster_size_median=sorted(len(x) for x in byv.values())[len(byv) // 2],
           false_progressive_share_top_video=dict(video='U4cONnQxgvo', sampled=len(byv['U4cONnQxgvo']), false=sum(1 - r['cut'] for r in byv['U4cONnQxgvo'])))
json.dump(out, open(A + '/14_SAMPLE_DESIGN_ANALYSIS.json', 'w'), indent=1); print(json.dumps(out, indent=1))
