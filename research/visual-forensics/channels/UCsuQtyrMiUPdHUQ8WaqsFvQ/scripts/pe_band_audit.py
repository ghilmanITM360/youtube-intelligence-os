"""Measure what the sheet label bar hides: pe_sheets.py paints 22 px over each tile's bottom, hiding the bottom 22/th of the frame in every sheet.
For every HOLD end frame of every built video: dark or saturated pixels in that hidden band. Writes campaign/SHEET_LABEL_BAND_AUDIT.json. Usage: python -I pe_band_audit.py"""
import csv, json, pathlib, cv2, numpy as np
W = pathlib.Path.home() / "YIOS-local-audits/primitive-education"; out = {}
for V in sorted((W / "videos").iterdir()):
    if not (V / "quality_gate.json").exists(): continue
    H = [s for s in csv.DictReader(open(V / "tables/segments_v1.csv")) if s["kind"] == "HOLD"]
    cap = cv2.VideoCapture((V / "evidence/source_path.txt").read_text().strip()); frac = None; rows = []
    want = {int(s["end_frame"]): s["seg"] for s in H}; k = 0; last = max(want)
    while k <= last:
        if k in want:
            ok, im = cap.read()
            if not ok: break
            h = im.shape[0]; b = im[h - round(h * (22 / 270 if im.shape[1] > h else 22 / 480)):]
            g = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY); hs = cv2.cvtColor(b, cv2.COLOR_BGR2HSV)
            rows.append((want[k], k, round(float(((g < 90) | (hs[..., 1] > 80)).mean()), 4)))
        elif not cap.grab(): break
        k += 1
    # full-black or full-ink frames are not hidden content, so exclude them from the review list
    hit = [r for r in rows if 0.002 < r[2] < 0.95]
    out[V.name] = dict(holds=len(rows), holds_with_band_content=len(hit), share=round(len(hit) / len(rows), 3), top=sorted(hit, key=lambda r: -r[2])[:6])
(W / "campaign/SHEET_LABEL_BAND_AUDIT.json").write_text(json.dumps(out, indent=1))
for k, v in out.items(): print(k, v["holds"], v["holds_with_band_content"], v["share"], v["top"][:3])
