# Authoring for 44ggG2I6JPY (720p, full-bleed after a 6-s title, DEPTH_C). Run from research dir.
import json
v='videos/44ggG2I6JPY/'
S=[];E=[];A=[]
def sc(i,f0,f1,label,layers,assets,purpose,trans="HARD_CUT",nac=False):
    d=dict(id=i,f0=f0,f1=f1,label=label,layers=layers,assets=assets,transition_in=trans,purpose=purpose+" [ART_DIRECTION_INFERENCE]",notes="")
    if nac: d["no_auto_cut"]=True
    S.append(d)
sc("S01",0,106,"Title text 'the world's safest market is breaking'; one map character then an ensemble of six country-map characters","title (first 6 s); map characters (pop at f28); caption","TY_TITLE,CH_USMAP,CH_MAPS6","Six countries, same pain in the same week","START",True)
sc("S02",106,128,"Stick figure alone under the title","title; figure; caption","CH_FIG","'At some point, the coincidence stops being a coincidence'")
sc("S03",128,189,"Meme photo 'Coincidence?' swapping to 'I THINK NOT!' with a zoom","title; meme photo (swap at f152-185); caption","MEME_PHOTO","Meme beat: coincidence")
sc("S04",189,646,"Calendar icon, then country 30-year yield charts appearing one after another with captions naming each country","calendar icon; charts x6 (appear at f238, f285, f352, f403, f525...); caption","PR_CALENDAR,SS_YIELD_CHARTS","US, Germany, UK, France, Canada highest in years; Japan all-time high")
sc("S05",646,726,"Stick figure at a green blackboard that gets 'DEBT' written","figure; blackboard; text appears f723; caption","CH_FIG,PR_BLACKBOARD","The obvious answer is debt")
sc("S06",726,811,"US-map character with paper stacks (lenders) and a tiny figure","map character; paper stacks; tiny figure; caption","CH_USMAP,PR_PAPERSTACKS,CH_TINY","Governments borrowed too much, lenders got nervous")
sc("S07",811,873,"Smiling green-tie man holding cash","figure; cash; caption","CH_SELLER","Lenders want more to keep lending")
sc("S08",873,1016,"Stick figure: 'but that explanation only gets you so far'","figure; caption","CH_FIG","Debt story is incomplete")
sc("S09",1016,1115,"Government-debt bubble chart zooming/panning","chart (zoom/pan); caption","SS_DEBT_BUBBLES","Germany carries the lightest debt among the G7")
sc("S10",1115,1258,"Row of debt bubbles with a red arrow; map character and Germany bubble","bubble row; red arrow; character; caption","SS_DEBT_BUBBLES,OV_REDARROW,CH_USMAP","'...by a pretty wide margin' but rates still hit a 15-year high")
sc("S11",1258,1316,"Detective figure with magnifier","figure; caption","CH_DETECTIVE","'There's clearly more to the story'")
sc("S12",1316,1423,"Country ensemble with speech bubbles ('I think I'm broke')","map characters; bubbles; caption","CH_MAPS6,OV_BUBBLE","'It's happening to everyone'")
sc("S13",1423,1544,"Detective with a black '?' circle sliding in","figure; ? circle; caption","CH_DETECTIVE,PR_QCIRCLE","'...nobody was looking'")
sc("S14",1544,1620,"Tiny '?' circle","? circle; caption","PR_QCIRCLE","'...one very particular buyer'")
sc("S15",1620,1641,"Earth with stacked bond tags and a '?' circle","Earth; bonds; caption","CH_EARTH,PR_BOND,PR_QCIRCLE","'...under every major bond market in the world'")
sc("S16",1641,1710,"Stick figure at a blackboard 'Defined benefit pension fund'","figure; blackboard; caption","CH_FIG,PR_BLACKBOARD","Name the buyer")
sc("S17",1710,1740,"Wall clock","clock; caption","PR_CLOCK","'They were patient'")
sc("S18",1740,1896,"Clock, money bags and a legal document ('legally required'); figure appears","clock; bags; document; figure; caption","PR_CLOCK,PR_BAGS,PR_DOC,CH_FIG","'Patient, deep pockets, legally required, unbothered by price'")
sc("S19",1896,2047,"Pension Plan card with green check; bond tags pop","card; check; bonds; caption","SS_PENSION_CARD,OV_GREENCHECK,PR_BOND","'The best customers of the long end'")
sc("S20",2047,2103,"Contributions-vs-benefits chart","chart; caption","SS_DB_CHART","'The last of a dying breed'")
sc("S21",2103,2202,"OECD logo","logo; caption","LOGO_OECD","Introduce the OECD")
sc("S22",2202,2301,"OECD member-country map (orange)","map graphic; caption","SS_OECD_MAP","'An international organization of 38 developed countries'")
sc("S23",2301,2348,"Avengers logo","logo; caption","LOGO_AVENGERS","Joke: the Avengers of economics")
sc("S24",2348,2392,"Country characters (US map and a large Russia-like map with a moustache)","map characters; caption","CH_MAPS6","Transition")
sc("S25",2392,2641,"Text page highlight with OECD logo and money bag","text page; highlight; bag; logo; caption","SS_OECD_TEXT,PR_BAGS,LOGO_OECD","'Pension funds' domestic bond holdings cut in half from 8% to 4%'")
sc("S26",2641,2762,"Country ensemble with charts reappearing","map characters; chart strip; caption","CH_MAPS6,SS_YIELD_CHARTS","'...six governments had the same week'")
sc("S27",2762,2818,"Heart-shaped icons labelled 'markets'","hearts icon; caption","PR_HEARTS","'Markets don't do coincidences'")
sc("S28",2818,2894,"Earth character","Earth; caption","CH_EARTH","'...when the same thing happens everywhere at once'")
sc("S29",2894,3026,"Newspaper reader, then a dark spider-like figure holding a newspaper","figure; newspaper; caption (end)","CH_NEWS","'The story being reported is usually not the story actually happening'")
def ev(scene,f0,f1,op,target,desc,ref="",conf="MEDIUM",amb="",geo="",ease="not measured",meas="",lab="DIRECTLY_OBSERVED",mclass="CONV"):
    E.append(dict(id="x",scene=scene,f0=f0,f1=f1,op=op,target=target,desc=desc,mclass=mclass,geometry=geo,easing=ease,measure=meas,evidence=ref,label=lab,confidence=conf,ambiguity=amb,trigger="",after=""))
