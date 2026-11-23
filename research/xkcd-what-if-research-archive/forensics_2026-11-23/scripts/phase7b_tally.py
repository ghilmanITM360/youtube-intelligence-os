"""Phase 7b coding (manual, scheme v1.1 = v1 + TITLE, EQUATION, SCENE declared before viewing) and tallies.
v1-equivalent mapping for comparison with the 47-frame set: TITLE->LABEL, EQUATION->LABEL, SCENE->MECH."""
import csv
from collections import Counter
F=list(csv.DictReader(open('07b_SAMPLE_FRAMES.csv')))
c='''LABEL YES NONE 0|LABEL NA NONE 0 fragment only "meters per second"|SBS YES NONE 0|TITLE PARTIAL NONE 0 logo card since 2003; 400 million not shown|SBS YES NONE 0|LABEL YES NONE 0 time stamp T=60 ns
|AXIS PARTIAL PRESENTER 1 log scale with named landmarks, no numerals|AXIS PARTIAL NONE 1 chart with named points|MECH PARTIAL SCALE 0 2 m and 7 cm shown; billionth not; tiny people at pool edge|SCENE NA NONE 0 date only|SCENE NO NONE 0 2000 years not shown|MAP YES NONE 1 2 km as -2000 m
|LABEL YES NONE 0 ~100 population|EQUATION PARTIAL PRESENTER 0 2500 kcal/day shown; 50 kg not|LABEL YES NONE 0 150,000/DAY|SCENE NO NONE 0 wages not shown|LABEL YES NONE 1 1000 km/h|LABEL PARTIAL NONE 0 95 min shown; 40 min longer not
|AXIS PARTIAL NONE 1 log ns axis, arrow at 1|EQUATION YES PRESENTER 0 1 ns = 1,000,000 fs|SCENE NA NONE 1 no quantity|EQUATION YES PRESENTER 1 574 MW|SCENE NA NONE 0 year only|LABEL NO PRESENTER 0 20 years not shown; $20 billion shown
|SCALEREF YES SCALE 0 1 m bracket|SCENE NA NONE 0 no quantity|AXIS PARTIAL NONE 0 magnitude 15 shown; million times not|AXIS YES NONE 0 magnitude 0 on axis|LABEL PARTIAL NONE 1 1,000,000 shown; 6 m not|SCALEREF YES NONE 1 1 m cable bracket
|LABEL YES NONE 0 470 m/s (1040 mph); spoken number cut off in ASR|MAP NO NONE 0 plain world map|LABEL YES NONE 0 10^44 W|SBS YES NONE 1 10^44 W vs 2e24 W|OBJ NA NONE 0 document cover; page number only|MECH YES PRESENTER 0 cfs figures
|LABEL YES NONE 1 ~$10 trillion|SCENE NO NONE 0 21 people not shown; 1919 and 15 m shown|SBS YES NONE 1 9.17 vs 1.36 kW/m2|MECH NA NONE 1 3D position; no quantity'''.replace('\n','|').split('|'); c=[x for x in c if x.strip()]
assert len(c)==len(F)==40,(len(c),len(F))
rows=[]
for f,x in zip(F,c):
    p=x.split(' ',4); rows.append({**f,'device':p[0],'spoken_qty_restated':p[1],'human_role':p[2],'red_accent':p[3],'note':p[4] if len(p)>4 else ''})
with open('07b_SCIENCE_VISUAL_CODING_20LONG.csv','w',newline='') as o:
    w=csv.DictWriter(o,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
MAP={'TITLE':'LABEL','EQUATION':'LABEL','SCENE':'MECH'}
def rep(name,R,v1=False):
    q=[r for r in R if r['spoken_qty_restated']!='NA']
    d=Counter((MAP.get(r['device'],r['device']) if v1 else r['device']) for r in R)
    print(name,len(R),'frames |',dict(d.most_common()),'| qty',len(q),dict(Counter(r['spoken_qty_restated'] for r in q)),'| human',dict(Counter(r['human_role'] for r in R)),'| red',sum(int(r['red_accent']) for r in R))
old=list(csv.DictReader(open('07_SCIENCE_VISUAL_CODING_SAMPLE.csv')))+list(csv.DictReader(open('07_SCIENCE_VISUAL_CODING_HOLDOUT.csv')))
rep('7b v1.1',rows); rep('7b v1-equiv',rows,True); rep('first47 v1',old); rep('pooled87 v1-equiv',old+rows,True)
print('videos in 7b',len({r['video_id'] for r in rows}))
