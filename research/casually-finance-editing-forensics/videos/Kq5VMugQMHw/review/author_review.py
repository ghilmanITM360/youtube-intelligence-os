import sys, json; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('Kq5VMugQMHw',1905)
A.scenes([
(0,"White frame, then a Japan Times article slides in with two yen notes; a blue shield pops over them, a host's head rises, red '$74B' pops: 'Japan mounted the largest currency defense in its history, 11.7 trillion yen... in four weeks'","article; yen notes; shield; host; red text; caption","SS_JAPANTIMES,PR_CASH,PR_SHIELD,CH_HOST,TY_RED","Japan's largest currency defense: nearly $74 billion in four weeks"),
(335,"Japan-map character with a paper; a 'US BONDS FOR SALE' stall and bond papers pop: 'that money came from selling down its American bond holdings'","map character; paper; stall; bond papers; caption","CH_JAPAN,PR_DOC,PR_STALL,PR_BOND","The money came from selling American bonds"),
(436,"Large Japan-map character with sunglasses and dollar bills: 'and it worked'","map character; bills; caption","CH_JAPAN,PR_CASH","It worked"),
(460,"Calendar icons pop in one under another: 'for about three weeks'","calendar icons; caption","PR_CALENDAR","For about three weeks"),
(503,"Dark red glowing frame with a monster silhouette and the Japan-map character: 'Then reality set in'","dark red frame; monster; map character; caption","FX_REDGLOW,CH_JAPAN","Then reality set in"),
(547,"Paper and a Japan benchmark-rate chart page that slides in and reveals its line: 'Japan's benchmark rate now sits around 1%'","paper; chart page; caption","PR_DOC,SS_RATE_CHART","Japan's rate sits around 1 %"),
(642,"US-map character above the Fed building; a bubble 'Fed Funds Target 3.50-3.75%' pops: 'while America's sits between'","map character; building; bubble; caption","CH_USMAP,PR_BANK,OV_BUBBLE","America's rate sits between 3.5 and 3.75 %"),
(748,"Paper, a dollar sign and a percent coin that move apart; bond papers pile up at the bottom, a US-map character and a DEBT paper pop: 'a bond's price and the interest rate on it move in opposite directions; flood the market with American bonds nobody asked for'","paper; dollar sign; percent coin; bond pile; map character; DEBT paper; caption","PR_BOND,TY_DOLLAR,PR_COIN,CH_USMAP,PR_DEBTDOC","Price and yield move in opposite directions"),
(1074,"Japan-map character holding a paper with a SALE tag: 'so Japan sells American debt'","map character; paper; caption","CH_JAPAN,PR_DOC","Japan sells American debt"),
(1127,"Large US-map character, a percent coin and a DEBT paper with bags that stack up: 'American borrowing costs go up'","map character; coin; DEBT paper; bags; caption","CH_USMAP,PR_COIN,PR_DEBTDOC,PR_BAGS","American borrowing costs go up"),
(1183,"Japan-map character above a red double arrow above the US-map character: 'the gap between the two countries gets wider'","map characters; red double arrow; caption","CH_JAPAN,CH_USMAP,OV_REDARROW","The gap gets wider"),
(1247,"Three figures with cash; bills fly between them: 'and capital still goes wherever it gets paid the most'","figures; bills; caption","CH_OFFICIAL,CH_FIG,PR_CASH","Capital goes where it gets paid the most"),
(1322,"Large US-map outline onto which dollar bills drop one by one: 'so it goes to America'","map; bills; caption","CH_USMAP,PR_CASH","So it goes to America"),
(1368,"Dollar bills pop one by one; a Japan-map character with a bag and a paper pops below: 'every dollar Tokyo raised to push the yen up'","bills; map character; bag; caption","PR_CASH,CH_JAPAN,PR_BAG","Every dollar Tokyo raised to push the yen up"),
(1454,"Yen note falls from the top and tilts, eyes pop on it, a bubble 'omg stop you're making it worse!!!' pops: 'made the reason the yen was falling slightly worse'","yen note; eyes; bubble; caption","PR_CASH,OV_BUBBLE","It made the reason the yen was falling worse"),
(1548,"Ring of three red arrows that turns, text typed inside it 'FX intervention feedback loop', a text page fades in behind","red arrow ring; typed text; text page","OV_REDARROWS,SS_TEXT_PAGE","The FX intervention feedback loop"),
(1663,"Dark red glowing card 'THE DOOM LOOP' that fades","glow card; text","FX_REDGLOW,TY_RED","The doom loop"),
(1688,"Host; an ouroboros image drops in from the top; caption 'like the ouroboros'","host; image; caption","CH_HOST,PHOTO_OUROBOROS","A machine that eats its own tail"),
(1758,"Sad host, a DEBT paper and red 'PROBLEMS' over a yen note; the paper leaves and a bag arrives: 'every force pushing the yen down before the operation was still pushing it down after'","host; DEBT paper; red text; yen note; bag; caption","CH_HOST,PR_DEBTDOC,TY_RED,PR_CASH,PR_BAG","Every force was still pushing it down after")])
A.event("S01",3,40,"SLIDE_IN","article and yen notes","Japan Times article enters from the right edge and two yen notes slide in from the left; both settle by f40 (38 frames).","SE001; ev_01",conf="MEDIUM",amb="paths and easing not measured")
A.event("S01",136,136,"POP_IN","blue shield","Blue shield appears over the yen notes in one frame.","SE003; ev_01",conf="HIGH")
A.event("S01",153,171,"CHARACTER_RISE_IN","host","Host's head rises from the bottom edge over ~19 frames to a surprised face.","SE004; ev_01",conf="HIGH")
A.event("S01",216,216,"OVERLAY_POP","red '$74B'","Red '$74B' appears in one frame (0 to 844 red px, 7.20 s).","SE005; color_red",conf="HIGH",label="MEASURED")
A.event("S02",364,364,"POP_IN","'US BONDS FOR SALE' stall","Stall appears over the Japan-map character in one frame.","SE009; ev_01",conf="HIGH")
A.event("S02",379,379,"POP_IN","bond papers","Bond papers appear at the left in one frame.","SE010; ev_01",conf="HIGH")
A.event("S04",475,475,"POP_IN","second calendar icon","Second calendar icon appears under the first in one frame (red 658 to 1296 px).","SE013; color_red",conf="HIGH",label="MEASURED")
A.event("S04",486,486,"POP_IN","third calendar icon","Third calendar icon appears in one frame (red 1297 to 1970 px).","SE014; color_red",conf="HIGH",label="MEASURED")
A.event("S05",504,546,"CHARACTER_LOOP_ANIMATION","monster and Japan-map character","The region at the lower right (x 0.3-1.0, y 0.46-0.92) changes on every frame by ~700-1200 px for ~43 frames while the dark frame holds (mean gray 23.5 throughout); a looping character animation is consistent but its mechanism is not resolved.","SE015; stage px f507-543",conf="MEDIUM",label="MEASURED",mclass="INDET",amb="loop versus keyframes not resolved")
A.event("S06",550,612,"SLIDE_IN","rate chart page","Chart page slides in and its line is revealed while the page moves (x pan ease-out cubic, y pan ease-in quad, both SUPPORTED, but the tracker reports a net shift near 0 because the line draws as the page moves).","SE015; camera_560_612",conf="MEDIUM",label="DIRECTLY_OBSERVED",amb="geometry not measured; tracker unreliable on a revealing line")
A.event("S07",688,688,"OVERLAY_POP","bubble 'Fed Funds Target 3.50 - 3.75%'","Bubble appears above the Fed building in one frame.","SE017; ev_01",conf="HIGH")
A.event("S08",813,826,"PROP_DRIFT","percent coin","Percent coin moves down and right away from the dollar sign over ~14 frames.","SE021; ev_01",conf="MEDIUM",amb="path and easing not measured")
A.event("S08",852,864,"PROP_DRIFT","percent coin","Percent coin moves further down over ~12 frames.","SE022; ev_01",conf="MEDIUM",amb="path and easing not measured")
A.event("S08",882,882,"POP_IN","first bond paper","First bond paper slides up at the bottom left in one step.","SE024; ev_02",conf="MEDIUM")
A.event("S08",888,888,"POP_IN","second bond paper","Second bond paper appears at the right edge.","SE025; ev_02",conf="MEDIUM")
A.event("S08",893,893,"POP_IN","third bond paper","Third bond paper appears.","SE026; ev_02",conf="MEDIUM")
A.event("S08",899,899,"POP_IN","fourth bond paper","Fourth bond paper appears.","SE027; ev_02",conf="MEDIUM")
A.event("S08",905,905,"POP_IN","fifth bond paper","Fifth bond paper appears; the pile now fills the bottom.","SE028; ev_02",conf="MEDIUM")
A.event("S08",951,973,"PROP_DRIFT","percent coin","Percent coin moves up and right over ~22 frames while the pile stays.","SE030; ev_02",conf="MEDIUM",amb="path and easing not measured")
A.event("S08",980,980,"POP_IN","US-map character","US-map character appears at the upper left in one frame.","SE031; ev_02",conf="HIGH")
A.event("S08",1050,1050,"POP_IN","DEBT paper and bag","DEBT paper and a bag appear beside the US-map character in one frame.","SE035; ev_02",conf="HIGH")
A.event("S10",1142,1163,"PROP_DRIFT","DEBT paper and bags","DEBT paper and bags rise into a stack beside the percent coin over ~21 frames.","SE038; ev_02",conf="MEDIUM",amb="path and easing not measured")
A.event("S11",1183,1235,"SCALE_TWEEN","red double arrow","Red double arrow appears at f1183-1187 (245 red px) and lengthens to 345 px by f1235 (about 2 px per frame), settling thereafter.","color_red",conf="MEDIUM",label="MEASURED",amb="onset frame within f1183-1187 not isolated")
A.event("S12",1247,1296,"PROP_DRIFT","cash","Bills fly between the three figures over ~50 frames.","SE040; ev_02",conf="LOW",amb="paths not tracked; several bills move")
A.event("S12",1306,1318,"PROP_DRIFT","bill","A bill rises toward the upper right over 13 frames.","SE041; ev_02",conf="MEDIUM",amb="path and easing not measured")
A.event("S13",1322,1339,"POP_IN","dollar bills on the map","Dollar bills land on the US map one after another over ~18 frames.","SE042; ev_03",conf="MEDIUM",amb="individual frames not isolated")
A.event("S14",1385,1385,"POP_IN","second bill","Second dollar bill appears beside the first in one frame.","SE044; ev_03",conf="HIGH")
A.event("S14",1401,1401,"POP_IN","third bill","Third dollar bill appears in one frame.","SE045; ev_03",conf="HIGH")
A.event("S14",1428,1428,"POP_IN","Japan-map character with bag and paper","Japan-map character with a bag and a paper appears under the bills in one frame.","SE046; ev_03",conf="HIGH")
A.event("S15",1460,1497,"PROP_DRIFT","yen note","Yen note falls from the top edge to the middle while tilting over ~37 frames.","SE048; ev_03",conf="HIGH",amb="path and easing not measured")
A.event("S15",1515,1515,"POP_IN","eyes on the yen note","Eyes appear on the yen note in one frame.","SE049; ev_03",conf="HIGH")
A.event("S15",1525,1525,"OVERLAY_POP","bubble 'omg stop you're making it worse!!!'","Bubble appears above the yen note in one frame.","SE050; ev_03",conf="HIGH")
A.event("S16",1548,1662,"ROTATION","red arrow ring","Ring of three red arrows (1928 red px from f1548) turns over ~115 frames while 'FX intervention feedback loop' is typed in and a text page fades in behind it (f1558-1578); rate and direction not measured.","SE051; color_red",conf="MEDIUM",label="DIRECTLY_OBSERVED",mclass="INDET",amb="rotation versus looped clip not resolved")
A.event("S17",1669,1688,"OPACITY_FADE","doom-loop card","Red area falls from 7295 to 0 px over f1669-1688 as the glowing card fades to white before the cut.","color_red",conf="MEDIUM",label="MEASURED")
A.event("S18",1703,1720,"SLIDE_IN","ouroboros image","Ouroboros image drops in from the top over ~18 frames (red ring area 0 to 664 px).","SE053; color_red",conf="HIGH",label="MEASURED")
A.event("S18",1749,1749,"OVERLAY_POP","caption 'like the ouroboros'","Tilted caption appears above the image in one frame.","SE055; ev_03",conf="HIGH")
A.event("S19",1759,1904,"PROP_DRIFT","note and 'PROBLEMS' group","Changed region (about 300 px per frame) slides down by about 0.05 of the frame height over ~146 frames (bbox y 0.45-0.61 at f1765 to 0.50-0.66 at f1900), i.e. a slow downward drift of the note and red text; easing not fitted.","stage px bbox f1765-1900",conf="MEDIUM",label="MEASURED",amb="drift read from the changed-region bbox")
A.event("S19",1842,1863,"PROP_DRIFT","DEBT paper and bag","DEBT paper slides out to the right and a bag arrives in its place over ~22 frames.","SE056; ev_03",conf="MEDIUM",amb="path and easing not measured")
A.fill_small(172)
A.E=[e for e in A.E if not (e['op']=='UNRESOLVED_CHANGE' and ('CUT' in e['desc'] or 'BIG_POP' in e['desc']) and any(e['f0']-2<=s['f0']<=e['f1']+2 for s in A.S))]
A.write(headline=None)