ev("S01",28,28,"POP_IN","ensemble of six country-map characters","The single map is replaced by six country characters in one frame.","SE003; ev_01",conf="HIGH")
ev("S01",66,86,"CAMERA_SCROLL_ZOOM","country ensemble and chart strip","Ensemble shifts while a strip of small charts appears above it over ~21 frames.","SE006; ev_01",conf="LOW",amb="mechanism unresolved")
ev("S03",152,185,"SCALE_TWEEN","meme photo","Photo zooms in on the face and the caption changes from 'Coincidence?' to 'I THINK NOT!' over ~34 frames.","SE009; ev_01",conf="MEDIUM")
ev("S04",238,238,"POP_IN","calendar icon and first chart","Calendar icon appears (f189); first chart appears at f238.","SE010/SE013; ev_01",conf="MEDIUM")
ev("S05",723,724,"TEXT_WRITE_ON","'DEBT' on the blackboard","Word appears on the blackboard within 4 frames (reveal, not letter-by-letter).","SE026; ev_01",conf="MEDIUM")
ev("S06",753,753,"POP_IN","paper stacks beside the map","Stacks of paper appear in one frame.","SE028; ev_01",conf="HIGH")
ev("S07",811,811,"POP_IN","smiling man with cash","Figure appears with cash at the scene start.","SE031; ev_01",conf="MEDIUM")
ev("S09",1016,1081,"CAMERA_SCROLL_ZOOM","Government-debt bubble chart","Chart zooms and pans over ~66 frames; the map character appears at ~f1079.","SE039; ev_01",conf="MEDIUM")
ev("S12",1381,1383,"OVERLAY_POP","speech bubbles ('Yeah, me too.')","Bubble grows from small to large within 3 frames.","SE055; ev_02",conf="MEDIUM")
ev("S13",1474,1490,"SLIDE_IN","black '?' circle","Circle slides in from the right edge over ~16 frames.","SE062; ev_02",conf="MEDIUM")
ev("S19",1965,1987,"POP_IN","green check and bond tags","Green check appears at ~f1964 and bond tags follow over ~22 frames.","SE089; ev_02",conf="MEDIUM")
ev("S29",2894,2897,"POP_IN","newspaper reader","Reader appears within 4 frames.","SE135",conf="MEDIUM")
fx=lambda f: f-1 if f>=106 else f
for s_ in S:
    s_['f0']=fx(s_['f0']); s_['f1']=3025 if s_['f1']==3026 else fx(s_['f1'])
for e_ in E:
    e_['f0']=fx(e_['f0']); e_['f1']=fx(e_['f1'])
json.dump(S,open(v+'review/scenes.json','w'),indent=1)
E.sort(key=lambda e:e['f0'])
json.dump(E,open(v+'review/events.json','w'),indent=1)
SC={s['id']:s for s in S}
A=[]

def ap(aid,fam,var,scene,role,desc="",f0=None,f1=None):
    A.append(dict(asset_id=aid,family=fam,variant=var,scene=scene,f0=SC[scene]['f0'] if f0 is None else f0,f1=SC[scene]['f1'] if f1 is None else f1,role=role,desc=desc))
