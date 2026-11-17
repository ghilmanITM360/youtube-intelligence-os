#!/usr/bin/env python3
"""Cross-video near-duplicate clustering of asset-library state frames (local, copies only).
usage: python3 -I dedup_channel.py <asset_library_root> [rms_threshold=3.0]
Method: 64x36 grayscale thumbnail per frame; greedy clustering (highest resolution first) with RMS pixel
difference <= threshold (0-255 scale). This merges near-identical frames only; it does NOT judge semantics.
Outputs <root>/_channel/unique_frames/*.jpg (copies), unique_frames_index.csv, cluster_members.csv."""
import csv, glob, hashlib, os, shutil, sys
import numpy as np
from PIL import Image

root = os.path.abspath(sys.argv[1]); thr = float(sys.argv[2]) if len(sys.argv) > 2 else 3.0
items = []
for p in sorted(glob.glob(f"{root}/*/states_index.csv")):
    vid = os.path.basename(os.path.dirname(p))
    for r in csv.DictReader(open(p)):
        items.append((vid, r))
vecs, sizes = [], []
for vid, r in items:
    im = Image.open(f"{root}/{vid}/{r['file']}"); sizes.append(im.size[0] * im.size[1])
    im.draft("L", (160, 90))
    vecs.append(np.asarray(im.convert("L").resize((64, 36), Image.BILINEAR), dtype=np.float32).ravel())
V = np.stack(vecs); order = np.argsort(-np.array(sizes), kind="stable")
reps, rep_idx, cluster = np.zeros((0, V.shape[1]), np.float32), [], np.full(len(items), -1)
for i in order:
    if rep_idx:
        d = np.sqrt(((reps - V[i]) ** 2).mean(axis=1)); j = int(d.argmin())
        if d[j] <= thr: cluster[i] = j; continue
    cluster[i] = len(rep_idx); rep_idx.append(i); reps = np.vstack([reps, V[i][None]])
out = f"{root}/_channel/unique_frames"; os.makedirs(out, exist_ok=True)
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
idx, mem = [], []
for c, i in enumerate(rep_idx):
    vid, r = items[i]; src = f"{root}/{vid}/{r['file']}"
    dst = f"{out}/U{c:05d}_{vid}_{r['state_id']}.jpg"; shutil.copy2(src, dst)
    assert sha(dst) == r["image_sha256"], dst
    members = [k for k in range(len(items)) if cluster[k] == c]
    vids = sorted({items[k][0] for k in members})
    idx.append({"cluster_id": f"U{c:05d}", "rep_file": os.path.relpath(dst, root), "rep_video": vid, "rep_state": r["state_id"],
                "rep_what_changed": r["what_changed"], "rep_visible_text": r.get("visible_text", ""), "n_members": len(members),
                "n_videos": len(vids), "videos": ";".join(vids), "rep_image_sha256": r["image_sha256"]})
    for k in members:
        v2, r2 = items[k]; mem.append({"cluster_id": f"U{c:05d}", "video_id": v2, "state_id": r2["state_id"], "file": f"{v2}/{r2['file']}"})
for name, rows in (("unique_frames_index.csv", idx), ("cluster_members.csv", mem)):
    with open(f"{root}/_channel/{name}", "w", newline="") as f:
        w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
multi = sum(1 for x in idx if x["n_videos"] > 1)
print(f"frames={len(items)} unique_clusters={len(idx)} thr={thr} clusters_spanning_multiple_videos={multi}")
