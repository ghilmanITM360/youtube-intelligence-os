import sys, json; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('06pN9dDvVVU',2154)
A.scenes([
(0,"Headline 'the cost of America's debt is changing the economy' over a blue net-interest area chart that grows; a worried host pops in under it: 'and it buys nothing'","headline; chart (growth); host; caption","SS_NETINT_CHART,CH_HOST","Interest is the fastest growing thing the US buys"),
(123,"Line chart of interest outlays with the host pointing; chart eases in: 'already runs more than a trillion dollars a year'","headline; chart (slow zoom); host; caption","SS_OUTLAY_CHART,CH_HOST","Over a trillion dollars a year"),
(241,"Text page with a growing yellow highlight; the US-map character slides in from the right: 'more than defense... it passes Medicare by 2028'","headline; text page; highlight; map character; caption","SS_TEXT_PAGE,OV_HIGHLIGHT,CH_USMAP","More than defense or veterans benefits; passes Medicare by 2028"),
(488,"US-map character beside a DEBT paper; bubble 'You gotta pay me' and a money bag; a red X crosses the scene: 'pay it off with tax revenue or a surplus'","map character; DEBT paper; bubble; bag; red X; caption","CH_USMAP,PR_DEBTDOC,OV_BUBBLE,PR_BAG,OV_REDX","Debt is not paid off from revenue or a surplus"),
(641,"Large US-map character with sunglasses and bubble 'I'd rather live on the edge': 'that would be too fiscally responsible'","map character; bubble; caption","CH_USMAP,OV_BUBBLE","Too fiscally responsible"),
(700,"Stick-figure host alone: 'that would be too fiscally responsible' / 'instead'","host; caption","CH_HOST","Instead"),
(720,"US-map character with DEBT paper and bubbles ('Oh yeah', 'Can't we just...'): 'instead it just borrows the money again'","map character; DEBT paper; bubbles; caption","CH_USMAP,PR_DEBTDOC,OV_BUBBLE","It just borrows again"),
(776,"DEBT paper alone, a green bond paper pops beside it: 'same debt, new bond, at today's rate'","DEBT paper; bond paper; caption","PR_DEBTDOC,PR_BOND","Same debt, new bond, today's rate"),
(855,"US-map character with a bubble between two DEBT papers; a money bag drifts: 'we pay the old debt by issuing new debt'","map character; DEBT papers; bubble; bag; caption","CH_USMAP,PR_DEBTDOC,OV_BUBBLE,PR_BAG","Pay old debt by issuing new debt"),
(927,"Bar chart of average interest rate by security type; bars grow, then a red oval and line mark the first bar: 'is sitting around 3.5%'","bar chart (growth); red oval; caption","SS_RATE_BARS,OV_REDOVAL","The average rate is around 3.5 %"),
(1077,"Multi-panel CBO figure page; the page enlarges 1.6x and the host peeks in: 'low because most was borrowed back when money was cheap'","chart page (zoom); host; caption","SS_CBO_FIG,CH_HOST","Low because it was borrowed when money was cheap"),
(1211,"Host beside the bar chart; a red X pops over the bars: 'but nothing being sold today costs 3.5%'","host; bar chart; red X; caption","CH_HOST,SS_RATE_BARS,OV_REDX","Nothing sold today costs 3.5 %"),
(1316,"U.S. Treasuries yield table; a red line draws under one row then another: 'short-term bills are around 4% while 30-year money runs around 5.2%'","table screenshot; red row lines; caption","SS_TREASURY_TABLE,OV_REDLINE","Bills near 4 %, 30-year near 5.2 %"),
(1460,"Composition of U.S. debt page with a yellow highlight and DEBT papers: 'a third comes due in 12 months, more than ten trillion dollars'","text page; highlight; DEBT papers; caption","SS_DEBT_COMPOSITION,OV_HIGHLIGHT,PR_DEBTDOC","A third comes due within 12 months"),
(1644,"Host beside a DEBT paper and a dollar bill that slide out; a new DEBT paper slides in: 'every dollar of that cheap debt gets replaced at the new price investors are charging today'","host; DEBT paper; bill; caption","CH_HOST,PR_DEBTDOC,PR_CASH","Cheap debt is replaced at today's price"),
(1807,"Yield chart with a red arrow that moves along the curve: 'so every time we roll the debt forward the average creeps up with it one maturity at a time'","chart; red arrow (moving); caption","SS_YIELD_CHART,OV_REDARROW","Rolling the debt pushes the average up"),
(1995,"Small movie-still clip at the left, 'Panik' meme image at the right: 'it doesn't take an auction to fail or everybody to panic sell'","video clip; meme image; caption","PHOTO_CLIP,PHOTO_MEME","No auction failure or panic needed"),
(2094,"Stick-figure host alone: 'it just takes time'","host; caption","CH_HOST","It just takes time"),
(2127,"Purple armoured figure with a golden gauntlet on a purple background: 'it's inevitable.'","meme image; caption","PHOTO_VILLAIN","Inevitable")])
A.event("S01",1,51,"SCALE_TWEEN","blue area series","Blue area grows from a flat band to the full rising curve over 51 frames (ink area in the stage rows fits ease-out quad, SUPPORTED, margin 0.025).","extent_0_52",conf="HIGH",label="MEASURED")
A.E[-1]["easing"]="ease_out_quad (SUPPORTED, margin 0.025; ink area, indicative)"; A.E[-1]["measure"]="extent_0_52.json"
A.event("S01",86,86,"POP_IN","host","Worried host appears under the chart in one frame.","SE002; ev_01",conf="HIGH")
A.event("S02",181,241,"CAMERA_SCROLL_ZOOM","line chart","Chart eases slowly: net scale 1.0125 with a shift of (-14.1,-31.0) px at analysis size over ~61 frames, ease-in quad on all channels (SUPPORTED, margin 0.135).","camera_180_242",conf="MEDIUM",label="MEASURED",geo="net scale x1.0125; image shift (-14.1,-31.0) px at 180-px analysis size")
A.E[-1]["easing"]="ease_in_quad (SUPPORTED, margin 0.135)"; A.E[-1]["measure"]="camera_180_242.json"
A.event("S03",356,383,"SLIDE_IN","US-map character","Map character slides in from the right edge over ~28 frames.","SE005; ev_01",conf="MEDIUM")
A.event("S03",413,448,"HIGHLIGHT_SWEEP","yellow highlight on the text page","Yellow area grows from 90 to 329 px over f413-444 (stage change continues to f448) on 'it passes Medicare by 2028' while the caption words arrive.","color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S04",581,615,"PROP_DRIFT","money bag","Money bag appears at the character's lower left at f581 and drifts to its lower right over ~35 frames.","SE010; ev_01",conf="LOW",amb="path and easing not measured")
A.event("S04",624,624,"OVERLAY_POP","red X","Red X appears across the map character and bag in one frame (0 to 662 red px) and is removed at the cut (f641).","SE011; color_red",conf="HIGH",label="MEASURED")
A.event("S07",745,745,"OVERLAY_POP","bubble text","Bubble text changes from 'Oh yeah.' to 'Can't we just...' in one frame.","SE015; ev_01",conf="MEDIUM",amb="bubble wording read at 360p")
A.event("S08",800,803,"POP_IN","green bond paper","Green bond paper appears next to the DEBT paper (pop and settle within 4 frames).","SE017; ev_01",conf="HIGH")
A.event("S09",855,881,"PROP_DRIFT","money bag","Bag drifts from the lower left toward the map character over ~27 frames.","SE018; ev_01",conf="MEDIUM",amb="path and easing not measured")
A.event("S09",901,921,"PROP_DRIFT","money bag","Bag drifts again toward the right DEBT paper over ~21 frames.","SE020; ev_01",conf="MEDIUM",amb="path and easing not measured")
A.event("S10",927,976,"SCALE_TWEEN","bars","Four bars grow from the baseline to full height over ~50 frames (ink area fit ease-in-out, AMBIGUOUS, margin 0.005).","extent_926_978",conf="HIGH",label="MEASURED")
A.E[-1]["easing"]="ease_in_out_smoothstep (AMBIGUOUS, margin 0.005)"; A.E[-1]["measure"]="extent_926_978.json"
A.event("S10",1035,1035,"OVERLAY_POP","red oval and line","Red oval and a thin red line appear around the first bar in one frame (40 red px) and are removed at the cut (f1077).","SE022; color_red",conf="MEDIUM",label="MEASURED")
A.event("S11",1111,1141,"CAMERA_SCROLL_ZOOM","CBO figure page","Page enlarges 1.60x with a shift of (+54.9,+29.4) px at analysis size over ~31 frames, linear on scale and both pans (SUPPORTED, margin 0.024-0.040).","camera_1110_1143",conf="HIGH",label="MEASURED",geo="net scale x1.605; image shift (+54.9,+29.4) px at 180-px analysis size")
A.E[-1]["easing"]="linear (SUPPORTED, margin 0.024-0.040)"; A.E[-1]["measure"]="camera_1110_1143.json"
A.event("S11",1137,1141,"POP_IN","host","Host's head appears at the lower left within five frames (absent at f1136, present at f1141).","SE024; ev_02",conf="MEDIUM",amb="exact frame within f1137-1141 not isolated")
A.event("S12",1257,1257,"OVERLAY_POP","red X","Red X appears across the bars in one frame (0 to 456 red px) and is removed at the cut (f1316).","SE026; color_red",conf="HIGH",label="MEASURED")
A.event("S13",1317,1360,"STROKE_REVEAL","red line under the first row","Red line draws along the first row over ~44 frames (stage change from f1317; red-pixel count reads 39 px at f1342, 159 px at f1360, steady f1360-1378; the thin antialiased start is below the colour threshold).","SE027; color_red",conf="MEDIUM",label="MEASURED",amb="onset read from stage change; colour count only from f1337")
A.event("S13",1381,1423,"STROKE_REVEAL","red box on the 30-year row","Red line and box draw along the 30-year row over ~43 frames (red area 159 to 455 px).","SE028; color_red",conf="MEDIUM",label="MEASURED",amb="progress fitted by pixel count only")
A.event("S14",1477,1481,"POP_IN","DEBT papers and red document","DEBT papers and a red-filled document appear at the lower right within five frames (red 0 to 287 px at f1481).","SE031; color_red",conf="MEDIUM",label="MEASURED")
A.event("S14",1544,1557,"HIGHLIGHT_SWEEP","second yellow highlight","Yellow area grows from 178 to 232 px over 14 frames on the composition page.","color_yellow",conf="LOW",label="MEASURED",amb="small area gain; attributed by colour only")
A.E[-1]["measure"]="color_yellow.json"
A.event("S15",1709,1726,"PROP_DRIFT","DEBT paper and bill","DEBT paper and dollar bill slide down and left out of the frame over ~18 frames.","SE042; ev_02",conf="MEDIUM",amb="path and easing not measured")
A.event("S15",1742,1762,"SLIDE_IN","DEBT paper","New DEBT paper slides in from the lower right to the host's right over ~21 frames.","SE043; ev_02",conf="MEDIUM",amb="path and easing not measured")
A.event("S16",1860,1946,"POINTER_TRANSLATE","red arrow","Red arrow travels along the yield curve from (0.17,0.49) to (0.80,0.42) of the frame over 87 frames; x and y fit linear (SUPPORTED, margin 0.058 and 0.053).","blob_1859_1946",conf="HIGH",label="MEASURED",geo="path (0.1745,0.4919) to (0.7979,0.4160) in frame fractions")
A.E[-1]["easing"]="linear (SUPPORTED, margin 0.053-0.058)"; A.E[-1]["measure"]="blob_1859_1946.json"
A.event("S17",1995,2094,"VIDEO_CLIP_INSERT","movie-still clip at the left","Clip region changes on 24 frames between f2010 and f2091 with 2-4 frame gaps (median gap 3 frames, about 9-10 updates per second) and a static stretch at f2060-2075; the clip is held from the cut f1995 to the cut f2094.","clip-region mean abs diff series",conf="MEDIUM",label="MEASURED",mclass="INDET",amb="source clip not identified; mean-diff series only")
A.event("S17",2045,2059,"POP_IN","'Panik' meme image","Meme image appears at the right from f2045 and its region keeps changing through f2059 (pop and settle); first frame within f2045-2047.","SE051; ev_02",conf="MEDIUM",amb="exact frame within f2045-2047 not isolated")
A.event("S19",2128,2128,"OVERLAY_POP","purple background","Background changes from white to dark purple in the frame after the cut, leaving the figure in place.","SE052; ev_02",conf="HIGH")
A.fill_small(172)
A.E=[e for e in A.E if not (e['op']=='UNRESOLVED_CHANGE' and ('HARD' in e['desc'] or 'CUT' in e['desc'] or 'BIG_POP' in e['desc']) and any(e['f0']-2<=s['f0']<=e['f1']+2 for s in A.S))]
A.write(headline="the cost of America's debt is changing the economy")
for p in ('videos/06pN9dDvVVU/review/assets.json',):
    a=json.load(open(p))
    for x in a:
        if x['asset_id']=='TY_HEADER': x['f1']=487
    json.dump(a,open(p,'w'),indent=1)
