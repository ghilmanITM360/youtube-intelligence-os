# Original music bed + SFX, synthesised from scratch (no samples, no third-party audio), then mixed
# UNDER the untouched narration with speech-keyed ducking. Deterministic: same input -> same output.
#   python3 tools/make_audio.py public/narration.mp3   -> audio/{music_bed,sfx,mix}.wav + audio/cues.json
import json, os, subprocess, sys, wave
import numpy as np

SR, DUR = 48000, 60.6
N = int(round(DUR * SR))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "audio")
rng = np.random.default_rng(1012)
mtof = lambda m: 440.0 * 2 ** ((m - 69) / 12)
tt = lambda n: np.arange(n) / SR

def decode(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.float32).reshape(-1, 2).astype(np.float64)
    y = np.zeros((N, 2)); y[: min(N, len(x))] = x[:N]
    return y

def write(name, x):
    with wave.open(os.path.join(OUT, name), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(x, -1, 1) * 32767).astype("<i2").tobytes())

def lufs(name):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", os.path.join(OUT, name), "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
    return float(r.split("Integrated loudness:")[1].split("I:")[1].split("LUFS")[0])

def place(buf, x, t0, pan=0.0):  # mono x -> stereo buf at time t0
    i = int(round(t0 * SR))
    if i < 0: x, i = x[-i:], 0
    x = x[: max(0, N - i)]
    buf[i:i + len(x), 0] += x * np.sqrt(0.5 * (1 - pan)) * 1.414
    buf[i:i + len(x), 1] += x * np.sqrt(0.5 * (1 + pan)) * 1.414

def lowpass(x, k):  # cheap moving-average low-pass
    return np.convolve(x, np.ones(k) / k, mode="same")

# ---------------- music: 84 BPM, F major -> D minor (serious section) -> back to F ----------------
BAR = 4 * 60 / 84
F7, AM7, DM7, BB7, GM7 = [53, 57, 60, 64], [52, 55, 57, 60], [50, 53, 57, 60], [50, 53, 57, 58], [50, 53, 55, 58]
ASUS, AMAJ, CSUS, F9 = [50, 52, 57], [49, 52, 57], [48, 53, 55, 60], [53, 57, 60, 64, 67]
SONG = [  # (pad voicing, bass, section)  A curious/warm, B lighter explainer, C serious, D lift, E resolve
    (F7, 41, "A"), (AM7, 45, "A"), (DM7, 38, "A"), (BB7, 46, "A"), (F7, 41, "A"), (AM7, 45, "A"), (DM7, 38, "A"), (BB7, 46, "A"),
    (F7, 41, "B"), (AM7, 45, "B"), (DM7, 38, "B"), (BB7, 46, "B"), (GM7, 43, "B"),
    (DM7, 38, "C"), (BB7, 46, "C"), (GM7, 43, "C"), (ASUS, 45, "C"), (AMAJ, 45, "C"),
    (BB7, 46, "D"), (CSUS, 36, "D"), (F9, 41, "E"), (F9, 41, "E"),
]
LEVEL = {"A": 1.0, "B": 0.78, "C": 0.85, "D": 0.9, "E": 0.9}

def pad_note(f, n):
    t = tt(n); x = np.zeros(n)
    for det in (-0.0023, 0.0023):  # +-4 cents chorus
        ff = f * (1 + det)
        x += np.sin(2 * np.pi * ff * t) + 0.22 * np.sin(4 * np.pi * ff * t) + 0.06 * np.sin(6 * np.pi * ff * t)
    return x * (1 + 0.04 * np.sin(2 * np.pi * 0.23 * t))

def pluck(f, dur=1.3, dec=0.33):
    n = int(dur * SR); t = tt(n)
    x = np.sin(2 * np.pi * f * t) + 0.32 * np.sin(4 * np.pi * f * t) * np.exp(-t / 0.12) + 0.08 * np.sin(2 * np.pi * 4.07 * f * t) * np.exp(-t / 0.05)
    return x * np.exp(-t / dec) * (1 - np.exp(-t / 0.004))

