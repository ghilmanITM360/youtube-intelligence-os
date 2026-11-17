#!/usr/bin/env python3
"""V3 soundtrack: an original procedural music bed and 10 restrained SFX, ducked under the untouched narration.

Every sound is synthesized by this file (numpy, fixed seed): no samples, loops, presets or third-party audio.
Effect times are read from KEYFRAME_TIMELINE.json, so a retimed timeline moves its sounds with it.

  python3 animation/tools/sound.py      # -> animation/audio/v3/*.wav + animation/V3_AUDIO_MIX.json
  python3 animation/tools/sound.py --music <licensed.wav>   # replace the bed (e.g. a YouTube Audio Library track)

Needs numpy and ffmpeg (decode/resample only). The narration WAV is read, never written.
"""
import json, subprocess, sys, wave
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
TL = json.loads((ROOT / 'animation/KEYFRAME_TIMELINE.json').read_text())
OUT = ROOT / 'animation/audio/v3'
SR = 48000
N = round(TL['frames'] / TL['fps'] * SR)
rng = np.random.default_rng(20261014)

# Mix settings (dB). Bed sits BED_REL below the narration's speech RMS in pauses and DUCK lower under speech.
BED_REL, DUCK, TP_TARGET = -20.0, 4.0, -1.5
FADE_IN, FADE_OUT = 0.25, 1.4


def db(x):
    return 10 ** (x / 20)


def decode(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', str(path), '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).astype(np.float64)


def write(path, x):
    y = np.clip(np.round(x * 32767 + rng.uniform(-0.5, 0.5, len(x)) - rng.uniform(-0.5, 0.5, len(x))), -32768, 32767).astype('<i2')  # TPDF dither
    with wave.open(str(path), 'wb') as f:
        f.setnchannels(1); f.setsampwidth(2); f.setframerate(SR); f.writeframes(y.tobytes())


def shape(x, fc, octaves):
    """Zero-phase log-gaussian band filter (fc Hz, width in octaves); fc=None with octaves<0 means low-pass at -octaves Hz."""
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR) + 1e-9
    H = 1 / (1 + (f / -octaves) ** 4) if fc is None else np.exp(-0.5 * (np.log2(f / fc) / octaves) ** 2)
    return np.fft.irfft(X * H, len(x))


def true_peak(x):
    """dBTP estimate: 4x band-limited oversampling (FFT zero padding)."""
    X = np.fft.rfft(x); Y = np.zeros(len(x) * 2 + 1, complex); Y[:len(X)] = X
    return 20 * np.log10(np.abs(np.fft.irfft(Y, len(x) * 4) * 4).max())


# ---------------------------------------------------------------- music bed (original)
BPM = 90
BAR = 4 * 60 / BPM
CHORDS = {  # calm, curious D-minor colour: Dm9, Bbmaj7, Gm9, A7sus4 (bass, pad notes, arpeggio notes as MIDI)
    'Dm9': (38, [53, 57, 60, 64], [62, 65, 69, 72, 76]),
    'Bbmaj7': (46, [53, 57, 58, 62], [58, 62, 65, 69, 74]),
    'Gm9': (43, [58, 62, 65, 69], [67, 70, 74, 65, 69]),
    'A7sus4': (45, [55, 57, 62, 64], [69, 74, 76, 67, 72]),
}
FORM = ['Dm9', 'Bbmaj7', 'Gm9', 'A7sus4'] * 2 + ['Dm9', 'Bbmaj7', 'Dm9', 'Dm9']  # two bars each; ends resolved on Dm9 for the payoff
ARP = [[0, None, 2, 1, None, 3, 2, None], [0, 2, None, 3, None, 1, 4, None]]  # eighth-note steps per bar


def add(buf, s, x):
    """Mix x into buf at sample s, clipped to the buffer."""
    if s < len(buf):
        e = min(len(buf), s + len(x)); buf[s:e] += x[:e - s]


def hz(m):
    return 440 * 2 ** ((m - 69) / 12)


def mallet(f, dur, vel):
    t = np.arange(int(dur * SR)) / SR
    env = (1 - np.exp(-t / 0.004)) * np.exp(-t / 0.35)
    return vel * env * (np.sin(2 * np.pi * f * t) + 0.25 * np.exp(-t / 0.12) * np.sin(4 * np.pi * f * t) + 0.08 * np.exp(-t / 0.06) * np.sin(6 * np.pi * f * t))


