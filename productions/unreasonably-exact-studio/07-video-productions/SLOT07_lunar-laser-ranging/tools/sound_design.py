"""Rough-cut sound design V1: procedurally synthesised (rights-clear: generated here, no third-party samples), dialogue-first.

Rules (V15 dialogue-first standard + this film's science rule):
  * only DIEGETIC sound where there is air: observatory night ambience, dome shutter motor, telescope drive (on Earth);
  * space and the Moon are silent: no 'whoosh' for the pulse, no impact on the Moon (no air);
  * NON-diegetic UI accents only for graphics (stopwatch ticks, a soft tonal accent on reveals), clearly musical, never 'the sound of light';
  * the bed is ducked 9 dB under the narration (envelope follower on the master narration); narration is never processed.
usage: ~/.venvs/uepipe/bin/python tools/sound_design.py   -> renders/roughcut/sfx_bed.wav, final_mix.wav (+ loudness report)
"""
import json, os, subprocess, sys, wave
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(ROOT, 'animation'))
from uemotion.narration import MASTER_WAV, NAR
SR = 48000; DUR = 96.0; N = int(SR * DUR); rng = np.random.default_rng(7)
t = np.arange(N) / SR

def read_wav(p):
    out = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True, check=True).stdout
    return np.frombuffer(out, np.float32).copy()
def env(t0, t1, a=0.3, r=0.6):
    """trapezoid gain: fade in a, hold, fade out r."""
    g = np.clip((t - t0) / a, 0, 1) * np.clip((t1 - t) / r, 0, 1); return g
def lowpass(x, fc):
    k = np.exp(-2 * np.pi * fc / SR); y = np.empty_like(x); acc = 0.0
    # one-pole, vectorised in blocks via lfilter-equivalent
    from scipy.signal import lfilter
    return lfilter([1 - k], [1, -k], x)
def db(x): return 10 ** (x / 20)

bed = np.zeros(N, np.float32)
noise = rng.standard_normal(N).astype(np.float32)
# 1. observatory night ambience (air): soft low wind + very faint high 'night' texture, only in observatory scenes
amb = lowpass(noise, 260) * 0.9 + lowpass(noise, 3000) * 0.05
amb_gain = env(0.0, 9.9, 0.4, 0.5) + env(51.1, 60.6, 0.5, 0.6)
bed += (amb * amb_gain * db(-30)).astype(np.float32)
# 2. dome shutter motor (P03 0.12-0.95 s): low hum 55/110 Hz + filtered rumble, slight pitch rise
def motor(t0, t1, f0=55.0, rise=1.08, lvl=-26):
    g = env(t0, t1, 0.08, 0.15); f = f0 * (1 + (rise - 1) * np.clip((t - t0) / (t1 - t0), 0, 1))
    ph = 2 * np.pi * np.cumsum(f) / SR
    s = 0.6 * np.sin(ph) + 0.3 * np.sin(2 * ph) + 0.15 * lowpass(noise, 400)
    return (s * g * db(lvl)).astype(np.float32)
bed += motor(0.12, 0.95)
# 3. telescope drive whir (0.9-2.75 s): smoother, higher servo tone
bed += motor(0.9, 2.75, f0=140.0, rise=1.15, lvl=-31)
# 4. pulse fire at the observatory (in air): a short, soft electronic 'tick' at the laser, not a blast
def tick(t0, f=1800.0, lvl=-28, dec=0.035):
    g = np.exp(-np.clip(t - t0, 0, None) / dec) * (t >= t0); return (np.sin(2 * np.pi * f * (t - t0)) * g * db(lvl)).astype(np.float32)
bed += tick(7.92, 2200.0, -27, 0.05)
# 5. NON-diegetic stopwatch ticks while stopwatches run (P11 B07 ~16.0-17.1; P08 legs; G12 B13; G30 B32 sweep)
for a, b in ((15.99, 17.14), (21.9, 25.5), (28.9, 30.2), (NAR.start('B32'), NAR.start('B32') + 1.0)):
    for k in np.arange(a, b, 0.1): bed += tick(float(k), 3200.0, -36, 0.012)
# 6. soft tonal reveal accents (non-diegetic, musical): 'yes.' array reveal, 'two.' fold, final lock 'where it is'
def bell(t0, f, lvl=-30, dec=1.2):
    g = np.where(t >= t0, np.exp(-(t - t0) / dec), 0.0) * np.clip((t - t0) / 0.01, 0, 1)
    return ((np.sin(2 * np.pi * f * (t - t0)) + 0.35 * np.sin(2 * np.pi * 2.01 * f * (t - t0))) * g * db(lvl)).astype(np.float32)
for t0, f in ((NAR.anchor('B17'), 660.0), (NAR.anchor('B35'), 523.25), (NAR.ws(242) + 0.6, 783.99)):
    bed += bell(float(t0), f)

# ducking under the narration (dialogue-first)
nar = read_wav(MASTER_WAV); nar = np.pad(nar, (0, max(0, N - len(nar))))[:N]
e = lowpass(np.abs(nar), 8.0); e = e / (e.max() + 1e-9)
duck = db(-9) + (1 - db(-9)) * (1 - np.clip(e / 0.08, 0, 1))
bed_d = bed * lowpass(duck, 4.0).astype(np.float32)
mix = nar + bed_d
peak = float(np.abs(mix).max()); mix = mix / max(1.0, peak / db(-1.0))           # never clip; narration gain unchanged unless the sum peaks
out = os.path.join(ROOT, 'renders', 'roughcut'); os.makedirs(out, exist_ok=True)
def write(p, x):
    with wave.open(p, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes())
write(os.path.join(out, 'sfx_bed.wav'), bed_d); write(os.path.join(out, 'final_mix.wav'), mix)
def lufs(p):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', p, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    import re; m = re.findall(r'I:\s+(-?[\d.]+) LUFS', r); return float(m[-1]) if m else None
rep = dict(narration_lufs=lufs(MASTER_WAV), mix_lufs=lufs(os.path.join(out, 'final_mix.wav')), sfx_bed_lufs=lufs(os.path.join(out, 'sfx_bed.wav')),
           mix_peak_dbfs=round(float(20 * np.log10(np.abs(mix).max() + 1e-12)), 2), duck_db=-9, sources='all synthesised in tools/sound_design.py (rights-clear)')
rep['bed_below_narration_lu'] = round(rep['narration_lufs'] - rep['sfx_bed_lufs'], 1) if rep['sfx_bed_lufs'] else None
json.dump(rep, open(os.path.join(out, 'mix_report.json'), 'w'), indent=1); print(rep)
