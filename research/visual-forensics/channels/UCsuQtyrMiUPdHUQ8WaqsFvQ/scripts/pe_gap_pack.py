"""Evidence pack for the remaining per-video visual gaps. Two sheet types in campaign/gap_review/:
UNRES_nn.jpg: every UNRESOLVED/LOW segment: native crop around the measured change (before | after | amplified diff), with bbox and changed px.
UNV_nn.jpg: every not-yet-viewed frame of partially viewed ACTIVITY segments, in order, full frame, nothing over the image.
Index: gap_items.csv. Usage: python -I pe_gap_pack.py"""
import csv, json, pathlib, cv2, numpy as np
W = pathlib.Path.home() / "YIOS-local-audits/primitive-education"; O = W / "campaign/gap_review"; O.mkdir(exist_ok=True)
items = []; un_rows = []; unv_groups = []
def label(s, w, h=18):
    l = np.zeros((h, w, 3), np.uint8); cv2.putText(l, s, (3, h - 5), cv2.FONT_HERSHEY_SIMPLEX, .42, (255, 255, 255), 1); return l
for V in sorted((W / "videos").iterdir()):
    if not (V / "quality_gate.json").exists(): continue
    S = list(csv.DictReader(open(V / "tables/state_ledger.csv")))
    cap = cv2.VideoCapture((V / "evidence/source_path.txt").read_text().strip())
    def fr(n): cap.set(cv2.CAP_PROP_POS_FRAMES, n); ok, im = cap.read(); assert ok, (V.name, n); return im
    for s in S:
        a, b = int(s["start_frame"]), int(s["end_frame"])
        if s["confidence"] == "LOW" or "UNRESOLVED" in s["description"]:
            p, q = fr(max(0, a - 1)), fr(b if s["kind"] == "ACTIVITY" else b)
            if s["kind"] == "HOLD": p = fr(a)
            d = cv2.absdiff(p, q).max(axis=2); ys, xs = np.where(d > 25); h, w = d.shape
            if len(xs): x0, x1, y0, y1 = max(0, xs.min() - 40), min(w, xs.max() + 40), max(0, ys.min() - 40), min(h, ys.max() + 40)
            else: x0, x1, y0, y1 = 0, w, 0, h
            rowh = 200; sc = rowh / (y1 - y0); tw = min(460, max(40, round((x1 - x0) * sc)))
            mk = lambda im: cv2.resize(im[y0:y1, x0:x1], (tw, rowh), interpolation=cv2.INTER_AREA if sc < 1 else cv2.INTER_NEAREST)
            dv = cv2.cvtColor(np.clip(d * 4, 0, 255).astype(np.uint8), cv2.COLOR_GRAY2BGR)
            row = np.hstack([mk(p), np.full((rowh, 6, 3), 90, np.uint8), mk(q), np.full((rowh, 6, 3), 90, np.uint8), mk(dv)])
            pad = np.full((rowh, max(0, 1420 - row.shape[1]), 3), 60, np.uint8); row = np.hstack([row, pad])
            tag = f"{V.name} {s['seg']} {s['kind'][0]} f{a}-{b} | before f{p is not None and max(0, a - 1) if s['kind'] == 'ACTIVITY' else a} / after f{b} / diff x4 | crop x{x0}-{x1} y{y0}-{y1} of {w}x{h} | changed px {int((d > 25).sum())}"
            un_rows.append(np.vstack([label(tag, row.shape[1]), row])); items.append(dict(type="UNRES", video=V.name, seg=s["seg"], start=a, end=b, sheet="", old_description=s["description"]))
        if s["kind"] == "ACTIVITY":
            view = {int(x) for x in s["view_frames"].split(";") if x}; miss = [f for f in range(a, b + 1) if f not in view]
            if miss:
                port = fr(a).shape[0] > fr(a).shape[1]; tw, th = (135, 240) if port else (240, 135); ts = []
                for f in miss:
                    t = cv2.resize(fr(f), (tw, th), interpolation=cv2.INTER_AREA); ts.append(np.vstack([label(f"f{f}", tw, 15), t]))
                unv_groups.append((f"{V.name} {s['seg']} f{a}-{b} unviewed {len(miss)}: {s['description'][:150]}", ts))
                items.append(dict(type="UNV", video=V.name, seg=s["seg"], start=a, end=b, sheet=";".join(map(str, miss)), old_description=s["description"]))
def paginate(rows, stem):
    page = 1; col = []; hh = 0; idx = []
    for r in rows:
        if hh + r.shape[0] > 1500 and col: cv2.imwrite(str(O / f"{stem}_{page:02d}.jpg"), np.vstack(col), [cv2.IMWRITE_JPEG_QUALITY, 88]); col = []; hh = 0; page += 1
        col.append(r); hh += r.shape[0]
    if col: cv2.imwrite(str(O / f"{stem}_{page:02d}.jpg"), np.vstack(col), [cv2.IMWRITE_JPEG_QUALITY, 88])
    return page if rows else 0
rows = []; PW = 1460
for head, ts in unv_groups:
    rows.append(label(head, PW, 20)); per = PW // (ts[0].shape[1] + 4); 
    for i in range(0, len(ts), per):
        chunk = ts[i:i + per]; line = np.hstack([np.hstack([t, np.full((t.shape[0], 4, 3), 90, np.uint8)]) for t in chunk]); rows.append(np.hstack([line, np.full((line.shape[0], PW - line.shape[1], 3), 60, np.uint8)]))
print("UNRES items", len(un_rows), "pages", paginate(un_rows, "UNRES")); print("UNV groups", len(unv_groups), "frames", sum(len(t) for _, t in unv_groups), "pages", paginate(rows, "UNV"))
with open(O / "gap_items.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(items[0])); w.writeheader(); w.writerows(items)
