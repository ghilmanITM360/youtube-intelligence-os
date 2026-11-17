import sys, json; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('JsK53moCyZA',1291)
A.scenes([
(0,"Small stage in the middle of a white page: a stick figure with a small caption, then a SpaceX-vs-companies bar chart and a pointer pop in beside it: 'Elon Musk is preparing the largest initial public offering in human history'","figure; chart; pointer; small typed caption","CH_FIG,SS_VALUATION_CHART","The largest IPO in history"),
(129,"A spiky-haired character in a black shirt marked 'X' wobbles beside a red SpaceX bar ($1.75T); a defense-contractor row and red 'more than all COMBINED!' pop in: 'at a $1.75 trillion target valuation, SpaceX would be worth more than every American defense contractor combined'","character (wobble); bar chart; red text; typed caption","CH_MUSK,SS_VALUATION_CHART,TY_RED","Worth more than every defense contractor"),
(352,"Only the red SpaceX bar remains with a small figure on its tip; logo rows (Coca-Cola, McDonald's, Disney, Nike, Starbucks) are added one by one: 'worth more than the market caps of Coca-Cola, McDonald's, Disney, Nike, and Starbucks all put together'","bar chart; logo rows; small figure; typed caption","SS_VALUATION_CHART,PHOTO_LOGOS,CH_FIG","More than five consumer giants"),
(517,"Two bars: SpaceX ($1.75T) and the 'Top 10 LSE Companies' ($1.58T, ten logos); a head rises at the lower left and changes expression: 'and worth more than the top 10 companies on the London Stock Exchange combined'","two bars; logo row; peeking figure; typed caption","SS_VALUATION_CHART,PHOTO_LOGOS,CH_FIG","More than the London top ten"),
(645,"A single stick figure with arms down: 'so if you're wondering who the f**** is buying SpaceX'","figure; typed caption","CH_FIG","Who is buying SpaceX?"),
(692,"SpaceX logo; a dark news card ('SpaceX posted nearly $5 billion loss in 2025') pops in below it and a red ellipse and a tiny 'much' are added: 'a company losing $5 billion per year'","logo; news card; red ellipse; typed caption","LOGO_SPACEX,SS_NEWS_CARD,OV_REDELLIPSE","A company losing $5 billion a year"),
(790,"Full bar chart 'SpaceX IPO vs. The Biggest Companies on Earth' with a yellow label on the SpaceX bar: 'at the largest IPO valuation in history'","bar chart; yellow label; typed caption","SS_VALUATION_CHART,OV_LABEL","The largest IPO valuation"),
(872,"A stick figure with a tiny angel and a tiny devil on its sides, then a larger pointing figure: 'well the answer is you'","figures; typed caption","CH_FIG,CH_ANGEL,CH_DEVIL","The answer is you"),
(913,"A '401K' paper grows from small to large at the centre: 'because within a few weeks your retirement account is going to be one of the biggest buyers'","paper (grow); typed caption","PR_401K","Your 401(k)"),
(1010,"The 401K paper gets a face, arms and a dollar note and a bubble 'Give me SPACEX stocks pls' pops: 'one of the biggest buyers of SpaceX stock whether you like it or not'","paper character; bubble; typed caption","CH_401K,OV_BUBBLE,PR_CASH","The 401(k) buys SpaceX"),
(1128,"Nasdaq logo; a rule paper pops in beside it and a tiny text 'ahh... you now nothing' appears: 'and that's because NASDAQ quietly introduced a brand new rule designed specifically to make that happen'","logo; rule paper; small text; typed caption","LOGO_NASDAQ,PR_RULE","Nasdaq's new rule")])

