import csv,datetime as dt,os,json
A=os.path.expanduser('~/Documents/YIOS-local-audits/2026-11-23-what-if-topic-cadence-deep-audit')
W=dict(O=20,P=15,S=20,F=15,V=10,E=10,C=10)  # originality/saturation, packaging, science clarity, production feasibility, visual explainability, evergreen, channel fit
# id,title,orig_slot,family,fmt,(O,P,S,F,V,E,C),confidence,decision,demand,counter,evidence
C=[
('WIB-36','Does a Higher Fall Hit Harder? Speed just before landing from 1 km vs the edge of space','D1 long; D2 Short excerpt','Falling physics','Long',(1,3,2,3,3,3,3),'Medium','KEEP WITH REVISED PACKAGING','promising (evergreen; generic terminal-velocity topic crowded)','Generic terminal-velocity/Red Bull Stratos coverage is deep; "204 vs 204" depends on one fixed drag value shared by all audits','SE:WIB-36; SC:fall; TR:terminal velocity; XB:WIB-36 (book unit is longest free fall, not this reframe)'),
('WIB-17','Could you jump into orbit on a tiny world? (radius 2.4-4.8 km by assumption)','D15 long; D19 Short','Scale/POV','Long',(2,3,3,3,3,3,3),'Medium','MOVE EARLIER','promising (near-premise videos exist, exact "orbit by jumping" not seen)','Printed book chapter (pp.117-121) is the same question; terrain/clearance caveat','SE:WIB-17; SC:orbit; XB:WIB-17; TR:orbital velocity'),
('WIB-55','Neutron-star pellet: what would 0.7 cm3 weigh if magically held together (190-700 million tonnes)','D3 long; D4 Short','Scale/POV','Long',(2,3,2,2,3,3,3),'Medium','KEEP WITH REVISED PACKAGING','promising (teaspoon-of-neutron-star facts widespread; "bullet" framing unusual)','Both prior audits said HOLD; firearm framing may hurt ad suitability (bank flagged); mass is only a range','SE:WIB-55; SC:neutron; XB:WIB-55; TR:neutron star'),
('NEWC-voyager','Why does a reply to Voyager 1 take two days? (one light-day, reached 2026-11-18)','new','Timeline/ops','Short',(1,3,3,2,2,1,3),'Medium','KEEP','promising short-term (Trends web last-4-wk mean 46 vs 12-mo mean 15 [OBS]); news peak already passing','Dozens of Voyager light-day videos in the last week; by launch the news hook is stale','SE:NEWC-voyager; TR:voyager 1; WS:NASA light-day (search-confirmed)'),
('WIB-52','Farthest any human has been from every other human (Worden 3,596.4 km, Apollo 15)','D25 long; D28 Short','Record/geometry','Short',(2,2,3,3,2,3,3),'Medium','KEEP WITH REVISED PACKAGING','uncertain-promising','"Loneliest" is dominated by Voyager 1 results; three different distance records must not be mixed; one-line calc fits a Short better than a long','SE:WIB-52; WS:Guinness (search-confirmed)'),
('WIB-22','What could aliens detect of Earth? (instrument-specific premise)','D8 long; D10 Short','Every-X ladder','Long',(1,3,1,2,2,3,3),'Low','MOVE LATER','promising (many "what aliens see" titles this month)','Original 10/100/10,000 ly framing is not a detectability statement; needs named instrument+noise; book chapter 141-145 is the same question','SE:WIB-22; XB:WIB-22'),
('WIB-24','What if you flew a small plane on other worlds (lift per planet)','D22 long; D26 Short','Every-X ladder','Long',(2,2,2,1,3,3,3),'Low','MOVE LATER','weak-uncertain (original grade C)','Titan "fly with arms" video exists; Mars helicopter well covered','SE:WIB-24; XB:WIB-24'),
('T-01','What will Apophis look like on 13 April 2029? (31.6k km, no impact)','D6 Short','Timeline','Short',(1,2,3,2,3,1,2),'Low','MOVE LATER','uncertain (heavy Apophis coverage incl. sensational titles)','Several "what you will see on April 13 2029" titles already (today filter)','SE:T-01; TR:apophis; WS:JPL/NASA (search-confirmed)'),
('NEW-07','Falling into Jupiter: what Galileo probe actually measured (Short)','D27 Short','Scale/POV','Short',(0,2,2,2,3,3,3),'Medium','KEEP WITH REVISED PACKAGING','promising but crowded','"What if you fell into Jupiter" has many exact-title copies (all-time and this month)','SE:NEW-07; TR:jupiter'),
('NEW-06','What if the Moon vanished tonight (generic)','D5 long; D9 Short','Timeline','Long',(0,2,1,2,2,3,2),'Medium','REPLACE','strong-but-saturated','>=10 near-identical titles in the last month/week [OBS titles]; any rework needs a distinct single-coast tide question','SE:NEW-06; TR:moon tides'),
('NEW-08','What if light were as slow as a car (100 km/h)','D11 long; D16 Short','Runaway','Long',(0,3,2,2,3,3,2),'Medium','REPLACE','strong-but-saturated','>=10 near-identical "light 100 km/h" titles this month; prior art Gamow 1940, MIT Game Lab','SE:NEW-08; TR:speed of light'),
('WIB-11','Which light goes out last after humans vanish','D18 long; D23 Short','Timeline','Long',(0,3,2,2,2,3,2),'High','REPLACE','n/a','xkcd already made this exact question (book unit MADE, video 2024-05-28 reported)','XB:WIB-11'),
('WIB-18','Drop a steak from space to cook it','D13 Short','Every-X ladder','Short',(0,3,2,2,2,3,2),'Medium','REPLACE','saturated','>=6 near-exact all-time results ("Could you cook a steak by dropping it from space")','SE:WIB-18; XB:WIB-18'),
('WIB-53','A whole storm as one raindrop','D20 Short','One-off calc','Short',(0,2,2,2,2,3,2),'Medium','REPLACE','saturated','>=8 near-identical titles this month','SE:WIB-53; XB:WIB-53'),
('SLOT-D29','Day-29 winner slot (decided by Day-14 family ranking)','D29 long','winner','Long',None,'n/a','NEEDS MORE DATA','n/a','Day-14 rule cannot pick a family from n=1-3; treat as reserve, not an exploitation slot','n/a'),
('NEWC-shadow','Can you see Earth\'s shadow after sunset? (Belt of Venus)','new (prior audit 2)','Everyday observation','Short',(2,2,3,3,3,3,2),'Low','KEEP','uncertain','No search depth on exact premise; weather/hemisphere dependent','SE:NEWC-shadow'),
('NEWC-laser','How long does a laser echo from the Moon take (lunar ranging)','new (prior audit 2)','Measurement','Short',(2,2,3,3,2,3,2),'Low','KEEP','uncertain','Needs careful retroreflector/round-trip framing','SE:NEWC-laser'),
('NEWC-mars-heli','Could the Mars helicopter fly on Earth?','new (prior audit 2)','Engineering','Long',(1,2,2,1,3,2,3),'Low','NEEDS MORE DATA','uncertain','Heavy Mars-helicopter coverage; airframe/rotor model unverified','SE:NEWC-mars-heli'),
('KETTLE','Can the same kettle boil at two temperatures? (pressure)','new (prior audit 2)','Everyday physics','Long',(2,2,3,2,3,3,2),'Low','NEEDS MORE DATA','unknown (no YouTube search run)','No evidence collected this audit beyond a Trends term','TR:kettle'),
('CLOCK','Can Earth\'s rotation add a second to your clock? (UTC/UT1)','new (prior audit 2)','Everyday physics','Short',(2,2,2,3,2,3,2),'Low','NEEDS MORE DATA','unknown','Not searched','n/a'),
('WIB-30/32/34','Highest a human can throw / fastest survivable speed bump / slow re-entry with rockets (book "A" tier, unused as videos)','discovery from question bank','various','Long',None,'Low','NEEDS MORE DATA','unknown','No live evidence collected; same book-adaptation collision caveat','XB:question_bank'),
]
rows=[]
for cid,t,slot,fam,fmt,sc,conf,dec,dem,ctr,ev in C:
    if sc: tot=round(sum(W[k]*v/3 for k,v in zip('OPSFVEC',sc)))
    else: tot='UNSCORED'
    rows.append(dict(candidate_id=cid,working_title=t,original_slot=slot,family=fam,proposed_format=fmt,score_O_P_S_F_V_E_C=' '.join(map(str,sc)) if sc else '',weights='O20 P15 S20 F15 V10 E10 C10',total_0_100=tot,confidence=conf,decision=dec,demand_outlook=dem,counterargument=ctr,evidence_ids=ev,score_note='0-3 per dimension, subjective editorial judgement; demand excluded from total'))
