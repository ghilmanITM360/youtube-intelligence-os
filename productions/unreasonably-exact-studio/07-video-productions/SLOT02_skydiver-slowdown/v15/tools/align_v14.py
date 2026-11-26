"""V14 narration timing: Hamza's clean narration -> word / phrase / sentence timings, captions, and the time warp
that drives the picture.

Inputs (run from v15/ after tools/prepare_voice.py):
  whisper-cli -m tools/whisper_models/ggml-small.en.bin -f qa/asr/clean16k.wav -ml 1 -sow -ojf -of qa/asr/clean_words \
              --dtw small.en -l en -np
  history/v13/narration_words.json + narration16k.wav (V13 narration timing = the timing V13's picture was built on)
Outputs:
  WORD_LEVEL_TIMESTAMPS.json   every spoken word: film / clean-narration / raw-recording time, emphasis estimate
  audio/narration_v14.json     sentences, phrases (caption cues), pauses
  audio/warp.json              anchor pairs (V14 film time -> V13 design time) for the picture and sound
  SKYDIVER_SLOWDOWN_FINAL_V15.srt

Word timing: whisper.cpp DTW word spans, snapped to voiced audio (energy VAD on the clean file; its pauses are digital
silence). Captions show what Hamza says (ASR verified by two decoders); only homophone spelling and punctuation are edited.
"""
import csv, difflib, json, re, wave
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
VO_AT = 0.30            # film time where HAMZA_VOICEOVER_CLEAN.wav starts (first word ~0.40 s)
TAIL = 1.50             # picture after the last word (end card), then audio and video end together
FPS = 24
SPELL = {'breaks?': 'brakes?'}                                   # homophone: script meaning
PUNCT = {('model,', 'where'): 'model', ('fixed.', 'That'): 'fixed,', ('That', 'upward'): 'that'}   # one sentence, not two
MAXC = 40

def load_words(js):
    out = []
    for s in json.load(open(js))['transcription']:
        w = s['text'].strip()
        if w: out.append([w, s['offsets']['from'] / 1000, s['offsets']['to'] / 1000])
    return out

def vad(wav):
    with wave.open(str(wav)) as f:
        x = np.frombuffer(f.readframes(f.getnframes()), np.int16).astype(float) / 32768
    rms = np.sqrt(np.convolve(x * x, np.ones(400) / 400, 'same')[::160])
    db = 20 * np.log10(rms + 1e-9)
    v = db > np.percentile(db, 95) - 30
    runs, i = [], 0
    while i < len(v):
        if v[i]:
            j = i
            while j < len(v) and (v[j] or v[j:j + 15].any()): j += 1
            runs.append((i / 100, j / 100)); i = j
        else: i += 1
    return runs, db

def snap(words, runs):
    """Word start: a voiced run that begins inside the word span wins (whisper spans absorb the preceding pause).
    Word end: clipped to the end of the voiced run it sits in."""
    out = []
    for w, a, b in words:
        st = [r0 for r0, r1 in runs if a - .02 <= r0 < b]
        a2 = st[-1] if st else a
        b2 = b
        for r0, r1 in runs:
            if r0 < b and r1 > a2 + .02: b2 = min(b, r1) if r1 < b else b; break
        out.append([w, round(a2, 3), round(max(b2, a2 + .06), 3)])
    for p, q in zip(out, out[1:]):                    # no overlaps
        if p[2] > q[1]: p[2] = q[1]
    return out

# ---------------------------------------------------------------- V14 words
words = load_words(ROOT / 'qa/asr/clean_words.json')
for i, w in enumerate(words):
    w[0] = SPELL.get(w[0], w[0])
    nxt = words[i + 1][0] if i + 1 < len(words) else ''
    w[0] = PUNCT.get((w[0], nxt), w[0])
    if (words[i - 1][0] if i else '', w[0]) in PUNCT: w[0] = PUNCT[(words[i - 1][0], w[0])]
runs, db = vad(ROOT / 'qa/asr/clean16k.wav')
words = snap(words, runs)

