#!/usr/bin/env python3
"""Native-frame measurement of marker/replacement events in a source window.
Per frame (native fps, 480px wide): global diff vs prev frame, yellow-marker px, red-mark px.
Events are measured, never assumed: cut = global diff > CUT; yellow/red onset/completion from pixel-count curves.
Usage: window_forensics.py <mp4> <start_s> <end_s> <outprefix>
Evidence labels: [M] numbers here are measured on pixels; technique labels need viewing [O]."""
import sys, subprocess, json, csv
import numpy as np
mp4, t0, t1, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
pr = json.loads(subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=r_frame_rate,width,height','-of','json',mp4]))['streams'][0]
n, d = pr['r_frame_rate'].split('/'); fps = float(n)/float(d)
W, H = 480, 270
cmd = ['ffmpeg','-v','error','-ss',str(t0),'-t',str(t1-t0),'-i',mp4,'-vf',f'scale={W}:{H}','-f','rawvideo','-pix_fmt','rgb24','-']
raw = subprocess.run(cmd, capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3).astype(np.int16)
rows = []; prev = None
for i, f in enumerate(fr):
    R, G, B = f[..., 0], f[..., 1], f[..., 2]
    yel = int(((R > 200) & (G > 180) & (B < 120)).sum())
    red = int(((R > 170) & (G < 70) & (B < 70)).sum())
    gd = 0.0 if prev is None else float(np.abs(f - prev).mean())
    rows.append((i, round(t0 + i / fps, 3), round(gd, 3), yel, red)); prev = f
with open(out + '_frames.csv', 'w', newline='') as fh:
    w = csv.writer(fh); w.writerow(['frame_in_window', 't_s', 'global_diff', 'yellow_px', 'red_px']); w.writerows(rows)
CUT = 12.0
cuts = [r for r in rows if r[2] > CUT]
def curve_events(idx, name):
    v = np.array([r[idx] for r in rows]); ev = []
    if v.max() < 40: return [f'{name}: none (max {int(v.max())} px)']
    on = np.where(v > 0.05 * v.max())[0]
    # split into runs by cuts: report onset/completion per run between cuts
    cut_f = [r[0] for r in cuts]
    bounds = [0] + cut_f + [len(v)]
    for a, b in zip(bounds[:-1], bounds[1:]):
        seg = v[a:b]
        if len(seg) < 2 or seg.max() < 40: continue
        mx = seg.max(); f_on = a + int(np.argmax(seg > 0.05 * mx)); f_done = a + int(np.argmax(seg >= 0.95 * mx))
        jump = (seg.max() - seg[0]) and (np.diff(seg).max() / max(mx, 1))
        steps = int((np.diff(seg[f_on - a:f_done - a + 1]) > 0.03 * mx).sum()) if f_done > f_on else 0
        kind = 'instant (<=1 frame to 95%)' if f_done - f_on <= 1 else f'progressive ({f_done-f_on} frames, {steps} growth steps)'
        pre = ' pre-marked on entry' if seg[0] > 0.5 * mx else ''
        ev.append(f'{name}: segment f{a}-{b-1} onset f{f_on} t={t0+f_on/fps:.3f}s, 95% at f{f_done} t={t0+f_done/fps:.3f}s, max {int(mx)} px, {kind}{pre}')
    return ev
rep = {'video': mp4.split('/')[-1], 'fps': fps, 'window': [t0, t1], 'frames': len(rows),
       'cuts_or_replacements': [(r[0], r[1], r[2]) for r in cuts],
       'yellow': curve_events(3, 'yellow'), 'red': curve_events(4, 'red')}
json.dump(rep, open(out + '_events.json', 'w'), indent=1)
print(json.dumps(rep, indent=1))
