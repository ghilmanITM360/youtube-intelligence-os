# Cross-correlate the narration envelope of the source MP3 and the final MP4 audio.
import subprocess, sys, numpy as np
def pcm(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vn", "-ac", "1", "-ar", "8000", "-f", "s16le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32)
a, b = pcm(sys.argv[1]), pcm(sys.argv[2])
env = lambda x: np.sqrt(np.convolve(x * x, np.ones(80) / 80, "same"))[::80]  # 10 ms
ea, eb = env(a), env(b)
n = min(len(ea), len(eb)); ea, eb = ea[:n] - ea[:n].mean(), eb[:n] - eb[:n].mean()
lags = range(-20, 21)
c = [np.dot(ea[max(0, -l):n - max(0, l)], eb[max(0, l):n - max(0, -l)]) for l in lags]
best = lags[int(np.argmax(c))]
print(f"source {len(a)/8000:.3f}s  final {len(b)/8000:.3f}s  best lag {best*10} ms  corr {max(c)/np.sqrt((ea**2).sum()*(eb**2).sum()):.4f}")
