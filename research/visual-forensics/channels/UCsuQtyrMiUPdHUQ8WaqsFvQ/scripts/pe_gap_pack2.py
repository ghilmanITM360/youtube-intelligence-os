"""Second bounded evidence pack for items the gap reviewer left STILL_UNRESOLVED: exactly the crops it named as missing, labelled, full frame context. Writes campaign/gap_review/R2_nn.jpg. Usage: python -I pe_gap_pack2.py"""
import csv, pathlib, cv2, numpy as np
W = pathlib.Path.home() / "YIOS-local-audits/primitive-education"; O = W / "campaign/gap_review"
def rng(v, seg):
    s = next(x for x in csv.DictReader(open(W / f"videos/{v}/tables/state_ledger.csv")) if x["seg"] == seg); return int(s["start_frame"]), int(s["end_frame"])
def fr(v, n):
    c = cv2.VideoCapture(str(W / "source_media" / f"{v}.mp4")); c.set(1, n); ok, im = c.read(); assert ok, (v, n); return im
def row(v, seg, frames, box=None, zoom=None, h=270):
    a, b = rng(v, seg); ts = []
    for n in frames:
        n = n if isinstance(n, int) else eval(n, dict(a=a, b=b)); im = fr(v, n)
        if box: x0, y0, x1, y1 = box; im = im[y0:y1, x0:x1]
        t = cv2.resize(im, (round(im.shape[1] * h / im.shape[0]), h), interpolation=cv2.INTER_NEAREST if im.shape[0] < h else cv2.INTER_AREA); l = np.zeros((16, t.shape[1], 3), np.uint8); cv2.putText(l, f"f{n}", (2, 12), 0, .4, (255, 255, 255), 1); ts.append(np.vstack([l, t]))
        ts.append(np.full((h + 16, 5, 3), 90, np.uint8))
    r = np.hstack(ts)[:, :1500]; r = np.hstack([r, np.full((r.shape[0], 1500 - r.shape[1], 3), 60, np.uint8)]); l = np.zeros((18, 1500, 3), np.uint8); cv2.putText(l, f"{v} {seg} f{a}-{b}", (2, 14), 0, .45, (0, 255, 255), 1); return np.vstack([l, r])
P = [("3AsDdMQr_nQ", "G0008", ["a+1", "(a+b)//2", "b"], None), ("6YHva7Me2ls", "G0090", ["b"], "GLYPH"), ("6YHva7Me2ls", "G0138", ["a"], None), ("DekaeZPzTAQ", "G0080", ["a-1", "a"], None),
     ("KyBWJPaF1KI", "G0140", ["a", "a+20", "a+40", "a+60", "b-1"], None), ("Nv4xJ_NsFdo", "G0086", ["a-1", "a"], None), ("RM_KBLDLsnQ", "G0052", [1529, 1530, 1531], None), ("RM_KBLDLsnQ", "G0106", ["a-1", "a"], None),
     ("RmTdnXHbI8s", "G0015", ["a", "(a+b)//2", "b"], None), ("W8AVd7RhTME", "G0049", ["a", "(a+b)//2", "b"], None), ("qB_EKkMyuUE", "G0174", ["a"], None), ("qB_EKkMyuUE", "G0084", ["a"], None), ("qB_EKkMyuUE", "G0202", ["a"], None), ("qB_EKkMyuUE", "G0106", ["a"], None),
     ("uIG2U_1xynQ", "G0024", ["a"], None), ("xBJ6suQSt98", "G0032", ["a", "a+1", "a+2", "a+3"], None), ("xBJ6suQSt98", "G0046", ["a", "a+1", "a+8"], None), ("xBJ6suQSt98", "G0047", ["a", "b"], None), ("RM_KBLDLsnQ", "G0101", ["a"], None)]
rows = []
for v, seg, frs, box in P:
    if box == "GLYPH": a, b = rng(v, seg); im = fr(v, b); ys, xs = np.where(cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) < 90); frs2 = [b]; rows.append(row(v, seg, [b])); continue
    rows.append(row(v, seg, frs))
page = 1; col = []; hh = 0
for r in rows:
    if hh + r.shape[0] > 1400 and col: cv2.imwrite(str(O / f"R2_{page:02d}.jpg"), np.vstack(col), [cv2.IMWRITE_JPEG_QUALITY, 90]); col = []; hh = 0; page += 1
    col.append(r); hh += r.shape[0]
cv2.imwrite(str(O / f"R2_{page:02d}.jpg"), np.vstack(col), [cv2.IMWRITE_JPEG_QUALITY, 90]); print("pages", page)
# deterministic checks
def pair(v, sa, sb):
    a = fr(v, rng(v, sa)[0]); b = fr(v, rng(v, sb)[0]); d = cv2.absdiff(a, b).max(axis=2); return sa, sb, round(float((d > 25).mean()), 5)
print(pair("qB_EKkMyuUE", "G0174", "G0084"), pair("qB_EKkMyuUE", "G0202", "G0106"), pair("RM_KBLDLsnQ", "G0106", "G0101"))
A, B = rng("xBJ6suQSt98", "G0032"); ds = []
for n in range(A, A + 6):
    d = cv2.absdiff(fr("xBJ6suQSt98", n), fr("xBJ6suQSt98", n + 1)).max(axis=2); ys, xs = np.where(d > 25); ds.append((n, int((d > 25).sum()), (int(xs.min()), int(xs.max()), int(ys.min()), int(ys.max())) if len(xs) else None))
print(ds)
for n in (1528, 1529, 1530, 1531, 1532):
    d = cv2.absdiff(fr("RM_KBLDLsnQ", n), fr("RM_KBLDLsnQ", n + 1)).max(axis=2); print(n, int((d > 25).sum()))
