"""Original vector illustration authoring; static sources only. No animation engine."""
from pathlib import Path
import json, csv, hashlib, argparse, html, re
P=Path(__file__).resolve().parents[1]
INK='#203336'; CREAM='#f5ecd9'; TEAL='#397c7b'; RED='#b84f40'; GOLD='#d9aa55'
LIB={}; SCENES={}
def g(id,s): return f'<g id="{id}">{s}</g>'
def path(d,fill='none',stroke=INK,sw=5): return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'
def rect(x,y,w,h,fill,rx=0,stroke='none',sw=4):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def ell(x,y,rx,ry,fill,stroke='none',sw=4):return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def txt(x,y,s,size=52,fill=INK,weight=700): return f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}">{html.escape(s)}</text>'
def lines(x,y,ss,size=52,fill=INK): return ''.join(txt(x,y+i*size*1.22,s,size,fill) for i,s in enumerate(ss))
def svg(w,h,s,title):return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><title>{html.escape(title)}</title>{s}</svg>'
def asset(id,w,h,s,kind,family,variant='',medical='',anchor=None,contacts=None):
 LIB[id]=dict(id=id,width=w,height=h,body=s,kind=kind,family=family,variant=variant,medical=medical,anchor=anchor or [w/2,h],contacts=contacts or {})
 return id
