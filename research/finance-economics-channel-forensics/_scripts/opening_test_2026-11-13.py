"""Opening-style vs views test. Input: _analysis/openings_tiered_2026-11-13.csv (from opening_dump). Rule-based labels (INFERRED, not human-blind).
STAKE = first 30 words contain a digit/$/%/year/'trillion|billion|million' and no persona/template start.
PERSONA = starts with persona/template: 'This is <Name>', 'Meet', '<Name> is <age>', 'Close your eyes', 'Monkey ...', 'What is/are', 'Let me ask', 'Ah,'.
OTHER = everything else (generic statement/question)."""
import csv,re,collections,statistics as st,sys
rows=list(csv.DictReader(open("../_analysis/openings_tiered_2026-11-13.csv")))
PERS=re.compile(r"^(This is [A-Z]|Meet |[A-Z][a-z]+ is \d|Close your eyes|Monkey|What (is|are) |Let me ask|Ah,|If monkeys|Uh)")
NUM=re.compile(r"(\d|\$|%|trillion|billion|million)",re.I)
def lab(t):
    t=t.strip(); w=" ".join(t.split()[:30])
    if PERS.match(t): return "PERSONA"
    return "STAKE" if NUM.search(w) else "OTHER"
for r in rows: r["lab"]=lab(r["opening_150w"]); r["v"]=int(r["views"] or 0)
med={c:st.median([r["v"] for r in rows if r["channel"]==c]) for c in {r["channel"] for r in rows}}
for r in rows: r["rel"]=r["v"]/med[r["channel"]]
csv.DictWriter(open("../_analysis/openings_labeled_2026-11-13.csv","w",newline=""),fieldnames=[k for k in rows[0]]).writeheader()
w=csv.DictWriter(open("../_analysis/openings_labeled_2026-11-13.csv","w",newline=""),fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def tab(sub,name):
    print(f"\n{name}: n={len(sub)}")
    print("label    n  strong weak mid  median(views/channel-median)")
    for l in ("STAKE","PERSONA","OTHER"):
        s=[r for r in sub if r["lab"]==l]
        if s: print(f"{l:8} {len(s):3} {sum(r['tier']=='S' for r in s):4} {sum(r['tier']=='W' for r in s):4} {sum(r['tier']=='M' for r in s):4}  {st.median(r['rel'] for r in s):.2f}")
for c in sorted(med): tab([r for r in rows if r["channel"]==c],c)
tab(rows,"POOLED")
import random,math
random.seed(7)
def stat(rs):
    a=[math.log(r["rel"]) for r in rs if r["lab"]=="STAKE"]; b=[math.log(r["rel"]) for r in rs if r["lab"]!="STAKE"]
    return st.mean(a)-st.mean(b)
def perm(rs,n=5000):
    obs=stat(rs); by=collections.defaultdict(list)
    for r in rs: by[r["channel"]].append(r)
    labs={c:[r["lab"] for r in v] for c,v in by.items()}; hit=0
    for _ in range(n):
        for c,v in by.items():
            l=labs[c][:]; random.shuffle(l)
            for r,x in zip(v,l): r["_l"]=x
        a=[math.log(r["rel"]) for r in rs if r["_l"]=="STAKE"]; b=[math.log(r["rel"]) for r in rs if r["_l"]!="STAKE"]
        hit+= (st.mean(a)-st.mean(b))>=obs
    return obs,hit/n
print("\nPermutation (labels shuffled within channel), mean log(rel views) STAKE minus not-STAKE, one-sided:")
print("all 7 channels:",perm(rows))
print("without Monkey (all PERSONA template):",perm([r for r in rows if r["channel"]!="024 Monkey"]))
for c in sorted(med):
    rs=[r for r in rows if r["channel"]==c]
    if len({r["lab"]=="STAKE" for r in rs})==2: print(c,perm(rs,2000))
