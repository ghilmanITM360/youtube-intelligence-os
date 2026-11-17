"""Second pass over tiles pe_hidden_audit.py marked EMPTY: the first metric misses faint marks on white and light text on a full-dark band.
Flags EMPTY bands with >0.2% pixels gray<235 (when bright background) or gray>150 (when dark background); landscape+portrait. Writes campaign/hidden_audit/FAINT_nn.jpg + faint_index.csv. Usage: python -I pe_hidden_audit_faint.py"""
import csv, pathlib, cv2, numpy as np, collections
W = pathlib.Path.home() / "YIOS-local-audits/primitive-education"; O = W / "campaign/hidden_audit"
rows = [r for r in csv.DictReader(open(O / "hidden_tiles.csv")) if r["status"] == "EMPTY"]; by = collections.defaultdict(list)
for r in rows: by[r["video"]].append(r)
tiles = []; idx = []; tot = collections.Counter()
for v, rs in by.items():
    cap = cv2.VideoCapture((W / "videos" / v / "evidence/source_path.txt").read_text().strip()); k = 0; seen = []
    for r in sorted(rs, key=lambda x: int(x["frame"])):
        f = int(r["frame"])
        while k < f: cap.grab(); k += 1
        ok, im = cap.read(); assert ok; k += 1
        h, w = im.shape[:2]; b = im[h - round(h * (22 / 270 if w > h else 22 / 480)):]; g = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY); dark = float(g.mean()) < 128
        fr = float((g > 150).mean()) if dark else float((g < 235).mean()); tot[v, "dark" if dark else "bright"] += 1
        if fr <= 0.002: continue
        small = cv2.resize(b, (240, 24)).astype(np.int16)
        if any(np.abs(small - s).mean() < 4 for s in seen): tot[v, "dup"] += 1; continue
        seen.append(small); t = cv2.resize(b, (960, round(960 * b.shape[0] / w))); lab = np.zeros((16, 960, 3), np.uint8)
        cv2.putText(lab, f"{v} {r['seg']} {r['kind']} f{f} {'dark' if dark else 'bright'} {fr:.3f}", (3, 12), cv2.FONT_HERSHEY_SIMPLEX, .4, (255, 255, 255), 1)
        tiles.append(np.vstack([lab, t])); idx.append((v, r["seg"], r["kind"], f, "dark" if dark else "bright", round(fr, 4)))
page = 1; col = []; hh = 0
for t in tiles:
    if hh + t.shape[0] > 1500: cv2.imwrite(str(O / f"FAINT_{page:02d}.jpg"), np.vstack(col), [cv2.IMWRITE_JPEG_QUALITY, 88]); col = []; hh = 0; page += 1
    col.append(t); hh += t.shape[0]
if col: cv2.imwrite(str(O / f"FAINT_{page:02d}.jpg"), np.vstack(col), [cv2.IMWRITE_JPEG_QUALITY, 88])
with open(O / "faint_index.csv", "w", newline="") as fh: csv.writer(fh).writerows([("video", "seg", "kind", "frame", "bg", "frac")] + idx)
print("EMPTY", len(rows), "flagged", len(tiles), "pages", page if tiles else 0, dict((str(k), v) for k, v in tot.items() if k[1] == "dark"))