def music():
    pad, pluck, bass = np.zeros(N), np.zeros(N), np.zeros(N)
    for i, name in enumerate(FORM):
        t0 = i * 2 * BAR
        if t0 >= N / SR:
            break
        b, notes, arp = CHORDS[name]
        n0, n1 = int(t0 * SR), min(N, int((t0 + 2 * BAR + 1.2) * SR))  # pad releases into the next chord
        t = np.arange(n1 - n0) / SR
        env = np.minimum(1, t / 0.9) * np.clip((2 * BAR + 1.2 - t) / 1.2, 0, 1)
        for m in notes:
            for det in (0.9985, 1.0015):
                f = hz(m) * det
                pad[n0:n1] += 0.025 * env * (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(4 * np.pi * f * t) + 0.1 * np.sin(6 * np.pi * f * t))
        for bar in range(2):
            tb = t0 + bar * BAR
            for k, (beat, a) in enumerate([(0, 0.10), (2, 0.05)]):  # soft root on beats 1 and 3
                s = int((tb + beat * BAR / 4) * SR); tt = np.arange(int(1.6 * SR)) / SR
                tone = a * (1 - np.exp(-tt / 0.01)) * np.exp(-tt / 0.9) * (np.sin(2 * np.pi * hz(b) * tt) + 0.2 * np.sin(4 * np.pi * hz(b) * tt))
                add(bass, s, tone)
            for step, idx in enumerate(ARP[(i * 2 + bar) % 2]):
                if idx is None:
                    continue
                s = int((tb + step * BAR / 8) * SR)
                note = mallet(hz(arp[idx]), 1.2, 0.11 * rng.uniform(0.8, 1.0))
                add(pluck, s, note)
    dry = shape(pad, None, -1800) + pluck + bass
    tt = np.arange(int(2.0 * SR)) / SR  # small synthetic room: decaying filtered noise, 20 ms pre-delay
    ir = shape(rng.normal(size=len(tt)) * np.exp(-tt / 0.5), None, -4000); ir[: int(0.02 * SR)] = 0; ir /= np.sqrt((ir ** 2).sum())
    L = 1 << int(np.ceil(np.log2(N + len(ir))))
    wet = np.fft.irfft(np.fft.rfft(pad + pluck, L) * np.fft.rfft(ir, L), L)[:N]
    x = dry + 0.35 * wet
    return shape(x, None, -9000) - shape(x, None, -70)  # keep it out of the sub-bass and the very top


# ---------------------------------------------------------------- effects (original)
def burst(dur, fc, oct_, tau, attack=0.002):
    t = np.arange(int(dur * SR)) / SR
    return shape(rng.normal(size=len(t)), fc, oct_) * (1 - np.exp(-t / attack)) * np.exp(-t / tau)


def norm(x, peak_db):
    return x / np.abs(x).max() * db(peak_db)


def sfx_rise():  # rate arrow up: short rising tone with air
    t = np.arange(int(0.32 * SR)) / SR
    f = 330 * 2 ** (t / 0.32)
    tone = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * t / 0.32) ** 2
    return norm(tone + 0.4 * burst(0.32, 4000, 0.7, 0.12, 0.08), -24)


def sfx_paper():  # bill sheet: two quick paper flicks
    a, b = burst(0.06, 3500, 0.8, 0.018), burst(0.09, 2600, 0.9, 0.03)
    x = np.zeros(int(0.16 * SR)); x[:len(a)] += a; s = int(0.035 * SR); x[s:s + len(b)] += b
    return norm(x, -22)


def sfx_marker(dur):  # highlight box: marker friction with stroke texture
    t = np.arange(int(dur * SR)) / SR
    x = shape(rng.normal(size=len(t)), 3000, 0.5) * (0.7 + 0.3 * np.sin(2 * np.pi * 31 * t)) * np.minimum(1, t / 0.02) * np.clip((dur - t) / 0.06, 0, 1)
    return norm(x, -22)


def sfx_swoosh():  # interest flow: soft air movement, low to high band
    d = 0.45; t = np.arange(int(d * SR)) / SR; u = t / d
    x = (1 - u) * shape(rng.normal(size=len(t)), 700, 0.8) + u * shape(rng.normal(size=len(t)), 2400, 0.8)
    return norm(x * np.sin(np.pi * u) ** 2, -21)


def sfx_pop(f0):  # key number: restrained pop with a falling pitch
    t = np.arange(int(0.14 * SR)) / SR
    f = f0 * (0.55 + 0.45 * np.exp(-t / 0.03))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * (1 - np.exp(-t / 0.002)) * np.exp(-t / 0.045)
    x[:int(0.002 * SR)] += 0.3 * rng.normal(size=int(0.002 * SR))
    return norm(x, -21)


