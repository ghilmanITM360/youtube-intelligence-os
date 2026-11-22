# Authoring for mT2hOLrCYSk (720p, full-bleed, DEPTH_C). Run from research dir.
import json
v='videos/mT2hOLrCYSk/'
S=[];E=[];A=[]
B=[0,134,397,511,569,764,886,970,1056,1239,1275,1399,1514,1641,1772,1965,2087,2390,2481,2620,2650,2712]
info=[("Chip character (NVIDIA) and tiny figure with speech bubbles 'Six years!' / 'YES WAY!' / 'No way!'; title 'nobody in ai can agree on this billion dollar decision'","title (first ~4 s); characters; bubbles; caption","TY_TITLE,CH_CHIP,CH_TINY,OV_BUBBLE","Hook: nobody agrees on a billion-dollar accounting guess"),
("Server rack with a timeline: calendar icons, bills, 'useful life', 'depreciation' labels appear one by one","server; arrow; calendar icons; bills; labels; caption","PR_SERVER,OV_ARROW,PR_CALENDAR,PR_BILLS","Define useful life and depreciation"),
("Depreciation-schedule table with a host pointing; red arrow","table screenshot; host; red arrow; caption","SS_DEPR_TABLE,CH_HOST,OV_REDARROW","Longer life lowers annual depreciation"),
("'Profit:' with three money bags","text; bags x3; caption","PR_BAGS,TY_PROFIT","Profits look bigger"),
("Depreciation table with host: shrink the life, expense rises; then 'Profit:' with fewer bills","table; host; red arrow; bills; caption","SS_DEPR_TABLE,CH_HOST,PR_BILLS","Shorter life lowers reported profit"),
("Figure holding a phone; chip icon with 'life?'","figure; phone; chip; caption","CH_PHONE,PR_CHIP","One boring accounting guess: how long a chip stays useful"),
("RAIN 1: money-bill overlay with big-tech logos (Amazon, Alphabet, Microsoft, Meta, Oracle)","overlay clip (bills); logos; caption","FX_MONEYRAIN,LOGO_BIGTECH","Billions in big-tech earnings"),
("Round table with three figures: '8 years? 2 years? 9 years? No, 6!'","table; figures x3; labels; caption","CH_COUNCIL,OV_BUBBLE","Nobody agrees on the answer"),
("Amazon 10-K pages with highlight sweeps and a host peeking in","filing pages (scroll/zoom); highlight; host; caption","SS_FILING,OV_HIGHLIGHT,CH_HOST","January 2024: servers last six years not five"),
("Figure: 'instead of 5, that single decision'","figure; caption","CH_FIG","Single decision"),
("Server rack with '-3.2B' depreciation label","server; red line; labels; caption","PR_SERVER,TY_NUMBER","Reduced depreciation by $3.2 billion"),
("RAIN 2: Amazon logo with '+2.5B' in green","overlay clip; logo; green number; caption","FX_MONEYRAIN,LOGO_AMAZON,TY_NUMBER","Added $2.5 billion to profit"),
("Amazon filing pages (12 months later) with host","filing pages; host; caption","SS_FILING,CH_HOST","Amazon walked back to five years"),
("Filing page with green highlight and host pointing","filing page; highlight; host; caption","SS_FILING,OV_HIGHLIGHT,CH_HOST","Subsets of servers and networking equipment"),
("Filing page with host; yellow and blue highlights","filing page; highlights; host; caption","SS_FILING,OV_HIGHLIGHT,CH_HOST","Reason: faster technology development, AI"),
("Amazon and Meta logos placed on white","logos; caption","LOGO_AMAZON,LOGO_META","While Amazon walked back, Meta went the other way"),
("Meta 10-K pages, then money bag with '-2.9B' in red","filing pages; bag; red number; caption","SS_FILING,PR_BAGS,TY_NUMBER","Meta extended server life to 5.5 years; cut 2025 depreciation by $2.9B"),
("RAIN 3: Meta logo with '$ PER SHARE' in green","overlay clip; logo; green text; caption","FX_MONEYRAIN,LOGO_META,TY_NUMBER","Added roughly $1 to EPS"),
("Amazon | Meta split by a red divider; chip, calendar and three-figure icons per side","two columns; red divider; icons; caption","LOGO_AMAZON,LOGO_META,OV_DIVIDER,PR_CHIP,PR_CALENDAR,CH_COUNCIL","Same technology, two accounting departments"),
("Host at a blackboard: 'These guys...'","host; blackboard; caption","CH_HOST,PR_BLACKBOARD","Punchline prep"),
("Host at a blackboard: 'and reaching opposite conclusions'","host; blackboard; caption (end)","CH_HOST,PR_BLACKBOARD","Opposite conclusions")]
for k,(lab,lay,ass,pur) in enumerate(info):
    S.append(dict(id="S%02d"%(k+1),f0=B[k],f1=B[k+1] if k+1<len(B) else 2712,label=lab,layers=lay,assets=ass,transition_in="START" if k==0 else "HARD_CUT",purpose=pur+" [ART_DIRECTION_INFERENCE]",notes="",**({"no_auto_cut":True} if k==0 else {})))
