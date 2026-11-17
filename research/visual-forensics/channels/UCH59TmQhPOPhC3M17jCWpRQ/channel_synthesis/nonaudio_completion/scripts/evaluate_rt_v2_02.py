# Evaluate RT-V2-02 against camera_ease/RT-V2-02_PREREGISTERED_CRITERION.json (registered before the render existed).
import json, subprocess, sys, numpy as np
from pathlib import Path
H = Path(__file__).resolve().parents[1]; D = Path(sys.argv[1]); PY = sys.executable
C = json.loads((H / 'camera_ease/RT-V2-02_PREREGISTERED_CRITERION.json').read_text()); tl = json.loads((D / 'timeline.json').read_text())
s0 = tl['PAN_start']; a, b = s0 - 3, s0 + 22; tj = D / 'EVAL_trajectory.json'
subprocess.run([PY, str(H / 'scripts/cam_traj.py'), str(D / 'rt.mp4'), str(a), str(b), str(tj)], check=True, capture_output=True)
R = json.loads(tj.read_text())['rows']; tx = np.array([r['tx'] for r in R]); ty = np.array([r['ty'] for r in R]); sc = np.array([r['scale'] for r in R])
v = np.diff(tx); mv = [i + 1 for i, x in enumerate(v) if abs(x) > 0.5]  # index into R
tot = tx[-1] - tx[0]; src = np.array(C['source_progress'])
held = [i for i in range(mv[0], mv[-1] + 1) if i not in mv] if mv else ['none']
def err(off):
    o = mv[0] - 1 + off; seg = (tx[o:o + len(src)] - tx[0]) / tot
    return (float(np.sqrt(np.mean((seg - src) ** 2))), float(np.max(np.abs(seg - src)))) if len(seg) == len(src) else (9, 9)
rms, mx = min((err(o) for o in (-1, 0, 1)), key=lambda e: e[0]); vm = v[mv[0] - 1:mv[-1]]; pk = int(np.argmax(np.abs(vm)))
res = dict(C1_axis=dict(ok=bool(np.abs(ty).max() <= 3 and sc.max() - sc.min() <= 0.004), ty_max=float(np.abs(ty).max()), scale_range=float(sc.max() - sc.min())),
    C2_magnitude=dict(ok=bool(abs(tot - 137.5) <= 7), total_tx=float(tot)),
    C3_duration=dict(ok=bool(15 <= len(mv) <= 17 and not held), moving_frames=len(mv), held=held, first_last=[R[mv[0]]['frame'], R[mv[-1]]['frame']]),
    C4_profile=dict(ok=bool(rms <= 0.04 and mx <= 0.08), rms=round(rms, 4), max_err=round(mx, 4)),
    C5_peak=dict(ok=bool(len(vm) // 3 <= pk < 2 * len(vm) - len(vm) // 3 - len(vm) // 3 + len(vm) // 3), peak_index=pk, n=len(vm)),
    C6_rest=dict(ok=bool(np.all(np.abs(v[mv[-1]:mv[-1] + 5]) <= 0.5))),
    C7_tracking=dict(ok=bool(min(r['inliers'] for r in R) >= 200), min_inliers=min(r['inliers'] for r in R)))
res['C5_peak']['ok'] = bool(len(vm) // 3 <= pk < 2 * len(vm) // 3 + 1)
out = dict(test='RT-V2-02', criterion_file='nonaudio_completion/camera_ease/RT-V2-02_PREREGISTERED_CRITERION.json', criteria=res,
           overall='PASS' if all(x['ok'] for x in res.values()) else 'FAIL', scope='camera pan trajectory only; scene art is an original procedural stand-in, not a style test')
(D / 'EVALUATION.json').write_text(json.dumps(out, indent=1)); print(json.dumps(out, indent=1))
