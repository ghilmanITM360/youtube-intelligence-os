"""Static authored asset/scene factory. --scene writes one completed narrative group.
No animation code: states are illustrations for review, not evaluated frame keyframes.
"""
from pathlib import Path
import argparse,base64,csv,hashlib,json,xml.etree.ElementTree as ET
import pen_art as a
R=a.ROOT;A=R/'assets';M=R/'manifests';SPECS={};SCENES={}
CATEGORIES={'characters','supporting_characters','props','environments','diagrams','evidence_overlays'}
REFS={
1:'REF09 / 2EZzwupIa80 S007.2 51.80s paper grip; REF11 / rSa2aziEsAI S010.9 46.21s institutional/rate composition',
2:'REF03 / rSa2aziEsAI M0027 38.7333-39.6997s note entrance; REF08 / 0ll9rEtoRrs S003.1-S003.3 9.76-10.78s additive paper',
3:'VISUAL_DNA / -X6YzlY_8tM 169-189s sequential numerical comparisons; REF05 M0047 30.375-32.750s isolated paper scale',
4:'VISUAL_DNA / 0ll9rEtoRrs 75-225s bond/payment metaphor; MOTION_DNA persistent additive financial explanations',
5:'REF09 / 2EZzwupIa80 S005.2-S005.6 32.54-35.61s and S006.1 44.75s actual source/highlight',
6:'REF09 / 2EZzwupIa80 S007.2 51.80s paper personification; VISUAL_DNA simple institutional finance props',
7:'SHORTS_DNA / rSa2aziEsAI ending yen/debt tradeoff; REF02 / -X6YzlY_8tM S018.9/S018.12 190.18/194.67s expression switch',
}
def spec(ident,cat,body,w,h,base=None,classification='ORIGINAL_DRAWING',anchors=None,source='Original authored paths; approved V2 identity retained'):
 SPECS[ident]={'asset_id':ident,'category':cat,'body':body,'width':w,'height':h,'base_id':base or ident,'classification':classification,'anchors':anchors or {'pivot':[w/2,h/2]},'provenance':source}
for ident,pose,expr,upper in [('HOST_NEUTRAL','STAND','NEUTRAL',False),('HOST_POINT','POINT','EXPLAIN',False),('HOST_BILL','BILL','WOW',False),('HOST_CONCERNED','STAND','WORRIED',False),('HOST_UP','UP','EXPLAIN',False),('HOST_OPEN','OPEN','EXPLAIN',False),('HOST_THINK','THINK','THINK',False),('HOST_POINT_LEFT','LEFT','EXPLAIN',False),('HOST_SHIELD','SHIELD','RESOLVE',False),('HOST_REPAIR','REPAIR','WORRIED',False),('HOST_UPPER','OPEN','EXPLAIN',True)]:
 anchors={'pivot':[139,269] if not upper else [139,208],'head':[145,100],'feet':[139,377],'near_hand':[207,196] if pose=='BILL' else {'POINT':[245,171],'UP':[242,140],'OPEN':[220,192],'THINK':[148,149],'LEFT':[49,171],'SHIELD':[219,207],'REPAIR':[224,263]}.get(pose,[146,243])}
 spec(ident,'characters',a.host(pose,expr,upper),290,400 if not upper else 265,'HOST', 'POSE_EXPRESSION_VARIANT',anchors)
for expr in ['NEUTRAL','EXPLAIN','WOW','WORRIED','THINK','RESOLVE']:
 spec('FACE_'+expr,'characters',a.g(a.face(expr),-100,-75),100,90,'HOST_FACE','EXPRESSION_OVERLAY',{'pivot':[45,25],'host_attach':[100,75]})
for ident,d in [('HAND_POINT','M8 39 L27 26 L42 11 M27 26 L47 22 M27 26 L41 34'),('HAND_GRIP','M17 44 Q7 25 13 17 Q18 7 26 17 L35 26 M17 44 Q9 47 12 34'),('HAND_OPEN','M9 40 L23 29 L18 10 M23 29 L29 6 M23 29 L40 13 M23 29 L44 26')]:
 spec(ident,'characters',a.p(d,a.SKIN if ident=='HAND_GRIP' else 'none',sw=3),55,55,'HOST_HAND','HAND_VARIANT',{'pivot':[17,40],'wrist':[17,40]})
