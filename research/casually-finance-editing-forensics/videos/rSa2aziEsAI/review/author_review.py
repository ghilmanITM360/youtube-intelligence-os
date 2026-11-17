import sys, json; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('rSa2aziEsAI',1815)
A.scenes([
(0,"Japan-map character with a yen moneybag and bond papers; bubble 'Don't worry Japan, I'll buy it!' is replaced by 'Omg thank you Japan!!!' as the character walks across: 'it's a country that solved its debt problem by buying its own debt'","map character (walk); moneybag; bond papers; bubbles; typed caption","CH_JAPAN,PR_BAG,PR_BOND,OV_BUBBLE","Japan bought its own debt"),
(108,"Dark red vignette with a monster silhouette behind the Japan-map character: 'they're trapped by a financial monster of their own creation'","red glow; monster silhouette; map character; typed caption","FX_REDGLOW,CH_JAPAN","Trapped by a monster of their own making"),
(227,"MacroMicro chart 'Japan - Benchmark Interest Rate' whose line is drawn in with a tooltip: 'to hold borrowing costs at zero for that long'","line chart (draw-on); tooltip; typed caption","SS_RATE_CHART","Borrowing costs held at zero"),
(301,"Bank of Japan building with a yen moneybag and bond papers; the bag moves down to the papers: 'the Bank of Japan had to buy its own government's bonds'","building; moneybag; bond papers; typed caption","PR_BLDG,PR_BAG,PR_BOND","The BoJ buys government bonds"),
(379,"Japan-map character with swirl eyes and tentacles in front of a full-page pile of semi-transparent bond papers; red 'trillions': 'trillions of yen of them, year after year'","map character; paper pile; red caption","CH_JAPAN,PR_BOND,TY_RED","Trillions of yen of bonds"),
(456,"Bar chart 'BOJ Is Dominant Investor in Japan's Bonds' pans left while red boxes are drawn on the BOJ row and its 52.0 %; a bond paper pops and the map character rises: 'until it owned about half of the entire Japanese government bond market'","bar chart (pan); red boxes; bond paper; map character","SS_BOJ_CHART,OV_REDBOX,PR_BOND,CH_JAPAN","The BoJ owns half the market"),
(551,"Full MacroMicro chart of the Japan benchmark rate whose line is drawn in; a stick figure rises at the lower left and gold coins pop at the top: 'and those bonds pay almost nothing, because paying nothing was the entire point'","line chart (draw-on); figure; coins; typed caption","SS_RATE_CHART,CH_FIG,PR_COINS","The bonds pay almost nothing"),
(684,"Yen notes pop in one by one until a pile slides off to the right; a stick figure with pink sunglasses and a briefcase pops in and a heart with a dollar note appears: 'so investors dump the yen, chase the higher yield in dollars'","yen notes; figure; heart; typed caption","PR_CASH,CH_FIG,PR_BRIEFCASE,PR_HEART","Investors dump the yen"),
(785,"Blue-sky cliff scene; a yen note slides off the edge and falls with a tiny red 'HELP ME': 'and drive the currency off a cliff'","cliff background; yen note; typed caption","FX_CLIFF,PR_CASH","The yen goes off a cliff"),
(847,"White page, a peeking figure; a rich man in a top hat and sunglasses rises in a red armchair and a bubble 'This s#!t is easy!' pops: 'which is usually where the armchair economists show up and ask'","figure; rich man in armchair; bubble; typed caption","CH_FIG,CH_RICHMAN,OV_BUBBLE","Armchair economists ask"),
(939,"A man under a large bubble that shows the Japan-map character, a green arrow, then 'The gap 1% / 3.5-3' and 'Problem solved!': 'why doesn't Japan just raise interest rates and close the gap? Problem solved'","figure; large bubble; arrow; text","CH_FIG,OV_BUBBLE,OV_GREENARROW,TY_RED","Why not just raise rates?"),
(1068,"Reality-TV meme clip of a woman captioned 'I CAN'T DO THIS RIGHT NOW' above the swirl-eyed map character: 'and it's because they can't'","clip; map character; typed caption","FX_CLIP_MEME,CH_JAPAN,TY_RED","They can't"),
(1106,"Bank of Japan building, then three bank buildings pop in each with a yen note and notes flow up to the central bank; a bubble with an orange coin pops: 'but the cash commercial banks park at the Bank of Japan get paid whatever the central bank's rate is'","building; bank buildings; yen notes; bubble; coin","PR_BLDG,PR_BANKS,PR_CASH,PR_COIN,OV_BUBBLE","Banks are paid the central bank's rate"),
(1263,"Large Bank of Japan building and an orange percent coin that rises to the upper right with a green up-arrow; red 'The gap 1% / 3.5-3.75%' pops and a note with a check: 'so the moment the Bank of Japan raises rates to close the gap'","building; coin; arrow; gap text; note","PR_BLDG,PR_COIN,OV_GREENARROW,TY_RED,PR_CASH","Raising rates to close the gap"),
(1396,"Bank of Japan building above three banks with yen notes flowing between them: 'and save the yen, it starts paying out trillions of yen in interest'","building; banks; notes (flow); typed caption","PR_BLDG,PR_BANKS,PR_CASH","The BoJ pays out trillions"),
(1471,"Percent coin above the building and a pile of large yen notes; bubbles 'Who decided on this low rate????' and 'Oh wait it was me...': 'while still collecting almost nothing on the pile it's stuck holding'","coin; building; notes; bubbles","PR_COIN,PR_BLDG,PR_CASH,OV_BUBBLE","It still collects almost nothing"),
(1571,"Frowning stick figure above a CFI 'Net Interest Income' page and a 3-D green-shirted character with 'OH S#!T NOT THE BAD MATH AGAIN!'; red 'that's a horrible deal': 'you don't need to have a degree in central banking to know that's a horrible deal'","figure; article page; 3-D character; red text","CH_FIG,SS_CFI_PAGE,CH_3D,TY_RED","A horrible deal"),
(1673,"Japan-map character with a shield and a moneybag above it; bond papers pop at the lower right and red crosses cover both: 'so Japan can now either defend the yen or it can afford the debt. It can't do both'","map character; shield; moneybag; bond papers; red crosses","CH_JAPAN,PR_SHIELD,PR_BAG,PR_BOND,OV_REDX","Defend the yen or afford the debt")])

