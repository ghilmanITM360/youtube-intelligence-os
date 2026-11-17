"""Which parent ¶ (or 40-word chunk for unpunctuated captions) a derived Short reuses.
A unit counts as reused when >50% of its 6-grams appear in the Short.
  python3 reuse.py V011 V033 [V0xx ...]
"""
import re, sys, locate
def g(t, n=6):
    w = re.findall(r"[a-z0-9']+", t.lower()); return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}
def reuse(parent, short):
    P = locate.paras(parent)
    if len(P) < 8:  # unpunctuated: fall back to 40-word chunks
        W = locate.words(parent); units = [(f"w{i+1}-{min(i+40, len(W))}", " ".join(W[i:i+40])) for i in range(0, len(W), 40)]
    else:
        units = [(f"¶{i}", p) for i, p in enumerate(P, 1)]
    S = g(" ".join(locate.paras(short)))
    return [lab for lab, u in units if g(u) and len(g(u) & S) / len(g(u)) > .5]
if __name__ == "__main__":
    for s in sys.argv[2:]: print(sys.argv[1], s, reuse(sys.argv[1], s))
