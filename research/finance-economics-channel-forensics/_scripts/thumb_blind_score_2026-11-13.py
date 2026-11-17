"""Blind thumbnail scoring. GUESS and FEAT were typed BEFORE the key was opened (see git history / file mtime). Then unblind and score."""
import csv,os,collections
G={ # my S-guess tiles per channel (all others guessed W)
"024_Monkey":"DFJBH","037_CasualFin":"BEGHD","039_Crayon":"ABEFH","040_EconExplained":"CFGIB","055_Primate":"BCDHJ","059_CapitalCase":"AFGHJ","066_Nutshell":"FGIDE"}
# features per tile: (NUM visible number/$/%/year, NAMED real person/company/event/place, Q question) as 3-char strings, tiles A..J
F={"024_Monkey":"010 010 000 010 100 101 100 100 100 100".split(),
"037_CasualFin":"100 110 000 100 110 010 110 100 101 001".split(),
"039_Crayon":"010 110 010 110 010 010 000 010 001 010".split(),
"040_EconExplained":"001 100 010 111 010 010 000 000 000 001".split(),
"055_Primate":"000 010 000 000 000 100 000 000 000 000".split(),
"059_CapitalCase":"010 101 010 010 010 010 010 010 000 010".split(),
"066_Nutshell":"101 000 100 001 000 000 000 010 001 101".split()}
K=os.path.expanduser('~/YIOS-local-audits/finance-viral-forensics-2026-11-12/blind_2026-11-13/KEY_do_not_open_before_scoring.csv')
key=list(csv.DictReader(open(K)))
tot=[0,0]; fe=collections.defaultdict(lambda:[0,0,0,0]) # feature -> [S with,S n,W with,W n]
print("channel  correct/10  (S-guess hit)")
out=[]
for ch,g in G.items():
    ks=[r for r in key if r["channel"].replace(" ","_")==ch]
    ok=0
    for r in ks:
        i=ord(r["tile"])-65; guess="S" if r["tile"] in g else "W"; ok+=guess==r["grp"]
        for j,nm in enumerate(("NUM","NAMED","Q")):
            a=fe[nm]; k=0 if r["grp"]=="S" else 2; a[k]+=int(F[ch][i][j]); a[k+1]+=1
        out.append(dict(r,guess=guess,feat=F[ch][i]))
    print(ch,ok,"/10"); tot[0]+=ok; tot[1]+=10
print("TOTAL",tot, "chance=35/70")
for nm,a in fe.items(): print(nm,f"strong {a[0]}/{a[1]}  weak {a[2]}/{a[3]}")
w=csv.DictWriter(open("_analysis/thumb_blind_scored_2026-11-13.csv","w",newline=""),fieldnames=list(out[0]));w.writeheader();w.writerows(out)
