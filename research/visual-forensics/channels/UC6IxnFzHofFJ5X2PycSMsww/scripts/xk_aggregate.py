"""Cross-video aggregation over videos with a built state_ledger (development set only unless --include-heldout).
Writes campaign/aggregate_<tag>.json + .csv. Usage: python3 -I xk_aggregate.py <ws> <tag> [--include-heldout]"""
import csv, json, sys, pathlib, statistics as st, collections
W = pathlib.Path(sys.argv[1]); tag = sys.argv[2]; inc = "--include-heldout" in sys.argv
sel = json.load(open(W / "selection/selection_v1.json"))
role = {**{i: "LONG_DEV" for i in sel["long_dev"]}, **{i: "LONG_HELDOUT" for i in sel["long_heldout"]},
        **{i: "SHORT_DEV" for i in sel["short_dev"]}, **{i: "SHORT_HELDOUT" for i in sel["short_heldout"]}}
s2 = W / "selection/selection_v2_heldout2.json"
if s2.exists(): role.update({i: "LONG_HELDOUT2" for i in json.load(open(s2))["long_heldout2"]})
rows = []
for vid, r in role.items():
    V = W / "videos" / vid
    if not (V / "tables/state_ledger.csv").exists() or ("HELDOUT" in r and not inc): continue
    S = list(csv.DictReader(open(V / "tables/state_ledger.csv"))); sm = json.load(open(V / "source_manifest.json"))["source"]
    pal = json.load(open(V / "tables/palette_measured.json")); dur = sm["duration_seconds"]
    acts = [x for x in S if x["kind"] == "ACTIVITY"]; holds = [x for x in S if x["kind"] == "HOLD"]
    fps = sm["decoded_frames"] / dur
    cuts = sum("SHOT_CUT" in x["event_class"] for x in acts)
    cls = collections.Counter(c for x in acts for c in x["event_class"].split("+"))
    sub = collections.Counter(x["subtype"] for x in acts)
    hd = [int(x["frames"]) / fps for x in holds]
    rows.append(dict(video_id=vid, role=r, duration_s=round(dur, 2), aspect=sm["resolution"], fps=sm["frame_rate_avg"],
                     segments=len(S), activities=len(acts), events_per_min=round(len(acts) / dur * 60, 1),
                     shot_cuts=cuts, cuts_per_min=round(cuts / dur * 60, 2),
                     camera_events=cls["CAMERA"], graphic_text_events=cls["GRAPHIC/TEXT"], character_events=cls["CHARACTER"],
                     effect_events=cls["LIGHT/COLOR/EFFECT"], false_positive=cls["FALSE_POSITIVE"],
                     pop_events=sum(v for k, v in sub.items() if k.startswith("POP")), write_on_events=sum(v for k, v in sub.items() if "WRITE_ON" in k),
                     dissolve_fade_events=sum(v for k, v in sub.items() if "DISSOLVE" in k or "FADE" in k),
                     hold_median_s=round(st.median(hd), 2), hold_p90_s=round(sorted(hd)[int(0.9 * (len(hd) - 1))], 2), hold_max_s=round(max(hd), 2),
                     activity_frame_share=round(sum(int(x["frames"]) for x in acts) / sm["decoded_frames"], 3),
                     bg=pal["background_exact_rgb"], mean_ink=pal["mean_dark_ink_frac"], red_hold_share=round(pal["holds_with_red_accent"] / max(1, pal["holds"]), 2),
                     top_subtypes=";".join(f"{k}:{v}" for k, v in sub.most_common(6))))
if rows:
    (W / "campaign").mkdir(exist_ok=True)
    with open(W / f"campaign/aggregate_{tag}.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    summ = {}
    for fmt in ("LONG", "SHORT"):
        g = [r for r in rows if r["role"].startswith(fmt)]
        if not g: continue
        summ[fmt] = {k: dict(n=len(g), median=st.median(r[k] for r in g), min=min(r[k] for r in g), max=max(r[k] for r in g))
                     for k in ("duration_s", "events_per_min", "cuts_per_min", "hold_median_s", "activity_frame_share", "mean_ink", "red_hold_share")}
    (W / f"campaign/aggregate_{tag}.json").write_text(json.dumps(dict(videos=[r["video_id"] for r in rows], include_heldout=inc, by_format=summ), indent=1))
    print(json.dumps(summ, indent=1))
