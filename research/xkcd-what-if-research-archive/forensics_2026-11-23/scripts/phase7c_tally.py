"""Phase 7c coding (manual, scheme v1.1) for 38 Short frames, and tallies vs the long-video sets (v1-equivalent mapping TITLE,EQUATION->LABEL, SCENE->MECH)."""
import csv
from collections import Counter
F=list(csv.DictReader(open('07c_SAMPLE_FRAMES.csv')))
c='''AXIS YES NONE 0 magnitude 11 on ruler; kilometres not shown
|AXIS YES NONE 0 magnitude 1 on ruler with truck and house
|OBJ NO NONE 0 building alone; lightning count not shown
|LABEL PARTIAL NONE 0 ~2000F (1100C) vs several thousand degrees
|SCENE NO NONE 0 one metre not shown
|SBS YES NONE 0 few billion per launch beside rocket
|LABEL YES NONE 0 LIMIT 4 Gs
|LABEL YES NONE 0 MAX ~1.5 km/s in the ball
|LABEL YES NONE 1 7 km/s red arrow
|MECH NO NONE 1 10 times the distance not shown
|MAP YES NONE 0 42N 42S and 85 percent of population
|SCENE NO NONE 0 spin duration not shown
|LABEL YES NONE 0 T=60 NANOSECONDS
|LABEL PARTIAL NONE 1 9.17 kW/m2 shown; nearly 10 times not in frame
|SCENE NA NONE 0 date only
|SCENE NO NONE 0 few thousand passengers not shown
|MAP UNCLEAR NONE 1 depth label caught mid-change
|SCALEREF PARTIAL NONE 1 column vs water, no numeral
|OBJ PARTIAL NONE 0 six printers drawn; hundred edits per minute not shown
|LABEL PARTIAL NONE 1 ~6000C crossed out joke label vs few thousand degrees
|MECH NO NONE 0 0.5 percent not shown
|AXIS YES NONE 0 height axis 100 m to 3 km with towers
|MECH NO NONE 1 30 km diameter not shown
|SCENE NO NONE 0 hundred feet not shown
|MECH NA NONE 1 no quantity
|MAP NO NONE 0 90 degrees not shown
|TITLE YES PRESENTER 0 question card text includes 90 degrees
|SCALEREF PARTIAL SCALE 0 YOU label and statue for size; 20 percent only implied by cap
|LABEL YES PRESENTER 0 Q >= 100,000 cfs
|SCENE NA NONE 0 year only
|EQUATION PARTIAL PRESENTER 1 9 ft and 1 ft shown; 55 mph not yet
|LABEL YES NONE 0 ~100 population
|EQUATION YES NONE 0 log2(8 billion) = 33 months
|EQUATION YES PRESENTER 1 10^53 electrons, 200,000 moles of moles
|MECH NO NONE 1 15 or 20 hours not shown
|LABEL YES NONE 1 millions of degrees
|SBS PARTIAL NONE 0 kJ labels on items; ten times not shown
|LABEL YES NONE 0 1 percent arrows and question card'''.replace('\n','|').split('|'); c=[x for x in c if x.strip()]
assert len(c)==len(F)==38,(len(c),len(F))
rows=[]
for f,x in zip(F,c):
    p=x.split(' ',4); rows.append({**f,'device':p[0],'spoken_qty_restated':p[1],'human_role':p[2],'red_accent':p[3],'note':p[4] if len(p)>4 else ''})
with open('07c_SCIENCE_VISUAL_CODING_SHORTS.csv','w',newline='') as o:
    w=csv.DictWriter(o,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
MAP={'TITLE':'LABEL','EQUATION':'LABEL','SCENE':'MECH'}
def rep(n,R,v1=False):
    q=[r for r in R if r['spoken_qty_restated']!='NA']
    print(n,len(R),dict(Counter((MAP.get(r['device'],r['device']) if v1 else r['device']) for r in R).most_common()),'| qty',len(q),dict(Counter(r['spoken_qty_restated'] for r in q)),'| human',dict(Counter(r['human_role'] for r in R)),'| red',sum(int(r['red_accent']) for r in R))
long87=list(csv.DictReader(open('07_SCIENCE_VISUAL_CODING_SAMPLE.csv')))+list(csv.DictReader(open('07_SCIENCE_VISUAL_CODING_HOLDOUT.csv')))+list(csv.DictReader(open('07b_SCIENCE_VISUAL_CODING_20LONG.csv')))
rep('shorts v1.1',rows); rep('shorts v1-equiv',rows,True); rep('long87 v1-equiv',long87,True); rep('all125 v1-equiv',long87+rows,True)
print('asr source',Counter(r['asr_source'] for r in rows))
