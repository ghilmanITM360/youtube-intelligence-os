#!/usr/bin/env python3
"""Find frame-exact visual reuse across analysed videos (MEASURED, appearance-level).

Usage: python3 -E cross_video_reuse.py <local_evidence_root> [stride=3] [thr=0.985]
Each frame (180x320 gray) is box-reduced to 45x80, z-scored; near-blank frames (std<8 gray levels) are skipped.
Pairs of frames from DIFFERENT videos with correlation >= thr are reported, grouped into runs per (video A, video B).
Writes evidence/cross_video_reuse.json. Caveat: correlation >= 0.985 on 3,600 pixels means near-identical composition at low resolution,
not proof of an identical source file; 360p vs 720p versions of the same asset differ slightly.
"""
import json, os, sys
import numpy as np
EV = sys.argv[1]; stride = int(sys.argv[2]) if len(sys.argv) > 2 else 3; thr = float(sys.argv[3]) if len(sys.argv) > 3 else 0.985
RDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
vids = sorted(v for v in os.listdir(EV) if os.path.exists(os.path.join(EV, v, "gray.npy")))
feats, meta = [], []
for v in vids:
    g = np.load(os.path.join(EV, v, "gray.npy"), mmap_mode="r")
    if g.shape[1:] != (320, 180):
        continue
    idx = np.arange(0, g.shape[0], stride)
    x = np.asarray(g[idx], np.float32).reshape(len(idx), 45, 7, 80 // 1 if False else 4, 45)[:, :, :, :, :] if False else None
    a = np.asarray(g[idx], np.float32)
    a = a.reshape(len(idx), 80, 4, 45, 4).mean((2, 4)).reshape(len(idx), -1)  # 80x45 = 3600
    sd = a.std(1)
    keep = sd >= 8
    a = a[keep]; ii = idx[keep]
    a = (a - a.mean(1, keepdims=True)) / (a.std(1, keepdims=True) + 1e-6)
    feats.append(a.astype(np.float32)); meta += [(v, int(i)) for i in ii]
F = np.concatenate(feats); vid_arr = np.array([m[0] for m in meta]); fr_arr = np.array([m[1] for m in meta])
print("frames", len(F), "videos", len(set(vid_arr)))
hits = {}
for s in range(0, len(F), 1500):
    c = (F[s:s + 1500] @ F.T) / F.shape[1]
    ci, cj = np.where(c >= thr)
    for a, b in zip(ci + s, cj):
        if vid_arr[a] < vid_arr[b]:
            hits.setdefault((vid_arr[a], vid_arr[b]), []).append((int(fr_arr[a]), int(fr_arr[b])))
out = {}
for (va, vb), pairs in sorted(hits.items(), key=lambda kv: -len(kv[1])):
    pairs.sort()
    runs, cur = [], [pairs[0]]
    for p in pairs[1:]:
        if p[0] - cur[-1][0] <= stride * 4 and abs((p[1] - cur[-1][1])) <= stride * 8:
            cur.append(p)
        else:
            runs.append(cur); cur = [p]
    runs.append(cur)
    out["%s|%s" % (va, vb)] = {"matched_frames": len(pairs), "runs": [{"a_frames": [r[0][0], r[-1][0]], "b_frames": [r[0][1], r[-1][1]], "n": len(r)} for r in runs if len(r) >= 2][:12]}
json.dump(out, open(os.path.join(RDIR, "evidence", "cross_video_reuse.json"), "w"), indent=1)
for k, v in list(out.items())[:12]:
    print(k, v["matched_frames"], "frames;", [(r["a_frames"], r["b_frames"], r["n"]) for r in v["runs"][:3]])