# Original characters. Coordinates fixed across poses; no mirrored badges or accessories.
people={'doctor':('#c88e67','#eff2e9','#394b50','short'),'diabetes':('#ae7455','#d69a4c','#303d42','curl'),'older-man':('#d2a17b','#668487','#ded8c9','bald'),'older-woman':('#ba896e','#a76b62','#dbd2c4','bob'),'risk-adult':('#805b46','#677d98','#252e35','sweep')}
def character(who,pose='stand',expression='neutral',view='front'):
 skin,coat,hair,style=people[who]; dx=18 if view=='three-quarter' else 0
 # Legs attach under pelvis; sitting variant has coherent knees and grounded shoes.
 legs=path('M245 633 L239 775 L206 803 L264 803 L287 662', '#34484e')+path('M310 660 L330 790 L383 803 L388 778 L360 633','#34484e')
 if pose=='sit':legs=path('M224 625 Q230 684 311 689 L333 787 L386 799 L389 775 L371 643 L306 606','#34484e')+path('M273 629 L240 693 L246 789 L296 802 L302 777 L294 704 L336 646','#425961')
 body=path('M221 424 Q184 441 183 497 L197 649 Q282 679 372 647 L381 497 Q374 443 338 424 Z',coat)
 body+=path('M229 430 L280 488 L334 431', '#f6f1e4')
 if who=='doctor':
  body+=path('M228 435 L251 508 L222 529 L269 646 M337 435 L317 507 L344 530 L299 651')
  body+=path('M239 454 C211 535 252 549 272 524 M320 452 L324 527',stroke='#507674',sw=8)+ell(324,535,13,13,'#607a78',INK)
  body+=rect(318,566,43,38,'#d5e4df',3,INK,3)+path('M326 576 L349 576 M326 585 L342 585',sw=3)
 else:body+=path('M207 582 Q280 603 367 580',stroke='#ffffff',sw=3)
 # Ears/head: distinct softly squared silhouette with cheek planes.
 head=ell(151,277,25,39,skin,INK)+ell(417,277,25,39,skin,INK)
 head+=path('M167 180 Q175 118 246 111 L323 115 Q402 129 407 200 L402 324 Q396 391 333 417 Q284 438 231 410 Q165 386 159 322 Z',skin)
 head+=path('M371 203 Q403 304 367 366 Q346 396 309 410 Q379 413 399 346 L406 238 Z','#00000020','none')
 if style=='short':head+=path('M159 240 Q133 130 226 105 Q306 82 372 131 Q421 156 407 241 L376 203 L356 157 Q284 188 202 165 L184 233 Z',hair)
 if style=='curl':head+=path('M157 233 Q123 207 147 174 Q133 140 176 136 Q176 96 215 108 Q244 78 276 103 Q310 81 338 113 Q382 102 388 141 Q431 146 415 188 Q438 213 406 240 L376 184 Q282 195 192 176 L181 234 Z',hair)
 if style=='bald':head+=path('M159 252 Q139 170 183 148 L194 187 L181 254 Z',hair)+path('M376 150 Q421 172 408 250 L388 248 L373 187 Z',hair)
 if style=='bob':head+=path('M157 290 Q117 169 181 126 Q239 74 332 104 Q427 124 426 246 L443 355 L389 365 L381 199 Q281 219 214 155 Q202 214 179 228 L183 359 L139 354 Z',hair)
 if style=='sweep':head+=path('M151 252 Q126 174 182 130 Q227 87 299 99 Q395 93 414 180 L411 247 L379 221 L363 166 Q281 236 189 201 L180 252 Z',hair)
 eyes=''
 for x in [228+dx,337+dx]:
  eyes+=path(f'M{x-24} 278 Q{x} 254 {x+24} 278 Q{x} 295 {x-24} 278 Z','#faf8ec',INK,3)+ell(x+4,277,8,12,INK)
 if expression=='concerned':eyes+=path(f'M203 249 L248 236 M315 236 L359 249',sw=6)
 else:eyes+=path(f'M204 242 Q227 234 249 244 M313 244 Q337 233 360 242',sw=6)
 eyes+=path(f'M{281+dx} 278 L{275+dx} 314 L{291+dx} 316',stroke='#805e49',sw=4)
 mouth=path('M257 352 Q283 362 310 351',sw=4)
 if expression=='explaining':mouth=ell(284,354,14,10,'#77433a',INK,3)
 if expression=='concerned':mouth=path('M259 360 Q282 345 307 360',sw=4)
 if who=='older-man':eyes+=rect(196,256,64,44,'none',14,INK,4)+rect(309,256,64,44,'none',14,INK,4)+path('M261 275 L308 275',sw=3)
 if who=='older-woman':eyes+=path('M206 320 L231 324 M336 324 L360 319',stroke='#875e4d',sw=3)
 # Each hand is attached to its sleeve; poses authored, never stretched joint rigs.
 left=path('M192 463 Q164 474 156 531 L155 587 L192 592 L214 500',coat)+path('M156 583 L153 616 Q153 641 174 640 Q193 639 193 619 L193 588 Z',skin)+path('M166 601 L166 622',stroke='#805e49',sw=2)
 right=path('M366 465 Q397 473 410 530 L411 588 L374 592 L346 502',coat)+path('M375 589 L376 620 Q378 641 398 640 Q416 637 411 611 L411 586 Z',skin)
 contacts={}
 if pose in ('open','point'):
  right=path('M367 465 Q395 463 415 502 L451 476 L469 505 L418 549 Q393 557 375 529 L348 498',coat)
  if pose=='open':right+=path('M450 480 Q451 464 460 450 Q467 441 475 449 L472 463 L507 455 Q524 454 522 466 L497 486 Q487 508 467 506 Z',skin);contacts={'right_palm':[488,474]}
  else:right+=path('M451 481 L469 451 L507 432 Q522 430 521 441 L487 463 L506 463 Q514 466 508 476 L489 492 L467 503 Z',skin);contacts={'right_index_tip':[519,437]}
 if pose in ('chest','breath'):
  right=path('M366 465 Q404 483 412 531 Q408 558 381 550 L291 509 L307 478 L367 503 Z',coat)+path('M308 479 L276 460 Q261 451 251 462 L242 478 Q241 489 254 493 L289 512 Z',skin)
  contacts={'right_palm_chest':[277,484]}
 if pose=='hold':
  left=path('M190 465 Q154 485 166 544 L239 555 L244 523 L201 513 L214 493',coat)+path('M236 524 L260 520 Q278 520 278 535 Q279 549 260 555 L238 553 Z',skin)
  contacts={'left_palm_object':[260,535]}
 s=g('legs',legs)+g('torso',body)+g('arm-left',left)+g('arm-right',right)+g('head',head)+g('eyes-brows',eyes)+g('mouth',mouth)
 return asset(f'CH-{who}-{pose}-{expression}-{view}',600,900,s,'character_variant','CH-'+who,f'{pose}/{expression}/{view}',anchor=[285,802],contacts=contacts)