for ident,name,w,h in [('PROP_FED','fed',300,250),('PROP_BANK','bank',245,225),('PROP_BILL','bill',210,230),('PROP_NOTE','note',175,95)]:spec(ident,'props',a.v2(name),w,h,source='Original V2 drawing; production lettering converted to original paths')
for ident,fn,w,h in [('PROP_CASH_BAG',a.moneybag,185,200),('PROP_CASH_BUNDLE',a.stack,210,205),('PROP_BOND',a.bond,210,260),('PROP_COUPON',a.coupon,180,125),('PROP_LEDGER',a.ledger,310,235),('PROP_TREASURY',a.treasury,320,250),('PROP_LOSS_PILE',a.deferredpile,235,205),('PROP_CLOCK',a.clock,175,165),('PROP_PAUSE',a.pause,105,125),('PROP_SHIELD',a.shield,175,185),('PROP_PRICE_PRESSURE',a.price,235,150),('PROP_WRENCH',a.wrench,155,130)]:spec(ident,'props',fn(),w,h)
spec('SUPPORT_BANKER','supporting_characters',a.bankrep(),190,330,'BANKER',anchors={'pivot':[99,237],'feet':[101,313],'near_hand':[151,190]})
spec('BG_WHITE','environments','<rect width="1080" height="1920" fill="#fff"/>',1080,1920,classification='CANVAS')
spec('ENV_GROUND','environments',a.p('M7 19 Q152 14 299 20 M27 25 L51 26 M242 28 L265 26',sw=2.8),310,40)
spec('ENV_ACCOUNT_DESK','environments',a.desk(),310,185)
spec('ENV_RECOVERY_STEPS','environments',a.stepbridge(),245,155)
for ident,color in [('ANN_ARROW_BLACK',a.INK),('ANN_ARROW_RED',a.RED),('ANN_ARROW_GREEN',a.GREEN)]:spec(ident,'evidence_overlays',a.arrow(color),125,48,'ATTENTION_ARROW','ANNOTATION_VARIANT',{'pivot':[8,22],'tip':[114,24]})
for ident,color in [('ANN_RATE_UP',a.GREEN),('ANN_EXPENSE_UP',a.RED)]:spec(ident,'evidence_overlays',a.up(color),65,195,'UP_ARROW','ANNOTATION_VARIANT',{'pivot':[29,181],'tip':[27,17]})
spec('ANN_SOURCE_BOX','evidence_overlays',a.p('M7 12 Q153 4 292 13 L289 112 Q148 121 7 113 Z',stroke=a.RED,sw=3.2),305,130,'SOURCE_HIGHLIGHT','ANNOTATION',{'pivot':[152,65]})
spec('ANN_SOURCE_WIDE','evidence_overlays',a.p('M8 10 Q414 2 806 12 L802 145 Q399 154 8 146 Z',stroke=a.RED,sw=3.4),820,160,'SOURCE_HIGHLIGHT','ANNOTATION')
spec('ANN_UNDERLINE','evidence_overlays',a.p('M7 16 Q110 9 225 19',stroke=a.RED,sw=5),235,35,'UNDERLINE','ANNOTATION')
spec('DGM_RESERVE_LINK','diagrams','<path d="M12 20 Q222 39 460 22 M441 9 L465 22 L442 38" fill="none" stroke="'+a.INK+'" stroke-width="4" stroke-linecap="round" stroke-dasharray="12 10"/>',480,55,anchors={'pivot':[240,25],'bank':[12,20],'fed':[465,22]},source='Original conceptual bank balance relationship, not physical cash movement')
spec('DGM_INTEREST_FLOW','diagrams',a.p('M460 21 Q244 81 14 21 M35 7 L10 21 L35 38',stroke=a.GREEN,sw=5),480,90,anchors={'pivot':[240,45],'from_fed':[460,21],'to_bank':[10,21]})
spec('DGM_MISMATCH','diagrams',a.txt(5,62,'EXPENSES',49,a.RED)+a.txt(257,62,'>',64)+a.txt(330,62,'INCOME',49)+a.p('M15 94 Q248 107 555 93',sw=3.1),590,120)
spec('DGM_CONDITION_DOWN','diagrams',a.p('M25 9 Q18 84 27 145 M7 123 L27 148 L46 124',sw=4),55,160)
spec('DGM_REMIT_FLOW','diagrams',a.p('M10 29 Q209 9 439 26 M418 9 L443 26 L419 44',stroke=a.GREEN,sw=5),460,60,anchors={'pivot':[230,28],'from_fed':[10,29],'to_treasury':[443,26]})
spec('DGM_SLOW_CHANGE','diagrams',a.p('M6 27 Q109 17 214 26 M192 11 L219 26 L193 42',stroke=a.INK,sw=3.8),235,55,source='Qualitative timing arrow; length/position does not encode financial data')
spec('DGM_COVER_FIRST','diagrams',a.p('M15 30 L168 30 M146 10 L173 30 L147 51 M202 31 L351 31 M329 11 L356 31 L332 53',stroke=a.GREEN,sw=4),375,65,source='Conceptual earnings cover balance before normal remittance path, no forecast')
# Actual documentary pixels. Metadata and overlays remain separate; no value redraw inside image.
def evidence(ident,crop,source):
 f=R/'ARTICLE_EVIDENCE/crops'/crop
 from PIL import Image
 w,h=Image.open(f).size;body=f'<image x="0" y="0" width="{w}" height="{h}" href="data:image/png;base64,{base64.b64encode(f.read_bytes()).decode()}"/>'
 spec(ident,'diagrams',body,w,h,classification='DOCUMENTARY_CROP',source=source+'; exact crop:'+str(f.relative_to(R)))
