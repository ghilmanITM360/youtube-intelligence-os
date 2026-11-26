"""Narration timing loader (same CSV columns and semantics as tools/animatic.load_beats) plus word-level timestamps."""
import csv, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BEAT_CSV = os.path.join(ROOT, 'narration', 'NARRATION_BEAT_MAP.csv')
WORDS_JSON = os.path.join(ROOT, 'narration', 'WORD_TIMESTAMPS.json')
# Official take since 2026-11-26 10:39 (V2, 95.39 s, same 245 words). V1 (92.53 s, narration/raw/) is historical.
MASTER_WAV = os.path.join(ROOT, 'narration', 'raw_v2', 'SLOT07_NARRATION_V2_RAW.wav')   # read-only: never written to
MASTER_DURATION = 95.39
V1_WORDS_JSON = os.path.join(ROOT, 'narration', 'v1_historical', 'WORD_TIMESTAMPS.json')


class Narration:
    def __init__(self):
        rows = list(csv.DictReader(open(BEAT_CSV)))
        self.beats = {}
        for i, r in enumerate(rows):
            s = float(r['start_s'])
            self.beats[r['id']] = dict(id=r['id'], start=s, end=float(r['end_s']), anchor=float(r['anchor_s']),
                                       anchor_word=r['anchor_word'], text=r['spoken_text'], first=int(r['first_word']),
                                       last=int(r['last_word']), reveal=r['reveal_opportunity'])
        j = json.load(open(WORDS_JSON))
        self.words = j['words']; self.phrases = j['phrases']; self.meta = j['meta']
        assert abs(self.meta['duration'] - MASTER_DURATION) < 1e-6
        # v1 -> v2 time warp: piecewise-linear through matching word edges (identical word lists, checked)
        v1 = json.load(open(V1_WORDS_JSON))['words']
        assert [w['word'].strip('.,?!').lower() for w in v1] == [w['word'].strip('.,?!').lower() for w in self.words]
        pts = sorted({(0.0, 0.0)} | {(a[k], b[k]) for a, b in zip(v1, self.words) for k in ('start', 'end')} |
                     {(92.53, MASTER_DURATION)})
        self._x = [p[0] for p in pts]; self._y = [p[1] for p in pts]

    def v1(self, t):
        """Map a time written against the V1 (92.53 s) take to the same spoken moment in the official take.
        Used for hand-set cues (clip starts, pauses) that are not a word index; word-indexed cues need no remap."""
        import numpy as np
        return float(np.interp(t, self._x, self._y))

    def beat(self, bid): return self.beats[bid]
    def anchor(self, bid): return self.beats[bid]['anchor']
    def start(self, bid): return self.beats[bid]['start']
    def end(self, bid): return self.beats[bid]['end']
    def w(self, i): return self.words[i]
    def ws(self, i): return self.words[i]['start']          # word start (narration_t)
    def we(self, i): return self.words[i]['end']
    def find(self, text, near):
        """index of the word `text` closest to narration time `near` (for self-documenting cues)."""
        c = [w for w in self.words if w['word'].strip('.,?!').lower() == text.lower()]
        return min(c, key=lambda w: abs(w['start'] - near))['i']
    def phrase_at(self, t, lead=0.05, tail=0.45):
        for p in self.phrases:
            if p['start'] - lead <= t <= p['end'] + tail: return p
        return None

NAR = Narration()