H="CHARACTER_STICK_FIGURE"
for sid,aid,fam,var,role in [("S01","CH_USMAP","CHARACTER_COUNTRY_MAP","green US map","country as actor"),("S01","CH_MAPS6","CHARACTER_COUNTRY_MAP","six country characters","comparison cast"),("S02","CH_FIG",H,"neutral stick figure","presenter"),("S03","MEME_PHOTO","SOURCE_PHOTO","meme photograph (two captions)","reaction"),("S04","PR_CALENDAR","PROP_DEVICE","calendar icon","same week"),("S04","SS_YIELD_CHARTS","SOURCE_SCREENSHOT","six yield charts (US, Germany, UK, France, Canada, Japan)","evidence"),("S05","CH_FIG",H,"figure with pointer","presenter"),("S05","PR_BLACKBOARD","PROP_OBJECT","green blackboard","explanation"),("S06","CH_USMAP","CHARACTER_COUNTRY_MAP","green US map","country as actor"),("S06","PR_PAPERSTACKS","PROP_FINANCIAL_PAPER","stacks of DEBT papers","lenders"),("S06","CH_TINY",H,"tiny figure","lender"),("S07","CH_SELLER",H,"smiling man with cash","lender"),("S08","CH_FIG",H,"neutral figure","presenter"),("S09","SS_DEBT_BUBBLES","SOURCE_SCREENSHOT","government-debt bubble chart","evidence"),("S10","SS_DEBT_BUBBLES","SOURCE_SCREENSHOT","bubble row","evidence"),("S10","OV_REDARROW","OVERLAY_ANNOTATION","red up arrow","Germany marker"),("S10","CH_USMAP","CHARACTER_COUNTRY_MAP","small map character","country as actor"),("S11","CH_DETECTIVE",H,"detective with magnifier","investigator"),("S12","CH_MAPS6","CHARACTER_COUNTRY_MAP","six country characters with bubbles","comparison cast"),("S12","OV_BUBBLE","OVERLAY_ANNOTATION","speech bubbles","speech"),("S13","CH_DETECTIVE",H,"detective","investigator"),("S13","PR_QCIRCLE","PROP_OBJECT","large black ? circle","the unknown"),("S14","PR_QCIRCLE","PROP_OBJECT","small ? circle","the unknown"),("S15","CH_EARTH","CHARACTER_PLANET","Earth with eyes","world"),("S15","PR_BOND","PROP_FINANCIAL_PAPER","stacked bond tags","bond market"),("S15","PR_QCIRCLE","PROP_OBJECT","small ? circle","the unknown"),("S16","CH_FIG",H,"figure","presenter"),("S16","PR_BLACKBOARD","PROP_OBJECT","blackboard 'Defined benefit pension fund'","explanation"),("S17","PR_CLOCK","PROP_DEVICE","wall clock","patient"),("S18","PR_CLOCK","PROP_DEVICE","wall clock","patient"),("S18","PR_BAGS","PROP_MONEY","money bags","deep pockets"),("S18","PR_DOC","PROP_FINANCIAL_PAPER","legal document","legally required"),("S18","CH_FIG",H,"figure","presenter"),("S19","SS_PENSION_CARD","SOURCE_PHOTO","Pension Plan card","pension funds"),("S19","OV_GREENCHECK","OVERLAY_ANNOTATION","green check","approval"),("S19","PR_BOND","PROP_FINANCIAL_PAPER","bond tags","bond market"),("S20","SS_DB_CHART","SOURCE_SCREENSHOT","contributions vs benefits chart","dying breed"),("S21","LOGO_OECD","SOURCE_LOGO","OECD logo","institution"),("S22","SS_OECD_MAP","SOURCE_SCREENSHOT","orange OECD member map","38 countries"),("S23","LOGO_AVENGERS","SOURCE_LOGO","Avengers logo","joke"),("S24","CH_MAPS6","CHARACTER_COUNTRY_MAP","US map and large Russia-like map","countries"),("S25","SS_OECD_TEXT","SOURCE_SCREENSHOT","OECD text page with highlight","evidence"),("S25","PR_BAGS","PROP_MONEY","money bag","pension holdings"),("S25","LOGO_OECD","SOURCE_LOGO","OECD logo","institution"),("S26","CH_MAPS6","CHARACTER_COUNTRY_MAP","six country characters","comparison cast"),("S26","SS_YIELD_CHARTS","SOURCE_SCREENSHOT","chart strip","evidence"),("S27","PR_HEARTS","PROP_OBJECT","heart-shaped icons","markets"),("S28","CH_EARTH","CHARACTER_PLANET","Earth with eyes","world"),("S29","CH_NEWS",H,"newspaper reader / dark spider figure","media")]:
    ap(aid,fam,var,sid,role)
ap("TY_TITLE","TYPOGRAPHY_PERSISTENT","'the world's safest market is breaking' (first 6 s only)","S01","headline",f0=0,f1=188)
ap("TY_CAPTION","TYPOGRAPHY_CAPTION","hand-lettered marker caption","S01","captions",f0=0,f1=3025)
json.dump(A,open(v+'review/assets.json','w'),indent=1)
print(len(S),'scenes',len(E),'authored events',len(A),'assets; contiguous',all(S[i]['f1']==S[i+1]['f0'] for i in range(len(S)-1)),S[-1]['f1'])
assert S[-1]['f1']==3025
