"""V14 narration edit: HAMZA_VOICEOVER_RAW.mp3 -> HAMZA_VOICEOVER_CLEAN.wav (48 kHz, 24-bit mono).

1. Speech runs from an energy voice-activity pass (10 ms hop). The recording's pauses are digital silence
   (RMS about -134 dB), so runs are unambiguous.
2. Script start = first run at or after PRE_END. The 0-8 s pre-roll was transcribed separately
   (qa/asr/preroll.txt: setup talk, "I will do a video recording here ... Start the video") and is removed.
3. Pauses longer than CAP are shortened to CAP by removing silence from their middle. Speech, breaths and
   every pause up to CAP are untouched. No time-stretch, no pitch change, no word removed.
4. Gentle chain: 70 Hz high-pass (rumble), light de-esser, 2:1 compression above -24 dB, then one linear
   gain to TARGET LUFS and a -3 dBFS safety limiter. No noise reduction: the gaps are already digital silence.
Writes audio/voice_edit.csv (raw -> clean time map) used by every later step.
Run from v15/:  .venv/bin/python tools/prepare_voice.py
"""
import csv, subprocess, json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'HAMZA_VOICEOVER_RAW.mp3'
SR, PRE_END, CAP, LEAD, TAIL, TARGET = 48000, 9.0, 1.5, 0.10, 0.45, -18.0

x = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', str(RAW), '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'],
                                 capture_output=True, check=True).stdout, np.float32)
hop = SR // 100
e = np.sqrt(np.convolve(x * x, np.ones(hop * 2) / (hop * 2), 'same')[::hop])
voiced = 20 * np.log10(e + 1e-12) > -60
runs, i = [], 0
while i < len(voiced):
    if voiced[i]:
        j = i
        while j < len(voiced) and voiced[j:j + 25].any(): j += 1     # gaps under 0.25 s stay inside a run
        runs.append((i / 100, j / 100)); i = j
    else: i += 1
runs = [r for r in runs if r[0] >= PRE_END]
start, end = runs[0][0] - LEAD, runs[-1][1] + TAIL

# keep-segments in raw time: each pause longer than CAP loses its middle
keep, a = [], start
for (r0, r1), (n0, n1) in zip(runs, runs[1:]):
    gap = n0 - r1
    if gap > CAP:
        keep.append((a, r1 + CAP / 2)); a = n0 - CAP / 2
keep.append((a, end))
rows, t = [], 0.0
for a, b in keep:
    rows.append(dict(raw_in=round(a, 3), raw_out=round(b, 3), clean_in=round(t, 3), clean_out=round(t + b - a, 3))); t += b - a
with open(ROOT / 'audio/voice_edit.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)

pieces = np.concatenate([x[int(round(a * SR)):int(round(b * SR))] for a, b in keep])
chain = 'highpass=f=70,deesser=i=0.25,acompressor=threshold=-24dB:ratio=2:attack=10:release=120:makeup=1'
def run(af, out=None):
    p = subprocess.run(['ffmpeg', '-v', 'info', '-hide_banner', '-y', '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-i', '-', '-af', af]
                       + (['-c:a', 'pcm_s24le', str(out)] if out else ['-f', 'null', '-']), input=pieces.tobytes(), capture_output=True)
    assert p.returncode == 0, p.stderr[-800:]
    return p.stderr.decode()
meas = run(chain + ',loudnorm=print_format=json')
js = json.loads(meas[meas.rindex('{'):meas.rindex('}') + 1])
gain = TARGET - float(js['input_i'])
run(f'{chain},volume={gain:.2f}dB,alimiter=limit=0.708:level=false:attack=3:release=60', ROOT / 'HAMZA_VOICEOVER_CLEAN.wav')
removed = (end - start) - t
print(f'script {start:.2f}-{end:.2f} s raw; {len(keep) - 1} long pauses capped at {CAP} s (removed {removed:.2f} s of silence); '
      f'clean {t:.2f} s; gain {gain:+.1f} dB to {TARGET} LUFS')