# --- S01 ---
A.event("S01",53,67,"PROP_DRIFT","Japan-map character","Character walks from the upper left across and down to the centre over ~15 frames (stage px 3000-4200 per frame on f62-67; 4936 px peak) while the caption restarts with 'by buying its own debt.' (f57).","SE001",conf="MEDIUM",label="MEASURED",amb="path and gait not measured")
A.event("S01",67,67,"OVERLAY_POP","bubble 'Omg thank you Japan!!!' and yen notes","Bubble and two yen notes appear in the last frame of the walk (f67); the earlier bubble 'Don't worry Japan, I'll buy it!' is gone by f55.","SE001; sheet f65-67",conf="MEDIUM",label="DIRECTLY_OBSERVED",amb="exact pop frame inside the move not isolated")
# --- S02 ---
A.event("S02",109,226,"OVERLAY_CLIP_LOOP","red glow, monster silhouette and map character","The dark-red vignette, the monster silhouette and the map character change on every frame for 118 frames (228-2660 changed px per frame); the bright-red area grows from 0 to 824 px over f108-128 and from 824 to 1532 px over f148-222. Mechanism (animated overlay clip versus character loop) is not resolved; the glow starts at the cut.","stage px f109-226; color_red",conf="MEDIUM",label="MEASURED",mclass="COMPLEX",amb="clip versus loop not resolved; origin unknown")
A.E[-1]["measure"]="color_red.json"
# --- S03 ---
A.event("S03",228,261,"STROKE_REVEAL","rate-chart line","Chart line is drawn in over ~34 frames (ink growth fits ease-in-out, SUPPORTED, margin 0.039; teal-line area 15 to 99 px on f232-251), starting 0.4 s after the cut.","extent_228_261; color_lgreen",conf="HIGH",label="MEASURED")
A.E[-1]["easing"]="ease_in_out_smoothstep (SUPPORTED, margin 0.039)"; A.E[-1]["measure"]="extent_228_261.json"
# --- S04 ---
A.event("S04",324,359,"PROP_DRIFT","yen moneybag","Moneybag moves down from the building to the bond papers over ~36 frames (3469 px peak); the green paper area falls from 2418 to 274 px on f332-356 as the papers leave.","SE005; color_lgreen",conf="MEDIUM",label="MEASURED",amb="path and easing not measured")
A.E[-1]["measure"]="color_lgreen.json"
# --- S05 ---
A.event("S05",380,455,"CHARACTER_LOOP_ANIMATION","bond-paper pile and swirl-eyed map character","Semi-transparent bond papers multiply into a full-page pile while the map character with swirl eyes and tentacles wobbles; every frame changes 21000-33000 px (37-58 % of the frame) for 76 frames, with no duplicate frames, until the f456 cut. Frame-to-frame change is too large to separate the paper layer from the character.","stage px f380-455",conf="MEDIUM",label="MEASURED",mclass="COMPLEX",amb="paper layer and character not separated")
# --- S06 ---
A.event("S06",458,495,"STROKE_REVEAL","red boxes on the BOJ row and its 52.0 %","Red boxes are drawn in two strokes: red area 0 to 152 px on f458-475 (around the BOJ row) and 152 to 311 px on f478-495 (around the 52.0 % value), starting 0.5 s after the cut.","color_red",conf="MEDIUM",label="MEASURED",amb="which box belongs to which stroke read from the sheet")
A.E[-1]["measure"]="color_red.json"
A.event("S06",467,485,"CAMERA_SCROLL_ZOOM","bar chart","Chart shifts left by about 94 px at the 180-px analysis size (0.52 frame widths) over 18 frames, ~5 px per frame (row cross-correlation of the title: 17, 22, 22, 22 and 11 px per 3-4 frames), revealing the 52.0 % end of the BOJ bar; the camera tracker returned no net motion on this repetitive chart.","row cross-correlation f467-485",conf="MEDIUM",label="MEASURED",geo="image shift about -94 px at 180-px analysis size (cross-correlation, not tracker)",amb="constant speed vs easing not resolved")
A.event("S06",510,513,"POP_IN","bond paper","Large bond paper pops in at the lower right within 4 frames (4659 px; green area 0 to 2424 px on f510-513), 1.7 s before ... at the caption words 'until it owned about half'.","SE008; color_lgreen",conf="HIGH",label="MEASURED")
A.E[-1]["desc"]="Large bond paper pops in at the lower right within 4 frames (4659 px; green area 0 to 2424 px on f510-513), 0.6 s before ASR 'half' (15.84 s)."
A.E[-1]["measure"]="color_lgreen.json"
A.event("S06",517,531,"CHARACTER_RISE_IN","Japan-map character","Map character rises into the lower right from the bottom edge over ~15 frames (4272 px peak).","SE009",conf="MEDIUM",label="MEASURED",amb="path and easing not measured")
# --- S07 ---
A.event("S07",558,598,"STROKE_REVEAL","benchmark-rate line","Chart line is drawn in over ~41 frames (teal-line area 78 to 209 px on f558-598; ink growth over f552-591 fits linear but is AMBIGUOUS, margin 0.0035), while the caption 'And those bonds pay almost nothing' is typed.","extent_552_591; color_lgreen",conf="MEDIUM",label="MEASURED")
A.E[-1]["easing"]="linear (AMBIGUOUS, margin 0.0035)"; A.E[-1]["measure"]="extent_552_591.json"
A.event("S07",610,610,"CAPTION_CHUNK_CHANGE","caption block","Caption restarts with 'because paying nothing was the entire point.' (2781 px at f610), 0.2 s before ASR 'because' (20.48 s).","SE012",conf="HIGH",label="MEASURED")
A.event("S07",618,633,"CHARACTER_RISE_IN","stick figure","Stick figure rises from the lower left over ~16 frames (3992 px peak) and settles at the left of the chart.","SE013",conf="MEDIUM",label="MEASURED",amb="path and easing not measured")
A.event("S07",646,660,"POP_IN","gold coins","Gold coins appear at the top right in two steps: f646 (yellow 0 to 138 px) and f660 (+139 px), 14 frames apart.","SE014; color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S07",664,674,"OVERLAY_POP","chart tooltip","Chart tooltip ('January 2024 ... Benchmark Interest Rate: -0.10') appears at the right end of the line in a few steps over ~11 frames (866 px peak); tooltip text read at low size.","SE014",conf="LOW",label="DIRECTLY_OBSERVED",amb="step frames not isolated; text read from the sheet")
# --- S08 ---
A.event("S08",684,704,"POP_IN","yen notes","Yen notes pop in one at a time and pile up: f684/685, f686, f691, f695, f699 and f704 (1388-1498 px per pop; gaps of 4-5 frames, about 7 notes per second).","SE015-019",conf="HIGH",label="MEASURED",amb="note count read from the sheet")
A.event("S08",711,720,"PROP_DRIFT","yen-note pile","The pile slides off to the right over 10 frames (6073 px peak).","SE020",conf="HIGH",label="MEASURED")
A.event("S08",724,724,"POP_IN","figure with pink sunglasses and briefcase","Figure and briefcase pop in together in one frame (5107 px) as the caption restarts with 'chase the higher yield in dollars,' (0.3 s before ASR 'chase', 24.42 s).","SE021",conf="HIGH",label="MEASURED")
A.event("S08",763,763,"POP_IN","heart with a dollar note","Large heart holding a dollar note pops in above the figure in one frame (8504 px; yellow 1 to 59 px).","SE022; color_yellow",conf="HIGH",label="MEASURED")
# --- S09 ---
A.event("S09",799,832,"PROP_DRIFT","yen note","A yen note slides along the cliff edge and falls out of frame over ~34 frames (1240 px peak) with a tiny red 'HELP ME'; green sky area stays 12306-13175 px.","SE024; color_lgreen",conf="MEDIUM",label="MEASURED",amb="path and falling curve not measured")
# --- S10 ---
A.event("S10",879,894,"CHARACTER_RISE_IN","rich man in a red armchair","Man in a top hat and sunglasses rises from the bottom edge over ~16 frames (8103 px peak; red armchair area 0 to 99 px on f886-894).","SE026; color_red",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_red.json"
A.event("S10",902,902,"OVERLAY_POP","bubble 'This s#!t is easy!'","Bubble pops in above the man in one frame (1742 px).","SE027",conf="HIGH",label="MEASURED")
# --- S11 ---
A.event("S11",1008,1008,"OVERLAY_POP","bubble content 'The gap 1% 3.5-3'","The bubble content changes in one frame (1787 px): the map and up-arrow are replaced by red 'The gap' with arrows and '1% 3.5 - 3' (orange arrow area 127 to 0 px).","SE031; color_orange",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_orange.json"
A.event("S11",1040,1040,"OVERLAY_POP","bubble text 'Problem solved!'","'Problem solved!' and a changed gap line appear in one frame (2943 px) as the figure's arms change pose; ASR 'Problem' 34.88 s = f1046.","SE033",conf="HIGH",label="MEASURED")
# --- S12 ---
A.event("S12",1068,1105,"VIDEO_CLIP_INSERT","reality-TV meme clip","Clip of a woman updates every 2 frames (f1073, 1075, ..., 1089, then a 3-frame gap, 1092, ..., 1104): about 15 pictures per second on a 30 fps timeline; origin UNKNOWN.","SE035; clip update frames",conf="HIGH",label="MEASURED",mclass="INDET",amb="clip identity unknown")
# --- S13 ---
for f,px in ((1127,1966),(1137,2073),(1147,1931)):
    A.event("S13",f,f,"POP_IN","bank building with a yen note","Grey bank building with a yen note pops in in one frame (%d px); three banks land at f1127, f1137 and f1147 (gaps of 10 frames)."%px,"SE036-038",conf="HIGH",label="MEASURED")
A.event("S13",1164,1188,"PROP_DRIFT","yen notes","Yen notes travel from the banks up to the central-bank building over ~25 frames (2362 px peak) and stack on it; the caption restarts with 'get paid whatever the central bank's rate is.' at f1188.","SE039",conf="MEDIUM",label="MEASURED",amb="individual note paths not measured")
A.event("S13",1213,1213,"OVERLAY_POP","bubble with an orange coin","Bubble containing an orange percent coin pops in one frame (915 px; orange 0 to 229 px).","SE040; color_orange",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_orange.json"
# --- S14 ---
A.event("S14",1306,1329,"PROP_DRIFT","orange percent coin","Coin rises from the building to the upper right over ~24 frames (2961 px peak; orange area 663 to 892 px on f1308-1319) while a green up-arrow pops at the upper left at f1306.","SE043; color_orange",conf="MEDIUM",label="MEASURED",amb="path and easing not measured; arrow pop frame read from the sheet")
A.E[-1]["measure"]="color_orange.json"
A.event("S14",1363,1363,"POP_IN","yen note with a green check","Yen note with a green check mark pops in beside the building in one frame (835 px), 0.6 s after ASR 'gap' (44.82 s).","SE044",conf="HIGH",label="MEASURED")
# --- S15 ---
A.event("S15",1397,1470,"PROP_DRIFT","yen notes between the building and the banks","Yen notes drift from the central bank toward the three banks and out of frame over 74 frames (stage px 15609 at the f1471 cut); the caption 'it starts paying out trillions of yen in interest' is typed beneath (ASR 'trillions' 47.26 s = f1417.8).","SE045",conf="LOW",label="DIRECTLY_OBSERVED",mclass="CONV",amb="individual note paths and counts not measured")
# --- S16 ---
A.event("S16",1492,1492,"OVERLAY_POP","bubble 'Who decided on this low rate????'","Bubble pops in beside the building in one frame (1049 px).","SE046",conf="HIGH",label="MEASURED")
A.event("S16",1535,1535,"OVERLAY_POP","bubble 'Oh wait it was me...'","Second bubble replaces the first in one frame (507 px).","SE047",conf="HIGH",label="MEASURED")
# --- S17 ---
A.event("S17",1634,1637,"OVERLAY_POP","red 'that's a horrible deal'","Red hand-lettered 'that's a horrible deal' appears in 4 frames (red 77 to 294 px; 2097 px at f1634), 0.4 s before ASR 'horrible' (54.86 s).","SE050; color_red",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_red.json"
# --- S18 ---
A.event("S18",1717,1717,"POP_IN","moneybag over the shield","Yen moneybag appears above the shield in one frame (1428 px).","SE055",conf="HIGH",label="MEASURED")
A.event("S18",1756,1756,"POP_IN","bond papers","Two bond papers pop in at the lower right in one frame (4342 px; green area 0 to 2053 px), 0.2 s after ASR 'afford' (58.34 s).","SE057; color_lgreen",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_lgreen.json"
A.event("S18",1796,1796,"OVERLAY_POP","red crosses","Red crosses appear over the bag-and-shield and over the papers in one frame (red 0 to 1636 px; 2271 px), 0.4 s after ASR 'can't' (59.48 s).","SE059; color_red",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_red.json"
A.fill_small(172)
A.E=[e for e in A.E if not (e['op']=='UNRESOLVED_CHANGE' and ('CUT' in e['desc'] or 'BIG_POP' in e['desc']) and any(e['f0']-2<=s['f0']<=e['f1']+2 for s in A.S))]
A.write(headline=None)
