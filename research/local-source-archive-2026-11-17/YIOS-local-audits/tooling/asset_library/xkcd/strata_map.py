#!/usr/bin/env python3
"""Deep-VF B0: strata map of every census video (local only). usage: /usr/bin/python3 -I strata_map.py
One uniform rhythm measure for all local longs: ACTIVITY segments/min from tables/segments_v1.csv (automated segmenter,
MEASURED; not the reviewed ledger rate). Non-canvas share = frames with mean_luma < 200 (FULL_FRAME_MEASUREMENTS, MEASURED).
Explanation type is INFERRED from the title only. Usage history from selection files + asset library."""
import csv, json, os, re, statistics
H = os.path.expanduser("~/YIOS-local-audits/xkcd-whatif"); OUT = f"{H}/asset_library/_channel/deep_vf"
cen = {r["video_id"]: r for r in csv.DictReader(open(f"{H}/census/census.csv"))}
mat = {r["video_id"]: r for r in csv.DictReader(open(f"{H}/campaign/campaign_matrix.csv"))}
reuse = {r["short"]: r for r in csv.DictReader(open(f"{H}/campaign/short_long_text_reuse_population.csv"))}
opening = {r["video_id"]: r for r in csv.DictReader(open(f"{OUT}/opening/opening_layout.csv"))}
lib = set(os.listdir(f"{H}/asset_library"))
use = {}
for f, tag in (("selection_v1.json", "DEV_v1"), ("selection_v2_heldout2.json", "HELDOUT2"), ("selection_v3_heldout3.json", "HELDOUT3"),
               ("selection_v4_heldout4.json", "HELDOUT4"), ("selection_v5_heldout5.json", "HELDOUT5"), ("selection_v6_pop6.json", "POP6_QUANT_ONLY")):
    for v in set(re.findall(r'"([\w-]{11})"', open(f"{H}/selection/{f}").read())) & set(cen): use.setdefault(v, tag)
if any(mat[v]["role"].endswith("HELDOUT") for v in mat):
    for v in mat:
        if mat[v]["role"] in ("LONG_HELDOUT", "SHORT_HELDOUT"): use[v] = "HELDOUT1"
def etype(t):
    t = t.lower()
    if re.search(r"how (many|much|long|big|fast|far|high|deep|hot|quickly)|how .* would it take", t): return "QUANTITY_ESTIMATE"
    if re.search(r"\b(stood|jumped|everyone|every person|all .* at once|simultaneous)", t): return "MASS_EVENT"
    if re.search(r"(made of|replaced|turned into|were (a|made)|was a)", t): return "SUBSTITUTION"
    if re.search(r"(travel|fly|fell|falling|walk|drive|dig|climb|ride|journey|swim)", t): return "JOURNEY"
    return "CONSEQUENCE"
rows = []
for v, c in cen.items():
    r = dict(video_id=v, format=c["format_class"], publish=c["publish_datetime"][:10], period=c["publish_datetime"][:4] + ("H1" if c["publish_datetime"][5:7] <= "06" else "H2"),
             title=c["title"], explanation_type_INFERRED=etype(c["title"]), local_source="YES" if c["local_paths"] else "NO", in_asset_library=v in lib,
             prior_use=use.get(v, "NEVER"), act_per_min="", noncanvas_share="", opening_layout="", card_at_f3="", short_relation="", short_parent="")
    seg, ffm = f"{H}/videos/{v}/tables/segments_v1.csv", f"{H}/videos/{v}/tables/FULL_FRAME_MEASUREMENTS.csv"
    if os.path.exists(seg):
        s = list(csv.DictReader(open(seg))); n = int(s[-1]["end_frame"]) + 1
        r["act_per_min"] = f"{sum(x['kind'] == 'ACTIVITY' for x in s) / (n / 24 / 60):.1f}"
    if os.path.exists(ffm):
        L = [float(x["mean_luma"]) for x in csv.DictReader(open(ffm))]; r["noncanvas_share"] = f"{sum(l < 200 for l in L) / len(L):.3f}"
    if v in opening: r["opening_layout"], r["card_at_f3"] = opening[v]["layout"], opening[v]["card_at_f3"]
    if v in reuse: r["short_relation"], r["short_parent"] = reuse[v]["relation"] or "NO_CAPTION_TEXT", reuse[v]["best_long"]
    rows.append(r)
L = sorted(float(r["act_per_min"]) for r in rows if r["format"] == "LONG_FORM" and r["act_per_min"])
S = sorted(float(r["act_per_min"]) for r in rows if r["format"] == "SHORT" and r["act_per_min"])
t = {"LONG_FORM": (L[len(L) // 3], L[2 * len(L) // 3]), "SHORT": (S[len(S) // 3], S[2 * len(S) // 3]) if S else (0, 0)}
for r in rows:
    if r["act_per_min"]:
        a, b = t[r["format"]]; x = float(r["act_per_min"]); r["rhythm_tertile"] = "CALM" if x < a else "BUSY" if x >= b else "MID"
    else: r["rhythm_tertile"] = ""
rows.sort(key=lambda r: (r["format"], r["publish"]))
with open(f"{OUT}/strata_map.csv", "w", newline="") as fo: w = csv.DictWriter(fo, list(rows[0])); w.writeheader(); w.writerows(rows)
print("tertile cuts", t, "longs measured", len(L), "shorts measured", len(S))
