import sys, json; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('2EZzwupIa80',1804)
A.scenes([
(0,"Green US-map character with pixel sunglasses and a bubble 'Debt? What debt?': 'nothing inside American politics forces anyone to deal with the debt'","map character; bubble; typed caption","CH_USMAP,OV_BUBBLE,OV_SUNGLASSES","Nothing forces anyone to deal with the debt"),
(89,"Congress seal above three tiny figures at a round table, bubble 'uh, what's 2+2?': 'no rule makes Congress balance a budget'","seal; table figures; bubble; typed caption","LOGO_CONGRESS,CH_FIGS,OV_BUBBLE","No rule makes Congress balance a budget"),
(146,"Two stick figures trading bubbles 'Your debt is growing!' and 'Yours too!', then shaking hands under 'we're even': 'no politician loses an election for letting the debt grow'","two figures; bubbles; typed caption","CH_FIGS,OV_BUBBLE","Nobody loses an election over debt"),
(219,"Grey-bob figure with a purple tie and a bubble 'I promise, we'll have less!'; the map character slides in at the top right: 'and nobody wins one by promising to take something away'","figure; bubble; map character; typed caption","CH_FIG,OV_BUBBLE,CH_USMAP","Nobody wins by promising less"),
(291,"Photo of Druckenmiller slides up to the top and his LinkedIn profile card rises beneath; a small admirer figure with a green briefcase pops in; green 'of all time': 'Druckenmiller is a billionaire hedge fund manager and widely considered one of the greatest investors of all time'","portrait photo; profile card; small figure; green caption","PHOTO_PORTRAIT,SS_LINKEDIN_PROFILE,CH_ADMIRER,TY_GREEN","Druckenmiller, one of the greatest investors"),
(430,"Enlarged LinkedIn profile that scrolls up to the 'Experience' section beside a pointer figure; a red box is drawn around 'Former President, Duquesne Capital Management': 'he then launched his own hedge fund, Duquesne Capital, where across nearly three decades'","profile card (scroll); figure; red box; typed caption","SS_LINKEDIN_PROFILE,CH_FIG,OV_REDBOX","He launched Duquesne Capital"),
(543,"Hustle Fund article text with a pink-faced figure holding a flower at the bottom; a yellow highlight sweeps line by line while the page pans: 'he averaged 30 percent annual returns without recording a single losing year'","article text (pan); highlight; figure","SS_HUSTLE_ARTICLE,OV_HIGHLIGHT,CH_ADMIRER","30 % a year, no losing year"),
(652,"'The Bank of England Trade' article with a Bank of England icon; the photo slides in from the lower left, yellow highlights sweep, bubbles 'XD' and 'NOT funny' pop, red 'broke': 'the 1992 trade where he became known as the investor who broke the Bank of England'","article page; bank icon; photo; bubbles; highlights; red word","SS_BOE_ARTICLE,PR_BANK,PHOTO_PORTRAIT,OV_BUBBLE,OV_HIGHLIGHT,TY_RED","The trade that broke the Bank of England"),
(860,"WSJ opinion text ('I have spent five decades trading on a simple premise...') above a stick figure with glasses at a desk with a laptop marked 'CF'; a yellow highlight follows the narration line by line while the page pans: 'His piece in the Wall Street Journal opened with...'","article text (pan); highlight; figure at desk","SS_WSJ_TEXT,OV_HIGHLIGHT,CH_ANALYST,PR_LAPTOP","The WSJ premise: prices carry information"),
(1131,"Chart '30-Year Bond Hits Highest Auction Yield Since 2001' above the map character that slides in from the left and gets a BILL paper; a pointer figure appears at the upper left: 'the rate lenders charge America, because that one arrives as a bill America has to pay for'","chart; map character; BILL paper; figure; typed caption","SS_AUCTION_CHART,CH_USMAP,PR_BILLPAPER,CH_FIG","The rate is a bill America has to pay"),
(1247,"WSJ opinion text again ('Every basis point of artificial yield suppression is a subsidy to procrastination') with the desk figure; the highlight follows the line while the page pans: 'Druckenmiller's issue is that every basis point of artificial yield suppression, he wrote, is a subsidy to procrastination'","article text (pan); highlight; figure at desk","SS_WSJ_TEXT,OV_HIGHLIGHT,CH_ANALYST,PR_LAPTOP","Yield suppression is a subsidy to procrastination"),
(1424,"A thin figure in a beanie and a long coat with folded arms; a Genius lyrics page ('His palms are sweaty, knees weak, arms are heavy ... mom's spaghetti') slides in; the coat opens to a shirt with a heart and spaghetti: 'a line so powerful, it can only be compared to the time Eminem rapped about his mom's spaghetti'","figure in beanie; lyrics page; pose swap; typed caption","CH_BEANIE,SS_GENIUS_LYRICS","A line like the mom's-spaghetti lyric"),
(1544,"WSJ opinion text ('If the 30-year must trade at 5.5% to clear, that isn't a crisis. It is an invoice...') with the desk figure; highlights and page pans follow the narration: 'then do the only thing that durably lowers long-term yields: address the primary deficit'","article text (pan); highlight; figure at desk","SS_WSJ_TEXT,OV_HIGHLIGHT,CH_ANALYST,PR_LAPTOP","It is an invoice: address the primary deficit")])

