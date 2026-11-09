import sys; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('zkeA5cH9nyM',1821)
A.scenes([
(0,"Treasury bond paper above hand-lettered 'And a bond is NOT money'; money bag pops","bond paper; caption (red NOT); money bag","PR_BOND,PR_BAG,TY_RED","A bond is not money"),
(46,"Japan-map character holding a bond faces a bowler-hatted man with cash; 'Monies pls' bubble","map character; man; bond; cash; bubble; caption","CH_JAPAN,CH_FIG,PR_BOND,PR_CASH,OV_BUBBLE","You can't hand a Treasury bond to a currency dealer and ask for change"),
(165,"Hand-lettered 'Currencies trade in pairs' with dollar and yen notes and bags","caption text; notes; bags","PR_DOLLAR,PR_BAG","Currencies trade in pairs"),
(301,"Large US-map character: 'And because the US dollar'","map character; caption","CH_USMAP","The dollar is on one side of nearly 90 % of trades"),
(350,"Dollar note, then yen, euro, real and rupee notes pop in one by one; globe character at the left edge","notes; globe character; caption","PR_DOLLAR,PR_CASH,CH_EARTH","Buying one currency means selling the other; dollars sit on one side"),
(466,"Dollar bag and yen bag: 'buying yen almost always means selling dollars'","two bags; caption","PR_BAG","Buying yen means selling dollars"),
(562,"Pointing host beside the Japan Ministry of Finance reserves page: zoom and pan to the securities row; bond papers pop","host; screenshot page (zoom/pan); bond papers; caption","CH_HOST,SS_MOF_PAGE,PR_BOND","Japan's reserves: about 930 billion sit in securities, mostly US bonds"),
(837,"Japan-map character: 'Japan needed dollars' with a thought bubble holding a dollar note","map character; thought bubble; dollar note; caption","CH_JAPAN,OV_BUBBLE,PR_DOLLAR","Japan needed dollars"),
(876,"Japan-map character behind a stall 'US BONDS FOR SALE!!!' with bond papers","map character; stall; bond papers; caption","CH_JAPAN,PR_BOND,PR_STALL","...and sold American paper to get them"),
(954,"News text page with a growing yellow highlight; bond papers slide in then out; red '66.7%' and a stunned man rise in","text page; highlight; bond papers; red 66.7%; man; caption","SS_NEWS_TEXT,OV_HIGHLIGHT,PR_BOND,TY_RED,CH_MAN","Holdings fell by 66.7 billion dollars in May, the largest one-month drop on record"),
(1115,"Same text page with Japan-map character holding a bond; second highlight grows; US-map character slides in from the left","text page; highlight; map characters; caption","SS_NEWS_TEXT,OV_HIGHLIGHT,CH_JAPAN,CH_USMAP","The record drop in Treasury holdings"),
(1257,"30-year Treasury yield chart: the line draws on, the chart pans and zooms while the host slides out","chart (draw-on, zoom); host; caption","SS_YIELD_CHART,CH_HOST","America's long-term borrowing costs are at their highest since 2007"),
(1394,"Japan-map character holding a bond: 'and America's single biggest foreign lender had just demonstrated'","map character; bond; caption","CH_JAPAN,PR_BOND","The lender demonstrated it will sell"),
(1490,"Big US-map face: 'IN PUBLIC'","map character; caption","CH_USMAP","In public"),
(1510,"Yen note tilting slowly: 'that when its currency gets in trouble'","yen note; caption","PR_CASH","When its currency gets in trouble"),
(1563,"Japan-map character behind the 'US BONDS FOR SALE!!!' stall; US-map character slides in from the left","stall; map characters; bond papers; caption","CH_JAPAN,CH_USMAP,PR_STALL,PR_BOND","It's willing to become a seller, which you'd rather your biggest lender not do"),
(1690,"Sad US-map character with a Japan-map character appearing at the bottom: 'a supply problem in a market at a 19-year high'","map characters; caption","CH_USMAP,CH_JAPAN","Seller becomes a supply problem"),
(1731,"Yield chart zooms in 1.29x; red circle blinks on the latest peak; a head edge peeks in at the end","chart (zoom); red circle; head edge; caption","SS_YIELD_CHART,OV_REDCIRCLE","19-year high")])
A.event("S01",22,22,"POP_IN","money bag","Money bag appears below the caption in one frame.","SE001",conf="HIGH")
A.event("S02",74,74,"OVERLAY_POP","bubble 'Monies pls'","Speech bubble appears above the map character in one frame.","SE003; ev_01",conf="HIGH")
A.event("S03",192,192,"POP_IN","dollar bag and note","Green bag and note appear at the left edge in one frame.","SE007; ev_01",conf="MEDIUM")
A.event("S03",199,199,"POP_IN","yen note","Pink yen note appears at the upper right in one frame.","SE008; ev_01",conf="MEDIUM",amb="region-consistent only")
A.event("S03",252,252,"POP_IN","yen bag","Yen bag appears at the right edge in one frame.","SE011; ev_01",conf="HIGH")
A.event("S05",387,387,"POP_IN","yen note","Yen note appears at the upper right in one frame.","SE015; ev_01",conf="HIGH")
A.event("S05",391,402,"POP_IN","euro, yuan, real and rupee notes","Four further currency notes pop in one after another between f391 and f402.","SE016-017; ev_01",conf="MEDIUM")
A.event("S05",446,446,"POP_IN","globe character","Globe character with eyes appears at the left edge in one frame.","SE018; ev_01",conf="HIGH")
A.event("S06",475,484,"SLIDE_IN","yen bag","Yen bag slides in from the right edge over 10 frames.","SE020; ev_01",conf="MEDIUM")
A.event("S06",523,528,"PROP_DRIFT","dollar bag","Dollar bag moves out through the left edge over 6 frames.","SE021; ev_01",conf="MEDIUM")
A.event("S07",584,616,"CAMERA_SCROLL_ZOOM","Ministry page","Page enlarges 1.91x and shifts left and up (-88.6,-56.2 px at analysis size) over 35 frames, linear on all channels; the host stays at the lower left.","camera_583_618",conf="HIGH",label="MEASURED",geo="net scale x1.906; image shift (-88.6,-56.2) px at 180-px analysis size")
A.E[-1]["easing"]="linear (SUPPORTED, margin 0.028-0.035)"; A.E[-1]["measure"]="camera_583_618.json"
A.event("S07",694,736,"CAMERA_SCROLL_ZOOM","Ministry table","Table enlarges 1.37x and pans left by about 179 px (analysis size) over 45 frames, linear on all channels; the host exits at the left.","camera_693_738",conf="HIGH",label="MEASURED",geo="net scale x1.368; image shift (-178.9,-40.2) px at 180-px analysis size")
A.E[-1]["easing"]="linear (SUPPORTED, margin 0.04-0.046)"; A.E[-1]["measure"]="camera_693_738.json"
A.event("S07",759,759,"CAPTION_CHUNK_CHANGE","hand-lettered caption 'Most of that is in American government bonds'","Caption block appears over the table in one frame and is removed at f827.","SE025; SE028",conf="HIGH")
A.event("S07",770,790,"SLIDE_IN","two bond papers","Two bond papers enter from the lower right over ~20 frames.","SE026; ev_02",conf="MEDIUM")
A.event("S07",796,796,"POP_IN","third bond paper","Another bond paper appears in one frame.","SE027; ev_02",conf="MEDIUM")
A.event("S07",827,827,"CAPTION_CHUNK_CHANGE","hand-lettered caption block","Caption block removed in one frame.","SE028; ev_02",conf="HIGH")
A.event("S08",854,854,"OVERLAY_POP","thought bubble with dollar note","Thought bubble appears in one frame.","SE030; ev_02",conf="HIGH")
A.event("S10",959,1063,"HIGHLIGHT_SWEEP","yellow highlight on the first text lines","Yellow area grows from f959 to ~95 % of maximum at f1063 (843 px at analysis size), monotone fraction 1.0.","color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S10",969,994,"SLIDE_IN","bond papers","Bond papers slide in from the lower left over 26 frames.","SE034; ev_02",conf="MEDIUM")
A.event("S10",1037,1057,"PROP_DRIFT","bond papers","Bond papers drift down and out of the frame over ~21 frames (stage change decays from 4300 to 460 px).","SE035; ev_02",conf="MEDIUM")
A.event("S10",1058,1058,"OVERLAY_POP","red '66.7%'","Red hand-lettered '66.7%' appears at full opacity in one frame (0 to 14,900 red px at native size).","SE035; color_red",conf="HIGH",label="MEASURED")
A.event("S10",1061,1078,"CHARACTER_RISE_IN","stunned man","Man's head rises from the bottom edge and reaches full view over ~18 frames.","SE035; ev_02",conf="MEDIUM")
A.event("S11",1118,1210,"HIGHLIGHT_SWEEP","yellow highlight on the second paragraph","Yellow area grows from f1118 to ~95 % of maximum at f1210 (871 px), monotone fraction 1.0.","color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S11",1174,1189,"SLIDE_IN","US-map character","Character slides in from the left edge over 16 frames.","SE037; ev_02",conf="MEDIUM")
A.event("S12",1258,1307,"STROKE_REVEAL","yield line","Blue yield line draws left to right over ~50 frames.","SE039; ev_02",conf="MEDIUM",amb="progress not tracked")
A.event("S12",1323,1356,"CAMERA_SCROLL_ZOOM","yield chart","Chart shifts left by about 14 px (analysis size) and enlarges ~1.09x over 34 frames with an ease-out cubic fit on all channels while the host slides out to the right.","camera_1322_1357",conf="MEDIUM",label="MEASURED",geo="net scale x1.085; image shift (-14.4,-1.1) px at 180-px analysis size")
A.E[-1]["easing"]="ease_out_cubic (SUPPORTED, margin 0.081-0.086; host motion mixed in)"; A.E[-1]["measure"]="camera_1322_1357.json"
A.event("S15",1511,1562,"ROTATION","yen note","Note tilts slowly over ~50 frames; amplitude and direction changes not measured.","SE043; ev_03",conf="LOW",amb="oscillation versus one-way tilt not resolved")
A.event("S16",1617,1634,"SLIDE_IN","US-map character","Character slides in from the left edge over ~18 frames while the caption block changes at f1609.","SE044; ev_03",conf="MEDIUM")
A.event("S17",1711,1711,"POP_IN","Japan-map character","Japan-map character appears at the bottom right in one frame.","SE046; ev_03",conf="HIGH")
A.event("S18",1731,1758,"CAMERA_SCROLL_ZOOM","yield chart","Chart enlarges 1.29x and shifts left by about 87 px (analysis size) over 28 frames, linear.","camera_1731_1758",conf="HIGH",label="MEASURED",geo="net scale x1.289; image shift (-87.3,+21.5) px at 180-px analysis size")
A.E[-1]["easing"]="linear (SUPPORTED, margin 0.045)"; A.E[-1]["measure"]="camera_1731_1758.json"
A.event("S18",1759,1778,"OVERLAY_POP","red circle","Red circle appears in one frame at the latest peak (615 px at analysis size) and settles to 698 px by f1766, a 13 % area gain, then holds to f1778.","color_red",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_red.json"
A.event("S18",1779,1779,"OVERLAY_POP","red circle off","Red circle disappears in one frame and reappears at f1793, remaining to f1817 (on-off blink).","SE048-049; color_red",conf="HIGH",label="MEASURED")
A.event("S18",1793,1793,"OVERLAY_POP","red circle on","Circle reappears in one frame (702 px).","SE049; color_red",conf="HIGH",label="MEASURED")
A.event("S18",1818,1820,"POP_IN","head edge at the left","A peach-coloured head edge appears at the left edge in the last three frames (circle removed at f1818).","SE050; ev_03",conf="MEDIUM")
A.write(headline=None)
