"""V14 sound design, rebuilt for Hamza's narration. Every non-voice sound is GENERATED here (noise, sines, envelopes),
so the whole mix is rights-clear; no library clip is used.

Each cue is tied to a picture event by its V13 design time (tools/v14_shots.py) and placed at the V14 frame where
that event is drawn (unwarp). Ambience keys follow the fall. All non-voice stems duck under Hamza's speech.

  .venv/bin/python tools/mix_v14.py  -> audio/stems/*.wav, audio/V14_mix.wav, SOUND_DESIGN_CUE_SHEET.csv
The audio is an illustrative soundscape, not a measurement of airflow or speed.
"""
import csv, json, subprocess, sys
from pathlib import Path
import numpy as np
sys.argv = [sys.argv[0]]
ROOT = Path(__file__).resolve().parents[1]
ns = {'__file__': str(Path(__file__).with_name('v14.py')), '__name__': 'mix'}
exec(open(Path(__file__).with_name('v14.py')).read(), ns)
unwarp, DUR = ns['unwarp'], ns['DUR']
NARR = json.loads((ROOT / 'audio/narration_v14.json').read_text())
SR = 48000; N = int(round(DUR * SR))
STEMS = ROOT / 'audio/stems'; STEMS.mkdir(parents=True, exist_ok=True)
rng = np.random.default_rng(14)