D0=character('doctor');D1=character('doctor','open','explaining');D2=character('doctor','point','explaining','three-quarter');D3=character('doctor','open','concerned');
P0=character('diabetes');P1=character('diabetes','breath','concerned');P2=character('diabetes','hold');P3=character('diabetes','sit','concerned');
M0=character('older-man');M1=character('older-man','chest','concerned');W0=character('older-woman');W1=character('older-woman','open','concerned');R0=character('risk-adult');R1=character('risk-adult','open','neutral')
# Environments: original perspective, structural depth and reusable furniture.
def plant(x,y):return path(f'M{x} {y} L{x+15} {y+110} L{x+95} {y+110} L{x+110} {y} Z','#c17c58')+path(f'M{x+55} {y} L{x+55} {y-180}',stroke='#4d705b',sw=8)+''.join(ell(x+55+(-25 if i%2 else 25),y-35-i*30,34,15,'#718867',INK,2) for i in range(5))
for env in ['home','clinic']:
 far=rect(0,0,1080,1920,'#e9e1cf' if env=='home' else '#dce7df')+rect(0,1200,1080,720,'#c4ad91')+rect(0,1170,1080,40,'#7e8880')
 far+=''.join(path(f'M{v} 1205 L{540+(v-540)*2} 1920',stroke='#a28d74',sw=3) for v in range(-100,1200,180))
 far+=rect(85,400,350,460,'#f7f0dc',6,INK)+rect(106,422,308,415,'#bdd8d5')+path('M260 424 L260 837 M107 625 L413 625',stroke='#f8f1df',sw=18)
 far+=path('M112 735 Q170 661 245 742 Q322 682 412 750 L412 835 L112 835 Z','#91b4a3','none')+ell(350,490,37,37,'#f4d994')
 far+=rect(82,380,40,490,'#a77f68' if env=='home' else '#7eaaa3')+rect(402,380,40,490,'#a77f68' if env=='home' else '#7eaaa3')
 mid=rect(636,390,300,33,'#806c55')+rect(636,646,300,33,'#806c55')+rect(636,389,20,290,'#806c55')+rect(918,389,18,290,'#806c55')
 for i,col in enumerate(['#b56b54','#536c76','#d1ad65','#879979','#bfb59d']):mid+=rect(670+i*43,475-i*8,31,167+i*8,col,2,INK,2)
 mid+=rect(657,741,267,271,'#fbf6e9',5,INK)+path('M689 936 L735 831 L789 917 L846 815 L891 936 Z','#86a59a','none')+ell(862,791,18,18,GOLD)
 mid+=plant(876,1125)
 if env=='home':
  mid+=rect(60,1000,400,250,'#9f7261',40,INK)+rect(80,1150,360,140,'#ba8973',30,INK)+rect(65,1100,50,230,'#9f7261',20,INK)+rect(410,1100,50,230,'#9f7261',20,INK)+path('M100 1330 L92 1375 M423 1330 L433 1375',sw=12)
  front=ell(570,1515,345,70,'#00000014')+rect(110,1470,190,26,'#755b46',12,INK)+path('M133 1495 L126 1640 M278 1495 L285 1640',sw=12)+rect(145,1435,70,35,'#f8f0dc',6,INK)+path('M215 1440 Q243 1449 218 1464',sw=5)
 else:
  mid+=rect(65,970,380,260,'#769a92',22,INK)+rect(80,1200,350,70,'#a0b7aa',15,INK)+path('M100 1268 L95 1370 M410 1268 L420 1370',sw=13)
  front=rect(80,1420,920,60,'#94775c',12,INK)+path('M120 1480 L120 1760 M955 1480 L955 1760',sw=20)+rect(560,1367,190,40,'#e9e0c9',8,INK)+path('M577 1380 L733 1380',sw=3)
 asset('ENV-'+env+'-far',1080,1920,g('architecture',far),'environment_layer','ENV-'+env,'far')
 asset('ENV-'+env+'-mid',1080,1920,g('furnishings',mid),'environment_layer','ENV-'+env,'mid')
 asset('ENV-'+env+'-front',1080,1920,g('foreground',front),'environment_layer','ENV-'+env,'front')
