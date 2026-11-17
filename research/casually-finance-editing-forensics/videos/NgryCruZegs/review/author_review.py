# Authoring for NgryCruZegs (banded, 360p, 30 fps timeline conformed from 24). Run from research dir.
import json
v='videos/NgryCruZegs/'
B=[0,117,184,295,334,357,577,626,863,999,1072,1204,1262,1331,1367,1380,1389,1576,1747,1798,1833,1881,1916,1973,2013]
info=[
("'BREAKING NEWS!!!' paper with bubbles ('This explains EVERYTHING!!', '100% or fake')","headline; news prop; bubbles; caption","PR_NEWSPAPER,OV_BUBBLE","Satire of click-driven media","START"),
("Man at a computer with bubble '...and that's why it's all REPTILIANS!!!'","headline; man+computer (photo-like card); bubble; caption","CH_COMPUTERMAN,OV_BUBBLE","Joke: conspiracy headline",None),
("Dramatic market photo card 'One big dramatic thing like'","headline; photo card; caption","PHOTO_MARKET","Financial risk as a single event",None),
("Blue bubble popping","headline; bubble prop (burst frames); caption","PR_BUBBLE","'like a bubble popping'",None),
("Newspaper reader: 'or a headline'","headline; newspaper reader; caption","CH_NEWSREADER","'...or a headline'",None),
("OECD report text with host peeking; DEBT paper then money bag","headline; text page; host; DEBT paper; bag; caption","SS_OECD_TEXT,CH_HOST,PR_DEBTDOC,PR_BAG","A third of the developed world's debt is getting swapped",None),
("Neutral/frowning figure: 'and we're already seeing it happen'","headline; figure; caption","CH_FIG","Already happening",None),
("Bond tags with an OECD sentence: '20% of fixed-rate bonds ... above 4%'","headline; text page; bond tags; caption","SS_OECD_TEXT,PR_BOND","One fifth of 2025 fixed-rate bonds yield above 4%",None),
("Article with DEBT icons and orange highlight","headline; text page; DEBT icons; highlight; caption","SS_OECD_TEXT,PR_DEBTDOC,OV_HIGHLIGHT","A third maturing by 2027",None),
("Frowning figure: 'not a forecast'","headline; figure; caption","CH_FIG","Not a forecast",None),
("OECD multi-panel figure zooming; host pointing","headline; figure (zoom); host; caption","SS_OECD_FIG,CH_HOST","Cheap to expensive debt",None),
("Figure: '2 percentage points higher ... for that to happen'","headline; figure; caption","CH_FIG","Two percentage points higher",None),
("Bond tag + red timeline; bills pop; bag at maturity; label 'Principal returned at maturity'","headline; bond; red line; bills; bag; label; caption","PR_BOND,OV_TIMELINE,PR_BILLS,PR_BAG,OV_CURVED_ARROW","Bonds just have to reach maturity",None),
("MUNDER DIFFLIN sign with paper boxes and a navy chart; red X over the logo","headline; sign; boxes; chart; red X; caption","PR_MUNDER,PR_PAPERBOXES,SS_CHART,OV_REDX","'The supply of paper' pun",None),
("Bond/certificate collage (note, green document, bond tag)","headline; collage; chart; caption","PR_PAPER,PR_BOND","Supply of paper is exploding",None),
("Same collage, caption advances","headline; collage; caption","PR_PAPER,PR_BOND","'...while demand for it thins'",None),
("Brown-haired figure beside a falling-demand chart with red arrow; then country-map ensemble with yield charts","headline; figure; chart; red arrow; map characters; chart strip; caption","CH_FIG,SS_DC_CHART,OV_REDARROW,CH_MAPS","Demand thins at the long end; cost rises for everyone",None),
("OECD borrowing-composition chart zooming","headline; chart (zoom); caption","SS_OECD_FIG","Long end more expensive; everyone moves short",None),
("Detective figure with magnifier","headline; figure; caption","CH_DETECTIVE","'...none of what's happening is hidden'",None),
("OECD member map (orange), then OECD figure and navy infographic page","headline; map graphic; figure pages; caption","SS_OECD_MAP,SS_OECD_FIG","'The data is sitting right in front of our eyes'",None),
("OECD text page and figure pages","headline; text page; figure; caption","SS_OECD_TEXT,SS_OECD_FIG","Evidence montage",None),
("Report text page, then bar chart page","headline; text page; chart; caption","SS_OECD_TEXT,SS_OECD_FIG","'You just have to know where to look'",None),
("Figure at a pinboard with red strings: 'to connect the dots'","headline; figure; pinboard; caption","CH_FIG,PR_PINBOARD","'Nobody takes the time to connect the dots'",None),
("Pinboard figure with 'let me cook' bubble (end)","headline; figure; pinboard; bubble; caption","CH_FIG,PR_PINBOARD,OV_BUBBLE","Closing joke",None)]
import numpy as np
_g=np.load('/Users/ghilmankhan/workprojects/yio-cf-editing-forensics-local-evidence/NgryCruZegs/gray.npy').astype(np.int16)
_h=_g.shape[1]; _a0,_a1=int(.30*_h),int(.665*_h)
_px=lambda i:int((np.abs(_g[i,_a0:_a1]-_g[i-1,_a0:_a1])>16).sum())
B=list(B)
for _k in range(1,len(B)-1):
    if _px(B[_k])<1000:
        _c=max(range(max(B[_k]-15,B[_k-1]+1),min(B[_k]+16,B[_k+1]-1)),key=_px)
        if _px(_c)>=1000: B[_k]=_c
