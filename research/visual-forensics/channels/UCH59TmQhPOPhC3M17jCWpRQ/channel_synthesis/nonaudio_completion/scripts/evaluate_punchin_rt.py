# Deterministic C1-C4 for RT-V1-P01 (single-frame punch-in). usage: evaluate_punchin_rt.py MP4 OUT.json
import json, subprocess, sys, cv2
from pathlib import Path
H = Path(__file__).resolve().parent; mp4, out = sys.argv[1], Path(sys.argv[2]); PY = sys.executable
pr = json.loads(subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height,r_frame_rate,codec_name', '-of', 'json', mp4]))['streams'][0]
nf = int(subprocess.check_output(['ffprobe', '-v', 'error', '-count_frames', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_frames', '-of', 'csv=p=0', mp4]).decode().strip())
cap = cv2.VideoCapture(mp4); n = 0
while cap.read()[0]: n += 1
tj = out.with_suffix('.traj.json'); subprocess.run([PY, H / 'cam_traj.py', mp4, '0', str(n - 1), tj], check=True, capture_output=True)
A = json.loads(tj.read_text())['rows']; S = [r['scale'] for r in A]
C = {'C1': dict(ok=(pr['width'], pr['height'], pr['r_frame_rate'], pr['codec_name']) == (1920, 1080, '30000/1001', 'h264') and 88 <= nf <= 92 and nf == n, frames=nf, cv2=n)}
jumps = [i for i in range(1, len(S)) if abs(S[i] - S[i - 1]) > 0.5]; j = jumps[0] if jumps else None
C['C2'] = dict(ok=len(jumps) == 1 and 40 <= j <= 50, jump_frames=jumps)
if j:
    tj2 = out.with_suffix('.jump.json'); subprocess.run([PY, H / 'cam_traj.py', mp4, str(j - 1), str(j), tj2], check=True, capture_output=True)
    r = json.loads(tj2.read_text())['rows'][-1]; s = r['scale']; fp = (round(r['tx'] / (1 - s)), round(r['ty'] / (1 - s)))
    C['C3'] = dict(ok=2.0 <= s <= 2.3 and abs(fp[0] - 627) <= 60 and abs(fp[1] - 818) <= 60, incremental_scale=round(s, 3), fixed_point=fp)
    steps = [abs(S[i] / S[i - 1] - 1) for i in range(1, len(S)) if i != j]; pre = abs(S[j - 1] - 1); post = abs(S[-1] / S[j] - 1)
    C['C4'] = dict(ok=max(steps) < .02 and pre < .03 and post < .03, max_other_step=round(max(steps), 4), drift_pre=round(pre, 4), drift_post=round(post, 4))
else: C['C3'] = dict(ok=False); C['C4'] = dict(ok=False)
res = dict(test='RT-V1-P01', mp4=mp4, criteria=C, deterministic='PASS' if all(v['ok'] for v in C.values()) else 'FAIL')
out.write_text(json.dumps(res, indent=1)); print(json.dumps({k: v for k, v in C.items()}))
