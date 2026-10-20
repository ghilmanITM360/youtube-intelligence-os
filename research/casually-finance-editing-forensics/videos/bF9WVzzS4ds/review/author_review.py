import sys; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('bF9WVzzS4ds',2010)
A.scenes([
(0,"Federal Reserve building grows under the hand-lettered caption 'There's a tool at the Federal Reserve where a'","building; caption","PR_BANK","A tool at the Fed"),
(57,"Small Fed building above a Japan-side building character holding a paper; paper and a money bag move; caption 'foreign government can hand over its American bonds' then 'take dollars in exchange'","two buildings; paper; bag; caption","PR_BANK,PR_BLDG,PR_DOC,PR_BAG","A foreign government hands over bonds and takes dollars"),
(175,"Green palm-leaf card with red 'TWO WEEKS LATER' text; caption 'and buy the bonds back later'","title card; caption","FX_TIMECARD","Time passes before the buy-back"),
(220,"Buildings again; money bags and paper trade places: 'at a slightly higher repurchase price'","two buildings; bags; paper; caption","PR_BANK,PR_BLDG,PR_BAG,PR_DOC","The buy-back price is slightly higher"),
(289,"Third-party video clip of a bald man in a shop above the Japan-map character holding a bag and paper; 'It's a pawn shop for governments', then 'only 20????'","video clip; map character; bag; paper; caption","PHOTO_CLIP,CH_JAPAN,PR_BAG,PR_DOC","It is a pawn shop for governments"),
(348,"US-map character with a bag next to a small Japan-map character; bubble 'Pls don't leave me!' then 'I'll stay for them dollars'; the bag glides across","map characters; bag; bubbles","CH_USMAP,CH_JAPAN,PR_BAG,OV_BUBBLE","A creditor you cannot afford to lose"),
(445,"Treasury seal on white; 'Ministry of Finance, JAPAN' kanji pops; seal and text shrink to the corner; caption 'executed a joint market operation'; US-map character and a yen note pop","seal; kanji text; map character; yen note; caption","LOGO_TREASURY,LOGO_MOF,CH_USMAP,PR_CASH","The joint market operation to prop up the yen"),
(647,"Dark news-card at the top, yen note at the lower left, red down arrow draws across the page","news card; yen note; red arrow","SS_NEWS_CARD,PR_CASH,OV_REDARROW","The yen keeps falling"),
(718,"White card with '48 hours later...' typed on","text card","TY_CARD","48 hours later"),
(772,"Grey-haired official figure rises from the bottom; a social-post card with a red oval slides in; caption 'these people LOVE announcing things on Twitter'; the card zooms and pans","official; social post screenshot (zoom/pan); red oval; caption","CH_OFFICIAL,SS_TWEET,OV_REDOVAL","The Treasury Secretary announces on social media"),
(1062,"Caption 'But here's the detail that makes the request strange' with a puzzled man rising in from the lower left","caption; man","CH_MAN","The detail that makes the request strange"),
(1136,"'Nobody was using it.' with large yellow outlined lettering 'FIMA Repo Facility' and a '*crickets*' aside","caption; big lettering; aside","TY_BIGTITLE","Nobody was using the facility"),
(1182,"Fed statement page with a yellow highlight that grows; five money bags rise from the bottom; '$60B' pops","page screenshot; highlight; bags; text","SS_FED_PAGE,OV_HIGHLIGHT,PR_BAGS,TY_AMOUNT","Ceiling of 60 billion dollars per country"),
(1278,"Pointing host beside a Bloomberg chart that pans; caption 'and the balance was sitting at zero' with red 'zero'","host; chart (pan); caption; red word","CH_HOST,SS_REPO_CHART,TY_RED","The balance was sitting at zero"),
(1332,"Official figure: 'Days after he asked,' then bubbles 'More money, please!', 'My guy...', 'It's been unused for 8 weeks!', a Bloomberg wordmark and eight calendar icons","official; bubbles; wordmark; calendar icons; caption","CH_OFFICIAL,OV_BUBBLE,LOGO_BLOOMBERG,PR_CALENDAR","Days after the request it had gone unused for eight weeks"),
(1469,"Round-head man and a pink piggy bank: 'So he wasn't asking for more room'; the piggy bank is replaced by the leaning official with a bag: 'because he'd run out.'","man; piggy bank; official; bag; caption","CH_MAN,PR_PIG,CH_OFFICIAL,PR_BAG","He was not asking because he had run out"),
(1551,"Pointing host beside the Bloomberg chart: 'Nobody was anywhere near the ceiling'","host; chart; caption","CH_HOST,SS_REPO_CHART","Nobody was near the ceiling"),
(1612,"Large official figure beneath the social-post card with a red oval; static hold","official; social post screenshot","CH_OFFICIAL,SS_TWEET,OV_REDOVAL","Asking publicly, 48 hours after the operation"),
(1768,"Host beside the Bloomberg chart: 'to build capacity for something that hadn't happened yet.'; three red question marks pop one by one","host; chart; caption; red question marks","CH_HOST,SS_REPO_CHART,TY_RED","Capacity for something that has not happened"),
(1856,"Treasury seal above the waving official: bubbles 'More money pls!', 'That's kinda sus...', 'But OK I guess?'","seal; official; bubbles","LOGO_TREASURY,CH_OFFICIAL,OV_BUBBLE","You don't ask publicly unless you know something is coming")])
A.event("S01",1,48,"SCALE_TWEEN","Fed building","Building grows from a small icon to about twice its size over 48 frames under the caption; ink area (rows 0.10-0.70, caption included) rises linearly from 4318 to 9216 px.","extent_0_52",conf="HIGH",label="MEASURED")
A.E[-1]["easing"]="linear (SUPPORTED, margin 0.024; ink area incl. caption, indicative)"; A.E[-1]["measure"]="extent_0_52.json"
A.event("S02",74,92,"PROP_DRIFT","paper","Paper moves from beside the lower building up to the right of the Fed building over ~19 frames.","SE003; ev_01",conf="MEDIUM",amb="path not tracked")
A.event("S02",133,136,"CAPTION_CHUNK_CHANGE","caption 'take dollars in exchange'","Caption changes from 'foreign government can hand over its American bonds' to 'take dollars in exchange' between f133 and f136 while a money bag appears.","SE004; ev_01",conf="MEDIUM",amb="exact frame within f133-136 not isolated")
A.event("S02",133,151,"PROP_DRIFT","money bag","Money bag drifts from the Fed building down to the Japan-side building over ~19 frames.","SE004; ev_01",conf="MEDIUM",amb="path and easing not measured")
A.event("S03",219,219,"CAPTION_CHUNK_CHANGE","caption 'at a slightly higher repurchase price'","Caption changes over the title card one frame before the card is removed (cut f220).","SE006; ev_01",conf="HIGH")
A.event("S04",221,281,"PROP_DRIFT","bags and paper","A money bag starts drifting to the right of the Japan-side building at f221 (changed region shifts ~0.01 of frame width per frame); money bags and the paper then trade places between the buildings through f281 (bags travel up to the Fed building, the paper returns), ~61 frames in all.","SE006; ev_01; stage px f221-231",conf="LOW",amb="path and easing not measured; two to three props move together")
A.event("S05",292,292,"OVERLAY_POP","caption 'It's a pawn shop for governments'","Hand-lettered caption appears beside the clip in one frame.","SE007; ev_01",conf="HIGH")
A.event("S05",289,346,"VIDEO_CLIP_INSERT","video clip in the upper frame","Clip region (rows 0.02-0.17) changes every third frame (f292, 295, 298, 301, 304, 316, 319, 322, 325, 328, 331, 334, 337, 340, 346), i.e. a 10 fps source inside the 30 fps file, held until the cut at f348; two expected updates (f313, f343) are unchanged.","clip-region mean abs diff series",conf="MEDIUM",label="MEASURED",mclass="INDET",amb="source clip not identified; mean-diff series only")
A.event("S05",317,317,"OVERLAY_POP","caption 'only 20????'","Small caption appears under the first one in a single frame.","SE009; ev_01",conf="HIGH")
A.event("S06",369,369,"OVERLAY_POP","bubble 'Pls don't leave me!'","Speech bubble appears above the US-map character in one frame.","SE012; ev_01",conf="HIGH")
A.event("S06",387,401,"PROP_DRIFT","dollar bag","Dollar bag glides from beside the US-map character down to the left of the Japan-map character over ~15 frames.","SE013; ev_01",conf="MEDIUM",amb="path and easing not measured")
A.event("S06",402,402,"OVERLAY_POP","bubble 'I'll stay for them dollars'","The first bubble is replaced by a new bubble beside the Japan-map character in one frame.","SE013; ev_01",conf="HIGH")
A.event("S07",489,489,"POP_IN","kanji text and Ministry label","Kanji and 'Ministry of Finance, JAPAN' appear above the seal in one frame while the seal shifts.","SE015; ev_01",conf="MEDIUM",amb="seal shift not measured")
A.event("S07",552,582,"SCALE_TWEEN","seal and Ministry text","Seal and Ministry text shrink and move to the upper left over ~31 frames while the caption 'executed a joint market operation' appears (f556 first seen).","SE016; ev_02",conf="MEDIUM",amb="scale and easing not measured")
A.event("S07",582,582,"POP_IN","US-map character","Large US-map character appears in one frame at the end of the shrink.","SE016; ev_02",conf="HIGH")
A.event("S07",614,614,"CAPTION_CHUNK_CHANGE","caption removed","Caption 'executed a joint market operation' disappears in one frame.","SE017; s3",conf="HIGH")
A.event("S07",619,619,"POP_IN","yen note","Yen note appears above the US-map character in one frame.","SE018; s3",conf="HIGH")
A.event("S08",652,686,"STROKE_REVEAL","red down arrow","Red zigzag arrow draws from the top left down to the right; red area grows from 123 px (f652) to 2174 px (95 % at f685), monotone fraction 0.988, then holds to f717.","color_red; colorfit_arrow_highlight",conf="HIGH",label="MEASURED")
A.E[-1]["easing"]="linear (SUPPORTED, margin 0.045)"; A.E[-1]["measure"]="color_red.json; colorfit_arrow_highlight.json"
A.event("S09",718,748,"TEXT_WRITE_ON","'48 hours later...'","Text is typed on in steps: ink is already 705 px at the cut (f718, '48 hou'), then rises at f720, 723, 726, 729, 732, 735 and 739 (every ~3 frames) to 1425 px and 1463 px by f748.","extent_717_770",conf="HIGH",label="MEASURED")
A.E[-1]["easing"]="stepwise, one step per ~3 frames (curve fit not meaningful)"; A.E[-1]["measure"]="extent_717_770.json"
A.event("S10",772,789,"CHARACTER_RISE_IN","official figure","Grey-haired official rises from the bottom edge over ~18 frames after the text card is removed.","SE022; ev_02",conf="MEDIUM")
A.event("S10",810,827,"SLIDE_IN","social post card","Social-post card slides in from the right edge over ~18 frames; its left edge moves from x=0.34 (f818) to the frame edge by f826 (about 0.05-0.06 of frame width per frame at the end) and the red oval on it reaches its full 339 px by f819.","SE023; color_red; stage px f818-828",conf="MEDIUM",label="MEASURED",amb="easing not fitted (card plus caption pop in one event)")
A.event("S10",828,828,"OVERLAY_POP","caption 'these people LOVE announcing things on Twitter'","Tilted hand-lettered caption appears at the lower right in one frame.","SE023; ev_02",conf="HIGH")
A.event("S10",867,867,"CAPTION_CHUNK_CHANGE","caption removed","Tilted caption disappears in one frame.","SE024; s3",conf="HIGH")
A.event("S10",889,915,"CAMERA_SCROLL_ZOOM","social post card","Card enlarges 1.96x and shifts right and up (+87.5,-63.2 px at analysis size) over 27 frames; x pan ease-in-out (SUPPORTED, margin 0.036), scale and y pan linear (AMBIGUOUS, margin 0.015-0.018).","camera_888_917",conf="HIGH",label="MEASURED",geo="net scale x1.962; image shift (+87.5,-63.2) px at 180-px analysis size")
A.E[-1]["easing"]="x pan ease_in_out (SUPPORTED); scale/y linear (AMBIGUOUS)"; A.E[-1]["measure"]="camera_888_917.json"
A.event("S10",941,997,"CAMERA_SCROLL_ZOOM","social post card","Card pans left by 170 px (analysis size) over 57 frames with no scale change; x and y pans ease-in-out (SUPPORTED, margin 0.057 and 0.034).","camera_938_1000",conf="HIGH",label="MEASURED",geo="net scale x1.000; image shift (-170.2,+0.1) px at 180-px analysis size")
A.E[-1]["easing"]="ease_in_out_smoothstep (SUPPORTED, margin 0.057)"; A.E[-1]["measure"]="camera_938_1000.json"
A.event("S10",1013,1027,"CAMERA_SCROLL_ZOOM","social post card","Card pans back right by 165 px over 15 frames with scale 0.99; ease-in-out on all channels (SUPPORTED, margin 0.023-0.050).","camera_1011_1030",conf="HIGH",label="MEASURED",geo="net scale x0.993; image shift (+165.5,0.0) px at 180-px analysis size")
A.E[-1]["easing"]="ease_in_out_smoothstep (SUPPORTED, margin 0.023-0.050)"; A.E[-1]["measure"]="camera_1011_1030.json"
A.event("S11",1073,1095,"CHARACTER_RISE_IN","puzzled man","Man's head rises from the lower-left edge over ~23 frames to a lowered-brow expression.","SE029; ev_02",conf="MEDIUM")
A.event("S12",1155,1155,"POP_IN","'*crickets*' aside","Small '*crickets*' aside appears at the top in one frame.","SE031; s3",conf="HIGH")
A.event("S12",1172,1172,"CAPTION_CHUNK_CHANGE","'*crickets*' aside","The aside jumps from the top to the lower right in one frame.","SE032; s3",conf="HIGH")
A.event("S13",1183,1266,"HIGHLIGHT_SWEEP","yellow highlight on a statement sentence","Yellow area grows from 7 px (f1183) to 492 px at f1266 (89 % at f1254, 96 % at f1262), monotone fraction 0.987, rate tapering after f1246.","color_yellow; colorfit_arrow_highlight",conf="HIGH",label="MEASURED")
A.E[-1]["easing"]="linear (AMBIGUOUS, margin 0.020; tapers at the end)"; A.E[-1]["measure"]="color_yellow.json; colorfit_arrow_highlight.json"
A.event("S13",1194,1204,"SLIDE_IN","five money bags","Five bags rise in from the bottom edge into a row over 11 frames.","SE034; ev_03",conf="MEDIUM")
A.event("S13",1217,1217,"OVERLAY_POP","'$60B'","Large '$60B' text appears above the bags in one frame.","SE035; s3",conf="HIGH")
A.event("S14",1278,1308,"CAMERA_SCROLL_ZOOM","Bloomberg chart","Chart image pans left by about 205 px (analysis size, more than one frame width) over ~31 frames, ease-out quad (SUPPORTED, margin 0.083); the scale fit (rmse 0.36) is not reliable (net 1.02x).","camera_1277_1310",conf="MEDIUM",label="MEASURED",geo="net image shift (-204.8,-24.2) px at 180-px analysis size; net scale x1.018 (unreliable)")
A.E[-1]["easing"]="pan x ease_out_quad (SUPPORTED, margin 0.083); scale unreliable"; A.E[-1]["measure"]="camera_1277_1310.json"
A.event("S14",1326,1326,"CAPTION_CHUNK_CHANGE","caption removed","Caption 'and the balance was sitting at zero' (red 'zero') disappears in one frame.","SE037; s3",conf="HIGH")
A.event("S15",1354,1354,"OVERLAY_POP","bubble 'More money, please!'","Bubble appears beside the official in one frame.","SE039; s3",conf="HIGH")
A.event("S15",1373,1373,"POP_IN","'Bloomberg' wordmark","Wordmark appears at the top in one frame.","SE040; s3",conf="HIGH")
A.event("S15",1404,1404,"OVERLAY_POP","bubble 'My guy...'","Bubble appears at the upper left in one frame.","SE041; s3",conf="HIGH")
A.event("S15",1433,1433,"CAPTION_CHUNK_CHANGE","bubble text","Bubble text changes from 'My guy...' to 'It's been unused for 8 weeks!' in one frame.","SE042; s3",conf="HIGH")
A.event("S15",1437,1459,"SLIDE_IN","eight calendar icons","Calendar icons enter from the right edge and settle into a 2x4 grid over ~23 frames; red area ramps from 13 px (f1437) to ~200 px (steady from f1453).","SE043; color_red",conf="MEDIUM",label="MEASURED",amb="per-icon timing not resolved")
A.event("S16",1472,1472,"OVERLAY_POP","caption 'So he wasn't asking for more room'","Hand-lettered caption appears under the piggy bank in one frame (cut and settle f1469-1472).","SE044; ev_03",conf="HIGH")
A.event("S16",1513,1513,"POP_IN","official figure with bag","Leaning official with a brown bag appears at the upper left and the piggy bank is removed in one frame.","SE045; ev_03",conf="HIGH")
A.event("S16",1517,1517,"OVERLAY_POP","caption 'because he'd run out'","Small caption appears beside the official in one frame.","SE046; ev_03",conf="HIGH")
A.event("S16",1545,1545,"CAPTION_CHUNK_CHANGE","caption removed","Caption disappears in one frame.","SE047; s3",conf="HIGH")
A.event("S17",1555,1555,"OVERLAY_POP","caption 'Nobody was anywhere near the ceiling'","Caption appears over the chart in one frame.","SE049; ev_03",conf="HIGH")
A.event("S17",1579,1579,"POSE_SWAP","host","Small local change at the host's arm/pointer in one frame.","SE050; s3",conf="LOW",amb="mechanism not isolated")
A.event("S17",1603,1603,"CAPTION_CHUNK_CHANGE","caption removed","Caption disappears in one frame.","SE051; s3",conf="HIGH")
A.event("S19",1807,1807,"OVERLAY_POP","first red '?'","First red question mark appears under the caption in one frame (+166 red px).","color_red; SE054",conf="HIGH",label="MEASURED")
A.event("S19",1820,1820,"OVERLAY_POP","second red '?'","Second red question mark appears in one frame (+166 red px).","color_red; SE055",conf="HIGH",label="MEASURED")
A.event("S19",1834,1834,"OVERLAY_POP","third red '?'","Third red question mark appears in one frame (+162 red px, total 494 px).","color_red; SE056",conf="HIGH",label="MEASURED")
A.event("S19",1846,1846,"CAPTION_CHUNK_CHANGE","caption removed","Caption disappears in one frame, leaving the three red '?'.","SE057; s3",conf="HIGH")
A.event("S20",1887,1887,"OVERLAY_POP","bubble 'More money pls!'","Bubble appears beside the waving official in one frame.","SE059; s3",conf="HIGH")
A.event("S20",1951,1951,"OVERLAY_POP","bubble 'That's kinda sus...'","Bubble 'More money pls!' is replaced by 'That's kinda sus...' at the seal in one frame.","SE060; s2",conf="HIGH")
A.event("S20",1990,1990,"OVERLAY_POP","bubble 'But OK I guess?'","Bubble text changes to 'But OK I guess?' in one frame.","SE061; s2",conf="HIGH")
A.write(headline=None)