for x in [('EVD_FOMC_QUARTER','A_FOMC_QUARTER_FOCUS.png','SOURCE_A,1/4 percentage point actual source phrase'),('EVD_FOMC','A_FOMC_decision.png','SOURCE_A,16 Sep2026 policy decision'),('EVD_FOMC_DATE','A_FOMC_date.png','SOURCE_A,16 Sep2026 original date'),('EVD_IORB','B_IORB_focus.png','SOURCE_B,3.90 percent IORB effective17 Sep2026'),('EVD_RESERVES','C_RESERVES_value_SHARP.png','SOURCE_C,H41 page2 Wednesday7 Oct2026,millions'),('EVD_DEFERRED','C_DEFERRED_value_SHARP.png','SOURCE_C,H41 page9 Total Wednesday7 Oct2026,-233587 millions'),('EVD_DEFERRED_LABEL','C_DEFERRED_label_SHARP.png','SOURCE_C,H41 page9 original row label'),('EVD_2021','E_2021_amount.png','SOURCE_E,107.4B preliminary2021 remittance,14 Jan2022 publication')]:evidence(*x)

# Per-state visible layers with concrete transforms. A label is an editable original
# lettering asset, not counted as a unique illustrated drawing.
def label(ident,value,size=50,color=a.INK):
 body,w=a.lettering(value,size,color);spec(ident,'evidence_overlays',a.g(body,4,4),w+8,size*1.18,base='ORIGINAL_LETTERING',classification='ORIGINAL_LETTERING',source='Original path alphabet in tools/pen_art.py; editable semantic text retained')
 SPECS[ident]['text']=value
 return ident
def L(key,asset,x,y,width,operation='STATIC',note=''):
 return {'layer_id':key,'asset_id':asset,'x':x,'y':y,'scale':width/SPECS[asset]['width'],'operation':operation,'contact_note':note}
def T(key,value,x,y,width,color=a.INK,operation='STATIC',size=50):
 ident=label('TX_'+key,value,size,color);return L(key,ident,x,y,width,operation)
def layers(*parts):return [L('CANVAS','BG_WHITE',0,0,1080)]+list(parts)
def state(n,key,parent,start,end,beat,items,cut=False,continuity='Retain preceding scene anchors; add only new argument layer'):
 SCENES.setdefault(n,[]).append({'state_id':key,'parent_state':parent,'scene_id':f'SCENE_{n:02d}','start':start,'end':end,'visual_beat':beat,'layers':items,'cut':cut,'continuity':continuity,'reference':REFS[n]})

# 01: contradiction in one persistent composition, one practical held paper.
s1=[T('RATES','RATES UP.',85,172,600),L('FED','PROP_FED',105,425,640),L('RATE','ANN_RATE_UP',783,472,68,'POP_IN')]
state(1,'S01_01','V01',0,1.5,'Institution and rate decision',layers(*s1,L('HOST','HOST_UP',115,1025,340,'POSE_SWITCH')))
state(1,'S01_02','V01',1.5,2.4,'Rate marker emphasis',layers(*s1,T('RATE_LABEL','INTEREST RATE',681,777,233,a.GREEN,'ADDITIVE_BUILD'),L('HOST','HOST_UP',115,1025,340)))
s1b=s1+[T('BILL_UP','BILL UP, TOO.',85,293,710,a.RED,'POP_IN'),L('HOST','HOST_BILL',115,985,357,'POSE_SWITCH','Held paper and near thumb are in one attachment group; wrist207,196'),L('BILL','PROP_BILL',617,1020,248,'POP_IN'),L('EMPHASIS','ANN_ARROW_RED',538,930,160,'TRACE_REVEAL')]
state(1,'S01_03','V02',2.4,3.8,'Unexpected bill / surprise grip',layers(*s1b))
state(1,'S01_04','V02',3.8,5,'Interest bill focus and readable hold',layers(*s1b,T('FED_BILL','FED INTEREST BILL',544,1330,346,a.RED,'ADDITIVE_BUILD')))