def db(x): return 10 ** (x / 20)
def T(t13): return unwarp(t13) if t13 > 0 else 0.0
def ffread(*args):
    raw = subprocess.run(['ffmpeg', '-v', 'error', *args, '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).astype(np.float64)
def write(path, x):
    p = subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f64le', '-ac', '2', '-ar', str(SR), '-i', '-', '-c:a', 'pcm_s24le', str(path)],
                       input=np.ascontiguousarray(x).tobytes(), capture_output=True)
    assert p.returncode == 0, p.stderr
def env(keys, t):
    k = np.array(keys, float); return np.interp(t, k[:, 0], k[:, 1])
tt = np.arange(N) / SR

# ---------------------------------------------------------------- generators (short clips, numpy)
def band(d, lo, hi, seed=None):
    """Noise band-limited lo..hi Hz (FFT mask with soft edges)."""
    r = np.random.default_rng(seed); n = int(d * SR); X = np.fft.rfft(r.standard_normal(n)); f = np.fft.rfftfreq(n, 1 / SR)
    m = 1 / (1 + (lo / np.maximum(f, 1)) ** 4) / (1 + (f / hi) ** 4); y = np.fft.irfft(X * m, n)
    return y / (np.abs(y).max() + 1e-9)
def sweep(d, f0, f1, f2, q=.9, seed=None):
    """Whoosh: noise whose band centre glides f0 -> f1 (peak) -> f2 (STFT overlap-add)."""
    r = np.random.default_rng(seed); n = int(d * SR); x = r.standard_normal(n + 4096); y = np.zeros(n + 4096)
    win = np.hanning(2048); f = np.fft.rfftfreq(2048, 1 / SR)
    for s in range(0, n, 512):
        u = s / n; fc = np.exp(np.interp(u, [0, .55, 1], np.log([f0, f1, f2])))
        m = np.exp(-.5 * (np.log(np.maximum(f, 1) / fc) / q) ** 2)
        y[s:s + 2048] += np.fft.irfft(np.fft.rfft(x[s:s + 2048] * win) * m, 2048) * win
    y = y[:n]; return y / (np.abs(y).max() + 1e-9)
def shape(n, attack, release, curve=2.0):
    u = np.arange(n) / SR; d = n / SR
    return np.clip(u / max(attack, 1e-3), 0, 1) ** curve * np.clip((d - u) / max(release, 1e-3), 0, 1) ** curve
def tone(d, freqs, tau, seed=0):
    """Soft mallet tone: partials with exponential decay + 3 ms noise touch."""
    n = int(d * SR); u = np.arange(n) / SR
    y = sum(a * np.sin(2 * np.pi * f * u) * np.exp(-u / (tau / (1 + i * .6))) for i, (f, a) in enumerate(freqs))
    y *= np.clip(u / .004, 0, 1)
    y[:int(.003 * SR)] += .15 * band(.003, 2000, 8000, seed)
    return y / (np.abs(y).max() + 1e-9)
def tick(seed=0):
    return tone(.06, [(1650, 1), (3300, .45), (5200, .2)], .012, seed)
def flutter(d, rate=9.0, seed=None):
    """Suit fabric in the airflow: band noise gated by an irregular flapping envelope."""
    r = np.random.default_rng(seed); u = np.arange(int(d * SR)) / SR
    lfo = sum(np.sin(2 * np.pi * rate * k * u + r.uniform(0, 6.3)) for k in (.8, 1.0, 1.37))
    g = np.clip(lfo / 3 + .35, 0, 1) ** 1.5
    return band(d, 250, 2600, seed) * g
def stereo(x, pan=0.0):
    a = (pan + 1) * np.pi / 4; return np.stack([x * np.cos(a), x * np.sin(a)], 1) * np.sqrt(2)

# ---------------------------------------------------------------- cue list: (stem, name, V13 design time, builder, level dB, pan, picture event)
def whoosh(d, f0, f1, f2, a, r, seed): return lambda: sweep(d, f0, f1, f2, seed=seed) * shape(int(d * SR), a, r)
def gust(d, lo, hi, a, r, seed): return lambda: band(d, lo, hi, seed) * shape(int(d * SR), a, r, 1.5)
def swell(d, seed):            # reverse-style rise that stops on the cut
    def f():
        n = int(d * SR); u = np.arange(n) / n; return sweep(d, 300, 900, 1800, seed=seed) * u ** 3 * np.clip((1 - u) / .02, 0, 1)
    return f
def pluck(f0, seed=0): return lambda: tone(.9, [(f0, 1), (f0 * 2, .25), (f0 * 3.01, .08)], .22, seed)
def ratchet(n_ticks, d, seed):  # needle easing down: a few ticks, spacing widening, plus a soft servo whir
    def f():
        y = np.zeros(int(d * SR)); ts = np.cumsum(np.linspace(.12, .32, n_ticks)) - .12
        for i, t0 in enumerate(ts):
            k = tick(seed + i) * (1 - .1 * i); s = int(t0 * SR); y[s:s + len(k)] += k[:len(y) - s]
        y += .35 * band(d, 900, 1500, seed) * shape(len(y), .15, .3)
        return y / (np.abs(y).max() + 1e-9)
    return f
G4, C5, E5, A4, D5 = 392.0, 523.3, 659.3, 440.0, 587.3
CUES = [
 ('TRANSITIONS', 'tilt whoosh', 1.10, whoosh(1.1, 260, 900, 420, .45, .55, 1), -27, -.2, 'Camera tilts to follow the falling figure (opening B)'),
 ('TRANSITIONS', 'approach air', 2.15, gust(1.4, 180, 1400, .7, .5, 2), -25, .15, 'Dolly in toward the faller through the depth layers (opening C)'),
 ('TRANSITIONS', 'cut-behind air', 3.22, whoosh(.7, 500, 1600, 700, .25, .35, 3), -27, 0, 'Direct cut behind the faller (closed pack)'),
 ('FOLEY', 'suit flutter', 5.25, lambda: flutter(3.2, 9, 4) * shape(int(3.2 * SR), .5, .9), -29, .2, 'Side tracking: suit fabric in the airflow'),
 ('OTHER_SFX', 'weight reveal', 5.50, pluck(G4, 5), -31, 0, 'Weight arrow draws down ("gravity")'),
 ('FOLEY', 'sleeve rustle', 8.38, lambda: flutter(.55, 14, 6) * shape(int(.55 * SR), .06, .3), -27, .25, 'Forearm lifts toward the face'),
 ('FOLEY', 'wrist tick', 9.70, tick, -27, .15, 'Cut to the wrist instrument'),
 ('FOLEY', 'needle eases', 9.95, ratchet(4, 1.1, 7), -33, .15, 'Needle eases down on the dial'),
 ('FOLEY', 'head snap', 11.15, whoosh(.35, 700, 2200, 1200, .03, .25, 8), -30, -.1, '"Wait, what?": head snaps up, arm drops'),
 ('OTHER_SFX', 'same-length check', 13.10, pluck(G4, 9), -34, -.2, 'Weight arrow re-measured: same'),
 ('WIND_AMB', 'brakes gust', 14.40, gust(2.2, 150, 1800, .5, 1.2, 10), -24, .2, '"grow brakes?": gust of streaks past the body'),
 ('WIND_AMB', 'air reverses', 17.75, gust(2.4, 200, 2400, .7, 1.0, 11), -25, -.2, 'Camera locks on: the air now streams up past the body'),
 ('OTHER_SFX', 'drag reveal', 19.35, pluck(C5, 12), -31, .1, 'Drag arrow grows up ("the air pushes back")'),
 ('TRANSITIONS', 'reset swell', 19.75, swell(1.17, 13), -29, 0, 'Rise into the MODEL reset; stops on the reset'),
 ('OTHER_SFX', 'thin-air box', 23.20, pluck(A4, 14), -34, -.2, 'Thin-air box appears'),
 ('OTHER_SFX', 'force pair', 24.95, pluck(G4, 15), -32, 0, 'Weight long, drag short'),
 ('OTHER_SFX', 'denser box', 29.20, pluck(A4 * 0.84, 16), -33, .2, 'Denser-air box fills'),
 ('OTHER_SFX', 'drag on body', 33.80, pluck(C5, 17), -32, .1, 'Drag arrow on the body (same air, same posture)'),
 ('WIND_AMB', 'speed x2 rise', 34.95, lambda: band(2.6, 200, 2600, 18) * shape(int(2.6 * SR), 2.0, .5, 1.3), -26, 0, 'Speed sweeps x1 -> x2; the air rushes harder'),
 ('OTHER_SFX', 'bars appear', 40.35, pluck(G4, 19), -32, .15, 'Force bars side by side, one scale'),
 ('OTHER_SFX', 'net force (cross)', 43.75, pluck(E5, 20), -29, .15, 'Drag bar passes the weight line; net force violet'),
 ('TRANSITIONS', 'push in', 44.10, whoosh(.9, 300, 800, 400, .4, .45, 21), -32, 0, 'Camera pushes in on the bar tops'),
 ('OTHER_SFX', 'trail', 47.66, pluck(D5, 22), -33, 0, 'Equal-time trail appears ("still moving down")'),
 ('OTHER_SFX', 'net force (trail)', 49.50, pluck(E5, 23), -31, .1, 'Net-force arrow points up beside the newest mark'),
 ('FOLEY', 'sleeve rustle 2', 54.33, lambda: flutter(.55, 14, 24) * shape(int(.55 * SR), .06, .3), -27, .25, 'Forearm lifts again'),
 ('FOLEY', 'wrist tick 2', 55.35, tick, -27, .1, 'Cut to the first-person instrument'),
 ('FOLEY', 'needle drops', 55.60, ratchet(5, 1.5, 25), -33, .1, 'Needle falls along the scale ("the speedometer drops")'),
 ('TRANSITIONS', 'tilt to ground', 57.20, whoosh(1.6, 220, 700, 260, .6, .8, 26), -28, -.1, 'Tilt from the wrist to the approaching ground'),
 ('FOLEY', 'pack flutter', 59.35, lambda: flutter(2.4, 8, 27) * shape(int(2.4 * SR), .4, .8), -29, -.15, 'Behind the faller: closed pack, fabric in the air'),
 ('OTHER_SFX', 'graph', 61.95, pluck(D5, 28), -33, 0, 'Speed-time graph builds'),
 ('OTHER_SFX', 'recap bars', 66.20, pluck(E5, 29), -32, .15, 'Recap force bars: drag slightly above weight'),
 ('TRANSITIONS', 'pull back', 70.53, whoosh(2.2, 180, 520, 240, .9, 1.1, 30), -27, 0, 'Pull back to the wide view'),
 ('OTHER_SFX', 'model graph', 70.95, pluck(D5, 31), -33, 0, '"this is a model": model graph draws in'),
 ('OTHER_SFX', 'alt curve 1', 75.20, pluck(A4, 32), -35, -.2, 'Alternative outcome: smaller drag area'),
 ('OTHER_SFX', 'alt curve 2', 76.00, pluck(A4 * 1.12, 33), -35, .2, 'Alternative outcome: larger drag area'),
]
# wind bed intensity in V13 design time (V13 WIND_KEYS), placed on the V14 frames that show those moments
WIND_KEYS = [(0, .16), (1.0, .22), (2.4, .40), (3.3, .66), (5.22, .66), (8.33, .62), (9.70, .52), (11.15, .60), (12.52, .64),
             (14.4, .72), (16.6, .70), (17.7, .62), (18.6, .76), (20.5, .62), (21.3, .05), (24.89, .07), (28.4, .55), (31.6, .66),
             (33.67, .60), (38.72, .68), (44.0, .66), (44.9, .54), (46.1, .54), (46.9, .66), (47.6, .64), (48.4, .50),
             (52.0, .50), (52.8, .70), (55.35, .70), (57.16, .74), (59.35, .66), (61.8, .58), (62.6, .44), (65.9, .44),
             (66.6, .56), (67.3, .50), (69.6, .50), (70.3, .52), (70.53, .48), (74.52, .24), (77.6, .06)]
AIR_KEYS = [(0, 0), (.15, 1), (1.6, .9), (3.0, 0)]

# ducking from Hamza's speech (phrase spans, 0.18 s ramps)
def duck_gain(depth_db):
    g = np.ones(N); k = db(depth_db)
    for q in NARR['cues']:
        a, b = q['speech_start'] - .18, q['speech_end'] + .18
        i0, i1 = max(0, int(a * SR)), min(N, int(b * SR))
        u = (np.arange(i0, i1) / SR); r = np.clip(np.minimum((u - a) / .18, (b - u) / .18), 0, 1)
        g[i0:i1] = np.minimum(g[i0:i1], 1 - (1 - k) * r)
    return g

def build():
    rows = []
    # VOICEOVER: Hamza, clean narration placed at VO_AT
    vo = ffread('-i', str(ROOT / 'HAMZA_VOICEOVER_CLEAN.wav'))
    V = np.zeros((N, 2)); s0 = int(round(NARR['vo_at'] * SR)); V[s0:s0 + len(vo)] = vo[:N - s0]
    rows.append(dict(stem='VOICEOVER', cue='Hamza narration', start=NARR['vo_at'], end=round(NARR['vo_at'] + len(vo) / SR, 3), v13_design_time='',
                     picture_event='Whole film', level='0 dB (clean file -18.5 LUFS)', pan='centre', source='HAMZA_VOICEOVER_CLEAN.wav', rights='Owner-supplied recording'))
    # ambience: wind bed (generated brown + pink noise) and aircraft hum, envelopes in V14 time
    wind = ffread('-f', 'lavfi', '-i', f'anoisesrc=d={DUR}:c=brown:r={SR}:s=11:a=.9', '-f', 'lavfi', '-i', f'anoisesrc=d={DUR}:c=pink:r={SR}:s=29:a=.5',
                  '-filter_complex', '[0]highpass=f=70,lowpass=f=900,volume=6dB[a];[1]highpass=f=900,lowpass=f=5200,volume=-14dB,tremolo=f=0.17:d=0.35[b];'
                  '[a][b]amix=inputs=2:normalize=0,aformat=channel_layouts=stereo,apulsator=hz=0.07:amount=0.25')[:N]
    hum = ffread('-f', 'lavfi', '-i', f'anoisesrc=d={DUR}:c=brown:r={SR}:s=5:a=.8', '-f', 'lavfi', '-i', f'sine=f=88:d={DUR}:r={SR}',
                 '-f', 'lavfi', '-i', f'sine=f=176.5:d={DUR}:r={SR}',
                 '-filter_complex', '[0]lowpass=f=320,volume=2dB[n];[1]volume=-20dB,tremolo=f=11:d=0.3[s1];[2]volume=-27dB[s2];[n][s1][s2]amix=inputs=3:normalize=0,aformat=channel_layouts=stereo')[:N]
    wk = [(T(a), v) for a, v in WIND_KEYS] + [(DUR - .6, .05), (DUR, 0)]
    ak = [(T(a), v) for a, v in AIR_KEYS]
    duck_amb = duck_gain(-7)
    A = wind * (env(wk, tt) * duck_amb * db(-5))[:, None] + hum * (env(ak, tt) * duck_gain(-9) * db(-6))[:, None]
    rows.append(dict(stem='WIND_AMB', cue='wind bed', start=0, end=round(DUR, 3), v13_design_time='WIND_KEYS', picture_event='Relative-air bed follows the fall; near-silent at the model reset (rest)',
                     level='-5 dB x keyed envelope, -7 dB under speech', pan='wide', source='Generated: brown + pink noise (tools/mix_v14.py)', rights='Rights-clear (generated)'))
    rows.append(dict(stem='WIND_AMB', cue='aircraft hum', start=0, end=round(T(3.0), 3), v13_design_time='0-3.0', picture_event='Aircraft in the establishing shot',
                     level='-6 dB, fades out as the aircraft leaves', pan='centre', source='Generated: brown noise + 88/176 Hz hum', rights='Rights-clear (generated)'))
    stems = {k: np.zeros((N, 2)) for k in ('FOLEY', 'TRANSITIONS', 'OTHER_SFX')}; stems['WIND_AMB'] = A
    duck_fx = duck_gain(-4.5)
    for stem, name, t13, fn, lvl, pan, what in CUES:
        x = stereo(fn() * db(lvl), pan)
        at = T(t13); s = int(round(at * SR)); e = min(N, s + len(x))
        if name == 'reset swell': s = int(round(T(20.92) * SR)) - len(x); e = s + len(x)     # ends exactly on the reset frame
        stems[stem][s:e] += x[:e - s] * duck_fx[s:e, None]
        rows.append(dict(stem=stem, cue=name, start=round(s / SR, 3), end=round(e / SR, 3), v13_design_time=t13, picture_event=what,
                         level=f'{lvl} dB peak, -4.5 dB under speech', pan=f'{pan:+.2f}', source='Generated in tools/mix_v14.py', rights='Rights-clear (generated)'))
    for k, x in stems.items(): write(STEMS / f'{k}.wav', x)
    write(STEMS / 'VOICEOVER.wav', V)
    mix = V + sum(stems.values())
    write(ROOT / 'qa/_mix_pre.wav', mix)
    out = subprocess.run(['ffmpeg', '-hide_banner', '-i', str(ROOT / 'qa/_mix_pre.wav'), '-af', 'loudnorm=print_format=json', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    li = float(json.loads(out[out.rindex('{'):out.rindex('}') + 1])['input_i'])
    g = -16.0 - li
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(ROOT / 'qa/_mix_pre.wav'), '-af', f'volume={g:.2f}dB,alimiter=limit=0.84:level=false:attack=3:release=80',
                    '-c:a', 'pcm_s24le', str(ROOT / 'audio/V14_mix.wav')], check=True)
    (ROOT / 'qa/_mix_pre.wav').unlink()
    rows.sort(key=lambda r: float(r['start']))
    with open(ROOT / 'SOUND_DESIGN_CUE_SHEET.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
    print(f'{len(CUES)} generated cues + bed; mix gain {g:+.1f} dB to -16 LUFS -> audio/V14_mix.wav')

if __name__ == '__main__':
    build()
