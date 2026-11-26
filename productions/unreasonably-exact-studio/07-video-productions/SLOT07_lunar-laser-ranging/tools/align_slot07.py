"""Slot 07 narration timing: raw WAV + whisper.cpp text -> phrase/word/pause timings.

Why not trust whisper word times: on this file the large-v3-turbo and small.en decodes AGREE on the words (245/245)
but disagree on word START times by a median 0.64 s, and both clump words at phrase starts (e.g. 'You fire a' within
10 ms). Phrase edges from the audio energy are reliable (+-0.02 s); word edges inside a phrase are an ESTIMATE
(syllable-weighted, snapped to the nearest energy minimum, +-0.12 s). Re-run with the first argument = ASR json.

usage: python align_slot07.py asr_small.json raw.wav out_dir
"""
import json, re, sys, wave
from pathlib import Path
import numpy as np

GAP = 0.25          # a silence shorter than this stays inside a phrase
HOP = 0.01
SYL = re.compile(r'[aeiouy]+', re.I)


def load_asr(p):
    out = []
    for s in json.load(open(p))['transcription']:
        w = s['text'].strip()
        if w:
            out.append((w, s['offsets']['from'] / 1000, s['offsets']['to'] / 1000))
    return out


def load_wav(p):
    with wave.open(str(p)) as f:
        sr = f.getframerate()
        x = np.frombuffer(f.readframes(f.getnframes()), np.int16).astype(float) / 32768
    return x, sr


def envelope(x, sr):
    n = int(sr * HOP)
    k = int(sr * 0.02)
    p = np.convolve(x * x, np.ones(k) / k, 'same')[::n]
    return 20 * np.log10(np.sqrt(p) + 1e-9)


def voiced_runs(db):
    thr = np.percentile(db, 95) - 30          # same rule V15 used
    v = db > thr
    runs, i = [], 0
    while i < len(v):
        if v[i]:
            j = i
            while j < len(v):
                if v[j]:
                    j += 1
                elif v[j:j + int(GAP / HOP)].any():
                    j += 1
                else:
                    break
            runs.append([i * HOP, j * HOP])
            i = j
        else:
            i += 1
    return runs, thr


def assign(asr, runs):
    """Split the word sequence into one contiguous chunk per voiced run (DP).
    V1 assigned greedily by whisper start time; whisper clumps times at phrase edges, so it put 'moon.' after
    a pause it was spoken before (2026-11-26, V2 take). Cost per run = duration misfit vs syllable count
    + weak pull to the whisper start (+-0.64 s median error, so capped) - bonus for cutting at punctuation."""
    W, R = len(asr), len(runs)
    sy = np.array([syl(w) for w, _, _ in asr], float)
    cs = np.concatenate([[0], np.cumsum(sy)])
    rate = sum(b - a for a, b in runs) / cs[-1]
    INF = 1e18
    best = np.full((R + 1, W + 1), INF); arg = np.zeros((R + 1, W + 1), int); best[0, 0] = 0
    for r in range(1, R + 1):
        t0, t1 = runs[r - 1]
        for j in range(0, W + 1):
            # a run may stay empty (breath, click); costly so real speech is never dropped
            if best[r - 1, j] + 1.5 < best[r, j]:
                best[r, j], arg[r, j] = best[r - 1, j] + 1.5, j
            for i in range(0, j):
                if best[r - 1, i] >= INF:
                    continue
                c = np.log((t1 - t0) / (rate * (cs[j] - cs[i]))) ** 2
                c += 0.3 * min(abs(asr[i][1] - t0), 2.0)
                c += -0.6 if asr[j - 1][0][-1] in '.?!,' else 0.4
                if best[r - 1, i] + c < best[r, j]:
                    best[r, j], arg[r, j] = best[r - 1, i] + c, i
    cuts, j = [], W
    for r in range(R, 0, -1):
        cuts.append((arg[r, j], j)); j = arg[r, j]
    return [[w for w, _, _ in asr[i:j]] for i, j in reversed(cuts)]  # empty list = non-speech run


def syl(w):
    return max(1, len(SYL.findall(re.sub(r"[^a-z']", '', w.lower()))))


def main(asr_json, wav, out):
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    asr = load_asr(asr_json)
    x, sr = load_wav(wav)
    db = envelope(x, sr)
    runs, thr = voiced_runs(db)
    chunks = assign(asr, runs)
    words_out, phrases = [], []
    for (t0, t1), ws in zip(runs, chunks):
        if not ws:
            continue
        wt = np.array([syl(w) + 0.3 for w in ws])
        edges = t0 + (t1 - t0) * np.concatenate([[0], np.cumsum(wt)]) / wt.sum()
        # snap interior edges to the lowest energy within +-60 ms (the dip between words)
        for k in range(1, len(edges) - 1):
            i0, i1 = int((edges[k] - .06) / HOP), int((edges[k] + .06) / HOP) + 1
            edges[k] = (i0 + int(np.argmin(db[i0:i1]))) * HOP
        edges = np.maximum.accumulate(edges)
        for w, a, b in zip(ws, edges[:-1], edges[1:]):
            words_out.append({'i': len(words_out), 'word': w, 'start': round(float(a), 3), 'end': round(float(b), 3)})
        phrases.append({'i': len(phrases), 'text': ' '.join(ws), 'start': round(t0, 3), 'end': round(t1, 3),
                        'first': words_out[-len(ws)]['i'], 'last': words_out[-1]['i'],
                        'ends_with': ws[-1][-1] if ws[-1][-1] in '.?!,' else ''})
    pauses = [{'after_phrase': phrases[k]['i'], 'start': phrases[k]['end'], 'end': phrases[k + 1]['start'],
               'dur': round(phrases[k + 1]['start'] - phrases[k]['end'], 3)} for k in range(len(phrases) - 1)]
    sentences, cur = [], []
    for p in phrases:
        cur.append(p)
        if p['ends_with'] in '.?!' and p['ends_with']:
            sentences.append({'i': len(sentences), 'text': ' '.join(q['text'] for q in cur),
                              'start': cur[0]['start'], 'end': cur[-1]['end'],
                              'words': sum(q['last'] - q['first'] + 1 for q in cur)})
            cur = []
    assert not cur, 'dangling phrase without terminal punctuation'
    meta = {'source': str(wav), 'duration': round(len(x) / sr, 3), 'voiced_threshold_db': round(float(thr), 1),
            'asr_words': len(asr), 'words': len(words_out), 'phrases': len(phrases), 'sentences': len(sentences),
            'method': 'DP word-to-run assignment (v2)', 'accuracy': 'phrase edges MEASURED (+-0.02 s, energy VAD); word edges ESTIMATE (+-0.12 s, syllable-weighted, '
                        'snapped to energy minima); text from whisper.cpp small.en, agreed by large-v3-turbo'}
    json.dump({'meta': meta, 'words': words_out, 'phrases': phrases, 'sentences': sentences, 'pauses': pauses},
              open(out / 'WORD_TIMESTAMPS.json', 'w'), indent=1)
    print(json.dumps(meta, indent=1))
    for p in phrases:
        print('%2d %6.2f-%6.2f %s' % (p['i'], p['start'], p['end'], p['text']))


if __name__ == '__main__':
    main(*sys.argv[1:4])
