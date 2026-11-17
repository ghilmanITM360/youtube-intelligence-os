# Rule M3 (camera vs object vs whole-content move). POST-HOC: designed 2026-11-05 AFTER seeing M2 output and batch 1/2 reviews,
# so it is NOT preregistered; its thresholds are frozen by sha256 (method_v3/M3_RULE_FREEZE.json) before running on the 850 rows and before the held-out check.
# Lineage: M0 cam_endpoint.py (preregistered, 11 claims, endpoints start-1/end+1). M1 chain over <=10-frame links (post-observation).
# M2 M1 + inlier spread >=0.5 of frame W and H (post-observation). M3 = M2's fit + edge-evidence test below + entry link.
# Usage: camera_m3.py --selfcheck | camera_m3.py VID
import csv, sys, cv2, numpy as np
from pathlib import Path
MIN_INL, BIG_S, BIG_T, SMALL_S, SMALL_T = 40, 0.005, 3.0, 0.002, 1.5   # unchanged from M0
SPREAD, M_CAM, M_WHOLE, M_OBJ, PATH_OSC, LOC = 0.5, 0.6, 0.9, 0.5, 6.0, 0.002
W, H = 1920, 1080
def edge_support(A, B, T):
    """moved_share = edges only explained by warping A onto B / (those + edges only explained by no motion)."""
    # for each edge pixel of A: "stays" = an edge of B is at the same place; "follows" = an edge of B is where T sends it.
    EA, EB = cv2.Canny(A, 50, 150) > 0, cv2.dilate(cv2.Canny(B, 50, 150), np.ones((3, 3), np.uint8))
    F = cv2.warpAffine(EB, T[:2], (A.shape[1], A.shape[0]), flags=cv2.INTER_NEAREST | cv2.WARP_INVERSE_MAP) > 0; St = EB > 0
    only_static, only_moved = (EA & St & ~F).sum(), (EA & F & ~St).sum(); n = max(1, EA.sum())
    return dict(moved_share=float(only_moved / max(1, only_moved + only_static)), id_match=float((EA & St).sum() / n), warp_match=float((EA & F).sum() / n), n_edges=int(EA.sum()))
def verdict(mn, sc, t, sp, moved_share, path, links):
    if links == 0: return 'NOT_APPLICABLE'
    big, small = abs(sc - 1) >= BIG_S or t >= BIG_T, abs(sc - 1) < SMALL_S and t < SMALL_T
    if mn < MIN_INL: return 'UNRESOLVED'
    if small: return 'UNRESOLVED_OSCILLATION' if path >= PATH_OSC else 'NO_CAMERA'
    if not big: return 'UNRESOLVED'
    if moved_share < M_OBJ: return 'OBJECT_MOVE'
    if sp >= SPREAD: return 'CAMERA_FRAMEWIDE' if moved_share >= M_CAM else 'UNRESOLVED_PARTIAL'
    return 'WHOLE_CONTENT_MOVE' if moved_share >= M_WHOLE else 'UNRESOLVED_PARTIAL'
orb = cv2.ORB_create(4000); bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
def fit(a, b):
    ka, da = a; kb, db = b; m = bf.match(da, db) if da is not None and db is not None else []
    if len(m) < 8: return None, 0, 0.0
    P, Q = np.float32([ka[x.queryIdx].pt for x in m]), np.float32([kb[x.trainIdx].pt for x in m])
    M, inl = cv2.estimateAffinePartial2D(P, Q, method=cv2.RANSAC, ransacReprojThreshold=2.0)
    if M is None or inl is None or not inl.sum(): return None, 0, 0.0
    P = P[inl.ravel() == 1]; return M, int(inl.sum()), float(min(np.ptp(P[:, 0]) / W, np.ptp(P[:, 1]) / H))
