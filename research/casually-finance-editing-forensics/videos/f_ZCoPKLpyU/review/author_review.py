import sys; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('f_ZCoPKLpyU',1848)
A.scenes([
(0,"'Gross govt. debt as % of GDP' bar chart under the headline; a globe character appears at the right","headline; bar chart; globe character; caption","SS_DEBT_CHART,CH_EARTH","Japan owes more relative to its economy than any major country"),
(138,"Japanese government bond issuance and interest chart with a pointing host; red '13T' and '122.3T total budget' pop","headline; chart; host; red text; caption","SS_JGB_CHART,CH_HOST,TY_RED","Debt service jumped nearly 11 % to 13 trillion yen of a 122.3 trillion budget"),
(431,"Green Japan-map character; DEBT papers pop in one after another","headline; map character; DEBT papers; caption","CH_JAPAN,PR_DEBTDOC","Japan's debt bill is spiralling"),
(496,"Yen chart at 40-year lows with a yen note at the lower right","headline; chart; yen note; caption","SS_YEN_CHART,PR_CASH","The yen has collapsed to 40-year lows"),
(579,"Host at a green blackboard: 'But why???' then 'The old math again!' (headline gone from this cut on)","host; blackboard; caption","CH_HOST,PR_BLACKBOARD","Why the currency is falling isn't complicated; it's basic math"),
(703,"Japan benchmark-rate chart on a data site","chart screenshot; caption","SS_RATE_CHART","For decades Japan kept borrowing costs pinned near zero"),
(828,"Japan-map character beside a man; a '0' weight pops in: 'whether this was a good idea...but they've recently started rolling it back'","map character; man; weight; caption","CH_JAPAN,CH_MAN,PR_WEIGHT","Rolling the zero-rate policy back"),
(999,"Japan benchmark-rate chart again: 'now sits around 1%'","chart screenshot; caption","SS_RATE_CHART","Japan's rate now sits around 1 %"),
(1085,"Central-bank building and US-map character with a 'Fed funds target 3.50-3.75 %' bubble","building; map character; bubble; caption","PR_BANK,CH_USMAP,OV_BUBBLE","America sits between 3.5 and 3.75 %"),
(1198,"'1%' and '3.5-3.75%' with red down arrows and a stunned face","text; red arrows; face; caption","TY_RED,OV_REDARROW,CH_FIG","That gap is the entire story"),
(1265,"Dollar note; a red X crosses it","dollar note; red X; caption","PR_DOLLAR,OV_REDX","Because capital doesn't catch feelings"),
(1322,"Woman with a 'One last chance pls?' bubble: 'it's not your clingy ex-girlfriend'","woman; bubble; caption","CH_WOMAN,OV_BUBBLE","Capital is not your clingy ex"),
(1377,"Figure with a dollar note between two grey men holding money: 'capital goes wherever it gets paid the most'","figures; notes; caption","CH_FIG,CH_OFFICIAL,PR_CASH","Capital goes where it gets paid the most"),
(1455,"Yen notes stack up beside a man holding a dollar note: 'investors dump the yen, chase the higher yield in dollars'","yen notes; man; dollar note; caption","PR_CASH,CH_MAN","Investors dump the yen and chase dollar yields"),
(1550,"Cliff scene: a yen note slides to the edge and drops","cliff; yen note; caption","PHOTO_CLIFF,PR_CASH","Drive the currency off a cliff"),
(1602,"Close-up of the green US-map character holding a dollar note","map character; note; caption","CH_USMAP,PR_DOLLAR","Because the US dollar"),
(1638,"Dollar note; yen, euro, yuan, real and rupee notes pop in; a globe character pops in","notes; globe character; caption","PR_DOLLAR,PR_CASH,CH_EARTH","Sits on one side of nearly 90 % of currency trades"),
(1757,"Dollar bag and yen bag; the dollar bag leaves: 'buying yen almost always means selling dollars'","two bags; caption (end)","PR_BAG","Buying yen almost always means selling dollars")])
A.event("S01",4,4,"POP_IN","bar chart","Debt-to-GDP bar chart appears under the headline in one frame.","SE001; ev_01",conf="HIGH")
A.event("S01",103,109,"POP_IN","globe character","Globe character with eyes appears at the right between f100 and f109 (stage active f88-110).","SE005; ev_01",conf="MEDIUM",amb="exact frame within f100-109 not isolated")
A.event("S02",276,285,"OVERLAY_POP","red '13T'","Red '13T' appears over the chart's right end (first red ink at f276, steady by f285).","SE; color_red",conf="MEDIUM",label="MEASURED")
A.event("S02",350,350,"OVERLAY_POP","red '122.3T total budget'","Red '122.3T' label appears at the left of the chart in one frame (red ink 14 to 50 px).","SE; color_red",conf="HIGH",label="MEASURED")
A.event("S03",454,495,"POP_IN","DEBT papers","DEBT papers pop onto the left one after another (f454, f458-465, f469-474, f493-495), four to five papers in all.","SE016-021; ev_01",conf="MEDIUM")
A.event("S05",654,654,"CAPTION_CHUNK_CHANGE","blackboard text","Board text changes from 'But why???' to 'The old math again!' (between f630 and f660, small stage change at f654).","SE029; overview",conf="LOW",amb="frame inferred from the stage series")
A.event("S07",882,883,"POP_IN","'0' weight","Weight labelled '0' appears next to the figures in 1-2 frames.","SE037; overview",conf="MEDIUM")
A.event("S09",1132,1132,"OVERLAY_POP","bubble 'Fed funds target 3.50-3.75%'","Speech bubble appears at the central-bank building in one frame.","SE047; ev_01",conf="MEDIUM")
A.event("S10",1198,1217,"POP_IN","red down arrows","First red arrow appears at f1198 and more follow (six by f1245) over the next frames; red area reaches 95 % by f1217 and the six-arrow row by f1245-1260.","color_red; SE051-052",conf="MEDIUM",label="MEASURED")
A.event("S10",1260,1260,"POP_IN","stunned face","Stunned face appears under the arrows in one frame.","SE052; ev_01",conf="MEDIUM")
A.event("S11",1301,1301,"OVERLAY_POP","red X","Red X appears over the dollar note in one frame (0 to 363 red px) and is removed at the cut f1320-1321.","SE055; color_red",conf="HIGH",label="MEASURED")
A.event("S14",1482,1528,"POP_IN","yen notes","Yen notes stack up one at a time (f1482, f1488, f1495, f1506, f1528).","SE067-071; ev_01",conf="MEDIUM")
A.event("S14",1547,1549,"POP_IN","man and dollar note","Man and dollar note appear on the right in 1-3 frames.","SE072; ev_01",conf="MEDIUM")
A.event("S15",1556,1601,"PROP_DRIFT","yen note","Yen note slides along the cliff to the edge and falls out of frame over ~45 frames; path not tracked.","SE073; ev_01",conf="MEDIUM",amb="path and easing not measured")
A.event("S17",1682,1688,"POP_IN","currency notes","Euro, yuan, real and rupee notes pop beside the dollar note within a few frames.","SE077; overview",conf="MEDIUM")
A.event("S17",1737,1737,"POP_IN","globe character","Globe character appears at the lower left in one frame.","SE080; ev_01",conf="HIGH")
A.event("S18",1814,1827,"PROP_DRIFT","dollar bag","Dollar bag leaves the frame to the left over ~14 frames, leaving the yen bag.","SE083; overview",conf="MEDIUM")
A.event("S13",1384,1400,"PROP_DRIFT","notes thrown by the grey men","Banknotes move between the two grey men and the central figure over ~17 frames; path not tracked.","SE059; ev_01",conf="LOW",amb="path and easing not measured")
A.fill_small(172)
A.write(headline="why japan s**** economy is now our problem")
