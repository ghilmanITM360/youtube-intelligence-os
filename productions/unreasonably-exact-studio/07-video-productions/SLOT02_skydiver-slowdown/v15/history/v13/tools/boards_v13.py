"""V13 review material from the RENDERED film (run from v13/ after the render):
  storyboard/panels/<shot>_{start,dev,payoff}.png   full-size 1080x1920 frames
  FULL_SCREEN_VISUAL_STORYBOARD.md, SHOT_MANIFEST.csv, timeline/V13_timeline.json, timeline/V13.edl
  qa/before_after/*.png        owner V11 screenshot | V13 frame at the same narration time
  qa/phone_size_check.png      critical panels at 360x640
  MOTION_DESIGN_PROOFS/        proof clips A-F cut from the film + 16-frame strips
"""
import csv, json, subprocess, sys
from pathlib import Path
from PIL import Image
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
src = (ROOT / 'tools/v13_shots.py').read_text()
SHOTS = eval(src[src.index('SHOTS = [') + 8: src.index(']\nSHOT_OBJS') + 1])
FILM = ROOT / 'SKYDIVER_SLOWDOWN_V13_picture.mp4'
def ff(*a): subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', *a], check=True)
def grab(t, out, scale=None):
    ff('-ss', f'{t:.3f}', '-i', str(FILM), '-frames:v', '1', *(['-vf', f'scale={scale}'] if scale else []), str(out))

P = ROOT / 'storyboard/panels'; P.mkdir(parents=True, exist_ok=True)
STAGES = (('START', .12), ('DEVELOPMENT', .5), ('PAYOFF', .88))
md = ['# V13 full-screen visual storyboard', '',
      'Panels are frames of the rendered film at 1080x1920 (not sketches), three per shot: START / DEVELOPMENT / PAYOFF.',
      'TRANSITION = how the shot hands over to the next. Phone-size check: `qa/phone_size_check.png`.', '']
rows = []
for i, (sid, a, b, kind, purpose) in enumerate(SHOTS):
    nxt = SHOTS[i + 1] if i + 1 < len(SHOTS) else None
    md += [f'## {sid} · {a:.2f}-{b:.2f} s · {kind}', '', purpose, '']
    for st, q in STAGES:
        f = P / f'{sid}_{st.lower()}.png'; grab(a + (b - a) * q, f)
        md.append(f'![{sid} {st}](storyboard/panels/{f.name})')
    md += ['', f'TRANSITION: {"cut to " + nxt[0] + " (" + nxt[3] + ")" if nxt else "end"}', '']
    rows.append(dict(shot=sid, start=a, end=b, kind=kind, purpose=purpose))