for id,col in [('cream',CREAM),('white','#fffdf5'),('ink','#18292d')]:asset('STAGE-'+id,1080,1920,g('field',rect(0,0,1080,1920,col)),'stage','STAGE-'+id)
asset('PROP-chair',500,500,g('back',rect(55,40,350,295,'#91aba0',32,INK))+g('seat',rect(40,300,390,55,'#b1c4b5',18,INK))+g('legs',path('M75 355 L65 480 M395 355 L405 480',sw=16)),'prop','PROP-chair',anchor=[250,480],contacts={'seat':[250,300]})
# Narrative objects, each drawn for this production, no stock-library dependency.
asset('PROP-glucose-kit',300,260,g('case',rect(40,65,175,160,'#eee8d7',25,INK)+rect(64,87,127,69,'#c7d5c9',7,INK)+txt(85,131,'CHECK',24)+ell(128,187,18,18,TEAL,INK))+g('strip',rect(216,135,24,90,'#faf7e9',3,INK)+rect(220,140,16,15,GOLD)),'prop','PROP-glucose-kit',medical='M01',anchor=[150,225])
asset('PROP-health-record',320,330,g('folder',path('M40 55 L127 55 L155 83 L280 83 L280 285 L40 285 Z','#d9aa55')+rect(63,99,193,160,'#fffaed',5,INK))+g('entries',txt(83,139,'HEALTH',27)+path('M83 170 L233 170 M83 201 L211 201 M83 232 L223 232',stroke=TEAL,sw=7)),'prop','PROP-health-record')
asset('PROP-pressure-cuff',370,300,g('cuff',path('M52 94 Q113 59 176 94 L176 218 Q114 244 52 213 Z','#628c8b')+path('M70 107 L159 107 M70 203 L159 203',stroke='#a4c4b8',sw=8))+g('monitor',rect(217,92,116,126,'#e6e4d4',18,INK)+rect(235,110,80,51,'#b8cbbf',7,INK)+txt(252,146,'BP',29)+ell(276,186,13,13,TEAL,INK)+path('M174 196 Q211 259 232 215',sw=7)),'prop','PROP-pressure-cuff',medical='M04')
asset('PROP-lab-tube',300,310,g('tube',rect(107,73,85,199,'#edf1de',36,INK)+path('M113 180 L186 180 L186 229 Q187 266 151 267 Q113 267 113 229 Z','#b65b4b','none')+rect(96,47,109,49,TEAL,9,INK))+g('blank-label',rect(111,118,77,51,'#fff9e9',3,INK)+path('M123 132 L176 132 M123 148 L161 148',sw=3)),'prop','PROP-lab-tube',medical='M04;M07')
asset('PROP-assessment',500,360,g('clipboard',rect(65,47,230,282,'#af906b',18,INK)+rect(84,70,192,238,'#fffbef',5,INK)+rect(133,33,90,51,'#779993',10,INK))+g('history',txt(105,137,'HISTORY',28)+path('M106 168 L251 168 M106 196 L240 196 M106 224 L250 224',sw=5))+g('stethoscope',path('M340 78 L340 158 Q340 215 392 215 Q444 215 444 158 L444 78 M393 216 L393 276',stroke=TEAL,sw=13)+ell(393,292,25,25,'#c5d4ca',INK)),'prop','PROP-assessment',medical='M07')
asset('PROP-call',330,390,g('phone',rect(72,35,186,320,29 if False else '#d2d6c7',25,INK)+rect(88,68,154,235,'#fff8e5',7,INK)+ell(164,328,9,9,INK))+g('receiver',path('M120 115 Q100 135 130 184 Q155 230 194 231 L213 202 L182 180 L166 194 Q141 175 141 150 L155 138 Z',TEAL)),'prop','PROP-call',medical='M05')
asset('FX-breath',300,260,g('breath-lines',path('M40 55 Q129 10 218 62 M43 113 Q114 80 191 118 M43 170 Q102 148 153 178',stroke=TEAL,sw=10)),'emphasis','FX-breath',medical='M02')
asset('FX-caution',200,200,g('triangle',path('M100 20 L184 172 L16 172 Z',GOLD))+g('mark',path('M100 70 L100 116',sw=12)+ell(100,143,7,7,INK)),'emphasis','FX-caution')
# Schematic external anterior heart. Deliberately no chamber flow arrows/ECG.
heart=path('M228 141 C165 120 92 150 86 228 C57 343 143 468 294 544 C373 486 429 365 423 267 C422 177 364 133 307 158 Z','#bc6658')
heart+=path('M289 176 C257 122 257 87 286 58 C317 24 362 43 369 84 L369 127 L338 129 L334 89 Q321 67 306 91 L309 175 Z','#b55348')
heart+=path('M203 178 L191 86 L225 76 L247 170 Z','#72979a')
heart+=path('M247 209 Q273 159 330 158 L397 164 L397 197 L337 192 Q296 194 285 228 Z','#86aaa5')
heart+=path('M268 257 Q309 338 291 484',stroke='#9f4c43',sw=5)
coronary=path('M285 177 L293 218 L320 242 L295 300 L294 382 L309 470',stroke='#f4c287',sw=12)+path('M320 242 Q374 237 397 285 M295 311 L341 340 M296 374 L340 401 M262 182 L242 215 Q170 198 126 252 L110 299 M160 230 L162 321 L193 371',stroke='#f4c287',sw=10)
asset('MED-heart-anterior',500,600,g('heart',heart),'medical','MED-heart',medical='M06',anchor=[250,300])
asset('MED-coronary-overlay',500,600,g('coronary-surface-branches',coronary),'medical_layer','MED-heart','coronary overlay',medical='M06',anchor=[250,300])
asset('MED-artery-wall',800,330,g('wall',rect(40,70,720,190,'#c88b75',60,INK)+rect(48,117,704,96,'#fff0d2',38,INK)),'medical','MED-artery',medical='M06',anchor=[400,165])
asset('MED-plaque',800,330,g('plaque',path('M205 119 Q299 116 332 151 Q376 185 437 157 Q484 118 572 119 Z',GOLD)+path('M205 211 Q295 210 335 189 Q391 170 449 190 Q482 208 572 211 Z',GOLD)),'medical_layer','MED-artery','plaque',medical='M06')
asset('MED-flow',800,330,g('direction',path('M85 166 L264 166 M244 149 L264 166 L244 183 M523 166 L702 166 M682 149 L702 166 L682 183',stroke=RED,sw=8)),'medical_layer','MED-artery','blood-flow direction',medical='M06')
# Source labels and caption cards are separate assets, never doctor quotations.
def label(id,title,body=(),source='',dark=False,medical='',status='SOURCE_REVIEWED_NOT_CLINICIAN_APPROVED'):
 col='#fff6e2' if dark else INK
 s=g('caption-fields',rect(55,135,940,315,'#18292d' if dark else CREAM,12)+rect(55,1350,940,290,'#18292d' if dark else CREAM,12))+g('eyebrow',txt(90,192,'HEART HEALTH / ILLUSTRATED',30,('#d9aa55' if dark else TEAL)))+g('headline',lines(90,300,title,78,col))
 if body:s+=g('explanatory-label',lines(90,1425,body,48,col))
 if source:s+=g('source-label',txt(90,1585,source,32,col,400))
 asset(id,1080,1920,s,'text','TEXT-'+id,medical=medical)
 LIB[id]['approval']=status
 return id