# 02: evidence then accounts and reverse expense flow; supporting banker is a distinct original.
s2a=[T('SEPT','SEPTEMBER',80,170,490),T('QUARTER_POINT','+0.25 PERCENTAGE POINT',80,290,793,a.GREEN),L('POLICY','EVD_FOMC',100,815,780,'POP_IN'),L('POLICY_FOCUS','EVD_FOMC_QUARTER',118,579,730,'SCALE'),L('POLICY_DATE','EVD_FOMC_DATE',100,438,265),L('POLICY_HL','ANN_SOURCE_WIDE',104,552,764,'SOURCE_HIGHLIGHT'),T('POLICY_ATTR','FED . 16 SEP 2026',85,1090,525,size=38)]
state(2,'S02_01','V03',5,6.6,'Real September decision excerpt',layers(*s2a),True,'Cut into genuine document; hold only rate sentence, narration carries detail')
state(2,'S02_02','V03',6.6,8.2,'Target range differentiated',layers(*s2a,T('TARGET_RANGE','TARGET: 3.75-4.00%',80,1280,744,size=47)))
s2base=[T('RESERVES','RESERVES AT THE FED',80,175,785),L('BANK','PROP_BANK',65,405,328),L('FED','PROP_FED',587,412,336),L('BANKER','SUPPORT_BANKER',132,1130,154)]
state(2,'S02_03','V04',8.2,10,'Problem becomes account relationship',layers(*s2base,L('HOST','HOST_THINK',705,1050,195,'POSE_SWITCH')),False,'Document exits; persistent bank/Fed account layout takes over by additive replacement')
s2res=s2base+[T('THREE_TRILLION','ABOUT $3 TRILLION',135,788,695),L('BALANCE_LINK','DGM_RESERVE_LINK',272,910,437,'TRACE_REVEAL'),T('BALANCE_LABEL','BANK BALANCES, NOT A CASH DELIVERY',104,983,763,size=38)]
state(2,'S02_04','V05',10,11.7,'Reserve account balance established',layers(*s2res))
state(2,'S02_05','V05',11.7,13.6,'Actual Wednesday reserve figure',layers(*s2res,L('RESERVE_SOURCE','EVD_RESERVES',364,1210,404,'POP_IN'),L('RESERVE_HL','ANN_SOURCE_BOX',344,1178,444,'SOURCE_HIGHLIGHT'),T('RESERVE_UNITS','MILLIONS . 7 OCT 2026',362,1430,540,size=36)))
s2pay=s2res+[T('INTEREST_TO_BANKS','INTEREST PAID TO BANKS',164,1080,665,a.GREEN),L('PAY_FLOW','DGM_INTEREST_FLOW',263,1170,476,'TRACE_REVEAL'),L('PAY_NOTE','PROP_NOTE',411,1184,125,'POSITION_XY','Payment node centered on conceptual Fed-to-bank path'),T('FED_EXPENSE','AN EXPENSE FOR THE FED',315,1345,581,a.RED)]
state(2,'S02_06','V06',13.6,14.5,'Reverse direction: interest expense',layers(*s2pay))
state(2,'S02_07','V06',14.5,15.6,'IORB documentary focus',layers(*s2pay,L('IORB','EVD_IORB',540,1450,345,'POP_IN'),T('IORB_LABEL','IORB',350,1449,155,size=37),T('IORB_ATTR','FED . EFFECTIVE 17 SEP 2026',350,1552,518,size=30)))

