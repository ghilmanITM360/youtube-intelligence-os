#!/usr/bin/env python3
"""P2 sheet plan: seeded random 24-tile sheets per primary category (long-form reps, 16:9) + Shorts sheets (9:16),
then one coverage sheet with a random cluster from every library video not yet shown. Calls make_sheet.py.
usage: <venv python> -I plan_sheets.py <asset_library_root>"""
import csv, os, random, subprocess, sys, collections
root = os.path.abspath(sys.argv[1]); out = f"{root}/_channel/review_sheets"; os.makedirs(out, exist_ok=True)
cat = list(csv.DictReader(open(f"{root}/_channel/category_index.csv")))
fmt = {r["video_id"]: r["format"] for r in csv.DictReader(open(f"{root}/_channel/coverage_by_video.csv"))}
rng = random.Random(20261108); here = os.path.dirname(os.path.abspath(__file__)); shown = set(); plan = []
def sheet(name, ids, mode, cols, tw):
    subprocess.run([sys.executable, "-I", f"{here}/make_sheet.py", root, f"{out}/{name}.jpg", str(cols), str(tw), mode, *ids], check=True)
    shown.update(r["rep_video"] for r in cat if r["cluster_id"] in ids); plan.append((name, len(ids)))
for c in ["characters", "environments", "props", "graphics_ui", "typography", "uncategorised"]:
    pool = [r["cluster_id"] for r in cat if r["primary"] == c and fmt[r["rep_video"]] == "LONG_FORM"]
    sheet(f"xk_long_{c}", rng.sample(pool, min(24, len(pool))), "landscape", 6, 320)
sh = [r for r in cat if fmt[r["rep_video"]] == "SHORT"]
for c in ["characters", "environments", "graphics_ui"]:
    pool = [r["cluster_id"] for r in sh if r["primary"] == c]
    sheet(f"xk_short_{c}", rng.sample(pool, min(24, len(pool))), "portrait", 12, 160)
pool = [r["cluster_id"] for r in sh if r["primary"] in ("props", "typography", "uncategorised")]
sheet("xk_short_props_typo_uncat", rng.sample(pool, 24), "portrait", 12, 160)
missing = sorted(set(fmt) - shown)
if missing:
    ids = [rng.choice([r["cluster_id"] for r in cat if r["rep_video"] == v]) for v in missing]
    L = [i for i, v in zip(ids, missing) if fmt[v] == "LONG_FORM"]; S = [i for i, v in zip(ids, missing) if fmt[v] == "SHORT"]
    if L: sheet("xk_coverage_long", L, "landscape", 6, 320)
    if S: sheet("xk_coverage_short", S, "portrait", 12, 160)
print(plan, "videos shown:", len(shown), "of", len(fmt), "missing before coverage:", missing)