# --- S01-S04 ---
A.event("S01",35,35,"OVERLAY_POP","bubble 'Debt? What debt?'","Speech bubble pops in at the lower right in one frame (1600 px).","SE004",conf="HIGH",label="MEASURED")
A.event("S02",122,122,"OVERLAY_POP","bubble 'uh, what's 2+2?'","Small bubble pops in beside the seal in one frame (626 px).","SE010",conf="HIGH",label="MEASURED")
A.event("S03",167,167,"OVERLAY_POP","bubble 'Yours too!'","Second bubble pops in under the first in one frame (654 px).","SE014",conf="HIGH",label="MEASURED")
A.event("S03",202,202,"POSE_SWAP","two figures and bubbles","In one frame (7677 px) the two bubbles are replaced by a 'we're even' bubble and the figures change to a handshake pose (red 110 to 40 px); the caption continues.","SE017; color_red",conf="MEDIUM",label="MEASURED",amb="partial replacement inside the scene; pose change read from the sheet")
A.E[-1]["measure"]="color_red.json"
A.event("S04",248,248,"OVERLAY_POP","bubble 'I promise, we'll have less!'","Bubble pops in beside the figure in one frame (1976 px).","SE020",conf="HIGH",label="MEASURED")
A.event("S04",268,281,"SLIDE_IN","green map character","Map character enters from the top-right corner and grows over ~14 frames (2128 px peak); its eyes show at f278.","SE021",conf="MEDIUM",label="MEASURED",amb="path and easing not measured")
# --- S05 ---
A.event("S05",291,306,"SLIDE_IN","Druckenmiller photo","Photo enters from the left and moves up to the top of the page over ~16 frames (30478 px at the cut, 3469 px at f293).","SE022",conf="MEDIUM",label="MEASURED",amb="path and easing not measured")
A.event("S05",311,324,"SLIDE_IN","LinkedIn profile card","Profile card rises from the lower right and enlarges beneath the photo over ~14 frames while the caption 'Druckenmiller is a billionaire hedge fund manager' is typed.","SE022",conf="MEDIUM",label="DIRECTLY_OBSERVED",amb="path and scale not measured")
A.event("S05",345,345,"CAPTION_CHUNK_CHANGE","caption block","Caption restarts with 'and' and the profile card steps up (1600 px), 0.1 s after the ASR 'manager' (14.0 s = f336).","SE024",conf="HIGH",label="MEASURED")
A.event("S05",351,354,"POP_IN","admirer figure with green briefcase","Small figure with pink glasses, a green briefcase and the tiny text 'omg I wanna be like you' pops in at the lower left within 4 frames (1227 px).","SE025",conf="MEDIUM",label="MEASURED",amb="text read at 720p")
A.event("S05",406,413,"CAPTION_CHUNK_CHANGE","green caption words 'of all time'","Green lettering 'of all' then 'time' is typed (light-green area 0 to 464 px on f406-413); 'time' lands at f413 (17.21 s), at ASR 'time.' (17.26 s).","color_lgreen",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_lgreen.json"
# --- S06 ---
A.event("S06",431,457,"CAMERA_SCROLL_ZOOM","LinkedIn profile","Profile scrolls up by about 108 px at the 180-px analysis size (0.34 frame heights) over 27 frames at ~7 px per frame, slowing to ~1 px per frame at the end, with two repeated frames; ease AMBIGUOUS (ease-out-quad best, margin 0.002).","camera_431_457",conf="MEDIUM",label="MEASURED",geo="net scale x1.018; image shift (-5.6,-108.1) px at 180-px analysis size")
A.E[-1]["easing"]="pan y ease_out_quad (AMBIGUOUS, margin 0.002)"; A.E[-1]["measure"]="camera_431_457.json"
A.event("S06",480,505,"STROKE_REVEAL","red box on 'Former President, Duquesne Capital Management'","Red box is drawn in steps (red area 0 to 59 px on f480-488, 59 to 166 px on f492-505), starting 0.1 s after ASR 'Duquesne' (19.88 s = f477).","SE034; color_red",conf="MEDIUM",label="MEASURED",amb="stroke order not resolved")
A.E[-1]["measure"]="color_red.json"
# --- S07 ---
A.event("S07",544,638,"HIGHLIGHT_SWEEP","article lines","Yellow highlight grows from 0 to 3239 px over 95 frames across the lines 'he had generated returns that most professional investors cannot conceptually achieve: 30% annual average, no down years, across nearly three decades', while the narration reads 'he averaged 30 percent annual returns without recording a single losing year' (ASR 22.5-26.9 s = f540-646).","color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S07",545,619,"CAMERA_SCROLL_ZOOM","article page","Page pans left at a constant speed in three passes with fast linear returns: -2.6 px per frame for 23 frames (f545-567), return +5.0 for 8 (f568-575); -2.0 for 17 (f576-592), return +4.7 for 7 (f593-599); -3.0 for 15 (f600-614), return +9.1 for 5 (f615-619); speeds are in px at the 180-px analysis size.","camera_544_650",conf="HIGH",label="MEASURED",geo="three left passes of -60, -34 and -45 px with linear returns (analysis size)")
A.E[-1]["easing"]="constant velocity per pass (linear); return linear"; A.E[-1]["measure"]="camera_544_650.json"
# --- S08 ---
A.event("S08",694,716,"HIGHLIGHT_SWEEP","title 'The Bank of England Trade'","Yellow highlight grows from 0 to 411 px over 23 frames on the title.","color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S08",695,717,"SLIDE_IN","Druckenmiller photo","Photo enters from the lower left and rises to the lower left of the page over ~22 frames (3697 px peak).","SE040",conf="MEDIUM",label="MEASURED",amb="path and easing not measured")
A.event("S08",738,823,"HIGHLIGHT_SWEEP","article lines","Yellow highlight grows in four more runs (411 to 507 px on f738-762, to 554 on f764-774, to 663 on f779-800, to 755 on f802-823) over the text that ends 'the investors who broke the Bank of England'.","color_yellow",conf="MEDIUM",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S08",754,754,"OVERLAY_POP","bubble 'XD'","Laughing bubble 'XD' pops in beside the photo in one frame (924 px).","SE041",conf="MEDIUM",label="MEASURED",amb="element read from the sheet")
A.event("S08",792,792,"OVERLAY_POP","bubble 'NOT funny'","Bubble 'NOT funny' pops in at the upper left in one frame (593 px).","SE042",conf="MEDIUM",label="MEASURED")
A.event("S08",823,823,"CAPTION_CHUNK_CHANGE","red caption word 'broke'","Red 'broke' appears in the caption in one frame (red 2 to 59 px, 34.29 s), 70 ms before ASR 'broke' (34.36 s).","color_red",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_red.json"
# --- S09 ---
A.event("S09",913,1121,"HIGHLIGHT_SWEEP","WSJ lines","Yellow highlight grows from 0 to 3872 px over 209 frames across the first three lines of the article (f913-1068 to 2298 px, f1076-1121 to 3872 px); it starts at f913 (38.04 s), 0.12 s before ASR 'I' (38.16 s), and ends at f1121 (46.7 s) with ASR 'makers.' (ends 46.88 s).","color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S09",957,982,"CAMERA_SCROLL_ZOOM","WSJ page, first line","Page pans left at a constant -3.9 px per frame for 26 frames (-101 px at the 180-px analysis size) while the highlight follows the line.","camera_861_1130",conf="HIGH",label="MEASURED",geo="image shift -101 px at 180-px analysis size")
A.E[-1]["easing"]="constant velocity (linear)"; A.E[-1]["measure"]="camera_861_1130.json"
A.event("S09",983,993,"CAMERA_SCROLL_ZOOM","WSJ page, return to line start","Page pans back right at a constant +8.8 px per frame for 11 frames (+97 px).","camera_861_1130",conf="HIGH",label="MEASURED",geo="image shift +97 px at 180-px analysis size")
A.E[-1]["easing"]="constant velocity (linear)"; A.E[-1]["measure"]="camera_861_1130.json"
A.event("S09",1035,1056,"CAMERA_SCROLL_ZOOM","WSJ page, second line","Page pans left at a constant -4.7 px per frame for 22 frames (-103 px) while the highlight follows 'markets aggregate information no committee possesses'.","camera_861_1130",conf="HIGH",label="MEASURED",geo="image shift -103 px at 180-px analysis size")
A.E[-1]["easing"]="constant velocity (linear)"; A.E[-1]["measure"]="camera_861_1130.json"
A.event("S09",1076,1080,"CAMERA_SCROLL_ZOOM","WSJ page, return to line start","Page pans back right at a constant +18.7 px per frame for 5 frames (+94 px).","camera_861_1130",conf="HIGH",label="MEASURED",geo="image shift +94 px at 180-px analysis size")
A.E[-1]["easing"]="constant velocity (linear)"; A.E[-1]["measure"]="camera_861_1130.json"
# --- S10 ---
A.event("S10",1131,1165,"SLIDE_IN","US-map character","Map character slides in from the left edge and enlarges over ~35 frames (peak 24746 px at the cut; 1265-1353 px per frame after it) beneath the typed caption 'the rate lenders charge America,'.","SE052",conf="MEDIUM",label="MEASURED",amb="path and scale not measured")
A.event("S10",1202,1202,"POP_IN","BILL paper","BILL paper pops in at the map's hand in one frame (1409 px), 0.24 s before ASR 'bill' (50.32 s).","SE054",conf="HIGH",label="MEASURED")
A.event("S10",1208,1231,"CHARACTER_RISE_IN","pointer figure","Stick figure's head and pointing arm enter at the upper-left corner over ~24 frames (884 px peak) and point at the chart line; the caption reads 'as a bill America has to pay for'.","SE055",conf="LOW",label="DIRECTLY_OBSERVED",amb="path and pose read from the sheet")
# --- S11 ---
A.event("S11",1285,1408,"HIGHLIGHT_SWEEP","WSJ line","Yellow highlight grows from 0 to 1780 px over 124 frames (f1285-1340 to 866 px, f1370-1408 from 910 to 1780 px) across 'Every basis point of artificial yield suppression is a subsidy to procrastination'; it starts 0.38 s before ASR 'Every' (53.92 s).","color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S11",1321,1389,"CAMERA_SCROLL_ZOOM","WSJ page","Page pans left at a constant -2.0 px per frame for 69 frames (-138 px at the 180-px analysis size) while the highlight follows the line.","camera_1248_1423",conf="HIGH",label="MEASURED",geo="image shift -138 px at 180-px analysis size")
A.E[-1]["easing"]="constant velocity (linear)"; A.E[-1]["measure"]="camera_1248_1423.json"
A.event("S11",1390,1397,"CAMERA_SCROLL_ZOOM","WSJ page, return to line start","Page pans back right at a constant +17.1 px per frame for 8 frames (+137 px).","camera_1248_1423",conf="HIGH",label="MEASURED",geo="image shift +137 px at 180-px analysis size")
A.E[-1]["easing"]="constant velocity (linear)"; A.E[-1]["measure"]="camera_1248_1423.json"
# --- S12 ---
A.event("S12",1462,1472,"SLIDE_IN","Genius lyrics page","Lyrics page enters from the upper left over ~11 frames (9021 px peak) with yellow lyric highlights appearing (yellow 8 to 101 px on f1466-1472), at the caption 'it can only be compared'.","SE061; color_yellow",conf="MEDIUM",label="MEASURED",amb="path not measured")
A.E[-1]["measure"]="color_yellow.json"
A.event("S12",1510,1514,"POSE_SWAP","figure's coat","Coat opens in 4 frames (10306 px) to show a white shirt with a red heart and spaghetti (red 14 to 55 px at f1513), 0.24 s before ASR 'mom's' (63.28 s).","SE065; color_red",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_red.json"
# --- S13 ---
A.event("S13",1544,1621,"UNRESOLVED_CHANGE","static WSJ page","Page holds still for 78 frames at its panned position while the yellow highlight grows (117 to 952 px, f1544-1620).","color_yellow",conf="MEDIUM",label="MEASURED",mclass="CONV",amb="highlight growth only; no pan detected")
A.E[-1]["op"]="HIGHLIGHT_SWEEP"; A.E[-1]["target"]="WSJ line 'If the 30-year must trade at 5.5% to clear'"; A.E[-1]["desc"]="Yellow highlight grows from 117 to 952 px over 77 frames (f1544-1620) while the page, already panned to the line's end, stays still; ASR '30' 64.66 s = f1551.8."; A.E[-1]["measure"]="color_yellow.json"; A.E[-1]["label"]="MEASURED"; A.E[-1]["ambiguity"]="no pan detected in this span"
A.event("S13",1622,1626,"CAMERA_SCROLL_ZOOM","WSJ page, return to line start","Page pans back right at a constant +16.6 px per frame for 5 frames (+83 px).","camera_1545_1803",conf="HIGH",label="MEASURED",geo="image shift +83 px at 180-px analysis size")
A.E[-1]["easing"]="constant velocity (linear)"; A.E[-1]["measure"]="camera_1545_1803.json"
A.event("S13",1680,1714,"CAMERA_SCROLL_ZOOM","WSJ page, 'Then do the only thing...'","Page pans left at a constant -3.0 px per frame for 35 frames (-105 px at the 180-px analysis size) starting 0.16 s before ASR 'Then' (70.16 s).","camera_1545_1803",conf="HIGH",label="MEASURED",geo="image shift -105 px at 180-px analysis size")
A.E[-1]["easing"]="constant velocity (linear)"; A.E[-1]["measure"]="camera_1545_1803.json"
A.event("S13",1715,1719,"CAMERA_SCROLL_ZOOM","WSJ page, return to line start","Page pans back right at a constant +21.3 px per frame for 5 frames (+107 px).","camera_1545_1803",conf="HIGH",label="MEASURED",geo="image shift +107 px at 180-px analysis size")
A.E[-1]["easing"]="constant velocity (linear)"; A.E[-1]["measure"]="camera_1545_1803.json"
A.event("S13",1760,1790,"CAMERA_SCROLL_ZOOM","WSJ page, 'Address the primary deficit'","Page pans left at a constant -3.0 px per frame for 31 frames (-93 px at the 180-px analysis size) starting 0.15 s before ASR 'Address' (73.48 s) and runs into the last frames.","camera_1545_1803",conf="HIGH",label="MEASURED",geo="image shift -93 px at 180-px analysis size")
A.E[-1]["easing"]="constant velocity (linear)"; A.E[-1]["measure"]="camera_1545_1803.json"
A.event("S13",1622,1797,"HIGHLIGHT_SWEEP","WSJ lines","Yellow highlight continues to grow 952 to 2420 px over f1622-1797 in several runs (to 1413 px by f1684, 1631 by f1700, 1571 by f1720, 2420 by f1797) over 'It is an invoice. Then do the only thing that durably lowers long-term yields: address the primary deficit'.","color_yellow",conf="MEDIUM",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.fill_small(172)
A.E=[e for e in A.E if not (e['op']=='UNRESOLVED_CHANGE' and ('CUT' in e['desc'] or 'BIG_POP' in e['desc']) and any(e['f0']-2<=s['f0']<=e['f1']+2 for s in A.S))]
A.write(headline=None)
