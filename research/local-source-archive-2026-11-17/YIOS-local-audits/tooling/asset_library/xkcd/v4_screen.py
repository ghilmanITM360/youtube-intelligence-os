import csv, json, sys, pathlib, numpy as np, cv2
root = pathlib.Path.home() / "YIOS-local-audits/xkcd-whatif"
cen = {r["video_id"]: r for r in csv.DictReader(open(root / "census/census.csv"))}
out = {}
for vid in sys.argv[1:]:
    src = cen[vid]["local_paths"].split("|")[0]; cap = cv2.VideoCapture(src); n = 0; prev = None; rec = []
    while True:
        ok, f = cap.read()
        if not ok: break
        if n % 6 == 0:
            s = cv2.resize(f, None, fx=.25, fy=.25, interpolation=cv2.INTER_AREA); h = cv2.cvtColor(s, cv2.COLOR_BGR2HSV)
            sat = float(((h[..., 1] >= 89) & (h[..., 2] >= 77)).mean()); g = cv2.cvtColor(s, cv2.COLOR_BGR2GRAY).astype(np.float32)
            d = sh = resp = 0.0
            if prev is not None:
                d = float(np.abs(g - prev).mean()); (dx, dy), resp = cv2.phaseCorrelate(prev, g); sh = float(np.hypot(dx, dy))
            rec.append((n, round(sat, 3), round(d, 2), round(sh, 1), round(resp, 2))); prev = g
            if sat >= .15 or (resp >= .3 and sh >= 2): cv2.imwrite(str(pathlib.Path(sys.argv[0]).parent / "_tmp_ignore"), s) if False else None
        n += 1
    cap.release()
    mapw = [r[0] for r in rec if r[1] >= .15]; shifts = [r for r in rec if r[4] >= .3 and r[3] >= 2]
    runs = []; cur = []
    for r in shifts:
        if cur and (r[0] - cur[-1][0]) / 24 > 3.0: runs.append(cur); cur = []
        cur.append(r)
    if cur: runs.append(cur)
    out[vid] = {"frames": n, "sat_max": max(r[1] for r in rec), "map_samples": len(mapw), "map_first_last": [mapw[0], mapw[-1]] if mapw else None,
                "shift_samples": len(shifts), "multi_shift_runs": [[x[0] for x in run] for run in runs if len(run) >= 2], "single_shifts": [run[0][0] for run in runs if len(run) == 1]}
    print(vid, json.dumps(out[vid]))
json.dump(out, open(pathlib.Path.home() / "YIOS-local-audits/xkcd-whatif/asset_library/_channel/deep_vf/v4_screen/screen_measures.json", "w"), indent=1)