# raw-recording time via the edit list
EDIT = [{k: float(v) for k, v in r.items()} for r in csv.DictReader(open(ROOT / 'audio/voice_edit.csv'))]
def raw_t(t):
    for r in EDIT:
        if t <= r['clean_out'] + 1e-6: return r['raw_in'] + (t - r['clean_in'])
    return EDIT[-1]['raw_out']

# emphasis estimate: word loudness vs its sentence median, and stretch vs the sentence's mean syllable rate
def wdb(a, b):
    seg = db[int(a * 100):max(int(a * 100) + 1, int(b * 100))]; return float(np.percentile(seg, 90))
sentences, cur = [], []
for w in words:
    cur.append(w)
    if w[0][-1] in '.?': sentences.append(cur); cur = []
if cur: sentences.append(cur)
def syl(w): return max(1, len(re.findall(r'[aeiouy]+', w.lower().strip('.,?'))))
emph = {}
for s in sentences:
    lv = [wdb(a, b) for _, a, b in s]; med = float(np.median(lv))
    rate = sum(b - a for _, a, b in s) / sum(syl(w) for w, _, _ in s)
    for j, ((w, a, b), l) in enumerate(zip(s, lv)):
        loud = l - med; stretch = (b - a) / syl(w) / rate
        content = len(w.strip('.,?')) > 3 and w.lower().strip('.,?') not in {'your', "you're", 'where', 'than', 'that', 'this', 'from', 'about'}
        final = j == len(s) - 1 or w[-1] in ','                # phrase-final lengthening is not emphasis
        emph[(w, a)] = dict(loud_db=round(loud, 1), stretch=round(stretch, 2),
                            emphasis=bool(content and (loud >= 3.0 or (stretch >= 1.8 and not final))))

F = lambda t: round(t + VO_AT, 3)
WORDS = [dict(i=i, word=w, start=F(a), end=F(b), clean_start=a, clean_end=b, raw_start=round(raw_t(a), 3), raw_end=round(raw_t(b), 3),
              **emph[(w, a)]) for i, (w, a, b) in enumerate(words)]
DUR = round(round((WORDS[-1]['end'] + TAIL) * FPS) / FPS, 4)

# ---------------------------------------------------------------- phrases (caption cues) and sentences
NO_SPLIT = {"slowing down doesn't mean you have stopped falling."}   # V15: a half of this sentence alone says the opposite
def split(g):
    s = ' '.join(w['word'] for w in g)
    if len(s) <= MAXC or len(g) < 4 or s.lower() in NO_SPLIT: return [g]
    weak = {'a', 'the', 'your', 'you', 'to', 'in', 'is', 'and', 'than', 'where', 'can', 'it', 'not'}
    best = min(range(2, len(g) - 1), key=lambda i: abs(len(' '.join(w['word'] for w in g[:i])) - len(s) / 2)
               + (12 if g[i - 1]['word'].lower() in weak or g[i - 1]['word'].isdigit() else 0))
    return split(g[:best]) + split(g[best:])
groups, cur = [], []
for w in WORDS:
    cur.append(w)
    if w['word'][-1] in ',.?': groups.append(cur); cur = []
if cur: groups.append(cur)
cues = [p for g in groups for p in split(g)]
merged = []
for g in cues:   # a one-word fragment joins the next phrase when short and close (e.g. "Up here," + "the air is thin.")
    if merged and len(merged[-1]) == 1 and len(' '.join(w['word'] for w in merged[-1] + g)) <= MAXC and g[0]['start'] - merged[-1][-1]['end'] < .5:
        merged[-1] += g
    else: merged.append(g)
CUES = []
for g in merged:
    CUES.append(dict(text=' '.join(w['word'] for w in g), speech_start=g[0]['start'], speech_end=g[-1]['end'], words=[w['i'] for w in g]))
for i, q in enumerate(CUES):   # display: 0.05 s lead, hold 0.25 s after speech, >= 0.9 s, never overlapping
    nxt = CUES[i + 1]['speech_start'] - .05 if i + 1 < len(CUES) else DUR
    q['start'] = round(max(0, q['speech_start'] - .05), 3)
    q['end'] = round(min(nxt, max(q['speech_end'] + .25, q['start'] + .9)), 3)