def sfx_page():  # ledger opening: three soft page rustles
    x = np.zeros(int(0.36 * SR))
    for k, (s, fc) in enumerate([(0.0, 2200), (0.07, 3000), (0.15, 1800)]):
        b = burst(0.16, fc, 1.0, 0.05, 0.01) * (1 - 0.25 * k); i = int(s * SR); x[i:i + len(b)] += b
    return norm(x, -20)


def sfx_thunk():  # payments pause: soft low knock
    t = np.arange(int(0.25 * SR)) / SR
    f = 220 * (0.75 + 0.25 * np.exp(-t / 0.04))  # high enough to survive phone speakers
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * (1 - np.exp(-t / 0.003)) * np.exp(-t / 0.08)
    return norm(x + 0.3 * burst(0.25, 900, 0.8, 0.02), -19)


def sfx_resolve():  # payoff: mallet dyad in the bed's key with a felt thump
    x = mallet(hz(74), 1.6, 1.0) + 0.7 * mallet(hz(81), 1.6, 1.0)
    t = np.arange(len(x)) / SR
    x += 0.6 * np.sin(2 * np.pi * 98 * t) * (1 - np.exp(-t / 0.004)) * np.exp(-t / 0.09)
    return norm(x, -21)


# (state, layer) of the visual each effect reinforces; the effect starts on that layer's entrance onset
CUE_SFX = [
    ('S01_01', 'RATE', 'rise', sfx_rise, 'interest-rate arrow rises'),
    ('S01_03', 'BILL', 'paper', sfx_paper, 'interest bill sheet enters'),
    ('S02_01', 'POLICY_HL', 'marker', lambda: sfx_marker(0.27), 'FOMC 1/4-point highlight box'),
    ('S02_06', 'PAY_FLOW', 'swoosh', sfx_swoosh, 'interest flows Fed -> banks'),
    ('S03_04', 'ANNUAL_COST', 'pop', lambda: sfx_pop(700), 'ABOUT $7.5B lands'),
    ('S05_02', 'LEDGER', 'page', sfx_page, 'ledger opens'),
    ('S05_05', 'SOURCE_HL', 'marker', lambda: sfx_marker(0.27), 'H.4.1 -233,587 highlight box'),
    ('S06_03', 'PAUSE', 'thunk', sfx_thunk, 'Treasury payments pause'),
    ('S06_05', 'HIST_AMOUNT', 'pop', lambda: sfx_pop(620), '$107.4B lands'),
    ('S07_04', 'BOTH', 'resolve', sfx_resolve, 'BOTH CAN BE TRUE payoff'),
]


def onset(state, layer):
    tr = next(t for t in TL['tracks'] if t['layer'] == layer and state in t['states'])
    ks = tr['keys']
    i = next(i for i, k in enumerate(ks) if k['o'] > 0)
    return ks[i]['t'] if ks[i]['e'] == 'step' or i == 0 else ks[i - 1]['t']