# 03: editable arithmetic with explicit fixed-balance assumption, not a projection.
s3=[T('QUARTER','ONE QUARTER POINT',80,177,786),L('HOST','HOST_POINT',63,989,283),L('CASH','PROP_CASH_BUNDLE',641,950,211)]
state(3,'S03_01','V07',15.6,16.9,'Quarter point expressed as percent',layers(*s3,T('DELTA','0.25%',153,433,649,a.GREEN)),True,'Keep banknote vocabulary while cut isolates calculation')
s3a=s3+[T('DECIMAL','0.25% = 0.0025',118,431,770,a.GREEN)]
state(3,'S03_02','V07',16.9,18.3,'Percentage converted to decimal',layers(*s3a))
s3calc=s3a+[T('MATH','ABOUT $3T X 0.0025',80,652,835),L('CALC_UNDERLINE','ANN_UNDERLINE',113,758,703,'TRACE_REVEAL')]
state(3,'S03_03','V08',18.3,20.1,'Apply only the incremental change',layers(*s3calc))
s3sum=s3calc+[T('ANNUAL_COST','ABOUT $7.5B',153,818,665,a.RED),T('PER_YEAR','MORE PER YEAR',250,930,496,a.RED),T('INTEREST_COSTS','IN INTEREST COSTS',336,1143,553)]
state(3,'S03_04','V08',20.1,22.2,'Annualized extra expense',layers(*s3sum))
state(3,'S03_05','V09',22.2,24,'Assumption visible with result',layers(*s3sum,T('FIXED','IF RESERVES STAY THE SAME',80,1405,824),T('ILLUSTRATION','ILLUSTRATION, NOT A FORECAST',118,1530,755,size=34)))

# 04: timing mismatch, conceptual arrows rather than false time-series data.
s4=[T('MISMATCH_HEADER','THE TIMING DOES NOT MATCH',80,170,820),L('BOND','PROP_BOND',112,398,281),L('CLOCK','PROP_CLOCK',598,423,191),T('BOND_INCOME','MUCH BOND INCOME',95,779,391)]
state(4,'S04_01','V10',24,25,'Existing bond and coupon income',layers(*s4,L('COUPON','PROP_COUPON',277,645,153)),True)
state(4,'S04_02','V10',25,26,'Coupon timing retained',layers(*s4,L('COUPON','PROP_COUPON',277,645,153),L('SLOW','DGM_SLOW_CHANGE',459,696,286,'TRACE_REVEAL'),T('SLOW_LABEL','DOES NOT RESET',489,845,411),T('AS_QUICKLY','AS QUICKLY',557,936,260)))
s4expense=s4+[L('SLOW','DGM_SLOW_CHANGE',459,696,286),T('SLOW_LABEL','DOES NOT RESET',489,845,411),T('AS_QUICKLY','AS QUICKLY',557,936,260),L('COUPON','PROP_COUPON',277,645,153),T('EXPENSE_LABEL','RESERVE INTEREST EXPENSE',97,1138,762,a.RED),L('BILL','PROP_BILL',618,1240,167),L('EXPENSE_UP','ANN_EXPENSE_UP',813,1258,50,'POP_IN'),L('HOST','HOST_CONCERNED',163,1250,187)]
state(4,'S04_03','V10',26,27,'Variable expense versus slower income',layers(*s4expense))
state(4,'S04_04','V10',27,28,'Unequal pace held for comprehension',layers(*s4expense,T('PACE','DIFFERENT SPEEDS',405,1510,468,size=39)),False,'Retain comparison into expense/income condition; no invented rate or income series')

# 05: accumulate on ledger, then isolate genuine dated source cells.
s5=[T('LOSSES','WHEN EXPENSES WIN...',80,171,803),L('HOST','HOST_CONCERNED',60,423,252),L('MISMATCH','DGM_MISMATCH',333,481,583)]
state(5,'S05_01','V11',28,29,'Condition, not inevitable loss',layers(*s5),False,'Additive build from prior comparison; not another mandatory cut')
state(5,'S05_02','V11',29,30,'Condition feeds loss ledger',layers(*s5,L('DOWN','DGM_CONDITION_DOWN',494,630,51,'TRACE_REVEAL'),L('LEDGER','PROP_LEDGER',307,875,436)))
s5ledger=s5+[L('DOWN','DGM_CONDITION_DOWN',494,630,51),L('LEDGER','PROP_LEDGER',307,875,436),L('LOSS_PILE','PROP_LOSS_PILE',667,1030,237,'ADDITIVE_BUILD'),T('DEFERRED','DEFERRED ASSET',254,1298,642,a.RED)]
state(5,'S05_03','V12',30,31.8,'Deferred asset is accumulated balance',layers(*s5ledger))
state(5,'S05_04','V12',31.8,33.4,'Cumulative accounting label',layers(*s5ledger,T('CUMULATIVE','CUMULATIVE LOSSES',242,1420,617),T('NOT_THIS_HIKE','NOT CREATED BY THIS HIKE ALONE',140,1540,737,size=33)))
s5ev=[T('DEFERRED_TITLE','DEFERRED ASSET',80,167,802),T('234B','ABOUT $234B',149,347,704,a.RED),T('OCT_DATE','7 OCTOBER 2026',163,526,664),L('LEDGER','PROP_LEDGER',92,746,253),L('HOST','HOST_CONCERNED',749,739,193),L('SOURCE_LABEL','EVD_DEFERRED_LABEL',91,1061,744),L('SOURCE_TOTAL','EVD_DEFERRED',215,1203,535,'SCALE'),L('SOURCE_HL','ANN_SOURCE_BOX',185,1171,602,'SOURCE_HIGHLIGHT'),T('MILLIONS','MILLIONS OF DOLLARS',97,1453,718,size=40)]
state(5,'S05_05','V13',33.4,35.2,'Dated actual H41 row and Total',layers(*s5ev),False,'Local reframe/replace ledger detail with source cells; focus only on one dated amount')
state(5,'S05_06','V13',35.2,37.4,'Negative line correctly interpreted',layers(*s5ev,T('NEGATIVE','NEGATIVE LINE = DEFERRED BALANCE',101,1552,780,size=32)),False,'No cash arrow to Treasury from the negative table value')

