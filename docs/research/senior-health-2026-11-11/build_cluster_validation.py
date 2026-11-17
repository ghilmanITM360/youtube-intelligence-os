"""Report 2 v2 Task 4.2: verify template-network duplication (titles + transcripts) and deduplicate outlier counts.
Run from repo root after build_benchmark.py/build_outlier_db.py. Read-only on sources. Similarity = Jaccard of word 5-gram shingles (OBSERVED text overlap; says nothing about ownership)."""
import csv, json, re, sqlite3, collections, itertools
csv.field_size_limit(10**9)
D = "docs/research/senior-health-2026-11-11"; E = "data/extracted/channel-data/senior-health-16-acquisition"
bm = {r["video_id"]: r for r in csv.DictReader(open(f"{D}/02-benchmark-video-table.csv")) if r["role"] == "COMPETITOR"}
NET = set(max(json.load(open(f"{D}/02-benchmark-summary.json"))["network"].values(), key=len))
tx = {}
for l in open(f"{E}/TRANSCRIPTS_ALL.jsonl"):
    r = json.loads(l); tx[r["video_id"]] = r["text"]
db = sqlite3.connect("file:data/catalog/youtube_channel_registry.db?mode=ro", uri=True)
for v, t in db.execute("select youtube_video_id, transcript_text from transcripts where is_placeholder=0"):
    if v in bm and v not in tx and t: tx[v] = t
norm = lambda t: re.sub(r"[^a-z0-9 ]", "", re.sub(r"\s+", " ", t.lower())).strip()
def sh(t):
    w = re.findall(r"[a-z']+", re.sub(r"\[[^\]]*\]", " ", t.lower())); return {tuple(w[i:i+5]) for i in range(len(w) - 4)}
S = {v: sh(t) for v, t in tx.items() if v in bm}
J = lambda a, b: len(a & b) / max(len(a | b), 1)
P = print
# 1. exact title duplicates
bt = collections.defaultdict(list)
for v, r in bm.items(): bt[norm(r["title"])].append(v)
dup = {t: vs for t, vs in bt.items() if len({bm[v]["channel"] for v in vs}) > 1}
P("titles shared across >=2 channels:", len(dup), "| videos involved:", sum(len(v) for v in dup.values()))
P("of those, all-network:", sum(all(bm[v]["channel"] in NET for v in vs) for vs in dup.values()), "| involve non-network:", [(t[:60], sorted({bm[v]['channel'] for v in vs})) for t, vs in dup.items() if not all(bm[v]["channel"] in NET for v in vs)])
# 2. transcript similarity for same-title cross-channel pairs vs random network pairs
same = [J(S[a], S[b]) for vs in dup.values() for a, b in itertools.combinations(vs, 2) if a in S and b in S and bm[a]["channel"] != bm[b]["channel"]]
same.sort(); P("same-title cross-channel transcript pairs:", len(same), "| median J:", round(same[len(same)//2], 3) if same else "-", "| >=0.5:", sum(j >= .5 for j in same), "| <0.1:", sum(j < .1 for j in same))
# 3. any transcript pair (all competitors, different channels) with J>=0.3 (near-copy) regardless of title
vids = [v for v in S if len(S[v]) > 200]; hi = []
idx = collections.defaultdict(set)
for v in vids:
    for g in list(S[v])[::7]: idx[g].add(v)
cand = collections.Counter()
for g, vs in idx.items():
    if 1 < len(vs) < 40:
        for a, b in itertools.combinations(sorted(vs), 2):
            if bm[a]["channel"] != bm[b]["channel"]: cand[(a, b)] += 1
for (a, b), n in cand.items():
    if n >= 3:
        j = J(S[a], S[b])
        if j >= 0.3: hi.append((round(j, 2), a, bm[a]["channel"], b, bm[b]["channel"], bm[a]["title"][:50]))
hi.sort(reverse=True)
P("cross-channel near-copy transcript pairs (J>=0.3):", len(hi), "| both network:", sum(x[2] in NET and x[4] in NET for x in hi), "| involve non-network:", [x for x in hi if not (x[2] in NET and x[4] in NET)][:8])
P("channel pairs with near-copies:", collections.Counter(tuple(sorted((x[2], x[4]))) for x in hi).most_common(12))
# 4. dedup outlier DB
out = list(csv.DictReader(open(f"{D}/03-outlier-database.csv")))
ckey = {}
for r in out:
    k = norm(r["original_title"]); ckey[r["video_id"]] = k
grp = collections.defaultdict(list)
for r in out: grp[ckey[r["video_id"]]].append(r)
# merge rows whose transcripts are near-copies
par = {r["video_id"]: r["video_id"] for r in out}
def f(x):
    while par[x] != x: x = par[x]
    return x
for vs in grp.values():
    for r in vs[1:]: par[f(r["video_id"])] = f(vs[0]["video_id"])
ov = [r["video_id"] for r in out]
for a, b in itertools.combinations(ov, 2):
    if a in S and b in S and J(S[a], S[b]) >= 0.3: par[f(b)] = f(a)
units = collections.defaultdict(list)
for r in out: units[f(r["video_id"])].append(r)
nn = [r for r in out if r["channel"] not in NET]
P("outlier rows:", len(out), "| unique content units after title+transcript dedup:", len(units), "| units containing only network rows:", sum(all(r["channel"] in NET for r in u) for u in units.values()))
P("non-network rows:", len(nn), "| their unique content units:", len({f(r['video_id']) for r in nn}), "| non-network channels:", len({r['channel'] for r in nn}))
P("non-network outliers by channel:", collections.Counter(r["channel"] for r in nn).most_common())
json.dump({"near_copy_pairs": hi, "outlier_units": {k: [r["video_id"] for r in u] for k, u in units.items()}}, open(f"{D}/04-cluster-validation.json", "w"), indent=0)
