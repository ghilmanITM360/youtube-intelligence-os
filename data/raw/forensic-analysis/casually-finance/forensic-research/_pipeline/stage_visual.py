"""Stage B: deterministic visual timeline. Decodes EVERY frame (native fps, passthrough) to a small gray stream, computes per-frame change features,
segments them into activity episodes (candidate cuts / transitions / local motions), derives candidate SHOTS and STATES, extracts one representative
full-res frame per state and builds labelled contact sheets for visual review. Auto outputs are CANDIDATES for review, not final observations.
Usage: python3 -B stage_visual.py <VIDEO_ID> <WORK_ROOT> <OUT_DIR> [decode|segment|frames|all]
"""
import csv, json, subprocess, sys
from pathlib import Path
import numpy as np

PX_THR = 10          # per-pixel gray change that counts as 'changed'
ACT_MIN_PX = 6       # changed pixels (of ~20k) for a frame pair to count as active
GAP_FRAMES = 3       # merge activity separated by <= this many quiet frames
BOUNDARY_FRAC = 0.30  # a frame pair changing >=30% of pixels => composition replaced (cut/wipe/dissolve)
MIN_STATE_SEC = 0.25


def meta(out, vid):
    return next(r for r in csv.DictReader(open(Path(out) / "00_MANIFEST/SELECTED_18.csv")) if r["video_id"] == vid)