# 06: cover losses first, then normal route; historic comparison separate from current pause.
s6=[T('EARNINGS','FUTURE EARNINGS',80,171,798),L('EARNINGS_BAG','PROP_CASH_BAG',102,442,284),L('LEDGER','PROP_LEDGER',548,447,352),L('COVER','ANN_ARROW_GREEN',397,578,146),T('COVER_FIRST','COVER THE DEFERRED BALANCE FIRST',94,870,797)]
state(6,'S06_01','V14',37.4,39,'Future earnings go to covering balance',layers(*s6),True,'Accounting recovery concept, not a truck of reserve cash')
state(6,'S06_02','V14',39,40.8,'Threshold before normal remittances',layers(*s6,L('STEPS','ENV_RECOVERY_STEPS',368,1123,328),T('BEFORE','BEFORE NORMAL PAYMENTS RESUME',84,1402,823)))
s6pause=[T('PAUSED_HEADER','TREASURY PAYMENTS: PAUSED',80,171,827),L('FED','PROP_FED',58,440,335),L('TREASURY','PROP_TREASURY',609,435,327),L('NORMAL_ROUTE','DGM_REMIT_FLOW',277,947,480),L('PAUSE','PROP_PAUSE',444,883,111,'POP_IN'),T('PAUSE_LABEL','PAUSED',366,1110,329,a.RED),T('WHILE_BALANCE','UNTIL EARNINGS COVER THE BALANCE',81,1340,823)]
state(6,'S06_03','V15',40.8,42,'Normal route blocked pending cover',layers(*s6pause))
state(6,'S06_04','V15',42,43.4,'No negative Treasury cash flow',layers(*s6pause,T('NO_NEGATIVE','NO NEGATIVE CASH PAYMENT',153,1510,737,size=34)))
s6hist=[T('HISTORY','BACK IN 2021',80,172,723),L('TREASURY','PROP_TREASURY',624,896,254),L('NOTE','PROP_NOTE',428,942,166),L('ROUTE','DGM_REMIT_FLOW',138,1071,616),T('HIST_AMOUNT','$107.4B',141,404,709,a.GREEN),T('HIST_REMITTED','REMITTED TO THE TREASURY',87,625,817),L('HIST_SOURCE','EVD_2021',279,1295,520,'POP_IN'),L('HIST_HL','ANN_SOURCE_BOX',252,1255,572,'SOURCE_HIGHLIGHT')]
state(6,'S06_05','V16',43.4,45.4,'Distinct historical 2021 payment',layers(*s6hist),False,'Full layout changes locally but fifth planned cut is reserved for payoff')
state(6,'S06_06','V16',45.4,47.4,'Preliminary remittance, not net income',layers(*s6hist,T('PRELIM','2021 PRELIMINARY . FED 14 JAN 2022',83,1510,804,size=31)))

