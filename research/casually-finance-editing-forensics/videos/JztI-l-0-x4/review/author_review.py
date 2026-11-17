import sys, json; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('JztI-l-0-x4',2423)
A.scenes([
(0,"Headline 'nobody can agree why america paid to save japan'; a 'MY MAN' meme image at the left, a green muscular figure pops, then a Pearl Harbor image and a worried head","headline; meme image; character; photo; caption","PHOTO_MEME,CH_FIG,PHOTO_HARBOR","Friendship, financial strength and Pearl Harbor in one conversation"),
(89,"Stick figure alone under the headline: 'all covered in one conversation'","headline; host; caption","CH_HOST","All in one conversation"),
(143,"Trump caricature at a lectern between flags, small periodic pose changes: 'if that isn't the most Trump thing you've heard'","headline; character; flags; caption","CH_TRUMP,PR_FLAGS","The most Trump thing"),
(249,"Statement text page with yellow highlights and two figures: 'Besant responded, saying the goal was to protect the US economy and keep any volatility offshore'","headline; text page; highlights; figures; caption","SS_STATEMENT,OV_HIGHLIGHT,CH_OFFICIAL,CH_FIG","The goal was to keep volatility offshore"),
(426,"Stick figure and Japan-map character with a bubble: 'Tokyo got asked the same question'","headline; figure; map character; bubble; caption","CH_FIG,CH_JAPAN,OV_BUBBLE","Tokyo answers in stiffer language"),
(536,"Ministry of Finance statement page with the Japan-map character; a US-map character and bag pop in; a highlight bar grows and a yen note arrives","headline; statement page; highlight; map characters; yen note; caption","SS_MOF_STATEMENT,CH_JAPAN,CH_USMAP,PR_BAG,PR_CASH","The action was taken in accordance with the US Treasury"),
(819,"Stick figure alone: 'translated out of Treasury speak'","host; caption","CH_HOST","Translated out of Treasury speak"),
(875,"Yen note and a green up arrow that turns red and points down: 'the yen was falling'","yen note; arrow; caption","PR_CASH,OV_ARROW","The yen was falling"),
(911,"Small Japan-map character that tints dark red, then a US-map character and a bubble: 'Japan was hurting, and America had to step in to make the pain stop'","map characters; bubble; caption","CH_JAPAN,CH_USMAP,OV_BUBBLE","Japan was hurting, America stepped in"),
(1040,"Host with 'Weird request' and 'Buying lots of yen' notes joined by a drawn red squiggle: 'maybe that's just my read ... dots that aren't connected'","host; notes; red squiggle; caption","CH_HOST,OV_NOTE,OV_REDLINE","Maybe I'm connecting dots that aren't connected"),
(1162,"Host alone: 'connecting them'","host; caption","CH_HOST","I'm not the only one connecting them"),
(1235,"CSIS profile page of Mark Sobel; the page zooms, zooms out, a green highlight grows, the article scrolls in and the host points: 'spent about four decades inside the US Treasury working on international monetary policy'","profile page (zoom); green highlights; host; caption","SS_CSIS_PAGE,OV_HIGHLIGHT,CH_HOST","A former Treasury official also connects them"),
(1533,"Article text page with a growing yellow highlight: 'aside from supporting a friend, ... could push American long-term rates higher'","text page; highlight; caption","SS_ARTICLE,OV_HIGHLIGHT","A weak yen could push long-term rates higher"),
(1749,"Man and Japan-map character with a meme image of a cartoon sponge (a clip): 'so the president says friendship'","characters; meme clip; caption","CH_MAN,CH_JAPAN,PHOTO_MEME","The president says friendship"),
(1805,"Grey-haired official alone; a 'Stability!' bubble pops: 'the Treasury Secretary says stability'","official; bubble; caption","CH_OFFICIAL,OV_BUBBLE","The Treasury Secretary says stability"),
(1867,"Photo of a man in a white shirt; a 'This is sus af' bubble pops: 'there's more to this story'","photo; bubble; caption","PHOTO_PERSON,OV_BUBBLE","The expert says there's more to this story"),
(2006,"Large Japan-map character holding a paper: 'a story where the country holding more American debt than anyone else on the planet'","map character; paper; caption","CH_JAPAN,PR_DOC","The biggest holder of American debt"),
(2144,"Small Japan-map character with a paper: 'than anyone else on the planet'","map character; paper; caption","CH_JAPAN,PR_DOC","The biggest holder"),
(2207,"'US BONDS FOR SALE' stall with cash and the Japan-map character that sinks behind it; a yen note and shield appear: 'demonstrates in public that it will sell that debt to fund its own currency defense'","stall; cash; map character; yen note; caption","PR_STALL,PR_CASH,CH_JAPAN","It will sell the debt to fund its own currency defense"),
(2297,"Worried stick figure alone: 'a supply problem'","host; caption","CH_HOST","A supply problem"),
(2337,"Treasury yield chart; a red circle draws on the latest peak, blinks off and on: 'in a market that is at a 19-year high'","chart; red circle; caption","SS_YIELD_CHART,OV_REDCIRCLE","A 19-year high")])
A.event("S01",21,38,"POP_IN","green muscular figure","Green figure appears beside the meme image at f21 (yellow area 36 to 131 px by f38 as it settles).","SE001; color_yellow",conf="MEDIUM",label="MEASURED")
A.event("S01",37,37,"POSE_SWAP","green figure","Figure changes pose in one frame.","SE002; ev_01",conf="MEDIUM")
A.event("S01",55,55,"POP_IN","Pearl Harbor image and worried head","Pearl Harbor image and a worried head appear in one frame.","SE003; ev_01",conf="HIGH")
A.event("S03",157,213,"CHARACTER_LOOP_ANIMATION","caricature","Small local pose changes at f157, 171, 185, 199 and 213 (every 14 frames) while the figure speaks at the lectern.","SE006-010; stage events",conf="MEDIUM",label="MEASURED",mclass="INDET",amb="mechanism (pose swap versus loop) not resolved")
A.event("S05",480,480,"OVERLAY_POP","bubble removed","Bubble disappears in one frame.","SE017; ev_01",conf="HIGH")
A.event("S06",642,642,"POP_IN","US-map character and bag","US-map character and a bag appear at the left in one frame.","SE019; ev_01",conf="HIGH")
A.event("S06",723,805,"HIGHLIGHT_SWEEP","highlight bar on the statement page","A highlight bar grows across the lines 'excessive volatility and disorderly movements' and a yen note arrives at the right (f779-805); measured by stage change only (the pale bar is below the colour threshold).","SE021; ev_01",conf="LOW",amb="highlight and yen note not separated")
A.event("S08",890,901,"ROTATION","arrow","Arrow turns from pointing up (green) to pointing down (red, red area 0 to 86 px at f897-900) over 11 frames.","SE024; color_red",conf="MEDIUM",label="MEASURED")
A.event("S08",889,898,"PROP_DRIFT","yen note","Yen note drops down and left out of the frame over ~10 frames.","SE024; ev_01",conf="MEDIUM")
A.event("S09",911,945,"POSE_SWAP","Japan-map character","Character changes on most frames between f911 and f944 and tints dark red in the sampled frames f923 and f935 ('hurting'); the flicker pattern is not resolved.","SE025; ev_01",conf="LOW",amb="flicker pattern not resolved")
A.event("S09",1010,1010,"OVERLAY_POP","bubble","Bubble appears beside the Japan-map character in one frame.","SE027; ev_01",conf="HIGH")
A.event("S10",1092,1092,"POP_IN","notes and smaller host","'Weird request' and 'Buying lots of yen' notes appear and the host shrinks in one frame.","SE029; ev_01",conf="MEDIUM")
A.event("S10",1093,1146,"STROKE_REVEAL","red squiggle","Red squiggle draws between the two notes over ~54 frames (red area up to ~117 px, removed at f1162).","SE029; color_red",conf="MEDIUM",label="MEASURED",amb="progress read from the sheet; colour count below threshold")
A.event("S12",1259,1319,"CAMERA_SCROLL_ZOOM","CSIS page","Page enlarges 1.72x with a shift of (-63.5,+10.8) px at analysis size over ~61 frames, linear on scale and both pans (SUPPORTED, margin 0.038-0.052).","camera_1258_1321",conf="HIGH",label="MEASURED",geo="net scale x1.720; image shift (-63.5,+10.8) px at 180-px analysis size")
A.E[-1]["easing"]="linear (SUPPORTED, margin 0.038-0.052)"; A.E[-1]["measure"]="camera_1258_1321.json"
A.event("S12",1361,1377,"CAMERA_SCROLL_ZOOM","CSIS page","Page zooms back out (net 0.58x) over 17 frames; linear fit is AMBIGUOUS (margin 0.005-0.007).","camera_1360_1378",conf="MEDIUM",label="MEASURED",geo="net scale x0.580; image shift (+30.0,-12.3) px at 180-px analysis size")
A.E[-1]["easing"]="linear (AMBIGUOUS, margin 0.005-0.007)"; A.E[-1]["measure"]="camera_1360_1378.json"
A.event("S12",1401,1442,"HIGHLIGHT_SWEEP","green highlight on the profile text","Green area grows from 0 to 280 px over ~42 frames under 'about 4 decades inside the US Treasury'.","color_lgreen",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_lgreen.json"
A.event("S12",1467,1490,"CAMERA_SCROLL_ZOOM","article page","Page scrolls from the profile header to the article body over ~24 frames (page content is replaced, so no zoom fit applies).","SE035; ev_02",conf="MEDIUM",label="DIRECTLY_OBSERVED",amb="geometry not measured")
A.event("S12",1484,1491,"POP_IN","host with pointer","Host with a pointer appears at the right within eight frames (absent at f1483, present at f1491).","SE035; ev_02",conf="MEDIUM",amb="exact frame within f1484-1491 not isolated")
A.event("S12",1491,1516,"HIGHLIGHT_SWEEP","second green highlight","Green area grows from 204 to 495 px over ~28 frames on the article text.","color_lgreen",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_lgreen.json"
A.event("S13",1557,1650,"HIGHLIGHT_SWEEP","yellow highlight on the article","Yellow area grows from 0 to 214 px over f1557-1628 and to 274 px by f1650 (second stage).","color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S14",1755,1804,"VIDEO_CLIP_INSERT","cartoon-sponge meme clip","Meme image appears at f1755 and its region updates every third frame (f1758, 1761, ... 1791) and then on f1797, 1800, 1801, 1803 and 1804 before the cut at f1805, i.e. a ~10 fps source.","SE039-040; clip-region mean abs diff",conf="MEDIUM",label="MEASURED",mclass="INDET",amb="source clip not identified")
A.event("S15",1845,1845,"OVERLAY_POP","bubble 'Stability!'","Bubble appears beside the official in one frame.","SE041; ev_02",conf="HIGH")
A.event("S16",1969,1969,"OVERLAY_POP","bubble 'This is sus af'","Bubble appears beside the photo in one frame.","SE043; ev_02",conf="HIGH")
A.event("S19",2230,2252,"LAYER_SLIDE_BEHIND","Japan-map character","Japan-map character sinks behind the stall over ~22 frames.","SE047; ev_02",conf="MEDIUM",amb="path and easing not measured")
A.event("S19",2259,2259,"POP_IN","yen note","Yen note appears at the upper right in one frame.","SE048; ev_02",conf="HIGH")
A.event("S21",2365,2376,"STROKE_REVEAL","red circle","Red circle draws around the latest peak over ~12 frames (red area 0 to 52 px), disappears at f2385 and reappears at f2399-2400 (on-off blink).","color_red",conf="HIGH",label="MEASURED")
A.fill_small(172)
A.E=[e for e in A.E if not (e['op']=='UNRESOLVED_CHANGE' and ('HARD' in e['desc'] or 'CUT' in e['desc'] or 'BIG_POP' in e['desc']) and any(e['f0']-2<=s['f0']<=e['f1']+2 for s in A.S))]
A.write(headline="nobody can agree why america paid to save japan")
a=json.load(open('videos/JztI-l-0-x4/review/assets.json'))
for x in a:
    if x['asset_id']=='TY_HEADER': x['f1']=818
json.dump(a,open('videos/JztI-l-0-x4/review/assets.json','w'),indent=1)