S=[]
for k,(lab,lay,ass,pur,start) in enumerate(info):
    d=dict(id="S%02d"%(k+1),f0=B[k],f1=B[k+1],label=lab,layers=lay,assets=ass,transition_in="START" if start else "HARD_CUT",purpose=pur+" [ART_DIRECTION_INFERENCE]",notes="")
    if start or (k>0 and _px(B[k])<1000): d["no_auto_cut"]=True
    S.append(d)
def ev(scene,f0,f1,op,target,desc,ref="",conf="MEDIUM",geo="",mclass="CONV"):
    return dict(id="x",scene=scene,f0=f0,f1=f1,op=op,target=target,desc=desc,mclass=mclass,geometry=geo,easing="not measured",measure="",evidence=ref,label="DIRECTLY_OBSERVED",confidence=conf,ambiguity="",trigger="",after="")
E=[ev("S01",33,33,"OVERLAY_POP","bubble 'This explains EVERYTHING!!'","Bubble appears in one frame.","SE001; ev_01","HIGH"),
ev("S01",74,74,"OVERLAY_POP","bubble '100% or fake'","Second bubble replaces the first.","SE002; ev_01","HIGH"),
ev("S02",144,144,"OVERLAY_POP","bubble 'REPTILIANS'","Bubble appears in one frame.","SE004; ev_01","HIGH"),
ev("S03",192,240,"SCALE_TWEEN","market photo card","Photo card appears and grows slightly over ~48 frames while the caption grows.","SE006; ev_01","MEDIUM"),
ev("S03",268,294,"SCALE_TWEEN","market photo card","Photo card changes (zoom/crossfade of its content) over ~27 frames.","SE008; ev_01","LOW"),
ev("S04",312,333,"SHAPE_MORPH","bubble burst","Bubble bursts into droplets over a few frames, then clears.","SE009-010; ev_01","MEDIUM"),
ev("S06",377,399,"CHARACTER_RISE_IN","host peeking","Host rises/peeks from the lower-right while the text page fills in over ~22 frames.","SE013; ev_01","MEDIUM"),
ev("S06",416,472,"CAMERA_SCROLL_ZOOM","OECD text page","Text page scroll/zoom over ~57 frames.","SE016; ev_01","MEDIUM"),
ev("S06",511,541,"POP_IN","DEBT paper then money bag","Documents/bags pop at f511, f541 and f577.","SE017-019; ev_02","MEDIUM"),
ev("S09",863,963,"HIGHLIGHT_SWEEP","orange highlight on OECD text","Highlight grows across the text over ~100 frames while the caption advances.","SE021; ev_02","MEDIUM"),
ev("S11",1072,1099,"CAMERA_SCROLL_ZOOM","OECD multi-panel figure","Figure zooms/pans over ~27 frames; host appears at ~f1096.","SE024; ev_02","MEDIUM"),
ev("S13",1272,1272,"POP_IN","bill #1","Bill appears (line already present).","SE027; ev_02","HIGH"),
ev("S13",1278,1278,"POP_IN","bill #2","Second bill.","SE028; ev_02","HIGH"),
ev("S13",1287,1287,"POP_IN","bill #3","Third bill.","SE029; ev_02","HIGH"),
ev("S13",1294,1294,"POP_IN","bill #4","Fourth bill.","SE030; ev_02","HIGH"),
ev("S13",1300,1300,"POP_IN","money bag at maturity","Bag at the right end.","SE031; ev_02","HIGH"),
ev("S13",1314,1314,"OVERLAY_POP","curved arrow + 'Principal returned at maturity'","Label and arrow appear in one frame.","SE032; ev_02","HIGH"),
ev("S14",1342,1342,"OVERLAY_POP","red X across MUNDER DIFFLIN logo","X appears in one frame.","SE034; ev_02","HIGH"),
ev("S17",1389,1525,"CAMERA_SCROLL_ZOOM","demand chart and country ensemble","Chart with host/arrow, then the country ensemble and chart strip enter over ~136 frames.","SE037; ev_02","LOW"),
ev("S18",1576,1576,"POP_IN","OECD chart","Chart replaces the ensemble.","SE038; ev_02","HIGH"),
ev("S18",1604,1656,"CAMERA_SCROLL_ZOOM","OECD borrowing-composition chart","Chart zooms/pans over ~52 frames.","SE039; ev_03","MEDIUM"),
ev("S18",1671,1671,"CHARACTER_RISE_IN","presenter figure","Figure appears beside the chart.","SE040; ev_03","MEDIUM"),
ev("S20",1799,1805,"SCALE_TWEEN","OECD map then figure pages","Map graphic and figure pages scale/replace over 6 frames.","SE042; ev_03","LOW"),
ev("S20",1815,1818,"POP_IN","navy infographic page","Page appears within 3 frames.","SE043; ev_03","MEDIUM")]
for e in E:
    if e["f1"]>=next(s["f1"] for s in S if s["id"]==e["scene"]): e["f1"]=next(s["f1"] for s in S if s["id"]==e["scene"])-1
