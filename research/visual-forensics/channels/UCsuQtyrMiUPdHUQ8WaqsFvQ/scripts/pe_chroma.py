"""D5 colour-change pass: per-frame count of pixels with max-channel diff>=40 at 480px width (catches hue swaps invisible to luma detectors). Writes tables/chroma_diff.csv. Usage: python -I pe_chroma.py <video_dir>"""
import csv, sys, pathlib, cv2
V = pathlib.Path(sys.argv[1]).resolve(); cap = cv2.VideoCapture((V / "evidence/source_path.txt").read_text().strip()); prev = None; i = 0
with open(V / "tables/chroma_diff.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["frame", "px_c40"])
    while True:
        ok, im = cap.read()
        if not ok: break
        s = cv2.resize(im, (480, int(480 * im.shape[0] / im.shape[1])), interpolation=cv2.INTER_AREA)
        w.writerow([i, 0 if prev is None else int((cv2.absdiff(s, prev).max(axis=2) >= 40).sum())]); prev = s; i += 1