L01=label('TXT-hook',['Could this be','a warning sign?'],['Symptoms can be less obvious.'], 'AHA • diabetes / heart attack',medical='M01;M02')
L01b=label('TXT-hook-care',['New, concerning','symptoms?'],['Seek emergency help.','Call local emergency services.'],'AHA • heart attack guidance',medical='M05')
L02=label('TXT-intro',['A closer look'],['Illustrated clinical presenter'], 'Name / credit awaiting owner approval',status='OWNER_IDENTITY_APPROVAL_PENDING')
L03=label('TXT-exertion',['Discomfort','with exertion'],['A recurring pattern still','needs medical assessment.'],'AHA • stable angina',medical='M03')
L03b=label('TXT-symptoms',['Beyond severe','chest pain'],['Breathlessness. Unusual fatigue.','Possible signs — not a diagnosis.'],'AHA/ACC • chest pain guidance',medical='M02')
L03c=label('TXT-urgent',['New or worsening?'],['New, worsening or rest symptoms:','seek emergency help now.'],'AHA • unstable angina',medical='M03;M05')
L04a=label('TXT-groups',['Three groups','in this excerpt'],['Other people can also be at risk.'],'Speaker’s grouping • not a risk score',dark=True,medical='M08')
L04=label('TXT-diabetes',['1 / Type 2','diabetes'],['Higher risk does not mean','every symptom is a heart attack.'],'AHA • diabetes / heart risk',medical='M01;M08')
L05=label('TXT-older',['2 / Older adults'],['Men and women.','Symptoms differ between people.'],'AHA • heart attack risk factors',medical='M04;M08')
L06=label('TXT-comorbid',['3 / Other','risk conditions'],['Examples: high blood pressure','and high cholesterol.'],'AHA • risk factors; examples, not quote',medical='M04;M08')
L07=label('TXT-heart',['The heart needs','its own blood supply'],['Coronary arteries feed heart muscle.'],'NIH / NHLBI • schematic, not to scale',medical='M06')
L07b=label('TXT-artery',['Reduced flow','can matter'],['Artery segment • simplified model','Not a patient scan or diagnosis.'],'AHA / NHLBI • coronary disease',medical='M06')
L07c=label('TXT-assessment',['Get the right','assessment'],['Symptoms + history + tests.','A clinician assesses the cause.'],'AHA • 2025 ACS patient guidance',medical='M07')
L07d=label('TXT-emergency',['Possible heart','attack symptoms?'],['Call local emergency services now.','Do not wait for a routine visit.'],'AHA • emergency guidance',medical='M05')
L08=label('TXT-ending-hold',['Ending reserved'],['Owner’s sentence ends “when…”','Do not publish this placeholder.'],'EDITORIAL HOLD • NOT NARRATION',status='MISSING_SCRIPT')
# Scene placement: asset canvas positioned by top-left, scale uniform, z increasing.
def inst(id,x=0,y=0,s=1,op='OPACITY'):return dict(asset_id=id,x=x,y=y,scale=s,operation=op)
def env(name):return [inst('ENV-'+name+'-far'),inst('ENV-'+name+'-mid')]
def state(id,scene,items,label_id,phrase,function,ref,medical,hold=4,status='PROVISIONAL_OWNER_REVIEW'):
 SCENES[id]=dict(state_id=id,scene_id=scene,layers=items+[inst(label_id)],script_words=phrase,narrative_function=function,reference=ref,medical_source_ids=medical,minimum_hold_seconds=hold,approval_status=status)
