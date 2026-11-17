import sys, json; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('PxgCsLSf-w4',1557)
A.scenes([
(0,"White page with a large persistent '30 years' title and a small typed caption ('is long enough that no election survives it, no Fed chair, no news cycle, no administration, which means a 30-year rate isn't a reaction to a headline'); a head, a Fed chair, a newspaper reader, a flag, a stick figure and a percent coin peek in and out; a 'BREAKING NEWS' paper pops and gets a red X","title; typed caption; peek-in characters; flag; coin; news paper; red X","TY_TITLE,CH_PRESIDENT,CH_OFFICIAL,CH_NEWSREADER,PR_FLAG,CH_FIG,PR_PCTCOIN,PR_NEWSPAPER,TY_RED","30 years outlasts every election"),
(239,"Phone screen with a green chat bubble 'how do u really feel about me' and a reply bubble 'u suck': 'it's the closest thing there is to an honest opinion on a country'","phone; chat bubbles","PR_PHONE,OV_BUBBLE","The rate as an honest opinion"),
(300,"Close-up of the US-map character holding a phone (20 frames)","map character (close-up); phone","CH_USMAP,PR_PHONE","The country on the phone"),
(320,"A black '?' disc inside two red circular arrows with moneybags, BILL papers and the walking US-map character around it; the whole picture enlarges and the disc fades into an Investopedia 'Treasury Yield' card: 'and sitting in the middle of it is the number everybody's talking about, the 30-year Treasury yield'","red ring; '?' disc; moneybags; papers; map; definition card","OV_RING,PR_BAGS,PR_PAPER,CH_USMAP,SS_INVESTOPEDIA","The number everybody is talking about"),
(447,"Investopedia 'Treasury Yield' definition card above a pointer stick figure: 'it's important because it acts as a gauge for the economy'","definition card; figure; typed caption","SS_INVESTOPEDIA,CH_FIG","The yield as a gauge"),
(479,"A gauge dial with a red sector and a stick figure leaning in from the upper left: 'as a gauge for the economy'","gauge; figure; typed caption","PR_GAUGE,CH_FIG","The gauge"),
(516,"Pointer stick figure with a typed caption; red up-arrows with angry eyes, cash, a LAW paper and four moneybags come and go: 'it captures structural economic conditions like long-run inflation expectations, monetary policy decisions, and potential economic growth'","figure; typed captions; prop parade","CH_FIG,OV_REDARROWS,PR_CASH,PR_LAW,PR_BAGS","What the yield captures"),
(705,"White page: 'and right now, it seems like every country across the world is losing control'; a blue 30-year yield chart and an orange chart pop in with tooltips, then the top chart swaps to a Japan long-bond chart","charts (pop-in); tooltips; typed caption","SS_YIELD_CHART,SS_GERMANY_CHART,SS_JAPAN_CHART","Every country is losing control"),
(807,"Country-map characters (a French map, a Japan map with swirl eyes, a small US map and a UK/Europe blob) wobble together: 'and the country sitting in the eye of the storm'","map characters (loop); typed caption","CH_MAPS,CH_USMAP","The country in the eye of the storm"),
(854,"Close-up of the US-map character with big eyes and legs; a small text 'f*ck me, not again' appears over it: 'is the United States'","map close-up; small text; typed caption","CH_USMAP","The United States"),
(889,"Stick figure with a smirk: 'but we need to back up first'","figure; typed caption","CH_FIG","But we need to back up first"),
(930,"Blank page, then a CNBC article card ('30-year Treasury yield tops 5.33%, new 19-year high, on inflation and spending concerns') slides in from the left; a percent coin and a bond paper pop in and the coin grows; red words 'in 19 years': 'on August 18th, the 30-year touched the highest level in 19 years'","article card (slide-in); coin; bond paper; red caption","SS_CNBC_CARD,PR_PCTCOIN,PR_BOND,TY_RED","The 30-year hit a 19-year high"),
(1038,"Treasury auction-results page with the pointer figure rising from the bottom; the page scrolls and red ink is added: 'a few days ago, the United States government went out to borrow $22 billion of 30-year debt'","document page; figure; red ink; typed caption","SS_TREASURY_DOC,CH_FIG,TY_RED,TY_YELLOW","A $22 billion 30-year auction"),
(1176,"Blank page with the figure (shocked, then hand on chin); a green map character slides in from the top right: 'the problem was, at what cost?'","figure; map character; typed caption","CH_FIG,CH_USMAP","At what cost?"),
(1232,"Treasury auction-results page again with the pointer figure; the page moves, a yellow highlight sweeps 'High Yield', a red ellipse is drawn and red '5.3%' pops: 'the sale cleared at a high yield a little over 5.3%'","document page; figure; highlight; red ellipse; red text","SS_TREASURY_DOC,CH_FIG,OV_HIGHLIGHT,TY_RED","Cleared at 5.3 %"),
(1320,"A green 'United States Treasury' bond paper; moneybags pile in from the lower right until they cover the page; red 'since 2001': 'the most expensive government bond sale of its kind since 2001'","bond paper; moneybags (pile-up); red text","PR_BOND,PR_BAGS,TY_RED","The most expensive sale since 2001"),
(1409,"The US-map character with eyes; a dark Reuters news card slides in at the bottom, DEBT papers pop in until they pile up and a red '$40T' appears: 'this comes a few weeks after America became the first country in history to cross $40 trillion in national debt'","map character; news card (slide-in); DEBT papers; red text","CH_USMAP,SS_REUTERS_CARD,PR_DEBTDOC,TY_RED","$40 trillion crossed"),
(1554,"Blank white page for the last 3 frames","blank page","","End card")])