w=csv.DictWriter(open(A+'/TOPIC_RESEARCH_CANDIDATES.csv','w',newline='',encoding='utf-8'),fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
for r in rows: print(r['candidate_id'],r['total_0_100'],r['decision'])
# --- 60-day plan (conditional anchor Mon 2026-12-07) ---
start=dt.date(2026,12,7)
P={1:('Long','WIB-36','Does a higher fall hit harder? (speed just before landing)','Falling physics','Only item with approved script v3 + fact-check + thumbnail; gate on drag-model second check','Kettle if science gate unresolved; else slip'),
5:('Short','NEWC-voyager','Why does a reply to Voyager 1 take two days?','Timeline/ops','Cheap Short; time hook partly gone, evergreen angle','skip'),
8:('Short','EX-WIB-36','Excerpt: why you slow down before you hit the ground','Falling physics','Excerpt after parent; test excerpt vs standalone','skip first'),
11:('Long','WIB-17','Could you jump into orbit on a tiny world?','Scale/POV','Second family (S); strong visual; different from falling','WIB-55'),
14:('Evaluation','-','Day-14 diagnostic (72h/7d reads for D1 long; D11 long only at 72h exactly)','-','Do not pick a winning family from n=1-2','-'),
15:('Short','WIB-52','Farthest any human has been from everyone else (3,596.4 km)','Record/geometry','Standalone Short; separate three distance records','NEWC-shadow'),
21:('Long','WIB-55','Neutron-star pellet: weight of 0.7 cm3 if held together','Scale/POV','After science scoping (density range, confinement stated)','WIB-24'),
25:('Short','EX-WIB-17','Excerpt: why you could not walk normally on a tiny world','Scale/POV','Excerpt after parent','skip'),
30:('Evaluation','-','Day-30 diagnostic (L1, L2 at 72h+7d; L3 at 7d)','-','Keep immature cohorts open','-'),
31:('Long','WIB-22','What could aliens detect of Earth? (instrument-specific)','Every-X ladder','Needs named-instrument premise; reviewed science','WIB-24'),
35:('Short','NEWC-shadow','Can you see Earth\'s shadow after sunset?','Everyday observation','Everyday-observation test','NEWC-laser'),
41:('Long','WIB-24','What if you flew a small plane on other worlds?','Every-X ladder','Low demand grade; ladder gap; second ladder test after aliens','KETTLE (needs data)'),
45:('Short','NEWC-laser','How long does a laser echo from the Moon take?','Measurement','Standalone Short','CLOCK (needs data)'),
51:('Long','RESERVE','Reserve long: best-supported unused candidate after Day-30 review (default KETTLE or NEWC-mars-heli once researched)','-','Replaces the Day-29 exploitation rule','slip'),
55:('Short','EX-WIB-55','Excerpt: if something held it together and you dropped it (state assumption)','Scale/POV','Excerpt; SIMULATION label','skip'),
58:('Short','T-01','What will Apophis look like on 13 April 2029?','Timeline','Standalone Short; crowded topic, tests packaging','skip'),
60:('Evaluation','-','Day-60 diagnostic: all longs have 7d; D51 long 9d','-','Re-rank; add data','-')}
sched=[]
for d in range(1,61):
    dd=start+dt.timedelta(days=d-1); p=P.get(d)
    sched.append(dict(seq_day=d,date_conditional=dd.isoformat(),weekday=dd.strftime('%a'),type=p[0] if p else 'Production / rest',id=p[1] if p else '',working_title=p[2] if p else '',family=p[3] if p else '',reason=p[4] if p else '',fallback=p[5] if p else ''))
w=csv.DictWriter(open(A+'/PROPOSED_60_DAY_ORDER.csv','w',newline='',encoding='utf-8'),fieldnames=list(sched[0]));w.writeheader();w.writerows(sched)
import collections;print(collections.Counter(s['type'] for s in sched))
json.dump(sched,open(A+'/raw/sched.json','w'))