state('S01-A','S01',env('home')+[inst(P1,230,565,.92,'POSE_SWITCH'),inst('FX-breath',650,850,.48),inst('ENV-home-front')],L01,'People with diabetes may be more likely to miss the warning signs of a heart attack.','Human-scale question; concerning symptom is illustrative, not diagnosed.','CE01;CE02','M01;M02',4)
state('S01-B','S01',env('home')+[inst(P1,230,565,.92),inst('PROP-call',690,930,.55,'POP_IN')],L01b,'People with diabetes may be more likely to miss the warning signs of a heart attack.','Safety overlay while acute symptoms are depicted; not added narration.','CE03','M05',5)
state('S02-A','S02',env('clinic')+[inst(D0,230,550,1),inst('ENV-clinic-front')],L02,'Lets listen what doctor rehan says:','Introduce fictional clinical presenter; hold real name pending approval.','CE02','',3)
state('S02-B','S02',env('clinic')+[inst(D1,230,550,1,'POSE_SWITCH'),inst('ENV-clinic-front')],L02,'Lets listen what doctor rehan says:','Open-hand explanation on same plate.','CE02','',3)
state('S03-A','S03',env('home')+[inst(P1,220,520,.92)],L03,'So in patients who have these atypical symptoms which are not particularly significantly angina but angina-like symptoms which appear on exertion,','Exertional context; no exercise test demonstrated.','CE02','M02;M03',5)
state('S03-B','S03',[inst('STAGE-cream'),inst('PROP-chair',120,800,.8),inst(P3,80,520,.82),inst('FX-breath',510,790,.65),inst('FX-caution',710,870,.62)],L03b,'So in patients who have these atypical symptoms which are not particularly significantly angina but angina-like symptoms which appear on exertion,','Possible symptom labels separate from ambiguous quote.','CE03','M02',5)
state('S03-C','S03',[inst('STAGE-cream'),inst('PROP-call',340,600,1.05),inst('FX-caution',690,750,.8)],L03c,'they should always be evaluated in certain subsets of patients which are','Distinguish new/changing/rest symptoms before group list.','CE03','M03;M05',6)
state('S04-A','S04',[inst('STAGE-ink')],L04a,'they should always be evaluated in certain subsets of patients which are','Chapter reset; grouping not exhaustive.','CE04','M08',3)
state('S04-B','S04',[inst('STAGE-cream'),inst(P2,150,500,.92),inst('PROP-glucose-kit',381,891,.60,'POP_IN')],L04,'number 1 type 2 diabetes,','Diabetes context; no fabricated glucose reading.','CE03','M01;M08',4)
state('S05-A','S05',[inst('STAGE-cream'),inst(M0,100,540,.8,'SLIDE_IN')],L05,'number 2 elderly males and elderly females','Older man introduced; no universal symptom depiction.','CE03','M04;M08',3)
state('S05-B','S05',[inst('STAGE-cream'),inst(M0,100,540,.8),inst(W0,510,540,.8,'SLIDE_IN')],L05,'number 2 elderly males and elderly females','Older woman joins on same plate.','CE03','M04;M08',4)
state('S06-A','S06',[inst('STAGE-cream')]+[inst(R0,100,550,.8),inst('PROP-pressure-cuff',570,850,.8,'POP_IN')],L06,'and number 3 with patients with comorbid conditions.','First supported example; not an assigned diagnosis.','CE03','M04;M08',4)
state('S06-B','S06',[inst('STAGE-cream')]+[inst(R1,100,550,.8,'POSE_SWITCH'),inst('PROP-pressure-cuff',550,700,.65),inst('PROP-lab-tube',650,950,.6,'POP_IN')],L06,'and number 3 with patients with comorbid conditions.','Add cholesterol lab-context symbol without a result.','CE03','M04;M08',4)
state('S07-A','S07',[inst('STAGE-white'),inst('MED-heart-anterior',275,535,1.02),inst('MED-coronary-overlay',275,535,1.02,'DIAGRAM_BUILD')],L07,'So these 3 groups of people should always be evaluated for acute chronic syndrome','Schematic mechanism; quoted terminology unresolved.','CE05','M06',5)
state('S07-B','S07',[inst('STAGE-white'),inst('MED-artery-wall',100,700,1),inst('MED-plaque',100,700,1,'DIAGRAM_BUILD'),inst('MED-flow',100,700,1,'DIAGRAM_BUILD')],L07b,'So these 3 groups of people should always be evaluated for acute chronic syndrome','Cut to generic artery segment; no diagnosed blockage.','CE05','M06',5)
state('S07-C','S07',env('clinic')+[inst(D2,45,560,.72,'POSE_SWITCH'),inst(P0,535,560,.72),inst('PROP-assessment',355,995,.55),inst('ENV-clinic-front')],L07c,'if they have sudden onset symptoms which I have just mentioned.','Assessment concept; not advice to book a routine visit for acute signs.','CE02','M07',4)
state('S07-D','S07',[inst('STAGE-cream'),inst('PROP-call',290,580,1.05),inst('FX-caution',650,735,.9)],L07d,'if they have sudden onset symptoms which I have just mentioned.','Emergency action overlay must accompany acute warning section.','CE03','M05',7)
state('S08-HOLD','S08',env('home')+[inst(P0,230,565,.92)],L08,'That is why, in someone with diabetes, a sudden unexplained symptom deserves more attention when…','Callback reserved; no completion invented.','CE06','',4,'MISSING_SCRIPT_NOT_FOR_PUBLICATION')

