"""Adds rv2 internal cuts to per-video shot_cuts (same convention as rv1 adjusted aggregate). Reads reconcile.csv + aggregates; writes campaign/aggregate_strip_rv2_adjusted.csv.
Quantitative frozen scores (Pop-6, held-outs) are NOT recomputed; this is an additive side table."""
import csv, glob, collections
agg = {}
for f in sorted(glob.glob("campaign/aggregate_*.csv")):
    if "adjusted" in f: continue
    for r in csv.DictReader(open(f)): agg.setdefault(r["video_id"], r)
add = collections.Counter(); prose = collections.Counter()
T = {(r["video"], r["seg"]): r for r in csv.DictReader(open("campaign/strip_review/strip_tasks_rv2.csv"))}
for r in csv.DictReader(open("campaign/strip_review/strip_rv2/reconcile.csv")):
    add[r["video"]] += int(r["new_cuts"])
    if int(r["new_cuts"]) and "cut" in T[(r["video"], r["seg"])]["prior_desc"].lower(): prose[r["video"]] += int(r["new_cuts"])
rows = []
for v, n in sorted(add.items()):
    a = agg[v]; dur = float(a["duration_s"]); sc = int(a["shot_cuts"])
    rows.append(dict(video_id=v, role=a["role"], shot_cuts=sc, rv2_internal_cuts=n, of_which_prose_mentioned_in_prior_desc=prose[v], cuts_adj=sc + n,
                     cuts_per_min=a["cuts_per_min"], cuts_per_min_adj=round((sc + n) / dur * 60, 2)))
w = csv.DictWriter(open("campaign/aggregate_strip_rv2_adjusted.csv", "w", newline=""), fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for r in rows: print(r)
print("total", sum(add.values()), "prose-mentioned", sum(prose.values()))