# 07: same host faces two consequences, not a second unrelated presenter card.
s7=[T('HIGHER_RATES','HIGHER RATES',80,170,720),L('PRICE','PROP_PRICE_PRESSURE',579,518,266),L('HOST','HOST_SHIELD',145,477,379,'POSE_SWITCH'),L('SHIELD','PROP_SHIELD',386,734,228,'POP_IN','Host near hand219,207 maps to shield left contact at x431,y748'),T('FIGHT','CAN FIGHT INFLATION',118,1103,753,a.GREEN)]
state(7,'S07_01','V17',47.4,48.4,'Benefit: resist price pressure',layers(*s7),True,'Return to original host for payoff, fifth actual planned cut')
state(7,'S07_02','V17',48.4,49.5,'Benefit held / gaze toward price',layers(*s7,L('RATE','ANN_RATE_UP',819,414,50)))
s7end=[T('HIGHER_RATES','HIGHER RATES',80,170,720),T('REPAIR_HEADER','HARDER TO REPAIR', 80,290,819,a.RED),L('HOST','HOST_REPAIR',118,735,358,'POSE_SWITCH'),L('LEDGER','PROP_LEDGER',628,846,278),L('WRENCH','PROP_WRENCH',362,1027,138,'ROTATE','Host hand224,263 mapped approximately x394,y1060; wrench handle matches wrist'),L('STEPS','ENV_RECOVERY_STEPS',575,1191,294),T('FED_RECOVERY','THE FED\'S OWN FINANCES',84,1435,822)]
state(7,'S07_03','V18',49.5,51.3,'Recovery work becomes harder',layers(*s7end))
state(7,'S07_04','V18',51.3,53,'Paradox held in one combined explanation',layers(*s7end,L('PRICE','PROP_PRICE_PRESSURE',716,454,189),L('SHIELD','PROP_SHIELD',480,466,134),T('BOTH','BOTH CAN BE TRUE',127,1583,708,size=42)))

# 36 explanatory build/pose/source states; no caption-driven filler quota.
def csvwrite(file,rows):
 with file.open('w',newline='') as f:
  if rows:w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
def unique_ids(root,prefix):
 counts={}
 for el in root.iter():
  tag=el.tag.split('}')[-1];counts[tag]=counts.get(tag,0)+1
  el.set('id',prefix+'_'+tag+'_'+str(counts[tag]))
def write_asset(ident):
 s=SPECS[ident];out=A/s['category']/(ident+'.svg');root=ET.fromstring(a.svg(s['body'],s['width'],s['height'],ident));unique_ids(root,ident)
 root.set('data-asset-id',ident);root.set('data-classification',s['classification'])
 if s.get('text'):root.set('data-text',s['text'])
 ET.register_namespace('',a.NS);ET.register_namespace('xlink','http://www.w3.org/1999/xlink');ET.ElementTree(root).write(out,encoding='unicode')
 return {k:v for k,v in s.items() if k!='body'}|{'source':str(out.relative_to(R)),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'qa_status':'STRUCTURAL_PASS_VISUAL_REVIEW_REQUIRED'}
def build(n):
 states=SCENES[n];used=sorted({x['asset_id'] for s in states for x in s['layers']});records={r['asset_id']:r for r in json.loads((M/'ASSET_DATA.json').read_text())} if (M/'ASSET_DATA.json').exists() else {}
 if n==1: used=sorted(set(used)|{'HOST_NEUTRAL'}|{x for x in SPECS if x.startswith(('FACE_','HAND_'))})
 for ident in used:records[ident]=write_asset(ident)
 for s in states:
  body=''
  for i,l in enumerate(s['layers']):
   asset=SPECS[l['asset_id']];root=ET.fromstring(a.svg(asset['body'],asset['width'],asset['height']));unique_ids(root,s['state_id']+'_'+l['layer_id'])
   inner=''.join(ET.tostring(el,encoding='unicode') for el in root)
   body+=f'<g id="{s["scene_id"]}_{l["layer_id"]}" data-asset-id="{l["asset_id"]}" data-operation="{l["operation"]}" transform="translate({l["x"]} {l["y"]}) scale({l["scale"]:.9f})">{inner}</g>'
  f=A/'scene_compositions'/(s['state_id']+'.svg');f.write_text(a.svg(body,1080,1920,s['state_id']))
 last=A/'scene_compositions'/(states[-1]['state_id']+'.svg');(A/'scene_compositions'/f'SCENE_{n:02d}.svg').write_bytes(last.read_bytes())
 (M/f'SCENE_{n:02d}.json').write_text(json.dumps({'scene':n,'reference':REFS[n],'classification':'Original art and staging; reference technique supported, particular composition inferred','states':states,'review_status':'NATIVE_MOBILE_REVIEW_PENDING'},indent=2))
 (M/'ASSET_DATA.json').write_text(json.dumps(list(records.values()),indent=2));refresh()