def write_asset(id):
 a=LIB[id]; target=P/'assets'/f'{id}.svg';target.parent.mkdir(exist_ok=True)
 target.write_text(svg(a['width'],a['height'],a['body'],id))
 # Independently exportable named parts, same canvas: swap without registration drift.
 import xml.etree.ElementTree as ET
 root=ET.fromstring(svg(a['width'],a['height'],a['body'],id))
 if a['kind']=='character_variant':
  for child in root:
   if child.tag.endswith('g'):
    cid=child.attrib['id']; d=P/'assets'/'parts'; d.mkdir(exist_ok=True)
    (d/f'{id}--{cid}.svg').write_text(svg(a['width'],a['height'],ET.tostring(child,encoding='unicode'),id+' / '+cid))

def compose(st):
 s=''; ids=[]
 for z,i in enumerate(st['layers']):
  a=LIB[i['asset_id']]; lid=f"{st['state_id']}-L{z:02d}";i.update(layer_id=lid,z=z,width=a['width'],height=a['height'],anchor_local=a['anchor'],opacity=1,rotation_deg=0)
  # Prefix internal IDs for collision-free standalone compositions.
  body=re.sub(r'id="([^"]+)"',lambda m:f'id="{lid}-{m[1]}"',a['body'])
  s+=f'<g id="{lid}" transform="translate({i["x"]} {i["y"]}) scale({i["scale"]})">{body}</g>'
  ids.append(lid)
 d=P/'scenes';d.mkdir(exist_ok=True);(d/f'{st["state_id"]}.svg').write_text(svg(1080,1920,s,st['state_id']+' review state'))
 st['layer_ids']=ids

def csvwrite(name,rows):
 if rows:
  with (P/name).open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator="\n");w.writeheader();w.writerows(rows)