# --- S01 ---
A.event("S01",40,49,"SLIDE_IN","blond head with a red tie","Head enters from the right edge over ~10 frames (orange 0 to 180 px, yellow 0 to 77 px on f40-49) beside the caption word 'election' (ASR 1.78 s = f42.7); holds to f58.","SE002; color_orange; color_yellow",conf="MEDIUM",label="MEASURED",amb="path and easing not measured; character identity not asserted")
A.event("S01",59,67,"PROP_DRIFT","blond head with a red tie","Head leaves to the right over ~9 frames (yellow 78 to 0 px on f59-66, orange 174 to 0 on f63-65).","SE004; color_yellow",conf="MEDIUM",label="MEASURED")
A.event("S01",70,70,"CAPTION_CHUNK_CHANGE","caption 'no election survives it,'","Caption chunk is cleared in one frame (1162 px); the next chunk 'no' starts at f76.","SE005",conf="HIGH",label="MEASURED")
A.event("S01",77,83,"SLIDE_IN","grey-haired Fed-chair figure","Figure with a green tie enters from the left edge over ~7 frames (1509 px peak) at ASR 'Fed' (3.38 s = f81.1); holds to f89.","SE006",conf="MEDIUM",label="MEASURED",amb="path and easing not measured")
A.event("S01",90,93,"PROP_DRIFT","Fed-chair figure","Figure leaves to the left edge over 4 frames (2081 px peak).","SE007",conf="MEDIUM",label="MEASURED")
A.event("S01",104,112,"CHARACTER_RISE_IN","newspaper reader","Man behind a newspaper rises from the bottom edge over ~9 frames (6896 px peak), 0.07 s before ASR 'news' (4.4 s = f105.6).","SE009",conf="HIGH",label="MEASURED")
A.event("S01",126,137,"PROP_DRIFT","newspaper reader","Reader lowers out of the bottom edge over ~12 frames (6697 px peak) at the caption chunk 'no administration,'.","SE010",conf="HIGH",label="MEASURED")
A.event("S01",143,156,"PROP_DRIFT","US flag","Flag on a pole enters at the top left, tumbles to the lower right and leaves the frame over ~14 frames (2366 px peak) while rotating; it appears 0.4 s after ASR 'administration,' (5.54 s).","SE011",conf="MEDIUM",label="MEASURED",amb="rotation and path not measured; drift plus rotation not separated")
A.event("S01",172,178,"SLIDE_IN","stick figure peeking from the left","Figure enters from the left edge over ~7 frames and holds at the upper left to f238 (image read from sheet).","SE014",conf="MEDIUM",amb="path and easing not measured")
A.event("S01",173,192,"SLIDE_IN","orange percent coin","Percent coin enters at the right edge and rolls leftward while rotating over ~20 frames (orange area 0 to 679 px on f172-192; stage px 534-2181 per frame on f173-182); it settles near the lower right.","SE014; color_orange",conf="MEDIUM",label="MEASURED",amb="path, rotation and easing not measured")
A.event("S01",211,211,"POP_IN","'BREAKING NEWS!!!' paper","Newspaper paper pops in at the upper right in one frame (1386 px), 0.5 s before ASR 'headline.' (9.32 s).","SE016",conf="HIGH",label="MEASURED")
A.event("S01",226,226,"OVERLAY_POP","red X over the news paper","Red X appears over the paper in one frame (0 to 286 red px, 438 stage px), 0.1 s after ASR 'headline.' (9.32 s).","SE018; color_red",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_red.json"
# --- S02 ---
A.event("S02",268,268,"OVERLAY_POP","reply bubble 'u suck'","Second chat bubble 'u suck' pops in under the first in one frame (1102 px), at ASR 'honest' (11.76 s = f282.2; 0.6 s earlier).","SE020",conf="HIGH",label="MEASURED")
# --- S04 ---
A.event("S04",321,446,"CAMERA_PUSH_IN","ring, '?' disc, props and map (whole composition)","Whole composition enlarges x1.61 about the centre over 126 frames (about 4.3-4.4 k stage px per frame at the start); no pan (net shift -0.03,-0.25 px); scale fit linear but AMBIGUOUS (margin 0.0045); the red ring area grows from 0 to 2399 px (f320-356) and 2405 to 4052 px (f392-424).","camera_321_446; color_red",conf="HIGH",label="MEASURED",geo="net scale x1.614; image shift (-0.03,-0.25) px at 180-px analysis size")
A.E[-1]["easing"]="scale linear (AMBIGUOUS, margin 0.0045)"; A.E[-1]["measure"]="camera_321_446.json"
A.event("S04",400,426,"OPACITY_FADE","'?' disc into the Investopedia card","Black '?' disc becomes translucent grey (f410), light grey (f420) and disappears by f426 while the 'Treasury Yield' card shows through it; the caption 'the 30-year Treasury yield' types over f395-426.","ring.png (f400,f410,f415,f420,f426)",conf="MEDIUM",mclass="INDET",amb="fade versus cross-fade of two layers not resolved; opacity curve not measured")
# --- S07 ---
A.event("S07",569,569,"CAPTION_CHUNK_CHANGE","caption block","Caption 'it captures structural economic conditions like' is cleared in one frame (1284 px); 'long-run' begins at f571.","SE031",conf="HIGH",label="MEASURED")
A.event("S07",572,582,"SLIDE_IN","three red up-arrows with angry eyes","Arrow-and-eyes group enters from the right edge and moves left to the upper centre over ~11 frames (red 0 to 746 px on f572-582), 0.4 s before ASR 'long' (23.84 s)... no: ASR 'long' 23.84 s = f572.2, the group starts at that word.","SE031; color_red",conf="MEDIUM",label="MEASURED",amb="path and easing not measured")
A.E[-1]["desc"]="Arrow-and-eyes group enters from the right edge and moves left to the upper centre over ~11 frames (red 0 to 746 px on f572-582), starting at ASR 'long' (23.84 s = f572.2)."
A.E[-1]["measure"]="color_red.json"
A.event("S07",603,611,"PROP_DRIFT","red arrows with angry eyes","Group leaves to the left over ~9 frames (red 746 to 0 px on f603-611).","SE033; color_red",conf="MEDIUM",label="MEASURED")
A.event("S07",614,614,"POP_IN","banknotes","Green banknotes pop in at the upper left in one frame (1165 px).","SE033",conf="HIGH",label="MEASURED")
A.event("S07",626,635,"SLIDE_IN","LAW paper","Paper marked 'LAW' enters from the right edge and settles at the upper right over ~10 frames (3293 px peak); the caption restarts with 'monetary' at f624 (ASR 'monetary' 25.94 s = f622.6).","SE035",conf="HIGH",label="MEASURED",amb="path and easing not measured")
A.event("S07",653,659,"PROP_DRIFT","banknotes and LAW paper","Banknotes and the LAW paper leave to the right over ~7 frames (8219 px peak; yellow 64 to 0 px on f653-657).","SE037; color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S07",677,688,"POP_IN","four moneybags","Moneybags pop in one after another at the upper left: f677, f681, f684, f688 (yellow area 0 to 75, 153, 232, 304 px; gaps 4, 3 and 4 frames); the last bag lands 30 ms after ASR 'growth.' (28.64 s).","SE039-040; color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
# --- S08 ---
A.event("S08",726,727,"POP_IN","blue 30-year yield chart","Blue chart appears at the top in one step (1626 px at f726) under the caption 'and right now,'.","SE042",conf="HIGH",label="MEASURED")
A.event("S08",737,737,"POP_IN","orange Germany chart","Orange chart appears at the bottom in one frame (1490 px; orange 0 to 121 px, yellow 0 to 237 px).","SE043; color_orange; color_yellow",conf="HIGH",label="MEASURED")
A.event("S08",763,763,"OVERLAY_POP","tooltip '4.7016%'","Chart tooltip appears over the blue chart in one frame (2039 px), 0.4 s after ASR 'country' (31.2 s).","SE046",conf="MEDIUM",label="MEASURED")
A.event("S08",775,775,"OVERLAY_POP","second chart tooltip","A second tooltip appears at the left of the chart in one frame (2310 px).","SE047",conf="MEDIUM",label="MEASURED")
A.event("S08",784,786,"POP_IN","Japan long-bond chart","Top chart is replaced by a 'Japan's Long-Maturity Bonds Have Been Soaring' chart within 3 frames (3905 px at f784; orange 148 to 238, yellow 202 to 353 px), 2.2 s after ASR 'right'... see ASR 'losing' (32.58 s = f781.9).","SE049; color_orange; color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["desc"]="Top chart is replaced by a 'Japan's Long-Maturity Bonds Have Been Soaring' chart within 3 frames (3905 px at f784; orange 148 to 238, yellow 202 to 353 px), 0.1 s after ASR 'losing' (32.58 s = f781.9)."
A.E[-1]["measure"]="color_orange.json"
# --- S09 ---
A.event("S09",808,853,"CHARACTER_LOOP_ANIMATION","country-map characters","The map characters wobble continuously for 46 frames (3800-7300 changed px per frame, median ~5.7 k) until the f854 cut; the Japan map has swirling eyes.","stage px f808-853",conf="MEDIUM",label="MEASURED",mclass="COMPLEX",amb="individual character loops not separated")
# --- S10 ---
A.event("S10",859,859,"OVERLAY_POP","small text, first step","First step of the small white text over the map appears in one frame (light-green count 53 to 132 px at f859); the rest follows at f868.","color_lgreen",conf="MEDIUM",label="MEASURED")
A.E[-1]["measure"]="color_lgreen.json"
A.event("S10",868,868,"OVERLAY_POP","small text 'f*ck me, not again'","Small white text appears over the map in one frame (658 px; light-green count 133 to 293 px), 0.1 s after ASR 'United' (35.92 s = f862.1)... text after 'storm'.","SE051; color_lgreen",conf="HIGH",label="MEASURED")
A.E[-1]["desc"]="Small white text 'f*ck me, not again' (as lettered) appears over the map in one frame (658 px; light-green count 133 to 293 px at f868), 0.25 s after ASR 'United' (35.92 s)."
A.E[-1]["measure"]="color_lgreen.json"
A.event("S10",888,888,"CAPTION_CHUNK_CHANGE","caption block","Caption is cleared and restarts with 'But' one frame (41.7 ms) before the picture changes at f889 (1379 px at f888, 35492 px at f889).","stage px f888=1379, f889=35492",conf="HIGH",label="MEASURED")
# --- S12 ---
A.event("S12",934,943,"SLIDE_IN","CNBC article card","Card enters from the left edge and settles over ~10 frames: net shift +118 px at the 180-px analysis size (0.66 frame widths), pan ease-out-quad (SUPPORTED, margin 0.06-0.08, 9 samples); it starts at ASR 'August' (38.98 s = f935.5).","camera_935_944",conf="HIGH",label="MEASURED",geo="net scale x0.973; image shift (+118.0,-22.2) px at 180-px analysis size")
A.E[-1]["easing"]="pan ease_out_quad (SUPPORTED, margin 0.06-0.08, 9 samples)"; A.E[-1]["measure"]="camera_935_944.json"
A.event("S12",959,962,"POP_IN","percent coin and bond paper","Small percent coin and a green bond paper pop in at the lower right (4253 px; orange 0 to 439, yellow 0 to 52 px at f962), 0.5 s before ASR 'touched' (40.6 s).","SE055; color_orange",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_orange.json"
A.event("S12",983,1005,"SCALE_TWEEN","percent coin","Coin enlarges over ~23 frames (orange area 439 to 2345 px on f983-1005, about x2.3 in linear size).","SE057; color_orange",conf="HIGH",label="MEASURED",amb="curve not fitted")
A.E[-1]["measure"]="color_orange.json"
A.event("S12",1004,1023,"CAPTION_CHUNK_CHANGE","red caption words 'in 19 years'","Red caption words appear in steps: 'in' at f1004, '19' at f1006 (red 30 to 72 to 139 px), 'years' by f1023 (red 138 to 335 px); ASR '19' 42.12 s = f1010.9.","color_red",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_red.json"
# --- S13 ---
A.event("S13",1039,1046,"SLIDE_IN","Treasury page and pointer figure","After the cut the page and the figure rise from the bottom over ~8 frames (7100-8400 px per frame); tracker shift 188 px at the 180-px analysis size (LOW_SAMPLE, 7 frames; direction read from the sheet).","camera_1039_1046",conf="MEDIUM",label="MEASURED",geo="net scale x1.01; image shift (0.1,+187.6) px at 180-px analysis size (LOW_SAMPLE)",amb="two layers move together; easing LOW_SAMPLE")
A.E[-1]["easing"]="not resolved (LOW_SAMPLE, 7 frames)"; A.E[-1]["measure"]="camera_1039_1046.json"
A.event("S13",1063,1101,"CAMERA_SCROLL_ZOOM","Treasury auction page","Page moves vertically by about 35 px at the 180-px analysis size over ~39 frames, decelerating (ease-out-cubic SUPPORTED, margin 0.07-0.09); scale change x1.008 only.","camera_1063_1101",conf="HIGH",label="MEASURED",geo="net scale x1.008; image shift (-0.01,-35.5) px at 180-px analysis size")
A.E[-1]["easing"]="pan y ease_out_cubic (SUPPORTED, margin 0.090)"; A.E[-1]["measure"]="camera_1063_1101.json"
A.event("S13",1108,1124,"OVERLAY_POP","red ink on the page and caption","Red area jumps to 56 px at f1108 (red '$22'), grows steadily from 56 to 133 px over f1110-1122 (progressive; ellipse or typed letters not separated) and jumps +67 px at f1124 when red 'billion' appears, 0.1 s after ASR 'billion' (46.86 s).","color_red",conf="MEDIUM",label="MEASURED",amb="identity of the progressive red growth not resolved")
A.E[-1]["measure"]="color_red.json"
A.event("S13",1142,1158,"CAPTION_CHUNK_CHANGE","yellow caption words '30-year debt'","Yellow caption words appear in two steps: +198 yellow px at f1142 and +141 px at f1158 (ASR 'debt.' 48.32 s = f1159.7).","color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
# --- S14 ---
A.event("S14",1203,1213,"SLIDE_IN","green map character","Map character enters from the top-right corner over ~11 frames (2241 px peak), 0.2 s before ASR 'cost?' (50.54 s).","SE068",conf="MEDIUM",label="MEASURED",amb="path and easing not measured")
# --- S15 ---
A.event("S15",1233,1262,"CAMERA_SCROLL_ZOOM","Treasury auction page","Page shifts by about 35 px at the 180-px analysis size and scale falls to x0.975 over ~30 frames (ease-in-quad SUPPORTED on scale and both pans, margins 0.04-0.16).","camera_1233_1262",conf="MEDIUM",label="MEASURED",geo="net scale x0.975; image shift (-0.09,+34.6) px at 180-px analysis size")
A.E[-1]["easing"]="ease_in_quad (SUPPORTED on scale and pans)"; A.E[-1]["measure"]="camera_1233_1262.json"
A.event("S15",1261,1275,"HIGHLIGHT_SWEEP","'High Yield' row","Yellow highlight grows from 0 to 138 px over ~15 frames (f1261-1275), 0.1 s after ASR 'high' (52.46 s).","color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S15",1270,1281,"STROKE_REVEAL","red ellipse on the yield value","Red area grows from 12 to 47 px over f1271-1280 (about 4 px per frame, progressive draw).","color_red",conf="MEDIUM",label="MEASURED",amb="ellipse identity read from the sheet")
A.E[-1]["measure"]="color_red.json"
A.event("S15",1281,1283,"OVERLAY_POP","red '5.3%,'","Red '5.3%,' appears in one step (red 47 to 600 px, 996 stage px at f1281), 0.13 s before ASR '5' (53.5 s).","SE072; color_red",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_red.json"
# --- S16 ---
A.event("S16",1326,1375,"SLIDE_IN","moneybags","Moneybags enter from the lower right and pile up over the bond paper in about 15 steps (yellow area 0 to 5806 px over f1326-1357, steps at f1326, 1328, 1331, 1333, 1335, 1338, 1340, 1345, 1350, 1354, 1357); the first bag starts 0.1 s after ASR 'most' (55.14 s).","SE074-077; color_yellow",conf="HIGH",label="MEASURED",amb="paths of the individual bags not measured")
A.E[-1]["measure"]="color_yellow.json"
A.event("S16",1375,1380,"OVERLAY_POP","red 'since 2001'","Red 'since' appears at f1375 (red 0 to 346 px), 30 ms before ASR 'since' (57.32 s), and red '2001' follows at f1380 (346 to 723 px), 80 ms before ASR '2001.' (57.58 s).","SE077-078; color_red",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_red.json"
A.event("S16",1408,1408,"CAPTION_CHUNK_CHANGE","caption block","Caption is cleared and restarts with 'This' one frame (41.7 ms) before the picture changes at f1409 (4556 px at f1408, 55687 px at f1409).","stage px f1408=4556, f1409=55687",conf="HIGH",label="MEASURED")
# --- S17 ---
A.event("S17",1430,1440,"SLIDE_IN","Reuters news card","Dark card enters from the right edge and settles at the lower right over ~11 frames (stage px 961, 1983, 3080, 3701 on f1430-1433), at ASR 'weeks' (59.44 s = f1426.6).","SE081",conf="HIGH",label="MEASURED",amb="path and easing not measured")
A.event("S17",1501,1513,"POP_IN","DEBT papers","DEBT papers pop in under the map one after another until about eleven are piled up (f1501, 1503, 1505, 1507, 1509, 1511, 1513); the first lands 60 ms after ASR '$40' (62.48 s).","SE086",conf="MEDIUM",label="MEASURED",amb="count of papers read from the sheet")
A.event("S17",1515,1515,"OVERLAY_POP","red '$40T'","Red '$40T' appears over the paper pile in one frame (red 1 to 696 px), 0.27 s after ASR 'trillion' (62.86 s).","SE086; color_red",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_red.json"
A.fill_small(172)
A.E=[e for e in A.E if not (e['op']=='UNRESOLVED_CHANGE' and ('CUT' in e['desc'] or 'BIG_POP' in e['desc']) and any(e['f0']-2<=s['f0']<=e['f1']+2 for s in A.S))]
A.write(headline=None)
