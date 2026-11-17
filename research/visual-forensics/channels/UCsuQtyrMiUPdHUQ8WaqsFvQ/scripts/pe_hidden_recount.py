"""Acceptance reconciliation of pe_hidden_audit output (read-only on hidden_tiles.csv). For each EMPTY/DUP tile recomputes the band from the source and records:
why_empty (LOW = under 0.2% content, FULL = over 95% content), pixel counts under the thresholds, whether the faint pass flagged it, and residual marks the two earlier metrics ignore (connected component >=12 px of pixels differing >=60 from the band's median).
DUP: max 8x8-block mean difference against the band it was deduped to, so small new text cannot hide inside the whole-band mean.
Writes campaign/hidden_audit/recount_tiles.csv, recount_summary.json and RECOUNT_nn.jpg (every tile no earlier pass opened whose band holds such a residual mark, plus all DUP). Usage: python -I pe_hidden_recount.py"""
import csv, json, pathlib, collections, cv2, numpy as np
W = pathlib.Path.home() / "YIOS-local-audits/primitive-education"; O = W / "campaign/hidden_audit"
rows = list(csv.DictReader(open(O / "hidden_tiles.csv"))); by = collections.defaultdict(list)
for r in rows: by[r["video"]].append(r)
faint = {(r["video"], int(r["frame"])) for r in csv.DictReader(open(O / "faint_index.csv"))}
out = []; pack = []; S = collections.Counter(); total_frames = {}; lastfr = {}
def frac(b): return float(((cv2.cvtColor(b, cv2.COLOR_BGR2GRAY) < 90) | (cv2.cvtColor(b, cv2.COLOR_BGR2HSV)[..., 1] > 80)).mean())
for v, rs in sorted(by.items()):
    V = W / "videos" / v; cap = cv2.VideoCapture((V / "evidence/source_path.txt").read_text().strip()); k = 0; seen = []
    total_frames[v] = json.load(open(V / "coverage.json"))["frames_total"]; lastfr[v] = max(int(r["frame"]) for r in rs)
    for r in sorted(rs, key=lambda x: int(x["frame"])):
        f = int(r["frame"])
        while k < f: cap.grab(); k += 1
        ok, im = cap.read(); assert ok; k += 1
        h, w = im.shape[:2]; b = im[h - round(h * (22 / 270 if w > h else 22 / 480)):]; g = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
        fr = frac(b); dark = float(g.mean()) < 128; fp = float((g > 150).mean()) if dark else float((g < 235).mean())
        med = np.median(b.reshape(-1, 3), axis=0); mask = (np.abs(b.astype(np.int16) - med).max(2) >= 60).astype(np.uint8)
        n, _, st, _ = cv2.connectedComponentsWithStats(mask, connectivity=8); big = int(st[1:, 4].max()) if n > 1 else 0
        small = cv2.resize(b, (240, 24)).astype(np.int16); blk = None
        st_ = r["status"]; whye = ""
        if st_ == "EMPTY": whye = "FULL" if fr >= 0.95 else "LOW"
        if st_ == "DUP" and seen:
            d = [np.abs(small - s).mean() for s in seen]; ref = seen[int(np.argmin(d))]
            blk = float(cv2.resize(np.abs(small - ref).astype(np.float32).mean(2), (30, 3), interpolation=cv2.INTER_AREA).max())
        if st_ != "EMPTY": seen.append(small)
        flagged = fp > 0.002 and st_ == "EMPTY"; opened = (v, f) in faint
        resid = st_ == "EMPTY" and big >= 12 and not opened
        S[st_] += 1; S[f"EMPTY_{whye}"] += st_ == "EMPTY"; S["EMPTY_faint_flagged"] += flagged; S["EMPTY_faint_opened"] += opened; S["EMPTY_faint_flagged_not_opened"] += flagged and not opened
        S["EMPTY_zero_marks"] += st_ == "EMPTY" and big < 12; S["EMPTY_residual_unopened"] += resid
        out.append(dict(video=v, seg=r["seg"], kind=r["kind"], frame=f, status=st_, why_empty=whye, frac_v1=round(fr, 5), frac_faint=round(fp, 5), faint_flagged=int(flagged), faint_opened=int(opened), largest_mark_px=big, dup_max_block_diff=None if blk is None else round(blk, 2), ring_only=r["ring_only"]))
        if resid or st_ == "DUP": pack.append((v, r["seg"], r["kind"], f, st_, big, b))
with open(O / "recount_tiles.csv", "w", newline="") as fh:
    wr = csv.DictWriter(fh, fieldnames=list(out[0])); wr.writeheader(); wr.writerows(out)
page = 1; col = []; hh = 0; idx = []
for v, seg, kind, f, st_, big, b in pack:
    t = cv2.resize(b, (960, round(960 * b.shape[0] / b.shape[1]))); lab = np.zeros((16, 960, 3), np.uint8)
    cv2.putText(lab, f"{v} {seg} {kind} f{f} {st_} mark {big}px", (3, 12), cv2.FONT_HERSHEY_SIMPLEX, .4, (255, 255, 255), 1); t = np.vstack([lab, t])
    if hh + t.shape[0] > 1500: cv2.imwrite(str(O / f"RECOUNT_{page:02d}.jpg"), np.vstack(col), [cv2.IMWRITE_JPEG_QUALITY, 88]); col = []; hh = 0; page += 1
    col.append(t); hh += t.shape[0]; idx.append((page, v, seg, kind, f, st_, big))
if col: cv2.imwrite(str(O / f"RECOUNT_{page:02d}.jpg"), np.vstack(col), [cv2.IMWRITE_JPEG_QUALITY, 88])
with open(O / "recount_index.csv", "w", newline="") as fh: csv.writer(fh).writerows([("page", "video", "seg", "kind", "frame", "status", "largest_mark_px")] + idx)
res = dict(counts=dict(S), tiles=len(rows), pack=len(pack), pages=page if pack else 0, frames_total=sum(total_frames.values()), distinct_tile_frames=len(rows), last_frame_is_tile={v: lastfr[v] == total_frames[v] - 1 for v in total_frames})
(O / "recount_summary.json").write_text(json.dumps(res, indent=1)); print(json.dumps(res))