def build(scene):
 for st in SCENES.values():
  if st['scene_id']==scene:
   for i in st['layers']:write_asset(i['asset_id'])
   compose(st)
 # Supplemental pose library delivered with its relevant character batch.
 extra={'S02':[D3],'S04':[P0],'S05':[M1,W1]}
 for id in extra.get(scene,[]):write_asset(id)
 existing={p.stem for p in (P/'scenes').glob('*.svg')}; built=[]
 for id,st in SCENES.items():
  if id in existing:compose(st);built.append(st)
 assets=[]
 for f in sorted((P/'assets').glob('*.svg')):
  a=LIB[f.stem];assets.append(dict(asset_id=f.stem,kind=a['kind'],authored_design_family=a['family'],variant=a['variant'],source=str(f.relative_to(P)),png='exports/assets/'+f.stem+'.png',width=a['width'],height=a['height'],anchor=json.dumps(a['anchor']),contact_points=json.dumps(a['contacts']),medical_source_ids=a['medical'],approval=a.get('approval','OWNER_REVIEW_PENDING'),source_sha256=hashlib.sha256(f.read_bytes()).hexdigest(),rights='ORIGINAL_VECTOR_AUTHORED_FOR_PROJECT',transparency='opaque' if a['kind']=='stage' or f.stem.endswith('-far') else 'alpha',dependencies='none; text assets use Arial or sans-serif fallback'))
 csvwrite('ASSET_REGISTER.csv',assets)
 maps=[]
 for st in built:
  for i in st['layers']:maps.append(dict(scene_id=st['scene_id'],state_id=st['state_id'],**i,source='assets/'+i['asset_id']+'.svg',dependencies='',source_sha256=hashlib.sha256((P/'assets'/f'{i["asset_id"]}.svg').read_bytes()).hexdigest()))
 csvwrite('SCENE_ASSET_MAP.csv',maps)
 board=[]
 for st in SCENES.values():
  board.append(dict(scene_id=st['scene_id'],state_id=st['state_id'],script_words=st['script_words'],narrative_function=st['narrative_function'],characters=';'.join(i['asset_id'] for i in st['layers'] if i['asset_id'].startswith('CH-')),pose_expression=';'.join(LIB[i['asset_id']]['variant'] for i in st['layers'] if i['asset_id'].startswith('CH-')),environment=';'.join(i['asset_id'] for i in st['layers'] if i['asset_id'].startswith(('ENV-','STAGE-'))),medical_concept=st['medical_source_ids'],original_illustrations=';'.join(i['asset_id'] for i in st['layers']),supporting_objects=';'.join(i['asset_id'] for i in st['layers'] if i['asset_id'].startswith(('PROP-','MED-','FX-'))),layer_ids=';'.join(st.get('layer_ids',[])),transition='CUT_OR_WIPE',keyframe_operations=';'.join(i['operation'] for i in st['layers']),reference_evidence=st['reference'],medical_source_reference=st['medical_source_ids'],minimum_hold_seconds=st['minimum_hold_seconds'],timing_status='ESTIMATE_ONLY_NO_MP3',approval_status=st['approval_status'],artwork_status='AUTHORED' if st['state_id'] in existing else 'PLANNED'))
 csvwrite('FULL_STORYBOARD.csv',board);csvwrite('PROVISIONAL_STORYBOARD.csv',board)
 recipes={
 'POP_IN':{'frames':9,'opacity':[0,1],'scale':[.94,1],'clearance_px':24},
 'SLIDE_IN':{'frames':12,'offset_xy_px':[90,0],'clearance_px':100},
 'TRANSLATE_XY':{'frames':18,'max_delta_px':80,'clearance_px':90},
 'SCALE':{'frames':12,'range':[1,1.04],'clearance_px':40},
 'ROTATE':{'frames':12,'degrees':[-2,0],'clearance_px':30},
 'OPACITY':{'frames':8,'range':[0,1],'clearance_px':0},
 'POSE_SWITCH':{'frames':1,'hold_swap':True,'clearance_px':0},
 'EXPRESSION_SWITCH':{'frames':1,'parts':['eyes-brows','mouth'],'clearance_px':0},
 'TEXT_REVEAL':{'frames':18,'unit':'whole line','clearance_px':0},
 'DIAGRAM_BUILD':{'frames':18,'method':'independent layer opacity or stroke reveal','clearance_px':0},
 'CAMERA_PUSH':{'frames':90,'scale':[1,1.03],'clearance_px':32,'exclude':['text','source-label']},
 'SOURCE_HIGHLIGHT':{'frames':12,'method':'opacity only; no flash','clearance_px':0},
 'CUT_OR_WIPE':{'frames':1,'optional_wipe_frames':8,'clearance_px':0}}
 (P/'KEYFRAME_HANDOFF.json').write_text(json.dumps({'schema_version':1,'canvas':[1080,1920],'suggested_fps':30,'audio':None,'timing_status':'PROVISIONAL_NOT_WORD_ALIGNED','coordinate_system':'top-left; anchor in asset local pixels; uniform scale; z ascending','approval':'OWNER_AND_CLINICAL_REVIEW_PENDING','recipes':recipes,'states':built},indent=2)+'\n')
 (P/'PRODUCTION_PROGRESS.json').write_text(json.dumps({'status':'ASSET_PRODUCTION_IN_PROGRESS','completed_scene_artwork':sorted(set(x['scene_id'] for x in built)),'state_count':len(built),'registered_asset_files':len(assets),'authored_design_families':len(set(a['authored_design_family'] for a in assets if a['kind'] not in ('text','stage'))),'remaining_inputs':['MP3','complete ending','doctor wording confirmation','display name and credential approval','generic presenter approval','clinical sign-off','publication policy recheck'],'rendered_video':False},indent=2)+'\n')
 print(scene, len(existing),'states;',len(assets),'registered sources')
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('scene',choices=['S%02d'%i for i in range(1,9)]);build(ap.parse_args().scene)
