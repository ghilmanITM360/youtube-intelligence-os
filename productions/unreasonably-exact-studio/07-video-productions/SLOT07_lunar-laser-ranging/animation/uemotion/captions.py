"""Caption renderer: phrase-level lines inside the caption safe band, word-level highlight from WORD_TIMESTAMPS.json
(word edges are an ESTIMATE of +-0.12 s per the file's own meta: highlights are therefore never used to judge sync tighter than that)."""
from . import tokens as T
from .narration import NAR
from .easing import seg, smoothstep

class CaptionRenderer:
    def __init__(self, nar=NAR, size=52, box=T.CAPTION_BOX, max_w=900):
        self.nar, self.size, self.box, self.max_w = nar, size, box, max_w

    def wrap(self, cv, words):
        """greedy wrap, then re-balance two-line captions so no single word is left alone on line 2."""
        sp = cv.text_width(' ', self.size, bold=True); ws = [cv.text_width(w['word'], self.size, bold=True) for w in words]
        def width(i, j): return sum(ws[i:j]) + sp * max(0, j - i - 1)
        if width(0, len(words)) <= self.max_w: return [[(w, x) for w, x in zip(words, ws)]]
        best = None
        for k in range(1, len(words)):                      # try every 2-line split, keep the most balanced that fits
            a_, b_ = width(0, k), width(k, len(words))
            if max(a_, b_) <= self.max_w and (best is None or max(a_, b_) < best[0]): best = (max(a_, b_), k)
        if best:
            k = best[1]; return [list(zip(words[:k], ws[:k])), list(zip(words[k:], ws[k:]))]
        lines, cur, w = [], [], 0.0
        for wd, ww in zip(words, ws):
            if cur and w + sp + ww > self.max_w: lines.append(cur); cur, w = [], 0.0
            cur.append((wd, ww)); w += ww + (sp if len(cur) > 1 else 0)
        if cur: lines.append(cur)
        return lines

    def draw(self, cv, n):
        p = self.nar.phrase_at(n)
        if p is None: return None
        a = smoothstep(seg(n, p['start'] - 0.05, p['start'] + 0.1)) * (1 - smoothstep(seg(n, p['end'] + 0.25, p['end'] + 0.45)))
        words = self.nar.words[p['first']:p['last'] + 1]; lines = self.wrap(cv, words)
        sp = cv.text_width(' ', self.size, bold=True); lh = self.size + 16
        y0 = self.box[1] + 40; active = None
        cv.rect((60, y0 - self.size * 0.95, T.DESIGN_W - 60, y0 + lh * (len(lines) - 1) + self.size * 0.95), fill=(5, 8, 20), radius=30, alpha=a * 0.55)   # scrim: legible over bright Earth
        for li, line in enumerate(lines):
            tw = sum(w for _, w in line) + sp * (len(line) - 1); x = (T.DESIGN_W - tw) / 2; y = y0 + li * lh
            for wd, ww in line:
                on = wd['start'] <= n < wd['end']; past = n >= wd['end']
                if on:
                    active = wd['i']
                    cv.rect((x - 10, y - self.size * 0.62, x + ww + 10, y + self.size * 0.62), fill=T.PANEL, outline=T.GOLD, width=2, radius=14, alpha=a * 0.95)
                col = T.WHITE if (on or past) else T.mix(T.BG, T.WHITE, 0.55)
                cv.text((x, y), wd['word'], self.size, T.GOLD if on else col, anchor='lm', bold=True, alpha=a)
                x += ww + sp
        return active