def envelope(x, att, rel, hop=0.005):
    """dB envelope on a hop grid: RMS over 2*hop windows, then attack/release smoothing (seconds)."""
    h = int(hop * SR); n = len(x) // h
    r = 10 * np.log10(np.convolve((x[:n * h] ** 2).reshape(n, h).mean(1), np.ones(2) / 2, 'same') + 1e-12)
    out, y = np.empty(n), r[0]
    a, b = np.exp(-hop / att), np.exp(-hop / rel)
    for i, v in enumerate(r):
        y = a * y + (1 - a) * v if v > y else b * y + (1 - b) * v
        out[i] = y
    return out, h


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    voice = decode(ROOT / 'animation' / TL['audio'])
    voice = np.pad(voice, (0, N - len(voice)))
    env, h = envelope(voice, 0.03, 0.25)
    speech = env > -40
    speech_rms = 10 * np.log10((voice[: len(env) * h].reshape(-1, h) ** 2).mean(1)[speech].mean())

    licensed = sys.argv[sys.argv.index('--music') + 1] if '--music' in sys.argv else None
    bed = decode(licensed)[:N] if licensed else music()
    bed = np.pad(bed, (0, N - len(bed)))
    bed *= db(speech_rms + BED_REL) / np.sqrt((bed ** 2).mean())
    # ducking: -DUCK dB while speech is present, fast down (60 ms), slow up (450 ms)
    duck_db = np.where(speech, -DUCK, 0.0)
    g, a, b = np.empty_like(duck_db), np.exp(-0.005 / 0.06), np.exp(-0.005 / 0.45)
    y = 0.0
    for i, v in enumerate(duck_db):
        y = a * y + (1 - a) * v if v < y else b * y + (1 - b) * v
        g[i] = y
    gain = np.repeat(db(g), h); gain = np.pad(gain, (0, N - len(gain)), mode='edge')
    t = np.arange(N) / SR
    fade = np.minimum(1, t / FADE_IN) * np.clip((N / SR - t) / FADE_OUT, 0, 1)
    bed_mixed = bed * gain * fade

    sfx = np.zeros(N); cues = []
    for state, layer, kind, make, why in CUE_SFX:
        t0 = onset(state, layer); x = make()
        add(sfx, int(round(t0 * SR)), x)
        i0 = int(round(t0 * SR)); seg = slice(i0, min(N, i0 + len(x)))
        rms = lambda z: round(float(10 * np.log10((z[seg] ** 2).mean() + 1e-12)), 1)
        cues.append(dict(t=round(t0, 3), state=state, layer=layer, sound=kind, reason=why, dur_s=round(len(x) / SR, 2), peak_dbfs=round(20 * np.log10(np.abs(x).max()), 1),
                         rms_dbfs=round(float(10 * np.log10((x ** 2).mean())), 1), voice_rms_same_window_dbfs=rms(voice)))

    pre = voice + bed_mixed + sfx
    master = min(0.0, TP_TARGET - true_peak(pre))
    mix = pre * db(master)

    # measured on the hop grid during speech: narration vs everything added to it
    bg = bed_mixed + sfx
    fr = lambda z: (z[: len(env) * h].reshape(-1, h) ** 2).mean(1)
    sv, sb = fr(voice), fr(bg)
    voiced = 10 * np.log10(sv + 1e-12) > -35  # frames where the voice itself is present (not the smoothed gate)
    ratio = 10 * np.log10(sv[voiced] / np.maximum(sb[voiced], 1e-12))
    band = lambda z: shape(z, 2000, 1.0)  # ~1-4 kHz intelligibility band
    bv, bb = fr(band(voice)), fr(band(bg))
    ratio_band = 10 * np.log10(bv[voiced] / np.maximum(bb[voiced], 1e-12))
    pause = ~speech & (np.arange(len(env)) * h / SR < TL['narration_duration'])

    write(OUT / 'FS02_V3_MUSIC_BED.wav', bed / np.abs(bed).max() * db(-6))
    write(OUT / 'FS02_V3_SFX_STEM.wav', sfx)
    write(OUT / 'FS02_V3_MIX.wav', mix)
    rep = dict(
        sample_rate=SR, samples=N, duration_sec=round(N / SR, 3), narration=TL['audio'], narration_sha256=TL['audio_sha256'],
        narration_processing='decoded and resampled 44.1->48 kHz by ffmpeg; otherwise unchanged except the uniform master gain below',
        music=('licensed file ' + licensed) if licensed else 'ORIGINAL procedural bed generated by tools/sound.py (seed 20261014): D-minor Dm9-Bbmaj7-Gm9-A7sus4, 90 BPM, pad + mallet arpeggio + soft root bass + synthetic room',
        settings=dict(bed_rel_speech_db=BED_REL, duck_db=DUCK, duck_attack_ms=60, duck_release_ms=450, speech_gate_dbfs=-40,
                      fade_in_s=FADE_IN, fade_out_s=FADE_OUT, true_peak_target_dbtp=TP_TARGET),
        master_gain_db=round(master, 2),
        measured=dict(speech_rms_dbfs=round(speech_rms, 1),
                      speech_to_background_db=dict(median=round(float(np.median(ratio)), 1), p5=round(float(np.percentile(ratio, 5)), 1)),
                      speech_to_background_1_4khz_db=dict(median=round(float(np.median(ratio_band)), 1), p5=round(float(np.percentile(ratio_band, 5)), 1)),
                      bed_in_pauses_rel_speech_db=round(10 * np.log10(sb[pause].mean() / sv[speech].mean()), 1),
                      mix_sample_peak_dbfs=round(20 * np.log10(np.abs(mix).max()), 2), mix_true_peak_dbtp=round(true_peak(mix), 2)),
        sfx=cues,
        stems=['audio/v3/FS02_V3_MUSIC_BED.wav (bed before ducking, peak -6 dBFS)', 'audio/v3/FS02_V3_SFX_STEM.wav (effects at mix level, before master gain)',
               'audio/v3/FS02_V3_MIX.wav (final mix)'],
    )
    (ROOT / 'animation/V3_AUDIO_MIX.json').write_text(json.dumps(rep, indent=1) + '\n')
    print(json.dumps(rep['measured'], indent=1), 'master', rep['master_gain_db'])
    for c in cues:
        print(c['t'], c['sound'], c['dur_s'], 'sfx rms', c['rms_dbfs'], 'voice rms', c['voice_rms_same_window_dbfs'], '|', c['reason'])


if __name__ == '__main__':
    main()