def decode(vid, work, out):
    m = meta(out, vid); fps = float(m["fps"]); vertical = int(m["height"]) > int(m["width"])
    W, H = (108, 192) if vertical else (192, 108)
    mm = work / "gray.u8"
    if mm.exists() and (work / "features.npz").exists(): return
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", m["local_path"], "-an", "-vf", f"scale={W}:{H}:flags=area,format=gray", "-fps_mode", "passthrough", "-f", "rawvideo", "-"], stdout=subprocess.PIPE)
    fs = W * H; chunks = []
    while True:
        b = p.stdout.read(fs * 512)
        if not b: break
        chunks.append(np.frombuffer(b[: len(b) // fs * fs], dtype=np.uint8).reshape(-1, H, W).copy())
    p.wait()
    F = np.concatenate(chunks); N = len(F)
    F.tofile(mm)
    D = np.zeros((N, H, W), dtype=bool); mad = np.zeros(N, dtype=np.float32)
    cnt = np.zeros(N, dtype=np.int32); lum = F.reshape(N, -1).mean(1).astype(np.float32)
    bbox = np.zeros((N, 4), dtype=np.float32); cen = np.zeros((N, 2), dtype=np.float32)
    ys, xs = np.mgrid[0:H, 0:W]
    for i in range(1, N):
        d = np.abs(F[i].astype(np.int16) - F[i - 1].astype(np.int16))
        mad[i] = d.mean(); msk = d > PX_THR; c = int(msk.sum()); cnt[i] = c
        if c >= ACT_MIN_PX:
            rs, cs = msk.sum(1), msk.sum(0)
            cr, cc = np.cumsum(rs) / c, np.cumsum(cs) / c
            bbox[i] = [np.searchsorted(cc, 0.02) / W, np.searchsorted(rr := cr, 0.02) / H, (np.searchsorted(cc, 0.98) + 1) / W, (np.searchsorted(cr, 0.98) + 1) / H]
            cen[i] = [xs[msk].mean() / W, ys[msk].mean() / H]
    np.savez_compressed(work / "features.npz", mad=mad, cnt=cnt, lum=lum, bbox=bbox, cen=cen, fps=fps, W=W, H=H, N=N)
    print("decoded", vid, N, "frames", W, H)


def segment(vid, work, out):
    z = np.load(work / "features.npz"); mad, cnt, lum, bbox, cen = z["mad"], z["cnt"], z["lum"], z["bbox"], z["cen"]
    fps, W, H, N = float(z["fps"]), int(z["W"]), int(z["H"]), int(z["N"]); area = W * H
    active = cnt >= ACT_MIN_PX
    eps, i = [], 1
    while i < N:
        if not active[i]: i += 1; continue
        j = i; last = i
        while j + 1 < N and (j + 1 - last) <= GAP_FRAMES:
            j += 1
            if active[j]: last = j
        eps.append((i, last)); i = last + 1
    rows = []
    for k, (a, b) in enumerate(eps):
        seg = slice(a, b + 1); c = cnt[seg]; frac = c / area; nf = b - a + 1
        bb = bbox[seg][c >= ACT_MIN_PX]
        bx0, by0, bx1, by1 = (bb[:, 0].min(), bb[:, 1].min(), bb[:, 2].max(), bb[:, 3].max()) if len(bb) else (0, 0, 0, 0)
        barea = float((bx1 - bx0) * (by1 - by0))
        cs = cen[seg][c >= ACT_MIN_PX]
        dvec = (cs[-min(3, len(cs)):].mean(0) - cs[:min(3, len(cs))].mean(0)) if len(cs) >= 2 else np.zeros(2)
        lum_before, lum_after = float(lum[max(a - 1, 0)]), float(lum[min(b + 1, N - 1)])
        peak, mean_f = float(frac.max()), float(frac.mean())
        if peak >= BOUNDARY_FRAC and nf <= 2: cls = "HARD_CUT"
        elif peak >= BOUNDARY_FRAC and nf > 2: cls = "WIPE_DISSOLVE_OR_LARGE_REPLACEMENT"
        elif nf >= 4 and barea > 0.6 and mean_f >= 0.03: cls = "GLOBAL_TRANSFORM_PAN_ZOOM_SCROLL_OR_FADE"
        elif peak < 0.004: cls = "MICRO_CHANGE"
        else: cls = "LOCAL_REVEAL_OR_MOVE"
        rows.append(dict(ep_id=f"E{k + 1:04d}", f0=a, f1=b, t0=round(a / fps, 3), t1=round((b + 1) / fps, 3), dur=round((b - a + 1) / fps, 3), n_frames=nf, peak_frac=round(peak, 4),
                         mean_frac=round(mean_f, 4), bbox_x0=round(float(bx0), 3), bbox_y0=round(float(by0), 3), bbox_x1=round(float(bx1), 3), bbox_y1=round(float(by1), 3), bbox_area=round(barea, 3),
                         centroid_dx=round(float(dvec[0]), 3), centroid_dy=round(float(dvec[1]), 3), lum_before=round(lum_before, 1), lum_after=round(lum_after, 1), cls=cls))
    # shots: boundary episodes split the timeline
    bnds = [r for r in rows if r["cls"] in ("HARD_CUT", "WIPE_DISSOLVE_OR_LARGE_REPLACEMENT")]
    dur_total = N / fps
    shot_starts = [0.0] + [r["t1"] if r["cls"] != "HARD_CUT" else r["t0"] for r in bnds]
    shots = []
    for k, s in enumerate(shot_starts):
        e = shot_starts[k + 1] if k + 1 < len(shot_starts) else dur_total
        shots.append(dict(shot_id=f"S{k + 1:03d}", start=round(s, 3), end=round(e, 3), transition_in="START" if k == 0 else bnds[k - 1]["cls"], transition_ep=("" if k == 0 else bnds[k - 1]["ep_id"])))
    # states: within each shot, stable intervals between non-boundary episodes (micro changes ignored)
    inner = [r for r in rows if r["cls"] not in ("HARD_CUT", "WIPE_DISSOLVE_OR_LARGE_REPLACEMENT", "MICRO_CHANGE")]
    states = []
    for sh in shots:
        evs = [r for r in inner if sh["start"] <= r["t0"] < sh["end"]]
        # merge episodes whose gap < MIN_STATE_SEC into one
        merged = []
        for r in evs:
            if merged and r["t0"] - merged[-1]["t1"] < MIN_STATE_SEC:
                merged[-1]["t1"] = r["t1"]; merged[-1]["eps"].append(r["ep_id"])
            else: merged.append(dict(t0=r["t0"], t1=r["t1"], eps=[r["ep_id"]]))
        cur = sh["start"]; k = 0
        for mg in merged:
            if mg["t0"] - cur >= MIN_STATE_SEC or k == 0:
                states.append(dict(state_id=f"{sh['shot_id']}.{k}", shot_id=sh["shot_id"], start=round(cur, 3), end=round(mg["t0"], 3), eps_after=";".join(mg["eps"]))); k += 1
            cur = mg["t1"]
        states.append(dict(state_id=f"{sh['shot_id']}.{k}", shot_id=sh["shot_id"], start=round(cur, 3), end=sh["end"], eps_after=""))
    for s in states:
        d = s["end"] - s["start"]; s["dur"] = round(d, 3)
        s["rep_t"] = round(s["start"] + max(min(d * 0.7, d - 0.06), 0.0), 3)
    json.dump(dict(video_id=vid, fps=fps, frames=N, duration=dur_total, params=dict(PX_THR=PX_THR, ACT_MIN_PX=ACT_MIN_PX, GAP_FRAMES=GAP_FRAMES, BOUNDARY_FRAC=BOUNDARY_FRAC, MIN_STATE_SEC=MIN_STATE_SEC),
                   episodes=rows, shots=shots, states=states), open(work / "visual_auto.json", "w"))
    from collections import Counter
    print(vid, "frames", N, "episodes", len(rows), Counter(r["cls"] for r in rows), "shots", len(shots), "states", len(states))


def frames_and_sheets(vid, work, out):
    from PIL import Image, ImageDraw, ImageFont
    m = meta(out, vid); va = json.load(open(work / "visual_auto.json")); fdir = work / "frames"; sdir = work / "sheets"; fdir.mkdir(exist_ok=True); sdir.mkdir(exist_ok=True)
    vertical = int(m["height"]) > int(m["width"])
    tw, th = (240, 426) if vertical else (640, 360)
    cols, rows_ = (8, 2) if vertical else (3, 4)
    for s in va["states"]:
        fp = fdir / f"{s['state_id']}.jpg"
        if not fp.exists():
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{s['rep_t']:.3f}", "-i", m["local_path"], "-frames:v", "1", "-vf", f"scale={tw}:{th}", "-q:v", "3", str(fp)], check=True)
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 22)
    per = cols * rows_; st = va["states"]
    for si in range(0, len(st), per):
        sheet = Image.new("RGB", (cols * tw, rows_ * th), (60, 60, 60))
        for k, s in enumerate(st[si: si + per]):
            im = Image.open(fdir / f"{s['state_id']}.jpg"); x, y = (k % cols) * tw, (k // cols) * th
            sheet.paste(im, (x, y)); d = ImageDraw.Draw(sheet)
            d.rectangle([x, y, x + 200, y + 28], fill=(200, 0, 0)); d.text((x + 4, y + 2), f"{s['state_id']} @{s['rep_t']:.2f}s", fill=(255, 255, 255), font=font)
            d.rectangle([x, y, x + tw - 1, y + th - 1], outline=(120, 120, 120))
        sheet.save(sdir / f"sheet_{si // per + 1:03d}.jpg", quality=80)
    print(vid, "frames", len(st), "sheets", (len(st) + per - 1) // per)


if __name__ == "__main__":
    vid, wroot, out = sys.argv[1:4]; mode = sys.argv[4] if len(sys.argv) > 4 else "all"
    work = Path(wroot) / vid; work.mkdir(parents=True, exist_ok=True)
    if mode in ("decode", "all"): decode(vid, work, out)
    if mode in ("segment", "all"): segment(vid, work, out)
    if mode in ("frames", "all"): frames_and_sheets(vid, work, out)