def refresh():
 records=json.loads((M/'ASSET_DATA.json').read_text());present={r['asset_id'] for r in records};allrows=[];maps=[]
 parents={r['state_id']:r for r in csv.DictReader((R/'STORYBOARD.csv').open())}
 for n,states in SCENES.items():
  for s in states:
   exists=(A/'scene_compositions'/(s['state_id']+'.svg')).exists()
   par=parents[s['parent_state']]
   allrows.append({'state_id':s['state_id'],'scene_id':s['scene_id'],'approved_parent_state':s['parent_state'],'provisional_start_sec':s['start'],'provisional_end_sec':s['end'],'narration_phrase':par['narration_phrase'],'visual_beat':s['visual_beat'],'required_asset_ids':';'.join(l['asset_id'] for l in s['layers']),'layer_order':';'.join(l['layer_id'] for l in s['layers']),'keyframe_options':';'.join(dict.fromkeys(l['operation'] for l in s['layers'])),'cut_at_start':s['cut'],'continuity':s['continuity'],'source_reference':s['reference'],'timing_status':'PROVISIONAL_NO_AUDIO','art_status':'AUTHORED' if exists else 'PLANNED'})
   if exists:
    for i,l in enumerate(s['layers']):
     asset=SPECS[l['asset_id']];piv=asset['anchors']['pivot'];maps.append({'scene_id':s['scene_id'],'state_id':s['state_id'],'layer_id':s['scene_id']+'_'+l['layer_id'],'asset_id':l['asset_id'],'z_order':i,'x':l['x'],'y':l['y'],'x_normalized':round(l['x']/1080,6),'y_normalized':round(l['y']/1920,6),'scale':round(l['scale'],9),'rotation_degrees':0,'pivot_local_x':piv[0],'pivot_local_y':piv[1],'future_operation':l['operation'],'contact_constraint':l['contact_note'] or 'Maintain original proportions; do not distort source pixels','source_reference':s['reference']})
 rows=[]
 for r in records:
  uses=[x for x in maps if x['asset_id']==r['asset_id']];f=R/r['source'];export=A/'exports'/(r['asset_id']+'.png')
  rows.append({'asset_id':r['asset_id'],'filename':r['source'],'category':r['category'],'base_design_id':r['base_id'],'classification':r['classification'],'scene_usage':';'.join(sorted({x['scene_id'] for x in uses})),'state_usage':';'.join(sorted({x['state_id'] for x in uses})),'layer_relationships':'Independent source; instantiated by scene/state map','anchor_pivot_json':json.dumps(r['anchors'],separators=(',',':')),'width':r['width'],'height':r['height'],'transparency':'opaque_white_canvas' if r['asset_id']=='BG_WHITE' else 'transparent_background','dependencies':'tools/pen_art.py original path alphabet' if r['classification']=='ORIGINAL_LETTERING' else ('ARTICLE_EVIDENCE/CROP_MANIFEST.json' if r['classification']=='DOCUMENTARY_CROP' else 'none; self-contained SVG'),'provenance':r['provenance'],'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'png_export':str(export.relative_to(R)),'png_sha256':hashlib.sha256(export.read_bytes()).hexdigest() if export.exists() else '', 'qa_status':r['qa_status']})
 csvwrite(R/'FULL_STORYBOARD.csv',allrows);csvwrite(R/'SCENE_ASSET_MAP.csv',maps);csvwrite(R/'ASSET_REGISTER.csv',rows)
 completed=[n for n in SCENES if (M/f'SCENE_{n:02d}.json').exists() and json.loads((M/f'SCENE_{n:02d}.json').read_text())['review_status']=='NATIVE_MOBILE_REVIEWED']
 progress=json.loads((R/'PRODUCTION_PROGRESS.json').read_text());progress.update({'status':'STATIC_ASSET_EXPANSION_IN_PROGRESS','scenes_completed':completed,'states_authored':sum(r['art_status']=='AUTHORED' for r in allrows),'states_planned':len(allrows),'completed_art_files':len(records),'reviewed_scene_count':len(completed)});(R/'PRODUCTION_PROGRESS.json').write_text(json.dumps(progress,indent=2))
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--scene',type=int,choices=range(1,8));parser.add_argument('--refresh',action='store_true');args=parser.parse_args()
 if args.scene:build(args.scene);print('Authored static scene',args.scene,'states',len(SCENES[args.scene]))
 if args.refresh:refresh()