def ev(scene,f0,f1,op,target,desc,ref="",conf="MEDIUM",amb="",geo="",ease="not measured",meas="",lab="DIRECTLY_OBSERVED",mclass="CONV"):
    E.append(dict(id="x",scene=scene,f0=f0,f1=f1,op=op,target=target,desc=desc,mclass=mclass,geometry=geo,easing=ease,measure=meas,evidence=ref,label=lab,confidence=conf,ambiguity=amb,trigger="",after=""))
for sid,a,b,k in (("S07",886,969,1),("S12",1399,1513,2),("S18",2390,2480,3)):
    ev(sid,a,b,"OVERLAY_CLIP_LOOP","money-bill rain overlay with big-tech logos","Dozens of overlapping banknote layers move across the upper half every frame while logos and captions stay fixed; rain %d of 3."%k,"mT2hOLrCYSk rain.png; correlation test",conf="HIGH",geo="bills cover y~0.30-0.55; every frame differs (lag-1 correlation 0.47)",meas="",lab="MEASURED",mclass="COMPLEX",amb="authoring method unknown (stock/particle overlay vs hand-built); pixel-identical across the three segments")
ev("S08",970,1055,"CHARACTER_LOOP_ANIMATION","three figures at the round table","Numbers and heads change during the council scene; frames not individually resolved.","SE-auto",conf="LOW",mclass="INDET")
fx=lambda f: f-1 if f>=100 else f   # authored on a decode with one duplicated early frame; native index = authored-1 for f>=100
for s_ in S:
    s_['f0']=fx(s_['f0']); s_['f1']=2711 if s_['f1']==2712 else fx(s_['f1'])
for e_ in E:
    e_['f0']=fx(e_['f0']); e_['f1']=fx(e_['f1'])
json.dump(S,open(v+'review/scenes.json','w'),indent=1)
E.sort(key=lambda e:e['f0'])
json.dump(E,open(v+'review/events.json','w'),indent=1)
SC={s['id']:s for s in S}
def ap(aid,fam,var,scene,role,desc="",f0=None,f1=None):
    A.append(dict(asset_id=aid,family=fam,variant=var,scene=scene,f0=SC[scene]['f0'] if f0 is None else f0,f1=SC[scene]['f1'] if f1 is None else f1,role=role,desc=desc))
