#!/usr/bin/env python3
"""Deep-VF held-out v9 (Shorts; rules: _channel/deep_vf/FROZEN_RULES_v3.md; sha file checked first). Copy of heldout_v8_eval.py; M1 numerator = camera instances.
usage: <venv python> -I heldout_v8_eval.py sheets   -> heldout_v8/<id>_holds.jpg (plain tiles, for M0 + C3) + colour_<id>.csv (not shown)
       <venv python> -I heldout_v8_eval.py score    -> needs heldout_v8/M0_format_labels.json; motion labels, non-default colour
                                                      sheets (<id>_nondefault.jpg, for C2), measured.json"""
import csv, hashlib, importlib.util, json, os, subprocess, sys
import numpy as np, cv2
H = os.path.expanduser("~/YIOS-local-audits/xkcd-whatif"); D = f"{H}/asset_library/_channel/deep_vf"; OUT = f"{D}/heldout_v9"; os.makedirs(OUT, exist_ok=True)
for line in open(f"{D}/FROZEN_RULES_v3.sha256").read().split("\n")[1:]:
    if line.strip():
        h, f = line.split(); assert hashlib.sha256(open(f"{D}/{f}", "rb").read()).hexdigest() == h, f"FROZEN FILE CHANGED {f}"
def load(name):
    s = importlib.util.spec_from_file_location(name, f"{D}/v2/{name}.py"); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
cc, mc = load("colour_classes"), load("motion_classes")
_s = importlib.util.spec_from_file_location("ci", f"{D}/v3/camera_instances.py"); ci = importlib.util.module_from_spec(_s); _s.loader.exec_module(ci)  # the frozen copies, not the working tools
sel = json.load(open(f"{D}/heldout_v9_selection.json"))
vids = [sel["MAP_FILL_case"]["id"], sel["SCROLL_case"]["id"]]
NONDEF = {"PAINTED_PLATE", "RED_SOLID", "TINT_REGION", "GLOW_DARK"}

def grab_colour(path, frames, w, hgt):
    want, out, n, sz = set(frames), {}, 0, w * hgt * 3
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-nostdin", "-i", path, "-an", "-vf", f"scale={w}:{hgt}:flags=area", "-fps_mode", "passthrough", "-f", "rawvideo", "-pix_fmt", "bgr24", "-"], stdout=subprocess.PIPE)
    while want - out.keys():
        b = p.stdout.read(sz)
        if len(b) < sz: break
        if n in want: out[n] = np.frombuffer(b, np.uint8).reshape(hgt, w, 3)
        n += 1
    p.kill(); p.wait(); return out