for a, b in zip(CUES, CUES[1:]): assert a['end'] <= b['start'] + 1e-6
SENT = [dict(text=' '.join(w['word'] for w in s2), start=s2[0]['start'], end=s2[-1]['end']) for s2 in
        [[WORDS[k] for k in range(len(WORDS)) if words[k] in s] for s in sentences]]
PAUSES = [dict(after=WORDS[i]['word'], start=WORDS[i]['end'], end=WORDS[i + 1]['start'], dur=round(WORDS[i + 1]['start'] - WORDS[i]['end'], 3))
          for i in range(len(WORDS) - 1) if WORDS[i + 1]['start'] - WORDS[i]['end'] >= .25]

# ---------------------------------------------------------------- warp: V14 film time -> V13 design time
# Same script, two performances. Words are matched in order; anchors are each spoken phrase's first-word onset in
# both recordings (V13 narration timing, history/v13; phrase ends are not used: V13's overlapped). Monotone cubic interpolation between anchors keeps every
# shot, camera move and reveal on the word it was designed for, with no global speed factor.
def norm(w): return re.sub(r"[^a-z0-9']", '', w.lower()).replace("you've", 'youve')
old = load_words(ROOT / 'history/v13/narration_words.json')
for w in old: w[0] = SPELL.get(w[0], w[0])
ow, nw = [norm(w[0]) for w in old], [norm(w['word']) for w in WORDS]
sm = difflib.SequenceMatcher(None, ow, nw, autojunk=False)
match = {}
for a, b, n in sm.get_matching_blocks():
    for k in range(n): match[b + k] = a + k
# V13 word times snapped with the same VAD method on the V13 narration (history/v13/narration16k.wav, reference only)
old = snap(old, vad(ROOT / 'history/v13/narration16k.wav')[0])
def old_onset(oi): return old[oi][1]
def old_offset(oi): return old[oi][2]
anchors = [(0.0, 0.0, 3)]                      # (V14 time, V13 time, priority)
sent_first = {s2[0]['i'] for s2 in [[WORDS[k] for k in range(len(WORDS)) if words[k] in s] for s in sentences]}
for g in groups:                               # one anchor per spoken phrase: its first word's onset
    i0 = g[0]['i']
    if i0 in match: anchors.append((WORDS[i0]['start'], old_onset(match[i0]), 2 if i0 in sent_first else 1))
# event anchors: the reveal lands ON the word that names it (Hamza finishes the set-up first)
EVENTS = [('stronger', 43.75, 'drag bar passes the weight line on "stronger"', 'start'),
          ('think', 46.60, 'push-in on the net force holds through "Think about that"; K2 starts as the sentence ends', 'sentence_end')]
for word, old_t, why, where in EVENTS:
    k = next(i for i, w in enumerate(WORDS) if norm(w['word']) == word)
    t = WORDS[k]['start'] if where == 'start' else next(s2['end'] for s2 in SENT if s2['start'] <= WORDS[k]['start'] <= s2['end'])
    anchors = [p for p in anchors if abs(p[0] - t) > .7] + [(t, old_t, 3)]
anchors.append((WORDS[-1]['end'], old_offset(len(old) - 1), 2))
anchors.append((DUR, 78.2, 3))
anchors.sort()
# keep the picture's speed within RATE (V13 s per V14 s): drop the weakest anchor at the worst segment until it fits.
# Slow stretches are not frozen: ambient motion (bob, airflow, streaks) runs in real film time (tools/v14.py).
RATE = (.34, 1.6)
while True:
    segs = [((q[1] - p[1]) / (q[0] - p[0]), i) for i, (p, q) in enumerate(zip(anchors, anchors[1:]))]
    bad = [(max(RATE[0] / r if r > 0 else 99, r / RATE[1]), i) for r, i in segs if not RATE[0] <= r <= RATE[1]]
    if not bad: break
    _, i = max(bad)
    cand = [j for j in (i, i + 1) if anchors[j][2] < 3]
    if not cand: raise SystemExit(f'cannot fit rate at {anchors[i]} {anchors[i + 1]}')
    anchors.pop(min(cand, key=lambda j: (anchors[j][2], -j)))
