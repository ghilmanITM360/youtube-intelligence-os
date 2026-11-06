"""Per-video composition measures and attention timeline (kit ref 04 composition, ref 08 output format). Deterministic; no viewing or model call.
review/state_composition.csv (MEASURED on each HOLD's settled frame): non-background bbox, centroid, coverage, negative space, red/yellow share; change bbox against the previous HOLD with the unchanged share.
review/attention_timeline.csv: ref 08 columns. predicted_salience is a hypothesis from measured change size, position and colour, never eye tracking. payoff_question takes the reviewer's own section (hook/chain/joke/payoff) that cites the segment. No retention figure is given or implied.
Usage: python -I pe_attention.py <video_dir>"""
import csv, pathlib, re, sys, statistics as st, cv2, numpy as np
V = pathlib.Path(sys.argv[1]).resolve(); vid = V.name
S = list(csv.DictReader(open(V / "tables/state_ledger.csv")))
obs = (V / f"review/rv1_{vid}/observations.md").read_text()
tags = {}; cur = None
for line in obs.splitlines():
    m = re.match(r"\W*(?:\d+\.\s*)?\W*([A-Za-z/ ]+)", line)
    if re.match(r"\s*(#+\s|\*\*\d+\.|\d+\.\s)", line) and m:  # section heading, with or without body on the same line
        w = m[1].lower(); cur = "hook" if w.startswith(("hook", "opening")) else "explanation" if w.startswith(("explanation", "chain")) else "joke/micro-payoff" if w.startswith("joke") else "payoff/ending" if w.startswith(("payoff", "ending")) else None
    if not cur: continue
    for a, b in re.findall(r"G(\d{4})(?:\s*[-\u2013]\s*G?(\d{4}))?", line):
        for n in range(int(a), int(b or a) + 1): tags.setdefault(f"G{n:04d}", cur)
holds = [x for x in S if x["kind"] == "HOLD"]; want = {int(x["end_frame"]) for x in holds}
cap = cv2.VideoCapture((V / "evidence/source_path.txt").read_text().strip()); fr = {}; k = 0; last = None; comp = []
def box(mask, w, h):
    ys, xs = np.where(mask)
    if not len(xs): return ("", "", "", "")
    return round(xs.min() / w, 3), round(ys.min() / h, 3), round((xs.max() - xs.min() + 1) / w, 3), round((ys.max() - ys.min() + 1) / h, 3)
for x in holds:
    f = int(x["end_frame"])
    while k < f: cap.grab(); k += 1
    ok, im = cap.read(); assert ok, f; k += 1
    im = cv2.resize(im, None, fx=.5, fy=.5, interpolation=cv2.INTER_AREA); h, w = im.shape[:2]
    bg = np.median(im.reshape(-1, 3), axis=0); m = np.abs(im.astype(np.int16) - bg).max(2) > 40; b = box(m, w, h)
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV); H, Sat, Val = hsv[..., 0], hsv[..., 1], hsv[..., 2]; sat = (Sat > 80) & (Val > 60)
    ys, xs = np.where(m); row = dict(video_id=vid, seg=x["seg"], state=x["visual_state_id"], frame=f, x=b[0], y=b[1], w=b[2], h=b[3], cx=round(xs.mean() / w, 3) if len(xs) else "", cy=round(ys.mean() / h, 3) if len(ys) else "", coverage=round(float(m.mean()), 4), negative_space=round(1 - float(m.mean()), 4), red=round(float((sat & ((H < 10) | (H > 170))).mean()), 4), yellow=round(float((sat & (H > 20) & (H < 35)).mean()), 4))
    if last is not None:
        d = np.abs(im.astype(np.int16) - last).max(2) > 40; c = box(d, w, h)
        row.update(chg_x=c[0], chg_y=c[1], chg_w=c[2], chg_h=c[3], chg_frac=round(float(d.mean()), 4), chg_red=round(float((d & sat & ((H < 10) | (H > 170))).sum() / max(d.sum(), 1)), 3))
    else: row.update(chg_x="", chg_y="", chg_w="", chg_h="", chg_frac="", chg_red="")
    comp.append(row); last = im.astype(np.int16)
with open(V / "review/state_composition.csv", "w", newline="") as fh:
    wr = csv.DictWriter(fh, fieldnames=list(comp[-1])); wr.writeheader(); wr.writerows(comp)
C = {r["seg"]: r for r in comp}; durs = [float(x["end_pts_exclusive"]) - float(x["start_pts"]) for x in holds]; longh = sorted(durs)[int(.95 * (len(durs) - 1))] if durs else 0
on = [float(x["start_pts"]) for x in S if x["kind"] == "ACTIVITY"]; rows = []
def place(x, y, w, h):
    cx, cy = x + w / 2, y + h / 2; return ("upper " if cy < .34 else "lower " if cy > .66 else "middle ") + ("left" if cx < .34 else "right" if cx > .66 else "centre")
for i, x in enumerate(holds):
    c = C[x["seg"]]; t0, t1 = float(x["start_pts"]), float(x["end_pts_exclusive"]); d = t1 - t0; prev = next((y for y in reversed(S[:S.index(x)]) if y["kind"] == "ACTIVITY"), None)
    if c["chg_frac"] == "" or c["chg_x"] == "": sal = "opening state, whole frame"; sf = 0
    else:
        sf = float(c["chg_frac"]); sal = f"changed area {place(c['chg_x'], c['chg_y'], c['chg_w'], c['chg_h'])}, {sf * 100:.1f}% of frame" + (", mostly saturated red" if float(c["chg_red"]) > .5 else "")
    burst = sum(t0 - 2 <= o <= t0 for o in on); fat = []
    if d >= longh and d > 2: fat.append(f"long hold {d:.2f}s (top 5% here): may tire, or may protect comprehension")
    if burst >= 4: fat.append(f"{burst} events in the prior 2 s: may overload, or may read as energy")
    rows.append(dict(video_id=vid, time_start=t0, time_end=t1, seg=x["seg"], visible_stimulus=x["description"][:200], state_change=(prev["subtype"] if prev else "OPENING"), predicted_salience_HYPOTHESIS=sal, payoff_or_question=tags.get(x["seg"]) or (tags.get(prev["seg"]) if prev else "") or "", potential_fatigue_or_overload="; ".join(fat), alternative_hypothesis="static surroundings or narration may hold attention instead; not measurable from pixels", evidence=f"tables/state_ledger.csv {x['seg']}; review/state_composition.csv", confidence="LOW" if not tags.get(x["seg"]) else "MEDIUM"))
with open(V / "review/attention_timeline.csv", "w", newline="") as fh:
    wr = csv.DictWriter(fh, fieldnames=list(rows[0])); wr.writeheader(); wr.writerows(rows)
print(vid, len(rows), "tagged", sum(bool(r["payoff_or_question"]) for r in rows), "fatigue", sum(bool(r["potential_fatigue_or_overload"]) for r in rows))
