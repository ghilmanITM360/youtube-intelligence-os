"""closure extras: all hold residue classified, crops of non-noise residue, cut before/after sheet. usage: extra.py <id>"""
import csv, json, sys, pathlib, numpy as np, cv2
v = sys.argv[1]; V = pathlib.Path.home()/f"YIOS-local-audits/xkcd-whatif/videos/{v}"; O = V/"closure_v1"; N = O/"native"
man = json.load(open(V/"source_manifest.json"))["source"]; rows = list(csv.DictReader(open(V/"tables/state_ledger.csv")))
px = np.array([int(m["px_diff_ge12"]) for m in csv.DictReader(open(V/"tables/FULL_FRAME_MEASUREMENTS.csv"))])
shots = list(csv.DictReader(open(V/"shot_ledger.csv")))
res = [i for r in rows if r["kind"] == "HOLD" for i in range(int(r["start_frame"])+1, int(r["end_frame"])+1) if px[i] > 50]
cuts = [int(s["start_frame"]) for s in shots[1:]]
want = sorted({j for i in res for j in (i-1, i)} | {j for c in cuts for j in (c-1, c)})
miss = [i for i in want if not (N/f"f{i:06d}.png").exists()]
if miss:
    cap = cv2.VideoCapture(man["file_path"]); ms = set(miss); n = 0
    while n <= max(miss):
        ok, fr = cap.read()
        if not ok: break
        if n in ms: cv2.imwrite(str(N/f"f{n:06d}.png"), fr)
        n += 1
    assert all((N/f"f{i:06d}.png").exists() for i in miss)
img = lambda i: cv2.imread(str(N/f"f{i:06d}.png"))
out = {}; crops = []
for i in res:
    d = cv2.absdiff(img(i), img(i-1)).max(2); n, lab, st, _ = cv2.connectedComponentsWithStats((d >= 12).astype(np.uint8))
    big = int(st[1:, 4].max()) if n > 1 else 0; cls = "NOISE" if big <= 20 else "VIEW"
    out[i] = {"px": int(px[i]), "max_diff": int(d.max()), "largest_component_px": big, "class": cls}
    if cls == "VIEW":
        k = 1 + int(st[1:, 4].argmax()); x, y, w, h = st[k, :4]; cx, cy = x + w//2, y + h//2
        x0, y0 = max(cx-120, 0), max(cy-90, 0); x1, y1 = min(x0+240, 1920), min(y0+180, 1080)
        a, b = img(i-1)[y0:y1, x0:x1], img(i)[y0:y1, x0:x1]; dd = np.clip(d[y0:y1, x0:x1].astype(int)*6, 0, 255).astype(np.uint8)
        t = np.hstack([a, b, cv2.cvtColor(dd, cv2.COLOR_GRAY2BGR)]); t = cv2.copyMakeBorder(t, 22, 2, 0, 0, cv2.BORDER_CONSTANT, value=(0,0,0))
        cv2.putText(t, f"f{i-1}|f{i}|diff x6  comp={big} max={int(d.max())} @({cx},{cy})", (4, 16), 0, .5, (0,0,255), 1); crops.append(t)
for s in range(0, len(crops), 8):
    c = crops[s:s+8]; W = max(x.shape[1] for x in c)
    cv2.imwrite(str(O/f"residue_crops_{s//8+1:02d}.png"), np.vstack([cv2.copyMakeBorder(x, 0, 0, 0, W-x.shape[1], cv2.BORDER_CONSTANT) for x in c]))
tiles = []
for c in cuts:
    p = [cv2.resize(img(j), None, fx=.25, fy=.25, interpolation=cv2.INTER_AREA) for j in (c-1, c)]
    t = np.hstack(p); cv2.putText(t, f"cut f{c-1}|f{c}", (6, 22), 0, .7, (0,0,255), 2); tiles.append(cv2.copyMakeBorder(t, 2, 2, 2, 2, cv2.BORDER_CONSTANT, value=(0,0,255)))
for s in range(0, len(tiles), 8):
    c = tiles[s:s+8]
    while len(c) % 2: c.append(np.zeros_like(c[0]))
    cv2.imwrite(str(O/f"cuts_{s//8+1:02d}.jpg"), np.vstack([np.hstack(c[k:k+2]) for k in range(0, len(c), 2)]), [cv2.IMWRITE_JPEG_QUALITY, 88])
json.dump({"residue_all": out, "cuts": cuts}, open(O/"extra_checks.json", "w"), indent=0)
print("residue", len(res), "view", sum(o["class"]=="VIEW" for o in out.values()), "crop sheets", -(-len(crops)//8), "cuts", len(cuts))
