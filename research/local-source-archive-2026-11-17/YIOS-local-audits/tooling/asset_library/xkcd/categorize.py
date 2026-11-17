#!/usr/bin/env python3
"""xkcd What If: provisional category tags for the 2,755 unique clusters (local only). Adapted copy of the CF tool;
CF keywords removed. usage: <venv python> -I categorize.py <xkcd asset_library_root>
Method (INFERRED, not human-verified): keyword rules on ledger `what_changed` + `event_class` of every cluster member,
plus pixel features of the representative frame (off-white canvas / dark / colour-field fractions).
Writes _channel/category_index.csv. `primary` = first hit in KW order; `tags` = all hits. A viewing pass audits purity."""
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
 ("graphics_ui", r"diagram|chart|graph\b|map\b|world.?map|axis|axes|ruler|scale bar|equation|formula|inset|photo|screenshot|cutaway|plot\b|grid|timeline|cross.?section|bar chart"),
 ("typography", r"title card|question box|grey rounded box|\bq\.|text card|heading|footnote|caption|typed|written on|lettered|end card|credits|banner|censored|redacted"),
 ("characters", r"stick|figure|person|people|crowd|\bman\b|woman|silhouette|astronaut|wise men|character|\bhead\b|pose|ponytail|\bhair\b|helmet"),
 ("props", r"toaster|banana|rifle|satellite|rover|hubble|telescope|rocket|tower|building|house|tree|book|lamp|desk|chair|car\b|boat|ship|submarine|ball\b|machine|board|whiteboard|blackboard|paper|sign\b|bottle|cell\b|dinosaur|mole\b|object"),
 ("environments", r"\bscene\b|landscape|horizon|\bsky\b|ocean|\bcity\b|\broom\b|desert|forest|surface of|ground line|night|underwater|space scene"),
]
WEAK_TYPO = r"\blabel|\btext\b|speech|bubble|'[^']{2,}'"
TRANS = r"dissolve|fade|cross.?fade|slide|pan\b|whip|scroll|zoom|blur"
rows = []
for r in csv.DictReader(open(f"{root}/_channel/unique_frames_index.csv")):
    ms = mem[r["cluster_id"]]
    txt = " ".join(f"{m.get('what_changed','')} {m.get('event_class','')}" for m in ms).lower()
    im = Image.open(f"{root}/{r['rep_file']}"); im.draft("RGB", (320, 320)); a = np.asarray(im.convert("RGB").resize((90, 160) if im.size[1] > im.size[0] else (160, 90)), dtype=np.int16)
    white = float((a.min(axis=2) > 225).mean()); dark = float((a.mean(axis=2) < 70).mean())
    chroma = float(((a.max(axis=2) - a.min(axis=2)) > 40).mean())
    tags = [c for c, pat in KW if re.search(pat, txt)]
    if re.search(WEAK_TYPO, txt) and "typography" not in tags: tags.append("typography")
    if re.search(TRANS, txt) or "camera" in txt: tags.append("transitions")
    feat = []
    if dark > 0.45: feat.append("dark_screen")
    if white < 0.35 and dark <= 0.45: feat.append("full_bleed_scene")
    if chroma > 0.25: feat.append("colour_field")
    if ("full_bleed_scene" in feat or "dark_screen" in feat) and "environments" not in tags: tags.insert(0, "environments")
    primary = next((t for t in tags if t != "transitions"), "uncategorised")
    rows.append(dict(cluster_id=r["cluster_id"], rep_file=r["rep_file"], rep_video=r["rep_video"], primary=primary, tags=";".join(dict.fromkeys(tags)),
                     features=";".join(feat), white_frac=f"{white:.3f}", dark_frac=f"{dark:.3f}", chroma_frac=f"{chroma:.3f}",
                     n_members=r["n_members"], n_videos=r["n_videos"], method="RULE_FROM_LEDGER_TEXT+PIXEL_FEATURES(INFERRED)", viewed_in_sheet="", viewed_verdict=""))
with open(f"{root}/_channel/category_index.csv", "w", newline="") as f:
    w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
print("primary", collections.Counter(r["primary"] for r in rows).most_common())
print("tag hits", collections.Counter(t for r in rows for t in r["tags"].split(";") if t).most_common())
print("features", collections.Counter(t for r in rows for t in r["features"].split(";") if t).most_common())
