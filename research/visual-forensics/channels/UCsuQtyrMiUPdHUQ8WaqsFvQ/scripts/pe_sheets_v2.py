"""Non-occluding review sheets: the SAME tiles as tables/sheet_index.csv, but the label sits above the image and the kind colour is a gutter, so 100% of each tile's frame is visible.
pe_sheets.py and frames/sheets stay untouched. Writes frames/sheets_v2/SHEET_nn.jpg. Usage: python -I pe_sheets_v2.py <video_dir>"""
import csv, sys, pathlib, cv2, numpy as np
V = pathlib.Path(sys.argv[1]); idx = list(csv.DictReader(open(V / "tables/sheet_index.csv")))
cap = cv2.VideoCapture((V / "evidence/source_path.txt").read_text().strip()); W0, H0 = int(cap.get(3)), int(cap.get(4))
tw, th, cols, rows_ = (270, 480, 5, 2) if H0 > W0 else (480, 270, 3, 4)
need = sorted({int(r["frame"]) for r in idx}); got = {}; k = 0
for f in need:
    while k < f: cap.grab(); k += 1
    ok, im = cap.read(); assert ok, f; k += 1
    got[f] = cv2.resize(im, (tw, th), interpolation=cv2.INTER_AREA)
out = V / "frames/sheets_v2"; out.mkdir(parents=True, exist_ok=True); G, L = 3, 20; per = cols * rows_
for sn in range(0, len(idx), per):
    c = np.full((rows_ * (th + L + 2 * G), cols * (tw + 2 * G), 3), 90, np.uint8)
    for j, r in enumerate(idx[sn:sn + per]):
        i, m = divmod(j, cols); y, x = i * (th + L + 2 * G), m * (tw + 2 * G); col = (0, 0, 200) if r["kind"] == "A" else (0, 120, 0)
        c[y:y + th + L + 2 * G, x:x + tw + 2 * G] = col
        cv2.putText(c, f"{r['seg']} {r['kind']} f{r['frame']} {float(r['pts'] or 0):.3f}s", (x + 4, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
        c[y + L + G:y + L + G + th, x + G:x + G + tw] = got[int(r["frame"])]
    cv2.imwrite(str(out / f"SHEET_{sn // per + 1:02d}.jpg"), c, [cv2.IMWRITE_JPEG_QUALITY, 88])
print(V.name, "tiles", len(idx), "sheets", (len(idx) + per - 1) // per)
