#!/usr/bin/env python3
"""Provisional category tags for the unique frames of an asset library (local only).
usage: <venv python> -I categorize.py <asset_library_root>
Method (all INFERRED, not human-verified): (a) keyword rules on the ledger text of every cluster member
(what_changed, visible_text, asset_ids, entering class), (b) pixel features of the representative frame
(white / green / dark fraction). Writes _channel/category_index.csv. A viewing pass (review_sheets/) then
audits the purity of each category; see CATEGORY_AUDIT.md. Categories are multi-tag; `primary` is the first hit."""
import csv, collections, glob, os, re, sys
import numpy as np
from PIL import Image
root = os.path.abspath(sys.argv[1])
st = {}
for p in glob.glob(f"{root}/*/states_index.csv"):
    for r in csv.DictReader(open(p)): st[(r["video_id"], r["state_id"])] = r
mem = collections.defaultdict(list)
for r in csv.DictReader(open(f"{root}/_channel/cluster_members.csv")): mem[r["cluster_id"]].append(st[(r["video_id"], r["state_id"])])
KW = [  # order = priority of `primary`
 ("graphics_ui", r"screenshot|chart|graph|logo|browser|tweet|ui\b|app\b|website|article|headline|document|\bf4\b|\bf5\b|table|map|dashboard|ticker|price|gfx_|diagram|photo|video clip|clip"),
 ("typography", r"text card|caption|title|chapter|quote|handwritten|txt_|lower.?third|typed|word|number|label|\btext\b"),
 ("characters", r"stick|man\b|men\b|woman|figure|character|ch_|char_|person|dave|boy|girl|guy|people|crowd|face|head|pose|expression"),
 ("props", r"obj_|banknote|coin|bitcoin|money|bag|briefcase|chalkboard|arrow|bubble|house|building|car\b|truck|barrel|gold|check|paper|newspaper|icon|object"),
 ("transitions", r"cut to black|slide_in|rise_in|drawon|screen_swap|pop_out|wipe|fade|transition"),
]
rows = []
for n, r in enumerate(csv.DictReader(open(f"{root}/_channel/unique_frames_index.csv"))):
    ms = mem[r["cluster_id"]]
    txt = " ".join(f"{m.get('what_changed','')} {m.get('visible_text','')} {m.get('asset_ids','')} {m.get('entering_class','')}" for m in ms).lower()
    im = Image.open(f"{root}/{r['rep_file']}"); im.draft("RGB", (320, 180)); a = np.asarray(im.convert("RGB").resize((160, 90)), dtype=np.int16)
    white = float((a.min(axis=2) > 235).mean()); green = float(((a[..., 1] > a[..., 0] + 25) & (a[..., 1] > a[..., 2] + 25)).mean())
    dark = float((a.mean(axis=2) < 70).mean())
    tags = [c for c, pat in KW if re.search(pat, txt)]
    feat = []
    if dark > 0.45: feat.append("dark_screen")
    if white < 0.35 and dark <= 0.45: feat.append("full_bleed_scene")
    if green > 0.35: feat.append("green_fill")
    if "full_bleed_scene" in feat and "graphics_ui" not in tags: tags.insert(0, "environments")
    if "dark_screen" in feat and "graphics_ui" not in tags: tags.insert(0, "graphics_ui")
    primary = tags[0] if tags else "uncategorised"
    rows.append(dict(cluster_id=r["cluster_id"], rep_file=r["rep_file"], primary=primary, tags=";".join(dict.fromkeys(tags)),
                     features=";".join(feat), white_frac=f"{white:.3f}", green_frac=f"{green:.3f}", dark_frac=f"{dark:.3f}",
                     n_members=r["n_members"], n_videos=r["n_videos"], method="RULE_FROM_LEDGER_TEXT+PIXEL_FEATURES", viewed_verdict=""))
with open(f"{root}/_channel/category_index.csv", "w", newline="") as f:
    w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
print(collections.Counter(r["primary"] for r in rows).most_common())