pad, plk, bass, glass = (np.zeros((N, 2)) for _ in range(4))
for b, (ch, root, sec) in enumerate(SONG):
    t0 = b * BAR
    if t0 >= DUR: break
    lv = LEVEL[sec]
    n = int((BAR + 1.0) * SR); env = np.minimum(1, tt(n) / 0.6) * np.minimum(1, (BAR + 1.0 - tt(n)) / 0.9)
    for m in ch:
        place(pad, pad_note(mtof(m), n) * env * 0.05 * lv * (0.8 if sec == "C" else 1), t0 - 0.05, pan=((m % 7) - 3) / 8)
    nb = int(BAR * SR); tb = tt(nb)
    place(bass, (np.sin(2 * np.pi * mtof(root) * tb) + 0.2 * np.sin(4 * np.pi * mtof(root) * tb)) * np.exp(-tb / 1.6) * np.minimum(1, tb / 0.06) * 0.16 * lv, t0)
    step = {"A": 0.5, "B": 1.0, "C": None, "D": 1.0, "E": 2.0}[sec]
    if step:
        order = [0, 2, 1, 3, 2, 1, 3, 2]
        for j in range(int(4 / step)):
            m = ch[order[j % 8] % len(ch)] + 12
            vel = (0.9 if j % 2 == 0 else 0.6) * lv
            place(plk, pluck(mtof(m)) * 0.11 * vel, t0 + j * step * 60 / 84, pan=0.35 if j % 2 else -0.35)
    if sec == "C":  # restrained tension: one quiet sustained high tone, slow swell
        g = pad_note(mtof(ch[-1] + 24), n) * np.sin(np.pi * np.clip(tt(n) / (BAR + 1.0), 0, 1)) ** 2
        place(glass, g * 0.012, t0)
dry = pad + plk + bass + glass
# synthetic room: decaying filtered noise impulse response (stereo-decorrelated)
irn = int(2.2 * SR); ir_t = tt(irn)
ir = np.stack([lowpass(rng.standard_normal(irn), 9) * np.exp(-ir_t / 0.55) for _ in range(2)], 1)
ir /= np.sqrt((ir ** 2).sum(0))
L = 1 << int(np.ceil(np.log2(N + irn)))
wet = np.stack([np.fft.irfft(np.fft.rfft(dry[:, c], L) * np.fft.rfft(ir[:, c], L), L)[:N] for c in range(2)], 1)
music = dry * 0.8 + wet * 0.55
tm = tt(N)
music *= (np.clip(tm / 1.2, 0, 1) ** 2)[:, None]  # gentle fade-in under the hook
fo = np.clip((DUR - tm) / 1.7, 0, 1)
music *= (0.5 - 0.5 * np.cos(np.pi * fo))[:, None]  # natural fade-out, finishing with the last frame

# ---------------- SFX (10 purposeful accents, all synthesised) ----------------
def noise(n): return rng.standard_normal(n)
def sfx_accent():  # gentle attention accent on the first pain reaction
    n = int(0.6 * SR); t = tt(n)
    return 0.6 * np.sin(2 * np.pi * (110 - 40 * np.minimum(1, t / 0.15)) * t) * np.exp(-t / 0.13) + 0.35 * pluck(mtof(76), 0.6, 0.18)[:n]
def sfx_shimmer():  # soft relief
    out = np.zeros(int(1.2 * SR))
    for i, m in enumerate([77, 81, 84]):
        p = pluck(mtof(m), 1.0, 0.4); s = int(i * 0.07 * SR); out[s:s + len(p)] += p[: len(out) - s] * 0.45
    n = len(out); air = lowpass(noise(n), 3) - lowpass(noise(n), 40)
    return out + 0.25 * air * np.sin(np.pi * np.clip(tt(n) / 0.8, 0, 1))
def sfx_pop():
    n = int(0.25 * SR); t = tt(n)
    return np.sin(2 * np.pi * np.cumsum(300 + 600 * np.minimum(1, t / 0.06)) / SR) * np.exp(-t / 0.07)
def sfx_whoosh(d=0.55):
    n = int(d * SR); t = tt(n); x = noise(n)
    lo, hi = lowpass(x, 60), lowpass(x, 8)
    mixw = np.sin(np.pi * t / d)
    return (lo * (1 - mixw) + hi * mixw) * np.sin(np.pi * t / d) ** 2 * 1.3
def sfx_bubble():
    out = np.zeros(int(0.6 * SR))
    for i in range(4):
        n = int(0.07 * SR); t = tt(n)
        b = np.sin(2 * np.pi * np.cumsum(260 + i * 60 + 900 * t / 0.07) / SR) * np.sin(np.pi * t / 0.07)
        s = int(i * 0.11 * SR); out[s:s + n] += b * 0.5
    return out
def sfx_tick():
    n = int(0.12 * SR); t = tt(n)
    return (np.sin(2 * np.pi * 1250 * t) * np.exp(-t / 0.012) + 0.6 * np.sin(2 * np.pi * 640 * t) * np.exp(-t / 0.02))