H="CHARACTER_STICK_FIGURE"
for sid,aid,fam,var,role in [("S01","CH_CHIP","CHARACTER_PROP_WITH_LIMBS","NVIDIA chip character","AI chip"),("S01","CH_TINY",H,"tiny figure","debater"),("S01","OV_BUBBLE","OVERLAY_ANNOTATION","speech bubbles","speech"),("S02","PR_SERVER","PROP_DEVICE","server rack","machine"),("S02","OV_ARROW","OVERLAY_ANNOTATION","red timeline arrow","time"),("S02","PR_CALENDAR","PROP_DEVICE","calendar icons","years"),("S02","PR_BILLS","PROP_MONEY","bills","depreciation"),("S03","SS_DEPR_TABLE","SOURCE_SCREENSHOT","depreciation table","evidence"),("S03","CH_HOST",H,"host with pointer","presenter"),("S03","OV_REDARROW","OVERLAY_ANNOTATION","red arrow","pointer"),("S04","PR_BAGS","PROP_MONEY","three money bags","profit"),("S05","SS_DEPR_TABLE","SOURCE_SCREENSHOT","depreciation table","evidence"),("S05","CH_HOST",H,"host with pointer","presenter"),("S05","PR_BILLS","PROP_MONEY","few bills","reduced profit"),("S06","CH_PHONE",H,"figure with phone","investor"),("S06","PR_CHIP","PROP_DEVICE","chip icon","AI chip"),("S07","FX_MONEYRAIN","FX_OVERLAY_CLIP","money-bill rain clip","wealth"),("S07","LOGO_BIGTECH","SOURCE_LOGO","five big-tech logos","companies"),("S08","CH_COUNCIL",H,"three figures at a table","debaters"),("S09","SS_FILING","SOURCE_SCREENSHOT","Amazon 10-K pages","evidence"),("S09","OV_HIGHLIGHT","OVERLAY_ANNOTATION","highlights","source emphasis"),("S09","CH_HOST",H,"host peeking","presenter"),("S10","CH_FIG",H,"neutral figure","presenter"),("S11","PR_SERVER","PROP_DEVICE","server with -3.2B","machine"),("S11","TY_NUMBER","TYPOGRAPHY_EMPHASIS","-3.2B","number"),("S12","FX_MONEYRAIN","FX_OVERLAY_CLIP","money-bill rain clip","wealth"),("S12","LOGO_AMAZON","SOURCE_LOGO","Amazon logo","company"),("S12","TY_NUMBER","TYPOGRAPHY_EMPHASIS","+2.5B green","number"),("S13","SS_FILING","SOURCE_SCREENSHOT","Amazon filing","evidence"),("S13","CH_HOST",H,"host","presenter"),("S14","SS_FILING","SOURCE_SCREENSHOT","Amazon filing","evidence"),("S14","OV_HIGHLIGHT","OVERLAY_ANNOTATION","green highlight","source emphasis"),("S14","CH_HOST",H,"host pointing","presenter"),("S15","SS_FILING","SOURCE_SCREENSHOT","Amazon filing","evidence"),("S15","OV_HIGHLIGHT","OVERLAY_ANNOTATION","yellow/blue highlights","source emphasis"),("S15","CH_HOST",H,"host","presenter"),("S16","LOGO_AMAZON","SOURCE_LOGO","Amazon logo","company"),("S16","LOGO_META","SOURCE_LOGO","Meta logo","company"),("S17","SS_FILING","SOURCE_SCREENSHOT","Meta filing","evidence"),("S17","PR_BAGS","PROP_MONEY","money bag with -2.9B","depreciation"),("S17","TY_NUMBER","TYPOGRAPHY_EMPHASIS","-2.9B red","number"),("S18","FX_MONEYRAIN","FX_OVERLAY_CLIP","money-bill rain clip","wealth"),("S18","LOGO_META","SOURCE_LOGO","Meta logo","company"),("S18","TY_NUMBER","TYPOGRAPHY_EMPHASIS","$ PER SHARE green","number"),("S19","LOGO_AMAZON","SOURCE_LOGO","Amazon logo","company"),("S19","LOGO_META","SOURCE_LOGO","Meta logo","company"),("S19","OV_DIVIDER","OVERLAY_ANNOTATION","red vertical divider","comparison"),("S19","PR_CHIP","PROP_DEVICE","chip icon","AI chip"),("S19","PR_CALENDAR","PROP_DEVICE","calendar icon","years"),("S19","CH_COUNCIL",H,"three figures","accountants"),("S20","CH_HOST",H,"host at blackboard","presenter"),("S20","PR_BLACKBOARD","PROP_OBJECT","blackboard","explanation"),("S21","CH_HOST",H,"host at blackboard","presenter"),("S21","PR_BLACKBOARD","PROP_OBJECT","blackboard","explanation")]:
    ap(aid,fam,var,sid,role)
ap("TY_TITLE","TYPOGRAPHY_PERSISTENT","'nobody in ai can agree on this billion dollar decision' (first ~4 s)","S01","headline",f0=0,f1=133)
ap("TY_CAPTION","TYPOGRAPHY_CAPTION","small black marker caption","S01","captions",f0=0,f1=2711)
json.dump(A,open(v+'review/assets.json','w'),indent=1)
print(len(S),'scenes',len(E),'authored events',len(A),'assets; contiguous',all(S[i]['f1']==S[i+1]['f0'] for i in range(len(S)-1)),S[-1]['f1'])
assert S[-1]['f1']==2711