anchors = [(a, b) for a, b, _ in anchors]

def pchip(xs, ys):
    """Fritsch-Carlson monotone cubic slopes."""
    h = np.diff(xs); d = np.diff(ys) / h; m = np.zeros(len(xs))
    m[0], m[-1] = d[0], d[-1]
    for i in range(1, len(xs) - 1):
        if d[i - 1] * d[i] <= 0: m[i] = 0
        else:
            w1, w2 = 2 * h[i] + h[i - 1], h[i] + 2 * h[i - 1]; m[i] = (w1 + w2) / (w1 / d[i - 1] + w2 / d[i])
    return m
X = np.array([a for a, _ in anchors]); Y = np.array([b for _, b in anchors]); M = pchip(X, Y)
def warp(t):
    i = int(np.clip(np.searchsorted(X, t) - 1, 0, len(X) - 2)); h = X[i + 1] - X[i]; s = (t - X[i]) / h
    return float((2*s**3 - 3*s**2 + 1) * Y[i] + (s**3 - 2*s**2 + s) * h * M[i] + (-2*s**3 + 3*s**2) * Y[i + 1] + (s**3 - s**2) * h * M[i + 1])
ts = np.arange(0, DUR, 1 / FPS); ws = [warp(t) for t in ts]
assert all(b >= a for a, b in zip(ws, ws[1:])), 'warp must be monotone'
rates = np.diff(ws) * FPS

# ---------------------------------------------------------------- write
(ROOT / 'WORD_LEVEL_TIMESTAMPS.json').write_text(json.dumps(dict(
    source='HAMZA_VOICEOVER_CLEAN.wav (edited from HAMZA_VOICEOVER_RAW.mp3, see audio/voice_edit.csv)',
    method='whisper.cpp small.en, DTW word timestamps, snapped to voiced audio (energy VAD); transcript cross-checked by greedy and beam-5 decoding',
    film_offset_s=VO_AT, fps=FPS, film_duration_s=DUR,
    columns='start/end = film seconds; clean_* = seconds in HAMZA_VOICEOVER_CLEAN.wav; raw_* = seconds in HAMZA_VOICEOVER_RAW.mp3; '
            'loud_db = word level vs sentence median; stretch = per-syllable duration vs sentence mean; emphasis = estimate, not a listening judgement',
    words=WORDS), indent=1))
(ROOT / 'audio/narration_v14.json').write_text(json.dumps(dict(duration=DUR, vo_at=VO_AT, sentences=SENT, cues=CUES, pauses=PAUSES), indent=1))
(ROOT / 'audio/warp.json').write_text(json.dumps(dict(
    note='V14 film time -> V13 design time (tools/v13_shots.py event times). Monotone cubic (Fritsch-Carlson) through the anchors.',
    duration=DUR, anchors=[[round(a, 3), round(b, 3)] for a, b in anchors], slopes=[round(float(m), 5) for m in M],
    events=[dict(word=w, v13_time=t, why=y, at=a) for w, t, y, a in EVENTS]), indent=1))
def tc(t): return f'{int(t // 3600):02}:{int(t % 3600 // 60):02}:{int(t % 60):02},{int(round(t % 1 * 1000)):03}'.replace(',1000', ',999')
(ROOT / 'SKYDIVER_SLOWDOWN_FINAL_V15.srt').write_text(''.join(f'{i + 1}\n{tc(q["start"])} --> {tc(q["end"])}\n{q["text"]}\n\n' for i, q in enumerate(CUES)))
print(f'{len(WORDS)} words, {len(SENT)} sentences, {len(CUES)} cues (max {max(len(q["text"]) for q in CUES)} chars), '
      f'{len(PAUSES)} pauses; film {DUR} s; {len(anchors)} warp anchors; picture rate V13-s per V14-s {rates.min():.2f}..{rates.max():.2f} '
      f'(median {np.median(rates):.2f}); unmatched words: {[WORDS[i]["word"] for i in range(len(WORDS)) if i not in match]}')
