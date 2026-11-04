"""Deterministic reuse tests over BUILT DEV videos only: (a) Short-vs-long ASR word overlap, (b) settled-frame reuse via dHash of hold ink crops. Writes campaign/reuse_dev.json. Usage: python -I pe_reuse.py"""
import csv, difflib, json, pathlib, re, cv2, numpy as np, collections
W = pathlib.Path.home() / "YIOS-local-audits/primitive-education"; sel = json.load(open(W / "selection/selection_v1.json"))["videos"]
built = [r for r in sel if r["split"] == "DEV" and (W / "videos" / r["video_id"] / "quality_gate.json").exists()]
T = {r["video_id"]: re.findall(r"[a-z0-9']+", " ".join(s["text"] for s in json.load(open(W / "videos" / r["video_id"] / "asr/asr_small_en.json"))["segments"]).lower()) for r in built}
text = []
for s in [r for r in built if r["displayed_format"] == "9:16"]:
    for l in [r for r in built if r["displayed_format"] == "16:9"]:
        a, b = T[s["video_id"]], T[l["video_id"]]; m = difflib.SequenceMatcher(None, a, b, autojunk=False); k = sum(x.size for x in m.get_matching_blocks())
        text.append(dict(short=s["video_id"], long=l["video_id"], short_words=len(a), matched=k, share_of_short=round(k / max(1, len(a)), 3)))
def dh(g): s = cv2.resize(g, (17, 16), interpolation=cv2.INTER_AREA); return (s[:, 1:] > s[:, :-1]).flatten()
H = []
for r in built:
    V = W / "videos" / r["video_id"]; cap = cv2.VideoCapture((V / "evidence/source_path.txt").read_text().strip()); segs = [s for s in csv.DictReader(open(V / "tables/segments_v1.csv")) if s["kind"] == "HOLD"]
    want = {int(s["end_frame"]): s["seg"] for s in segs}; i = 0; top = max(want)
    while i <= top:
        ok, im = cap.read()
        if not ok: break
        if i in want:
            g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY); ys, xs = (g < 200).nonzero()
            if len(xs) > 500: c = g[ys.min():ys.max() + 1, xs.min():xs.max() + 1]; H.append((r["video_id"], want[i], c.shape[1] / c.shape[0], dh(c)))
        i += 1
pairs = collections.Counter(); ex = {}; same = 0; n = len(H)
for i in range(n):
    for j in range(i + 1, n):
        if abs(H[i][2] - H[j][2]) < .03 and (H[i][3] != H[j][3]).sum() <= 10:
            k = tuple(sorted((H[i][0], H[j][0]))); pairs[k] += 1; ex.setdefault(k, (H[i][1], H[j][1]))
out = dict(method="ASR SequenceMatcher (ASR_UNCERTIFIED); dHash 16x16 of ink crop, Hamming<=10 and aspect within .03 (candidate reuse incl. re-scaled)", holds_hashed=n, text_overlap=sorted(text, key=lambda x: -x["share_of_short"]), hold_reuse_pairs=[dict(a=k[0], b=k[1], matches=v, example=ex[k]) for k, v in pairs.most_common()])
(W / "campaign/reuse_dev.json").write_text(json.dumps(out, indent=1)); print(json.dumps(out)[:1500])