def sfx_boom():  # restrained shift to the serious section
    n = int(2.0 * SR); t = tt(n)
    return np.sin(2 * np.pi * 55 * t) * np.minimum(1, t / 0.04) * np.exp(-t / 0.7) + 0.15 * lowpass(noise(n), 200) * np.exp(-t / 0.5)
def sfx_thumps():  # two soft low thumps under the beating heart (not a monitor beep)
    out = np.zeros(int(0.9 * SR))
    for s0, a in ((0.0, 1.0), (0.28, 0.75)):
        n = int(0.3 * SR); t = tt(n); s = int(s0 * SR)
        out[s:s + n] += a * np.sin(2 * np.pi * (75 - 20 * t / 0.3) * t) * np.exp(-t / 0.08)
    return out
def sfx_chime():  # warm resolved ending
    out = np.zeros(int(1.6 * SR))
    for i, m in enumerate([77, 81, 84, 89]):
        p = pluck(mtof(m), 1.3, 0.55); s = int(i * 0.075 * SR); out[s:s + len(p)] += p[: len(out) - s] * 0.4
    return out

CUES = [  # (time s, name, fn, peak dBFS, pan, purpose)
    (0.92, "accent", sfx_accent, -21, 0.0, "first pain reaction (calf clutch)"),
    (2.05, "shimmer", sfx_shimmer, -25, 0.2, "relief as he sits"),
    (4.74, "pop", sfx_pop, -23, 0.2, "Dr. Rehan Omar badge"),
    (5.63, "whoosh", sfx_whoosh, -25, -0.3, "zoom into the calf close-up"),
    (10.45, "bubble", sfx_bubble, -26, 0.0, "artery / plaque reveal"),
    (16.92, "tick", sfx_tick, -24, 0.0, "walk -> rest state change"),
    (25.24, "whoosh", sfx_whoosh, -25, 0.4, "slide to the doctor's board"),
    (37.3, "boom", sfx_boom, -21, 0.0, "shift to the serious rest-pain contrast"),
    (53.98, "thumps", sfx_thumps, -22, 0.0, "elevated cardiovascular risk (heart icon)"),
    (59.82, "chime", sfx_chime, -24, 0.0, "final 'investigate' emphasis"),
]
sfx = np.zeros((N, 2))
for t0, name, fn, pk, pan, _ in CUES:
    x = fn(); x = x / np.abs(x).max() * 10 ** (pk / 20)
    place(sfx, x, t0, pan)

# ---------------- mix under the narration ----------------
narr = decode(sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "public", "narration.mp3"))
os.makedirs(OUT, exist_ok=True)
write("music_bed.wav", music / np.abs(music).max() * 0.5)
NARR_LUFS, MUSIC_LU_BELOW = -11.7, 20.0  # narration measured with ebur128; music sits ~20 LU under it
gain = 10 ** ((NARR_LUFS - MUSIC_LU_BELOW - lufs("music_bed.wav")) / 20)
music = music / np.abs(music).max() * 0.5 * gain
# speech-keyed ducking (10 ms frames, 60 ms attack / 450 ms release, up to -5 dB)
mono = narr.mean(1); fr = 480; nf = N // fr
db = 10 * np.log10(np.maximum(1e-10, (mono[: nf * fr].reshape(nf, fr) ** 2).mean(1)))
pres = np.clip((db + 46) / 14, 0, 1); env = np.zeros(nf); e = 0.0
for i, p in enumerate(pres):
    e = p + (e - p) * (np.exp(-10 / 60) if p > e else np.exp(-10 / 450)); env[i] = e
duck = 1 - (1 - 10 ** (-5 / 20)) * np.interp(np.arange(N), np.arange(nf) * fr + fr / 2, env)
bed = music * duck[:, None] + sfx
write("music_bed.wav", music); write("sfx.wav", sfx)
mix = narr + bed
peak = np.abs(mix).max()
g = min(1.0, 10 ** (-1.5 / 20) / peak)  # one static gain on the WHOLE mix (voice unprocessed otherwise)
write("mix.wav", mix * g)
json.dump({"bpm": 84, "music_gain_db": round(20 * np.log10(gain), 2), "mix_gain_db": round(20 * np.log10(g), 2),
           "pre_gain_peak_dbfs": round(20 * np.log10(peak), 2),
           "cues": [{"t": t0, "sfx": name, "peak_dbfs": pk, "purpose": why} for t0, name, _, pk, _, why in CUES]},
          open(os.path.join(OUT, "cues.json"), "w"), indent=1)
print("music LUFS", round(lufs("music_bed.wav"), 1), "| sfx", len(CUES), "| mix gain dB", round(20 * np.log10(g), 2), "| mix LUFS", round(lufs("mix.wav"), 1))
