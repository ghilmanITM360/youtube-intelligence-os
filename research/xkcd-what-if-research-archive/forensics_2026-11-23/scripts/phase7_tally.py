"""Tally Phase 7 coding. Holdout was coded AFTER the scheme was frozen (device/restate/human/red definitions in 07_SCIENCE_VISUAL_PASS.md)."""
import csv
from collections import Counter
H=list(csv.DictReader(open('07_HOLDOUT_FRAMES.csv')))
c=[('LABEL','YES','NONE',1,''),('MECH','NA','NONE',1,'qualitative comparison'),('OBJ','NA','NONE',0,'date only'),('LABEL','NA','NONE',0,'title card; scheme has no TITLE class'),
('MECH','UNCLEAR','NONE',0,'scene illustration; no SCENE class'),('LABEL','YES','PRESENTER',0,''),('LABEL','NO','NONE',0,'equation card; thousands of degrees not shown; no EQUATION class'),
('OBJ','NO','NONE',1,'200 MW not shown'),('SCALEREF','PARTIAL','NONE',1,'column vs water level, no numeral'),('MAP','NA','NONE',0,''),
('LABEL','PARTIAL','NONE',1,'240 mph and 2:05:00 shown'),('LABEL','YES','NONE',0,'formula'),('LABEL','YES','NONE',0,'~30 tons/day'),('MECH','NO','NONE',0,'scene; 50 years not shown'),
('MAP','PARTIAL','NONE',0,'latitude lines dashed, 30 deg not labelled'),('MAP','YES','NONE',0,'dashed outline of ice-sheet extent'),('OBJ','NO','PRESENTER',0,'billions not shown'),
('MECH','NO','NONE',0,'0.5 percent not shown'),('SCALEREF','YES','SCALE',0,'1 KILOMETER bracket beside figure'),('SCALEREF','YES','SCALE',0,'8 km, tiny climber vs mountains'),
('LABEL','YES','NONE',1,'millions of degrees'),('LABEL','NO','NONE',1,'single square meter not shown; energy ratios shown'),('AXIS','YES','PRESENTER',0,'ordinal FINE to HORRIBLE axis; 1/3 pound title')]
assert len(c)==len(H)==23
with open('07_SCIENCE_VISUAL_CODING_HOLDOUT.csv','w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(H[0])+['device','spoken_qty_restated','human_role','red_accent','note']); w.writeheader()
    for h,k in zip(H,c): w.writerow({**h,'device':k[0],'spoken_qty_restated':k[1],'human_role':k[2],'red_accent':k[3],'note':k[4]})
S=list(csv.DictReader(open('07_SCIENCE_VISUAL_CODING_SAMPLE.csv'))); Hh=list(csv.DictReader(open('07_SCIENCE_VISUAL_CODING_HOLDOUT.csv')))
for name,R in (('sample',S),('holdout',Hh),('combined',S+Hh)):
    q=[r for r in R if r['spoken_qty_restated']!='NA']
    print(name,len(R),'device',dict(Counter(r['device'] for r in R)),'| qty frames',len(q),dict(Counter(r['spoken_qty_restated'] for r in q)),'| human',dict(Counter(r['human_role'] for r in R)),'| red',sum(int(r['red_accent']) for r in R))
