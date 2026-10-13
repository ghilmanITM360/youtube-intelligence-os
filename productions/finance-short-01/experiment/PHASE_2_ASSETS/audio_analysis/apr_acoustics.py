"""Acoustic check of the 'introductory APR' segment: syllable nuclei + LPC formants.

Discriminator: spelled "A-P-R" contains a long /i:/ ("pee": F1 ~300 Hz, F2 > 2000 Hz)
after the /p/ release and three vowel nuclei; "April" has two nuclei and no /i:/.
Usage: python apr_acoustics.py vo_24k.wav START END
"""
import sys
import wave

import numpy as np

path, t0, t1 = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
with wave.open(path) as w:
    sr = w.getframerate()
    x = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(float) / 32768
seg = x[int(t0 * sr):int(t1 * sr)]

hop, win = int(0.010 * sr), int(0.030 * sr)
frames = [seg[i:i + win] for i in range(0, len(seg) - win, hop)]
times = t0 + (np.arange(len(frames)) * hop + win / 2) / sr

def band_energy(f, lo=300, hi=2500):
    spec = np.abs(np.fft.rfft(f * np.hanning(len(f)))) ** 2
    freqs = np.fft.rfftfreq(len(f), 1 / sr)
    return spec[(freqs >= lo) & (freqs <= hi)].sum()

def lpc_formants(f, order=12):
    f = np.append(f[0], f[1:] - 0.97 * f[:-1]) * np.hamming(len(f))
    r = np.correlate(f, f, "full")[len(f) - 1:len(f) + order]
    if r[0] <= 0:
        return []
    a, e = np.array([1.0]), r[0]
    for i in range(1, order + 1):  # Levinson-Durbin
        k = -(r[i] + np.dot(a[1:], r[i - 1:0:-1])) / e
        a = np.append(a, 0) + k * np.append(0, a[::-1])
        e *= 1 - k * k
    roots = [z for z in np.roots(a) if np.imag(z) > 0]
    out = []
    for z in roots:
        freq = np.angle(z) * sr / (2 * np.pi)
        bw = -np.log(abs(z)) * sr / np.pi
        if 200 < freq < 4000 and bw < 400:
            out.append(round(freq))
    return sorted(out)[:3]

env = np.array([band_energy(f) for f in frames])
env_db = 10 * np.log10(env / env.max() + 1e-12)
smooth = np.convolve(env_db, np.ones(5) / 5, mode="same")

# Syllable nuclei: local maxima >= -12 dB re segment max, separated by a dip of >= 4 dB.
peaks = []
for i in range(2, len(smooth) - 2):
    if smooth[i] == smooth[max(0, i - 6):i + 7].max() and smooth[i] > -12:
        if not peaks or (smooth[peaks[-1]:i].min() < min(smooth[peaks[-1]], smooth[i]) - 4):
            peaks.append(i)
        elif smooth[i] > smooth[peaks[-1]]:
            peaks[-1] = i

print(f"segment {t0:.2f}-{t1:.2f}s  frames={len(frames)}  sr={sr}")
print("nuclei (time s, level dB, F1/F2/F3 Hz):")
for p in peaks:
    print(f"  {times[p]:6.3f}  {smooth[p]:6.1f}  {lpc_formants(frames[p])}")
print("formant track every 20 ms (time, dB, formants):")
for i in range(0, len(frames), 2):
    if smooth[i] > -25:
        print(f"  {times[i]:6.3f} {smooth[i]:6.1f} {lpc_formants(frames[i])}")