(ROOT / 'FULL_SCREEN_VISUAL_STORYBOARD.md').write_text('\n'.join(md))
with (ROOT / 'SHOT_MANIFEST.csv').open('w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
T = ROOT / 'timeline'; T.mkdir(exist_ok=True)
(T / 'V13_timeline.json').write_text(json.dumps(dict(fps=24, duration=78.2, source='tools/v13_shots.py SHOTS', shots=rows,
                                                    audio=['audio/stems/*.wav', 'audio/V13_mix.wav'], captions='SKYDIVER_SLOWDOWN_V13.srt'), indent=1))
def tc(x): f = round(x * 24); return f'{f // 86400:02}:{f // 1440 % 60:02}:{f // 24 % 60:02}:{f % 24:02}'
(T / 'V13.edl').write_text('TITLE: SKYDIVER_SLOWDOWN_V13\nFCM: NON-DROP FRAME\n\n' + ''.join(
    f'{i + 1:03}  V13PIC  V  C  {tc(r["start"])} {tc(r["end"])} {tc(r["start"])} {tc(r["end"])}\n* {r["shot"]} {r["kind"]}\n'
    for i, r in enumerate(rows)))

# before/after: owner V12 opening screenshots (times read from the player bar) vs V13 at the same time
OWN = sorted((ROOT / 'qa/owner').glob('*.png'))
TIMES = {'2.54.04': 0.0, '2.54.11': 1.0, '2.54.18': 3.0}
BA = ROOT / 'qa/before_after'; BA.mkdir(parents=True, exist_ok=True)
for f in OWN:
    key = next((k for k in TIMES if k in f.name), None)
    if not key: continue
    t = TIMES[key]; g = BA / f'_v13_{t:05.1f}.png'; grab(t + .02, g)
    a = Image.open(f).convert('RGB'); a = a.resize((int(a.width * 960 / a.height), 960))
    b = Image.open(g).convert('RGB').resize((540, 960))
    s = Image.new('RGB', (a.width + 560, 960), 'white'); s.paste(a, (0, 0)); s.paste(b, (a.width + 20, 0))
    s.save(BA / f'V12_vs_V13_{int(t // 60)}m{int(t % 60):02}s.png'); g.unlink()
# opening comparison: V10 / V11 / V12 / V13 at the same moments (rows), 0.0 .. 5.0 s (columns)
REF = ROOT / 'qa/reference/opening_frames'   # V10-V12 frames saved before those folders were removed
VERS = [(n, None) for n in (10, 11, 12)] + [(13, ROOT / 'SKYDIVER_SLOWDOWN_V13.mp4')]
TS = [0.0, 0.8, 1.6, 2.4, 3.0, 3.6, 4.4, 5.0]
sheet = Image.new('RGB', (180 * len(TS), 320 * len(VERS)), 'white')
for r, (n, f) in enumerate(VERS):
    for k, t in enumerate(TS):
        g = BA / '_cmp.png' if f else REF / f'V{n}_t{t}.png'
        if f: ff('-ss', f'{t:.2f}', '-i', str(f), '-frames:v', '1', '-vf', 'scale=180:320', str(g))
        sheet.paste(Image.open(g).convert('RGB'), (180 * k, 320 * r))
sheet.save(ROOT / 'qa/OPENING_V10_V11_V12_V13.png'); (BA / '_cmp.png').unlink()

# phone size
crit = ['A1_start', 'A1_payoff', 'E1_payoff', 'I1_payoff', 'J1_payoff', 'K1_development', 'K1_payoff', 'L1_payoff', 'N1_payoff', 'Q2_payoff']
ims = [Image.open(P / f'{c}.png').convert('RGB').resize((360, 640)) for c in crit]
s = Image.new('RGB', (360 * 5, 640 * 2), 'white')
for k, im in enumerate(ims): s.paste(im, ((k % 5) * 360, (k // 5) * 640))
s.save(ROOT / 'qa/phone_size_check.png')

# proofs A-F (cut from the integrated film; each was first developed as still strips, see qa/*_strip.png)
PR = ROOT / 'MOTION_DESIGN_PROOFS'; PR.mkdir(exist_ok=True)
for name, a, b in [('A_opening', 0, 5.22), ('B_airflow_to_drag', 16.80, 20.92), ('C_thin_vs_dense', 28.63, 31.42),
                   ('D1_gravity_dominates', 24.89, 28.63), ('D2_equal_then_drag_exceeds', 38.72, 47.71),
                   ('E_down_while_slowing', 47.71, 55.35), ('F_wrist_instrument', 8.2, 12.52), ('F2_pov_needle', 55.35, 59.35)]:
    ff('-ss', str(a), '-to', str(b), '-i', str(ROOT / 'SKYDIVER_SLOWDOWN_V13.mp4'), '-c:v', 'libx264', '-crf', '18', '-c:a', 'aac', str(PR / f'{name}.mp4'))
    ff('-ss', str(a), '-to', str(b), '-i', str(FILM), '-vf', f'fps={16 / (b - a):.3f},scale=216:384,tile=8x2', '-frames:v', '1', str(PR / f'{name}_strip.png'))
print('boards, before/after, opening comparison, phone check, proofs written')
