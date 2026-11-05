"""Targeted review sheets of the band hidden by the sheet label: stacks, for every HOLD flagged by pe_band_audit (full list recomputed), the hidden bottom strip with seg label.
Writes campaign/band_review/BAND_nn.jpg + band_index.csv. Usage: python -I pe_band_sheet.py"""
import csv, pathlib, cv2, numpy as np
W = pathlib.Path.home() / "YIOS-local-audits/primitive-education"; O = W / "campaign/band_review"; O.mkdir(exist_ok=True); tiles = []; idx = []
for V in sorted((W / "videos").iterdir()):
    if not (V / "quality_gate.json").exists(): continue
    H = {int(s["end_frame"]): s["seg"] for s in csv.DictReader(open(V / "tables/segments_v1.csv")) if s["kind"] == "HOLD"}
    cap = cv2.VideoCapture((V / "evidence/source_path.txt").read_text().strip()); k = 0; last = max(H)
    while k <= last:
        if k in H:
            ok, im = cap.read()
            if not ok: break
            h, w = im.shape[:2]; b = im[h - round(h * (22 / 270 if w > h else 22 / 480)):]
            g = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY); hs = cv2.cvtColor(b, cv2.COLOR_BGR2HSV); fr = float(((g < 90) | (hs[..., 1] > 80)).mean())
            if 0.002 < fr < 0.95:
                t = cv2.resize(b, (700, round(700 * b.shape[0] / w))); pad = np.full((70, 700, 3), 255, np.uint8); pad[:t.shape[0]] = t[:70]
                lab = np.zeros((18, 700, 3), np.uint8); cv2.putText(lab, f"{V.name} {H[k]} f{k}", (3, 13), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (255, 255, 255), 1)
                tiles.append(np.vstack([lab, pad[:t.shape[0] if w > h else 44]]) if False else np.vstack([lab, pad[:44]])); idx.append((V.name, H[k], k, round(fr, 4)))
        elif not cap.grab(): break
        k += 1
n = 48
for i in range(0, len(tiles), n):
    c = tiles[i:i + n]; c += [np.full_like(tiles[0], 90)] * (n - len(c))
    cv2.imwrite(str(O / f"BAND_{i // n + 1:02d}.jpg"), np.hstack([np.vstack(c[:24]), np.vstack(c[24:])]), [cv2.IMWRITE_JPEG_QUALITY, 88])
with open(O / "band_index.csv", "w", newline="") as f: csv.writer(f).writerows([("video", "seg", "frame", "band_frac")] + idx)
print(len(tiles), "strips")
