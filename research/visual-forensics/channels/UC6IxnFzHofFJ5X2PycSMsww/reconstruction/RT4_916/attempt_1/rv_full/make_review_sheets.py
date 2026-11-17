"""Review sheets for RT4 attempt_1: (A) stride-24 whole-render sheets (2 x 30 frames); (B) before/after pair sheets for all 26 intended events (4 sheets). Labels under tiles."""
import cv2, numpy as np, csv
ev = [(int(r["start_frame"]), int(r["end_frame"]), r["device"], r["description"]) for r in csv.DictReader(open("RT1_intended_timeline.csv"))]
need = set(range(0, 1440, 24)) | {1439}
for s, e, *_ in ev: need |= {max(0, s - 1), e}; 
need |= {703}
cap = cv2.VideoCapture("RT4_animatic.mp4"); k = 0; got = {}
while True:
    ok, im = cap.read()
    if not ok: break
    if k in need: got[k] = im
    k += 1
def tile(f, w, h):
    t = cv2.resize(got[f], (w, h), interpolation=cv2.INTER_AREA); c = np.full((h + 18, w, 3), 50, np.uint8); c[:h] = t
    cv2.putText(c, f"f{f}", (3, h + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1, cv2.LINE_AA); return c
def sheet(fs, cols, w, h, name):
    rows = -(-len(fs) // cols); H = h + 18; canvas = np.full((rows * H, cols * (w + 2), 3), 30, np.uint8)
    for i, f in enumerate(fs):
        r, c = divmod(i, cols); canvas[r * H:(r + 1) * H, c * (w + 2):c * (w + 2) + w] = tile(f, w, h)
    cv2.imwrite(name, canvas)
strides = list(range(0, 1440, 24)) + [1439]
sheet(strides[:31], 8, 210, 373, "rv_full/A1_stride24_f0-720.png"); sheet(strides[31:], 8, 210, 373, "rv_full/A2_stride24_f744-1439.png")
for i in range(4):
    chunk = ev[i * 7:(i + 1) * 7]; fs = []
    for s, e, *_ in chunk: fs += [max(0, s - 1), e]
    sheet(fs, 14, 130, 231, f"rv_full/B{i+1}_event_pairs_{chunk[0][0]}-{chunk[-1][0]}.png")
print(len(ev), len(got))
