"""Paragraph locators (¶N) for the What If? script files.
¶N = the Nth blank-line-separated paragraph under '## Script' in the VID's script file.
  python3 locate.py V001 5 9        -> print ¶5 and ¶9
  python3 locate.py V001 find Hubble -> ¶ numbers containing the text
  python3 locate.py V003 w 120 160   -> words 120-160 (for unpunctuated auto-captions)
  python3 locate.py V003 wfind fighter pilots -> word index of each match
  python3 locate.py check            -> every ¶N / wA-B cited in audits/*.md exists
wA-B = 1-based word positions in the script text (same words as the raw transcript).
"""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
INV = {r["vid"]: r for r in json.loads((HERE / "inventory.json").read_text())}

def paras(vid):
    t = (HERE.parent / INV[vid]["script"]).read_text().split("## Script\n", 1)[1]
    return [p for p in t.split("\n\n") if p.strip()]

def words(vid):
    return " ".join(paras(vid)).split()

def check():
    bad = 0
    for f in sorted((HERE / "audits").glob("V*.md")):
        for v, m in re.findall(r"(?:(V\d{3}) )?¶(\d+)", f.read_text()):  # "V002 ¶5" = another video's ¶
            n = len(paras(v or f.stem))
            if not 1 <= int(m) <= n:
                print(f"{f.name}: {v or f.stem} ¶{m} out of range (1-{n})"); bad += 1
        for v, a, b in re.findall(r"(?:(V\d{3}) )?\bw(\d+)(?:[-–](\d+))?\b", f.read_text()):  # w5, w2–33, "V003 w311–400"
            nw = len(words(v or f.stem)); b = b or a
            if not 1 <= int(a) <= int(b) <= nw:
                print(f"{f.name}: {v or f.stem} w{a}-{b} out of range (1-{nw})"); bad += 1
    print("locator check:", "FAIL" if bad else "ok"); return bad

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "check": sys.exit(check())
    if a[1] == "w":
        W = words(a[0]); print(" ".join(W[int(a[2]) - 1:int(a[3])])); sys.exit()
    if a[1] == "wfind":
        norm = lambda x: re.sub(r"[^a-z0-9']", "", x.lower()); W = [norm(w) for w in words(a[0])]; q = [norm(x) for x in " ".join(a[2:]).split()]
        print([i + 1 for i in range(len(W)) if W[i:i + len(q)] == q], "of", len(W)); sys.exit()
    P = paras(a[0])
    if a[1] == "find":
        q = " ".join(a[2:]).lower(); print([i for i, p in enumerate(P, 1) if q in p.lower()], "of", len(P))
    else:
        for i in map(int, a[1:]): print(f"¶{i}: {P[i-1]}")
