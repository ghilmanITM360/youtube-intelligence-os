"""Structural checks for the deliverables. Run from anywhere: python3 scripts/validate_outputs.py
Checks: files exist; CSVs parse with constant column counts; 10 slots (days 1,4,...,28) in crosswalk and ledger; every claim ID cited in a
blueprint exists in the ledger; every SRC id cited in the ledger/blueprints exists in the register; ledger status values come from the allowed set
(none says VERIFIED); blueprints contain sections A-J and a STATUS line; blueprints do not carry the phrases SCIENCE VERIFIED / READY FOR PUBLICATION
as a status; key numbers in the ledger match scripts/output/fall_results.csv. STRUCTURAL ONLY: it cannot judge science or originality."""
import csv, os, re, sys, glob
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=lambda *a: os.path.join(ROOT,*a)
errs=[]; ok=[]
def need(c,msg): (ok if c else errs).append(msg)
req=["00_MASTER_DIRECTIVE.md","01_RULES_AND_SUCCESS_CRITERIA.md","02_PROGRESS_CHECKPOINT.md","03_SOURCE_REGISTER.csv","04_OPEN_QUESTIONS_AND_DECISIONS.md","05_EXISTING_RESEARCH_AND_REFERENCE_MAP.md","06_TEN_VIDEO_REFERENCE_AND_ORIGINALITY_CROSSWALK.csv","07_CLAIM_AND_SOURCE_LEDGER.csv","08_CALCULATIONS_AND_ASSUMPTIONS.md","09_CALENDAR_COHERENCE_AND_DEPENDENCIES.md","10_SELF_REVIEW_AND_OPEN_ISSUES.md","START_HERE.md"]
for f in req: need(os.path.exists(P(f)),f"exists {f}")
BP=["01_LONG_HIGHER_FALL","02_SHORT_SKYDIVER_SLOWDOWN","03_SHORT_VOYAGER_SIGNAL","04_LONG_TINY_WORLD_ORBIT","05_SHORT_PHOBOS_ESCAPE","06_LONG_VOYAGER_REPLY","07_SHORT_LUNAR_LASER","08_LONG_MOON_OCEAN","09_SHORT_SOLAR_TIDES","10_SHORT_FARTHEST_HUMAN"]
for b in BP: need(os.path.exists(P("blueprints",b+".md")),f"exists blueprints/{b}.md")
def load(f):
    rows=list(csv.reader(open(P(f),encoding="utf-8"))); n=len(rows[0]); bad=[i for i,r in enumerate(rows) if len(r)!=n]
    need(not bad,f"{f}: constant column count ({n}), bad rows {bad}"); return rows[0],rows[1:]
h3,r3=load("03_SOURCE_REGISTER.csv"); h6,r6=load("06_TEN_VIDEO_REFERENCE_AND_ORIGINALITY_CROSSWALK.csv"); h7,r7=load("07_CLAIM_AND_SOURCE_LEDGER.csv")
src={r[0] for r in r3}; ids=[r[0] for r in r7]; claimset=set(ids)
need(len(ids)==len(claimset),"ledger claim ids unique")
need(sorted(int(r[0]) for r in r6)==list(range(1,11)),"crosswalk has slots 1..10")
need([int(r[1]) for r in r6]==[1,4,7,10,13,16,19,22,25,28],"crosswalk calendar days 1,4,...,28")
slots={r[1] for r in r7 if r[1].isdigit()}; need(slots=={str(i) for i in range(1,11)},"ledger covers slots 1..10")
allowed={"SOURCE_READ_EXTRACT","COMPUTED_SELF","ASSUMPTION","BOOK_CLAIM_READ_OCR","SNIPPET_ONLY","SECONDARY_ONLY","RECALLED_NOT_SOURCED","OPEN_HOLD"}
need(all(r[11] in allowed for r in r7),"ledger statuses in allowed set: "+str(sorted({r[11] for r in r7}-allowed)))
need(not any("VERIFIED" in r[11].upper() for r in r7),"no ledger status says VERIFIED")
cited=set()
for r in r7:
    for s in re.findall(r"SRC-\d+",r[4]): cited.add(s)
need(cited<=src,"ledger SRC ids resolve; missing "+str(sorted(cited-src)))
tok=re.compile(r"\b(?:V\d{2}-C\d{2}|NS-\d{2})\b")
for b in BP:
    t=open(P("blueprints",b+".md"),encoding="utf-8").read()
    need("STATUS:" in t[:400],f"{b}: STATUS line")
    need(all(re.search(rf"^## {L}\. ",t,re.M) for L in "ABCDEFGHIJ"),f"{b}: sections A-J")
    c=set(tok.findall(t)); miss=sorted(c-claimset); need(not miss,f"{b}: {len(c)} claim ids resolve; missing {miss}")
    ss=set(re.findall(r"SRC-\d+",t)); need(ss<=src,f"{b}: SRC ids resolve; missing {sorted(ss-src)}")
    need("SELF-REVIEW" in t,f"{b}: labelled SELF-REVIEW")
    need(not re.search(r"STATUS:[^\n]*(SCIENCE VERIFIED|READY FOR PUBLICATION)",t),f"{b}: no forbidden status words")
    need(bool(re.search(r"BLUEPRINT READY FOR OWNER REVIEW|PARTIAL — NEEDS SOURCE/CALCULATION|BLOCKED — MATERIAL SCIENCE OR PREMISE UNRESOLVED",t[:600])),f"{b}: status uses an allowed phrase")
# key numbers vs script output
fr=list(csv.DictReader(open(P("scripts","output","fall_results.csv"))))
def g(s,h,k): return float([r for r in fr if r["set"].startswith(s) and r["h0_m"]==str(h)][0][k])
need(abs(g("B_",100000,"ground_kmh")-189.0)<0.2 and abs(g("B_",1000,"ground_kmh")-188.8)<0.2,"ledger V01-C01/C02 (189.0 / 188.8 km/h) matches fall_results.csv")
need(abs(g("A_",100000,"ground_kmh")-204.3)<0.2,"ledger A-set landing 204.3 matches")
need(abs(g("B_",39000,"peak_kmh")-1315)<2,"B-set 39 km peak 1,315 km/h matches")
print("\n".join("OK   "+m for m in ok)); print("\n".join("FAIL "+m for m in errs)); print(f"\n{len(ok)} passed, {len(errs)} failed"); sys.exit(1 if errs else 0)