def sheet(imgs, labels, name, cols):
    th, tw = imgs[0].shape[:2]; rows = (len(imgs) + cols - 1) // cols; S = np.full((rows * (th + 16), cols * tw, 3), 40, np.uint8)
    for i, (im, lb) in enumerate(zip(imgs, labels)):
        X, Y = (i % cols) * tw, (i // cols) * (th + 16); S[Y + 16:Y + 16 + th, X:X + tw] = im; cv2.putText(S, lb, (X + 2, Y + 12), 0, 0.38, (0, 255, 255), 1)
    cv2.imwrite(f"{OUT}/{name}", S, [cv2.IMWRITE_JPEG_QUALITY, 88])

def holds(v):
    seg = list(csv.DictReader(open(f"{H}/videos/{v}/tables/segments_v1.csv")))
    return [s for s in seg if s["kind"] == "HOLD"], [s for s in seg if s["kind"] == "ACTIVITY"]

phase = sys.argv[1]
if phase == "sheets":
    for v in vids:
        path, sha = mc.source(v); hs, _ = holds(v); port = mc.CEN[v]["format_class"] == "SHORT"; w, hgt = (180, 320) if port else (320, 180)
        mids = [(int(s["start_frame"]) + int(s["end_frame"])) // 2 for s in hs]; F = grab_colour(path, mids, w, hgt)
        sheet([F[m] for m in mids], [f"{s['seg']} {float(s['start_pts']):.1f}s" for s in hs], f"{v}_holds.jpg", 10 if port else 6)
        rows = []
        for s, m in zip(hs, mids):
            c, f = cc.classify(F[m]); rows.append(dict(video_id=v, sha256=sha[:12], seg=s["seg"], frame=m, start_pts=s["start_pts"], cls=c, **f))
        keys = sorted({k for r in rows for k in r}, key=lambda k: list(rows[0]).index(k) if k in rows[0] else 99)
        with open(f"{OUT}/colour_{v}.csv", "w", newline="") as fo:
            wr = csv.DictWriter(fo, keys, restval=""); wr.writeheader(); wr.writerows(rows)
        print(v, sha[:12], len(hs), "holds")
elif phase == "score":
    M0 = json.load(open(f"{OUT}/M0_F_labels.json"))
    assert set(M0["labels"]) == set(vids)
    mrows, res = [], {}
    for v in vids:
        path, sha = mc.source(v); hs, acts = holds(v); port = mc.CEN[v]["format_class"] == "SHORT"; w, hgt = (180, 320) if port else (320, 180)
        A = mc.acts(v); pairs = [[(f, f + 2) for f in np.linspace(int(r["start_frame"]) + 1, int(r["end_frame"]) - 3, max(3, min(20, (int(r["end_frame"]) - int(r["start_frame"])) // 12))).astype(int)] for r in A]
        G = mc.grab(path, [f for p in pairs for pr in p for f in pr], w, hgt) if pairs else {}
        lab = []
        for r, p in zip(A, pairs):
            labs = [mc.label_pair(G[x], G[y]) for x, y in p if x in G and y in G]; mv = [l for l, _ in labs if l != "NO_TRANSLATION"]
            L = max(mc.PRI[:3], key=lambda c: (mv.count(c), -mc.PRI.index(c))) if mv and len(mv) * 3 >= len(labs) else "NO_TRANSLATION"
            lab.append(L); mrows.append(dict(video_id=v, seg=r["seg"], start_frame=r["start_frame"], frames=r["frames"], start_pts=r["start_pts"], motion_label=L, moving_pairs=f"{len(mv)}/{len(labs)}"))
        inst = ci.instances(v, {r["seg"]: L for r, L in zip(A, lab)})
        n = len(acts); cam, rul, obj = lab.count("WHOLE_FRAME_CAMERA"), lab.count("RULER_SCROLL"), lab.count("OBJECT_MOTION")
        col = list(csv.DictReader(open(f"{OUT}/colour_{v}.csv"))); nd = [r for r in col if r["cls"] in NONDEF]
        if nd:
            F = grab_colour(path, [int(r["frame"]) for r in nd], w, hgt)
            sheet([F[int(r["frame"])] for r in nd], [f"{r['seg']} {r['cls'][:9]} {float(r['start_pts']):.1f}s" for r in nd], f"{v}_nondefault.jpg", 10 if port else 6)
        ffm = list(csv.DictReader(open(f"{H}/videos/{v}/tables/FULL_FRAME_MEASUREMENTS.csv")))
        red_full = sum(float(x["mean_r"]) > 150 and float(x["mean_g"]) < 110 and float(x["mean_b"]) < 110 for x in ffm)
        fmt = M0["labels"][v]; cls = {c: sum(r["cls"] == c for r in col) for c in sorted({r["cls"] for r in col})}
        lim1 = {("L", "ORDINARY"): .13, ("L", "MAP_TOUR"): .20, ("L", "JOURNEY_LADDER"): .13, ("S", "ORDINARY"): .13, ("S", "MAP_TOUR"): .45}.get(("S" if port else "L", fmt))
        r = dict(format="SHORT" if port else "LONG", sha256=sha, M0=fmt, activities=n, gt6=len(A), cam=cam, ruler=rul, obj=obj, cam_share=round(cam / n, 3), obj_share=round(obj / n, 3),
                 M1=("UNDEFINED (no frozen Short limit for this format)" if lim1 is None else "PASS" if inst["instances"] / n <= lim1 else "FAIL") + f" {inst['instances']} instances/{n} ≤ {lim1} (raw moves {cam}/{n}={cam/n:.3f}, not scored)", camera_instances=inst, M3=("PASS" if obj / n <= (.33 if port else .25) else "FAIL") + f" {obj}/{n}",
                 hold_tiles=len(col), colour_classes=cls, nondefault_tiles=len(nd), red_full_frames=red_full,
                 C4=None if port else ("PASS" if any(r["cls"] in ("RED_MARK", "RED_SOLID") for r in col) else "FAIL"))
        if port: r["C1"] = "PASS" if red_full == 0 else f"FAIL {red_full}"
        else: r["M2"] = ("PASS" if (rul >= 3) == (fmt == "JOURNEY_LADDER") else "FAIL") + f" ruler={rul} fmt={fmt}"
        res[v] = r; print(v, r, flush=True)
    with open(f"{OUT}/motion_labels.csv", "w", newline="") as fo:
        wr = csv.DictWriter(fo, list(mrows[0])); wr.writeheader(); wr.writerows(mrows)
    json.dump(res, open(f"{OUT}/measured.json", "w"), indent=1, ensure_ascii=False)
