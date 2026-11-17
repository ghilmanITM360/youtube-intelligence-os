"""Hidden-region audit v2 for every sheet tile of every built video (HOLD, D4 first/mid/last, ACTIVITY), using sheet_index.csv frames.
Hidden = bottom label band (22/th of frame) + 3 px tile border ring (scaled to native). Band content metric same as pe_band_audit: (gray<90)|(S>80), excluded >0.95 (full dark) or <0.002 (empty).
Status per tile: EMPTY, COVERED_V1 (HOLD end strip already reviewed in campaign/band_review; portrait strips showed only top 44/57 of band), DUP (band within mean abs diff <4 of an earlier queued/covered band in same video), TO_REVIEW.
Writes campaign/hidden_audit/hidden_tiles.csv, STRIP_nn.jpg (TO_REVIEW bands plus the lowest 23% of COVERED_V1 portrait bands never shown), summary.json. Usage: python -I pe_hidden_audit.py"""
import csv, json, pathlib, cv2, numpy as np
W = pathlib.Path.home() / "YIOS-local-audits/primitive-education"; O = W / "campaign/hidden_audit"; O.mkdir(exist_ok=True)
v1 = {(r["video"], int(r["frame"])) for r in csv.DictReader(open(W / "campaign/band_review/band_index.csv"))}
SW = 960; rows = []; strips = []; summary = {}
def frac(b):
    return float(((cv2.cvtColor(b, cv2.COLOR_BGR2GRAY) < 90) | (cv2.cvtColor(b, cv2.COLOR_BGR2HSV)[..., 1] > 80)).mean())
for V in sorted((W / "videos").iterdir()):
    if not (V / "quality_gate.json").exists(): continue
    idx = list(csv.DictReader(open(V / "tables/sheet_index.csv")))
    want = sorted({int(r["frame"]) for r in idx}); meta = {int(r["frame"]): r for r in idx}
    cap = cv2.VideoCapture((V / "evidence/source_path.txt").read_text().strip()); k = 0; seen = []
    c = dict(tiles=len(want), ACTIVITY=0, EMPTY=0, COVERED_V1=0, DUP=0, TO_REVIEW=0, ring_only=0)
    for f in want:
        while k < f: cap.grab(); k += 1
        ok, im = cap.read(); assert ok, (V.name, f); k += 1
        h, w = im.shape[:2]; bh = round(h * (22 / 270 if w > h else 22 / 480)); r = round(3 * h / (270 if w > h else 480))
        b = im[h - bh:]; fr = frac(b); m = meta[f]
        # border ring (top/left/right; bottom is inside the band): content in the ring with nothing just inside it = fully hidden element
        ring = [im[:r], im[:, :r], im[:, w - r:]]; inner = [im[r:2 * r], im[:, r:2 * r], im[:, w - 2 * r:w - r]]
        ring_only = any(0.002 < frac(a) < 0.95 and frac(i) < 0.002 for a, i in zip(ring, inner))
        c["ring_only"] += ring_only; c["ACTIVITY"] += m["kind"] == "A"
        small = cv2.resize(b, (240, 24)).astype(np.int16)
        if not 0.002 < fr < 0.95: st = "EMPTY"
        elif (V.name, f) in v1:
            st = "COVERED_V1"; seen.append(small)
            if w < h and frac(b[-round(bh * 13 / 57):]) > 0.002: strips.append((V.name, m["seg"], f, m["kind"], "PORTRAIT_LOW_23PCT", b[-round(bh * 13 / 57):]))
        elif any(np.abs(small - s).mean() < 4 for s in seen): st = "DUP"
        else: st = "TO_REVIEW"; seen.append(small); strips.append((V.name, m["seg"], f, m["kind"], "BAND", b))
        c[st] += 1; rows.append(dict(video=V.name, seg=m["seg"], kind=m["kind"], frame=f, band_frac=round(fr, 4), status=st, ring_only=int(ring_only)))
    summary[V.name] = c; print(V.name, c, flush=True)
with open(O / "hidden_tiles.csv", "w", newline="") as fh:
    wr = csv.DictWriter(fh, fieldnames=list(rows[0])); wr.writeheader(); wr.writerows(rows)
tiles = []; sidx = []
for v, seg, f, kind, what, b in strips:
    t = cv2.resize(b, (SW, round(SW * b.shape[0] / b.shape[1]))); lab = np.zeros((16, SW, 3), np.uint8)
    cv2.putText(lab, f"{v} {seg} {kind} f{f} {what}", (3, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
    tiles.append(np.vstack([lab, t])); sidx.append(f"{v},{seg},{kind},{f},{what}")
H = 1500; i = 0; page = 1; col = []; 
def flush(col, page):
    cv2.imwrite(str(O / f"STRIP_{page:02d}.jpg"), np.vstack(col), [cv2.IMWRITE_JPEG_QUALITY, 88])
hh = 0
for j, t in enumerate(tiles):
    if hh + t.shape[0] > H: flush(col, page); sidx[j] += ""; col = []; hh = 0; page += 1
    col.append(t); hh += t.shape[0]; sidx[j] = f"STRIP_{page:02d}.jpg," + sidx[j]
if col: flush(col, page)
(O / "strip_index.csv").write_text("page,video,seg,kind,frame,what\n" + "\n".join(sidx) + "\n")
(O / "summary.json").write_text(json.dumps(dict(per_video=summary, strips=len(tiles), pages=page if tiles else 0), indent=1))
print("strips", len(tiles), "pages", page)
