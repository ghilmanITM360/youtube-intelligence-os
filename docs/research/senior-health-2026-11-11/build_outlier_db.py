"""Report 2 Phase 2.2: traceable Outlier Database + cross-channel evidence units.
Run from repo root after build_benchmark.py: python3 -I docs/research/senior-health-2026-11-11/build_outlier_db.py
Outlier ratio = views / median views of the SAME channel's OTHER long-form videos (Playbook variant F, p554). Ratios are inflated when the base is tiny, so
the DB keeps views>=5,000 and reports both ratio and base. Evergreen-vs-spike is INFERRED from age/views-per-day only (single snapshot, no time series).
"""
import csv, json, collections, statistics as st
D = "docs/research/senior-health-2026-11-11"
rows = [r for r in csv.DictReader(open(f"{D}/02-benchmark-video-table.csv"))]
summ = json.load(open(f"{D}/02-benchmark-summary.json"))
NET = set(max(summ["network"].values(), key=len))  # 12 channels linked by identical titles = ONE evidence unit (AGENTS rule 9)
for r in rows:
    for k in ("views", "age_d"): r[k] = int(r[k])
    for k in ("mult", "base", "vpd"): r[k] = float(r[k]) if r[k] not in ("", None) else 0.0
comp = [r for r in rows if r["role"] == "COMPETITOR" and r["is_short"] == "0"]
unit = lambda ch: "NETWORK_12" if ch in NET else ch
URL = lambda v: f"https://www.youtube.com/watch?v={v}"
out = [r for r in comp if r["mult"] >= 5 and r["views"] >= 5000 and r["immature"] == "0"]

def age_class(r):
    if r["age_d"] >= 365: return "OLD_GT1Y_accumulated"
    if r["age_d"] >= 90: return "MID_90_365D"
    if r["age_d"] >= 30: return "RECENT_30_90D"
    return "FRESH_LT30D"

# concept -> independent evidence units having >=1 outlier AND total units covering the concept
conc_units = collections.defaultdict(set); conc_out_units = collections.defaultdict(set)
for r in comp:
    for c in filter(None, r["concepts"].split("|")): conc_units[c].add(unit(r["channel"]))
for r in out:
    for c in filter(None, r["concepts"].split("|")): conc_out_units[c].add(unit(r["channel"]))
top_ch = collections.Counter()
with open(f"{D}/03-outlier-database.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["channel", "video_id", "url", "original_title", "views", "published", "age_days", "views_per_day", "channel_baseline_median_other", "outlier_ratio", "tier",
                "topic_regex", "concept_family", "format_features", "duration_min", "age_class_INFERRED", "cross_channel_units_with_outlier_for_concept", "evidence_note"])
    for r in sorted(out, key=lambda r: -r["views"]):
        cs = [c for c in r["concepts"].split("|") if c]
        xu = max([len(conc_out_units[c]) for c in cs], default=0)
        note = []
        if r["channel"] in NET: note.append("network_member(duplicate-title cluster: not independent)")
        if r["base"] < 500: note.append("tiny_base(ratio inflated)")
        if r["age_d"] < 30: note.append("fresh(<30d, views still accumulating)")
        if xu >= 3: note.append(f"concept_seen_as_outlier_in_{xu}_independent_units")
        w.writerow([r["channel"], r["video_id"], URL(r["video_id"]), r["title"], r["views"], r["published"], r["age_d"], round(r["vpd"], 1), int(r["base"]), round(r["mult"], 1), r["tier"],
                    r["topics"], r["concepts"], r["formats"], round(int(r["duration_s"]) / 60), age_class(r), xu, "; ".join(note) or "-"])
        top_ch[r["channel"]] += 1
P = print
P("outliers in DB:", len(out), "| channels:", len(top_ch), "| network members:", sum(v for k, v in top_ch.items() if k in NET), "| non-network:", sum(v for k, v in top_ch.items() if k not in NET))
P("age class:", collections.Counter(age_class(r) for r in out))
P("\n== concept families: independent units covering vs having an outlier (network counted once) ==")
P("concept | units_covering | units_with_outlier | videos | median_views")
for c in sorted(conc_units, key=lambda c: -len(conc_out_units[c])):
    vs = [r for r in comp if c in r["concepts"].split("|")]
    if len(vs) < 3: continue
    P(c, "|", len(conc_units[c]), "|", len(conc_out_units[c]), "|", len(vs), "|", int(st.median(r["views"] for r in vs)))
P("\n== topics: independent units with outlier ==")
tu = collections.defaultdict(set); tc = collections.defaultdict(set); tn = collections.Counter()
for r in comp:
    for t in r["topics"].split("|"): tc[t].add(unit(r["channel"])); tn[t] += 1
for r in out:
    for t in r["topics"].split("|"): tu[t].add(unit(r["channel"]))
for t in sorted(tc, key=lambda t: -len(tu[t])): P(t, "| units", len(tc[t]), "| units_with_outlier", len(tu[t]), "| videos", tn[t])
P("\n== evergreen vs recent (outliers >=100k views) ==")
big = [r for r in out if r["views"] >= 100000]
for k, v in collections.Counter(age_class(r) for r in big).items(): P(k, v)
P("median vpd by age_class (all outliers):")
for k in ("OLD_GT1Y_accumulated", "MID_90_365D", "RECENT_30_90D", "FRESH_LT30D"):
    v = [r["vpd"] for r in out if age_class(r) == k]
    if v: P(k, len(v), int(st.median(v)))
P("\n== format features among outliers vs all mature (share %) ==")
ma = [r for r in comp if r["immature"] == "0"]
fo = collections.Counter(f for r in out for f in set(filter(None, r["formats"].split("|")))); fa = collections.Counter(f for r in ma for f in set(filter(None, r["formats"].split("|"))))
for f in fa: P(f, "| outliers", round(100 * fo[f] / len(out)), "| all", round(100 * fa[f] / len(ma)))
P("\n== duration of outliers vs all (median min) ==", round(st.median(int(r["duration_s"]) for r in out) / 60), round(st.median(int(r["duration_s"]) for r in ma) / 60))
P("\n== non-network outliers >=20k views (independent evidence) ==")
for r in sorted([r for r in out if r["channel"] not in NET and r["views"] >= 20000], key=lambda r: -r["views"])[:30]:
    P(r["views"], f'x{r["mult"]:.0f}', r["channel"], r["video_id"], r["published"], r["title"][:85])
P("\n== reference: shorts vs long-form competitor ==", sum(1 for r in rows if r["role"] == "COMPETITOR" and r["is_short"] == "1"), "shorts;",
  "median shorts views", int(st.median([r["views"] for r in rows if r["role"] == "COMPETITOR" and r["is_short"] == "1"] or [0])))