def run_chain(frames):
    """frames: list of gray frames; returns the measured dict. Entry handling is done by the caller."""
    feats = [orb.detectAndCompute(f, None) for f in frames]; T = np.eye(3); mn = 10**9; sp = 1.0; path = 0.0; res = 0.0
    c = np.array([W / 2, H / 2, 1.0])
    for i in range(len(frames) - 1):
        M, n, s = fit(feats[i], feats[i + 1]); mn = min(mn, n); sp = min(sp, s)
        if M is not None:
            T = np.vstack([M, [0, 0, 1]]) @ T; path += float(np.hypot(*(M @ c - c[:2])))
            wa = cv2.warpAffine(frames[i], M, (W, H), borderMode=cv2.BORDER_REPLICATE); res = max(res, float((cv2.absdiff(wa, frames[i + 1]) > 25).mean()))
    sc = float(np.hypot(T[0, 0], T[1, 0])); t = float(np.hypot(*((T @ c)[:2] - c[:2])))
    return T, (mn if len(frames) > 1 else 0), sc, t, sp, path, res
def selfcheck():
    rng = np.random.default_rng(7); tex = cv2.GaussianBlur(rng.integers(0, 255, (H, W), dtype=np.uint8), (0, 0), 3); tex = cv2.normalize(tex, None, 0, 255, cv2.NORM_MINMAX)
    white = np.full((H, W), 255, np.uint8)
    def art(n, off=(0, 0), base=None, xr=(600, 1300), yr=(440, 640), k=60):
        im = white.copy() if base is None else base.copy(); r = np.random.default_rng(n)
        for _ in range(k):
            x, y = int(r.integers(*xr)) + off[0], int(r.integers(*yr)) + off[1]; cv2.rectangle(im, (x, y), (x + int(r.integers(8, 50)), y + int(r.integers(8, 50))), int(r.integers(0, 120)), -1)
        return im
    bg = art(3, (-500, 300), k=8); bg2 = art(5, (-500, -400), xr=(600, 2300), yr=(440, 1300), k=250)
    LINES = white.copy()
    for y in range(20, 1060, 14): cv2.line(LINES, (0, y), (W, y + 9), 60, 1)
    for x in range(20, 1900, 14): cv2.line(LINES, (x, 0), (x + 9, H), 60, 1)
    shift = lambda im, dx, dy, s=1.0: cv2.warpAffine(im, np.float32([[s, 0, dx + (1 - s) * W / 2], [0, s, dy + (1 - s) * H / 2]]), (W, H), borderMode=cv2.BORDER_REPLICATE)
    def lab(fr):
        T, mn, sc, t, sp, path, res = run_chain(fr); return verdict(mn, sc, t, sp, edge_support(fr[0], fr[-1], T)['moved_share'], path, len(fr) - 1)
    cases = {'pan_textured': ([tex, shift(tex, 12, 0), shift(tex, 24, 0)], 'CAMERA_FRAMEWIDE'),
             'zoom_textured': ([tex, shift(tex, 0, 0, 1.015), shift(tex, 0, 0, 1.03)], 'CAMERA_FRAMEWIDE'),
             'static_textured': ([tex, tex.copy()], 'NO_CAMERA'),
             'slide_on_white': ([art(1), art(1, (10, 0)), art(1, (20, 0))], 'WHOLE_CONTENT_MOVE'),
             'minority_object_on_static': ([art(2, base=bg2, k=20), art(2, (20, 0), base=bg2, k=20)], 'NO_CAMERA'),   # static features dominate the fit: identity; the object shows as residual
             'dominant_object_small_static': ([art(2, base=bg, k=120), art(2, (20, 0), base=bg, k=120)], 'WHOLE_CONTENT_MOVE'),   # ceiling: <10% static content cannot veto
             'object_with_large_static_lines': ([art(2, base=LINES, k=120), art(2, (20, 0), base=LINES, k=120)], 'OBJECT_MOVE'),
             'cut': ([tex, art(4)], 'UNRESOLVED')}
    bad = {k: (lab(f), want) for k, (f, want) in cases.items() if lab(f) != want}
    print('selfcheck', 'PASS' if not bad else bad, list(cases)); return not bad
