"""V13 caption alignment: whisper.cpp word timings (small.en, DTW) + an energy voice-activity check on the narration.
Run from v13/ after:  whisper-cli -m tools/whisper_models/ggml-small.en.bin -f qa/asr/narration16k.wav -ml 1 -sow -ojf \
                        -of qa/asr/narration_words --dtw small.en -l en -np
Writes audio/captions_v13.json (used by the caption overlay), SKYDIVER_SLOWDOWN_V13.srt, qa/asr/caption_alignment.csv.
Whisper word ENDS absorb following silence, so each cue start/end is snapped to voiced audio inside the word span."""
import csv, json, wave
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
FIX = {'breaks?': 'brakes?'}          # homophone: script wording (owner's narration text) kept
MAXC = 40                             # characters per cue (one or two short lines on a phone)

words = []
for s in json.load(open(ROOT / 'qa/asr/narration_words.json'))['transcription']:
    w = s['text'].strip()
    if w: words.append([FIX.get(w, w), s['offsets']['from'] / 1000, s['offsets']['to'] / 1000])

with wave.open(str(ROOT / 'qa/asr/narration16k.wav')) as f:
    x = np.frombuffer(f.readframes(f.getnframes()), np.int16).astype(float) / 32768
hop = 160                                                   # 10 ms
rms = np.sqrt(np.convolve(x * x, np.ones(400) / 400, 'same')[::hop])
db = 20 * np.log10(rms + 1e-9)
thr = np.percentile(db, 95) - 30                            # voiced = within 30 dB of loud speech
voiced = db > thr
GAP = 15                                                    # >=150 ms of silence separates speech runs
runs, i, n = [], 0, len(voiced)
while i < n:
    if voiced[i]:
        j = i
        while j < n and (voiced[j] or (j + GAP < n and voiced[j:j + GAP].any())): j += 1
        runs.append((i / 100, j / 100)); i = j
    else: i += 1
def onset(a, b):
    """Speech onset of a cue's first word: start of the last speech run that begins inside the word span
    (a word span that starts in the previous word's tail and crosses a pause begins after the pause)."""
    st = [r0 for r0, r1 in runs if a - .02 <= r0 < b]
    if st: return st[-1]
    inside = [r0 for r0, r1 in runs if r0 < a < r1]; return a if inside else a
def offset(a, b, lo):
    """Speech offset of a cue's last word: end of the first speech run overlapping the word after the cue onset lo."""
    for r0, r1 in runs:
        if r0 < b and r1 > max(a, lo) + .02: return min(r1, b + .3)
    return b

# segment: break after , . ? ; split anything longer than MAXC at the word nearest its middle
groups, cur = [], []
for w in words:
    cur.append(w)
    if w[0][-1] in ',.?': groups.append(cur); cur = []
if cur: groups.append(cur)
def split(g):
    s = ' '.join(w[0] for w in g)
    if len(s) <= MAXC or len(g) < 4: return [g]
    weak = {'a', 'the', 'your', 'you', 'to', 'in', 'is', 'and', 'than', 'where', 'can', 'it'}
    best = min(range(2, len(g) - 1), key=lambda i: abs(len(' '.join(w[0] for w in g[:i])) - len(s) / 2)
               + (12 if g[i - 1][0].lower() in weak or g[i - 1][0].isdigit() else 0))
    return split(g[:best]) + split(g[best:])
cues = [p for g in groups for p in split(g)]
# merge one-word fragments forward (e.g. "Still" + "closed.") when the pair is short
merged = []
for g in cues:
    short = merged and (len(merged[-1]) == 1 or merged[-1][-1][2] - merged[-1][0][1] < .5)
    if short and len(' '.join(w[0] for w in merged[-1] + g)) <= MAXC + 2 and g[0][1] - merged[-1][-1][2] < .6:
        merged[-1] += g
    else: merged.append(g)

out = []
for g in merged:
    a = onset(g[0][1] - .05, g[0][2])
    b = offset(g[-1][1], g[-1][2], a)
    out.append(dict(text=' '.join(w[0] for w in g), speech_start=round(a, 2), speech_end=round(b, 2)))
# display times: start with the speech (lead 0.05 s), hold 0.25 s after speech, min 0.9 s on screen, never overlap
for i, q in enumerate(out):
    nxt = out[i + 1]['speech_start'] - .05 if i + 1 < len(out) else 78.2
    q['start'] = round(max(0, q['speech_start'] - .05), 2)
    q['end'] = round(min(nxt, max(q['speech_end'] + .25, q['start'] + .9)), 2)
for a, b in zip(out, out[1:]): assert a['end'] <= b['start'] + 1e-6, (a, b)
assert all(q['end'] > q['start'] for q in out)

(ROOT / 'audio/captions_v13.json').write_text(json.dumps(out, indent=1))
def tc(t): return f'{int(t // 3600):02}:{int(t % 3600 // 60):02}:{int(t % 60):02},{int(round(t % 1 * 1000)):03}'
(ROOT / 'SKYDIVER_SLOWDOWN_V13.srt').write_text(''.join(f'{i + 1}\n{tc(q["start"])} --> {tc(q["end"])}\n{q["text"]}\n\n' for i, q in enumerate(out)))
with open(ROOT / 'qa/asr/caption_alignment.csv', 'w', newline='') as f:
    wr = csv.DictWriter(f, ['n', 'start', 'end', 'speech_start', 'speech_end', 'chars', 'cps', 'text']); wr.writeheader()
    for i, q in enumerate(out):
        d = q['end'] - q['start']
        wr.writerow(dict(n=i + 1, **{k: q[k] for k in ('start', 'end', 'speech_start', 'speech_end', 'text')}, chars=len(q['text']), cps=round(len(q['text']) / d, 1)))
print(len(out), 'cues; max chars', max(len(q['text']) for q in out), '; max cps',
      max(round(len(q['text']) / (q['end'] - q['start']), 1) for q in out))