# caption block clears one frame before the picture changes at 6 of the 10 cuts (see findings)
A.event("S01",128,128,"CAPTION_CHUNK_CHANGE","caption block","Caption is cleared one frame before the cut at f129 (585 px at f128, 5409 px at f129).","stage px f128/f129",conf="HIGH",label="MEASURED")
A.event("S01",38,38,"CAPTION_CHUNK_CHANGE","caption block","Caption restarts with 'the largest' (304 px at f38), 0.14 s before ASR 'largest' (1.4 s = f42).","stage px f38",conf="HIGH",label="MEASURED")
A.event("S01",40,40,"POP_IN","chart, pointer and open-mouth figure","Bar chart with a pointer appears and the figure's mouth opens in one frame (2774 px; red 0 to 59 px at f40, 1.33 s).","SE003; color_red",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_red.json"
# --- S02 ---
A.event("S02",139,349,"POSE_SWAP","wobbling character","Character swaps between two poses every 10 frames, exactly at f139, 149, 159, ..., 339 and 349 (22 swaps, 583-595 px each, i.e. 3 poses per second on a 30 fps timeline) for the whole scene.","SE007-029; changed-px series",conf="HIGH",label="MEASURED",mclass="CONV")
A.event("S02",269,270,"POP_IN","'Everyone Else' defense-contractor row","Second bar row of logos appears under the SpaceX bar within 2 frames (1221 px; red +118 px), 0.7 s before ASR 'defense' (9.7 s = f291).","SE020; color_red",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_red.json"
A.event("S02",324,324,"OVERLAY_POP","red 'more than all COMBINED!'","Red hand-lettered text appears at the right in one frame (410 px; red +85 px), at ASR 'combined.' (10.82 s = f324.6).","SE027; color_red",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_red.json"
A.event("S02",351,351,"CAPTION_CHUNK_CHANGE","caption block","Caption is cleared one frame before the cut at f352 (583 px at f351, 5711 px at f352).","stage px f351/f352",conf="HIGH",label="MEASURED")
# --- S03 ---
A.event("S03",363,509,"POSE_SWAP","small figure on the bar tip","Small figure at the upper right changes pose at f363, 385, 419, 442, 475, 498 and 509 (about 230 px each; gaps of 11-34 frames, irregular).","SE031-047",conf="MEDIUM",label="MEASURED",amb="swap content read from the box size, not resolved")
A.event("S03",393,393,"POP_IN","Coca-Cola logo row","First logo row appears at the left (374 px; red +127 px), 60 ms before ASR 'Coca' (13.16 s).","SE034; color_red",conf="MEDIUM",label="MEASURED")
A.E[-1]["measure"]="color_red.json"
A.event("S03",409,409,"POP_IN","McDonald's logo row","Next logo row appears (red +143 px at f409, 289 px).","SE036; color_red",conf="MEDIUM",label="MEASURED",amb="identity of the row read from the sheet")
A.E[-1]["measure"]="color_red.json"
A.event("S03",433,487,"POP_IN","Disney, Nike and Starbucks rows","Further logo rows appear in steps at about f433, f453, f464 and f487 (240-393 px each); the last (Starbucks) lands at ASR 'Starbucks' (15.5 s = f465).","SE039-045",conf="LOW",label="DIRECTLY_OBSERVED",amb="step frames read from small events; row identity not isolated")
A.event("S03",516,516,"CAPTION_CHUNK_CHANGE","caption block","Caption is cleared one frame before the cut at f517 (403 px at f516, 6255 px at f517).","stage px f516/f517",conf="HIGH",label="MEASURED")
# --- S04 ---
A.event("S04",538,552,"CHARACTER_RISE_IN","peeking head","Head rises at the lower-left edge over ~15 frames (410 px at f538, 491 px at f552) and keeps changing expression through f618.","SE049-050",conf="LOW",label="DIRECTLY_OBSERVED",amb="path and easing not measured")
A.event("S04",577,610,"POSE_SWAP","peeking figure's face and hand","Face and hand change over f577-579 and in a 27-frame run (f584-610, ~700 px per active frame); a tiny thought text appears near the head by f600.","SE051-052",conf="LOW",label="MEASURED",amb="changes not individually classified")
# --- S05 ---
A.event("S05",664,664,"POSE_SWAP","stick figure's face","Face changes in one frame (475 px).","SE056",conf="MEDIUM",label="MEASURED")
# --- S06 ---
A.event("S06",720,720,"POP_IN","dark news card","News card ('SpaceX posted nearly $5 billion loss in 2025...') pops in under the logo in one frame (3662 px at f720; 406 px at f719).","SE060",conf="HIGH",label="MEASURED")
A.event("S06",744,744,"OVERLAY_POP","red ellipse on the loss figure","Red ellipse appears around '$5 billion' in one frame (red 0 to 86 px), 0.16 s before ASR 'billion' (24.96 s).","color_red",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_red.json"
A.event("S06",775,775,"OVERLAY_POP","tiny text 'much'","Tiny text 'much' appears under the card in one frame (403 px).","SE062",conf="MEDIUM",label="MEASURED",amb="text read at low size")
# --- S07 ---
A.event("S07",807,807,"OVERLAY_POP","yellow label on the SpaceX bar","Yellow label appears on the SpaceX bar in one frame (yellow 2 to 71 px; 484 px).","SE064; color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S07",871,871,"CAPTION_CHUNK_CHANGE","caption block","Caption is cleared two frames before the cut at f872 (177 px at f870, 312 px at f871, 4786 px at f872).","stage px f870-872",conf="HIGH",label="MEASURED")
# --- S08 ---
A.event("S08",893,893,"POP_IN","large pointing figure","Larger figure pointing at the viewer replaces the small figure in one frame (3261 px), 70 ms before ASR 'you.' (29.84 s).","SE067",conf="HIGH",label="MEASURED")
A.event("S08",912,912,"CAPTION_CHUNK_CHANGE","caption block","Caption is cleared one frame before the cut at f913 (369 px at f912, 3507 px at f913).","stage px f912/f913",conf="HIGH",label="MEASURED")
# --- S09 ---
A.event("S09",913,980,"SCALE_TWEEN","'401K' paper","Paper grows from small to large over 68 frames (about 410 px per active frame); the changed-pixel series skips every 5th frame (f916, 921, ... ), the signature of a 24 fps animation conformed to 30 fps, and the growth ends at ASR 'is' (32.72 s = f981.6).","SE069; changed-px series",conf="HIGH",label="MEASURED",amb="size curve not fitted")
A.event("S09",1009,1009,"CAPTION_CHUNK_CHANGE","caption block","Caption is cleared one frame before the cut at f1010 (610 px at f1009, 4545 px at f1010).","stage px f1009/f1010",conf="HIGH",label="MEASURED")
# --- S10 ---
A.event("S10",1048,1050,"OVERLAY_POP","bubble 'Give me SPACEX stocks pls'","Bubble pops in over 2 frames (629 and 598 px at f1048 and f1050), about 0.1 s before ASR 'SpaceX' (35.16 s = f1054.8).","SE072",conf="MEDIUM",label="MEASURED",amb="bubble identity read from the sheet")
# --- S11 ---
A.event("S11",1165,1165,"POP_IN","rule paper","Paper pops in beside the logo in one frame (2418 px), at ASR 'quietly'.","SE076",conf="HIGH",label="MEASURED")
A.event("S11",1224,1224,"OVERLAY_POP","tiny text 'ahh... you now nothing'","Tiny text appears above the logo in one frame (664 px), 0.4 s before ASR 'make' (42.1 s).","SE079",conf="MEDIUM",label="MEASURED",amb="text read at low size")
A.fill_small(172)
A.E=[e for e in A.E if not (e['op']=='UNRESOLVED_CHANGE' and ('CUT' in e['desc'] or 'BIG_POP' in e['desc']) and any(e['f0']-2<=s['f0']<=e['f1']+2 for s in A.S))]
A.write(headline=None)