if __name__ == '__main__':
    if sys.argv[1] == '--selfcheck': sys.exit(0 if selfcheck() else 1)
    N = Path(__file__).resolve().parents[1]; SRC = Path.home() / 'Downloads/videos in mp3/BarelyEvolved-MP4'; vid = sys.argv[1]
    rows = list(csv.DictReader(open(N / f'dense_review/DENSE_REVIEW_LEDGER_{vid}_v2.csv')))
    need = {}
    for r in rows:
        a, b = int(r['start_frame']), int(r['end_frame'])
        for f in {a - 1, b + 1, *range(a, b, 10), b}: need.setdefault(f, []).append(r['interval_id'])
    G = {}; cap = cv2.VideoCapture(str(next(SRC.glob(f'*{vid}*.mp4')))); i = 0; last = max(need); out = []; by = {r['interval_id']: r for r in rows}; endmap = {}
    for r in rows: endmap.setdefault(int(r['end_frame']) + 1, []).append(r)
    done = set()
    def flush(r):
        a, b = int(r['start_frame']), int(r['end_frame']); fs = sorted({*range(a, b, 10), b})
        if a - 1 not in G or any(f not in G for f in fs): return
        M, n, s = fit(orb.detectAndCompute(G[a - 1], None), orb.detectAndCompute(G[a], None)); entry = n >= MIN_INL
        chain = ([a - 1] if entry else []) + fs; fr = [G[f] for f in chain]; T, mn, sc, t, sp, path, res = run_chain(fr); links = len(fr) - 1
        ES = edge_support(fr[0], fr[-1], T) if links else dict(moved_share=0, id_match=0, warp_match=0, n_edges=0)
        v = verdict(mn, sc, t, sp, ES['moved_share'], path, links)
        # M0 re-applied to every interval for the sensitivity table: endpoints start-1 vs end+1, no chain and no spread (preregistered only for the 11 claims).
        m0 = 'UNRESOLVED'
        if b + 1 in G:
            M0, n0, _ = fit(orb.detectAndCompute(G[a - 1], None), orb.detectAndCompute(G[b + 1], None))
            if M0 is not None and n0 >= MIN_INL:
                s0 = float(np.hypot(M0[0, 0], M0[1, 0])); c = np.array([W / 2, H / 2, 1.0]); t0 = float(np.hypot(*(M0 @ c - c[:2])))
                m0 = 'CAMERA_VERIFIED' if abs(s0 - 1) >= BIG_S or t0 >= BIG_T else 'CAMERA_REJECTED' if abs(s0 - 1) < SMALL_S and t0 < SMALL_T else 'UNRESOLVED'
        out.append(dict(video=vid, interval_id=r['interval_id'], start_frame=a, end_frame=b, entry_link_used=int(entry), links=links, min_link_inliers=mn, inlier_spread=round(sp, 3), scale=round(sc, 5), centre_shift_px=round(t, 2), path_px=round(path, 2), moved_share=round(ES['moved_share'], 3), id_match=round(ES['id_match'], 3), warp_match=round(ES['warp_match'], 3), n_edges=ES['n_edges'], max_link_residual=round(res, 5), local_change_after_comp=int(res >= LOC), camera_m3=v, camera_m2=r['camera_measured_v2'], m0_endpoint_all=m0, ledger_event_class=r['event_class'])); done.add(r['interval_id'])
    while i <= last:
        ok, im = cap.read()
        if not ok: break
        if i in need: G[i] = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        for r in endmap.get(i, []): flush(r)
        if i % 500 == 0:
            live = min((int(r['start_frame']) - 1 for r in rows if r['interval_id'] not in done), default=i)
            for f in [f for f in G if f < live]: del G[f]
        i += 1
    for r in rows:
        if r['interval_id'] not in done: flush(r)
    assert len(out) == len(rows), (len(out), len(rows))
    out.sort(key=lambda o: o['start_frame'])
    with open(N / f'method_v3/CAMERA_M3_{vid}.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(out[0])); w.writeheader(); w.writerows(out)
    import collections; print(vid, collections.Counter(o['camera_m3'] for o in out))