for e in E:
    _s=next(s for s in S if s["id"]==e["scene"])
    if e["f0"]<_s["f0"]: e["f0"]=_s["f0"]
json.dump(S,open(v+'review/scenes.json','w'),indent=1); json.dump(E,open(v+'review/events.json','w'),indent=1)
SC={s['id']:s for s in S}; A=[]
H="CHARACTER_STICK_FIGURE"
def fam(a):
    p=a.split('_')[0]
    return {"CH":H,"PR":"PROP_FINANCIAL","SS":"SOURCE_SCREENSHOT","TY":"TYPOGRAPHY_EMPHASIS","OV":"OVERLAY_ANNOTATION","LOGO":"SOURCE_LOGO","PHOTO":"SOURCE_PHOTO"}[p]
over={"CH_USMAP":"CHARACTER_COUNTRY_MAP","CH_MAPS":"CHARACTER_COUNTRY_MAP","PR_DEBTDOC":"PROP_FINANCIAL_PAPER","PR_BOND":"PROP_FINANCIAL_PAPER","PR_PAPER":"PROP_FINANCIAL_PAPER","PR_NEWSPAPER":"PROP_FINANCIAL_PAPER","PR_BILLS":"PROP_MONEY","PR_BAG":"PROP_MONEY","PR_MUNDER":"PROP_FINANCIAL_PAPER","PR_PAPERBOXES":"PROP_OBJECT","PR_BUBBLE":"PROP_OBJECT","PR_PINBOARD":"PROP_OBJECT"}
for s in S:
    for aid in s['assets'].split(','):
        A.append(dict(asset_id=aid,family=over.get(aid,fam(aid)),variant=s['label'][:60],scene=s['id'],f0=s['f0'],f1=s['f1'],role="",desc=""))
A.append(dict(asset_id="TY_HEADER",family="TYPOGRAPHY_PERSISTENT",variant="two-line headline 'The Cheap Money Era Is Coming to an End'",scene="S01",f0=0,f1=2013,role="headline",desc=""))
A.append(dict(asset_id="TY_CAPTION",family="TYPOGRAPHY_CAPTION",variant="small one-line caption",scene="S01",f0=0,f1=2013,role="captions",desc=""))
json.dump(A,open(v+'review/assets.json','w'),indent=1)
print(len(S),'scenes',len(E),'events',len(A),'assets',S[-1]['f1'])
