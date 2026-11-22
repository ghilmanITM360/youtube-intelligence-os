import sys; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('wo71JwXSYIs',2122)
A.scenes([
(0,"UK flag beside the green UK-map character: 'Britain went first'","headline; flag; map character; caption","PR_FLAG_UK,CH_UKMAP","Britain was first to shorten its issuance"),
(35,"Four-line issuance chart with a red arrow that travels along a line and a red circle at its end","headline; chart; red arrow; red circle; caption","SS_GILT_CHART,OV_REDARROW,OV_REDCIRCLE","A decade ago long gilts were nearly 30 % of the programme; this year under 10 %"),
(250,"UK debt-office remarks page with a pointing host and a growing yellow highlight","headline; text page; highlight; host; caption","SS_DMO_TEXT,OV_HIGHLIGHT,CH_HOST","The debt office noted declining demand, especially from domestic pension funds"),
(530,"Lone figure: 'the polite way of saying we asked around and nobody wants them'","headline; figure; caption","CH_LONE","Joke: nobody wants long gilts"),
(650,"Japan text page with a green Japan-map character; red '17T' and a money bag pop; pointing host pops at the lower left","headline; text page; map character; red text; bag; host; caption","SS_MOF_TEXT,CH_JAPAN,TY_RED,PR_BAG,CH_HOST","Japan cut super-long issuance to about 17 trillion yen, the lowest in 17 years"),
(900,"Japanese Ministry of Finance page (kanji header, green paper) with a growing yellow highlight","headline; ministry page; paper; highlight; caption","SS_MOF_DOC,PR_PAPER,OV_HIGHLIGHT","The Ministry is considering reducing issuance further"),
(1059,"Green US-map character holding a paper; 'Short and sweet!' bubble pops","headline; map character; paper; bubble; caption","CH_USMAP,PR_PAPER,OV_BUBBLE","America is moving to the short end as well"),
(1130,"Treasury text page with a light-green highlight; the US-map character slides in from the left edge","headline; text page; highlight; map character; paper; caption","SS_TBILL_TEXT,OV_HIGHLIGHT,CH_USMAP,PR_PAPER","T-bills run about 22 % of the debt"),
(1232,"'Considerations for T-bill issuance' advisory-committee page with Treasury seal and a growing yellow highlight","headline; page; seal; highlight; caption","SS_TBAC_PAGE,LOGO_TREASURY,OV_HIGHLIGHT","Above the 15-20 % range the Treasury's own committee recommends"),
(1374,"OECD chart page: linear 1.85x pan/zoom to the right chart, pointing host pops in","headline; chart page (pan/zoom); host; caption","SS_OECD_FIG,CH_HOST","Across the OECD, T-bills now out-issue fixed-rate bonds entirely"),
(1713,"OECD text page: zoom in 1.66x and a yellow highlight grows","headline; text page (zoom); highlight; caption","SS_OECD_TEXT,OV_HIGHLIGHT","The ratio of 30-year-plus to 1-5-year debt is the lowest since 2008; the OECD calls it cost-efficient ex ante"),
(1844,"Host at a desk with a laptop showing a dictionary page for 'ex ante'","headline; host; desk; browser page; caption","CH_HOST,PR_DESK,SS_DICTIONARY","Joke: which is Latin for beforehand"),
(1898,"OECD chart page with a thinking figure at the left","headline; chart; figure; caption","SS_OECD_FIG,CH_FIG","So what they're saying is it's cheaper for now"),
(1982,"Two green bond papers ('30 yrs', '5 yrs'); a 'DEBT' paper pops between them, then a thinking figure","headline; two papers; debt paper; figure; caption (end)","PR_BOND,PR_DEBTDOC,CH_FIG","Shortening doesn't reduce what you owe; it changes how often you ask")])
# S02
A.event("S02",105,105,"POP_IN","red arrow","Red arrow appears at the upper left of the chart in one frame.","SE003; d2",conf="HIGH")
A.event("S02",106,125,"POINTER_TRANSLATE","red arrow","Arrow drifts right by about 0.067 of the frame width and down by about 0.013 of its height over 20 frames, ending where the second move starts (f178).","blob_105_125",conf="MEDIUM",label="MEASURED")
A.E[-1]["easing"]="x linear (SUPPORTED, margin 0.021); y linear (AMBIGUOUS, margin 0.008)"; A.E[-1]["measure"]="blob_105_125.json"
A.event("S02",179,203,"POINTER_TRANSLATE","red arrow","Arrow travels from the upper left to the right end of the lower line over 25 frames; x fits linear, y ease-in (path follows the curve).","blob_178_204",conf="HIGH",label="MEASURED")
A.E[-1]["easing"]="x linear (SUPPORTED, margin 0.047); y ease_in_quad (SUPPORTED, margin 0.16)"; A.E[-1]["measure"]="blob_178_204.json"
# S03
A.event("S03",385,468,"HIGHLIGHT_SWEEP","yellow highlight on the market-feedback sentence","Yellow area grows from f385 to ~95 % of its maximum at f468 (99 px at analysis size), monotone fraction 0.91.","color_yellow",conf="MEDIUM",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
# S05
A.event("S05",792,792,"POP_IN","red '17T'","Red hand-lettered '17T' appears in one frame.","SE012; ev_01",conf="MEDIUM")
A.event("S05",825,825,"POP_IN","money bag","Money bag appears next to '17T' in one frame.","SE013; ev_01",conf="HIGH")
A.event("S05",862,862,"POP_IN","pointing host","Host with a pointer appears at the lower left in one frame.","SE014; ev_01",conf="HIGH")
# S06
A.event("S06",905,992,"HIGHLIGHT_SWEEP","yellow highlight on the ministry text","Yellow area grows from f905 to ~95 % of maximum at f992 (98 px), monotone fraction 0.94.","color_yellow",conf="MEDIUM",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
# S07
A.event("S07",1098,1098,"OVERLAY_POP","bubble 'Short and sweet!'","Speech bubble appears next to the map character in one frame.","SE017; d1",conf="HIGH")
# S08
A.event("S08",1135,1203,"HIGHLIGHT_SWEEP","light-green highlight on the T-bill sentence","Light-green area grows from f1135 to ~95 % of maximum at f1203 (143 px), monotone fraction 0.91.","color_lgreen",conf="MEDIUM",label="MEASURED")
A.E[-1]["measure"]="color_lgreen.json"
A.event("S08",1172,1192,"SLIDE_IN","US-map character","Character is absent at f1171 and slides in from the left edge over 21 frames, peeking in at the left of the page.","SE019; d1",conf="MEDIUM")
# S09
A.event("S09",1232,1297,"HIGHLIGHT_SWEEP","yellow highlight on the advisory-range sentence","Yellow highlight is already partly present at the cut and grows to ~95 % of maximum at f1297 (334 px).","color_yellow",conf="MEDIUM",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
# S10
A.event("S10",1409,1459,"CAMERA_SCROLL_ZOOM","OECD chart page","Page enlarges to 1.85x and pans left by about 88 px (at analysis size) over 52 frames, linear on all three channels.","camera_1408_1460",conf="HIGH",label="MEASURED",geo="net scale x1.846; image shift (-87.9,-3.6) px at 180-px analysis size")
A.E[-1]["easing"]="linear (SUPPORTED, margin 0.030 scale, 0.055 pan_x, 0.047 pan_y)"; A.E[-1]["measure"]="camera_1408_1460.json"
A.event("S10",1459,1460,"POP_IN","pointing host","Host face appears at the right at f1459 and the pointer arm at f1460.","SE022; d1",conf="MEDIUM")
A.event("S10",1518,1518,"POSE_SWAP","host arm","Host's pointer arm extends toward the chart in one frame.","SE024; d1",conf="MEDIUM")
# S11
A.event("S11",1745,1834,"CAMERA_SCROLL_ZOOM","OECD text page","Page enlarges to 1.66x with a vertical shift of about 36 px (analysis size) over 90 frames; scale fits ease-out cubic, pan_y ease-out cubic, pan_x ease-out quad.","camera_1744_1836",conf="HIGH",label="MEASURED",geo="net scale x1.655; image shift (0.1,-36.0) px at 180-px analysis size")
A.E[-1]["easing"]="ease_out_cubic (SUPPORTED, margin 0.092; pan_y agrees)"; A.E[-1]["measure"]="camera_1744_1836.json"
A.event("S11",1774,1832,"HIGHLIGHT_SWEEP","yellow highlight on the OECD phrase","Yellow area grows from f1774 to ~95 % of maximum at f1832 (747 px) while the page is still zooming.","color_yellow",conf="MEDIUM",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
# S14
A.event("S14",2035,2035,"POP_IN","'DEBT' paper","Red-labelled paper appears between the two bond papers in one frame.","SE035; ev_01",conf="HIGH")
A.event("S14",2065,2065,"POP_IN","thinking figure","Figure with hand to chin appears at the lower left in one frame.","SE036; ev_01",conf="HIGH")
A.event("S14",1995,1995,"POP_IN","'30 yrs' label","Label appears above the left paper in one frame.","SE033; ev_01",conf="MEDIUM")
A.event("S14",2010,2010,"POP_IN","'5 yrs' label","Label appears above the right paper in one frame.","SE034; ev_01",conf="MEDIUM")
A.write(headline="The REAL Reason the Bond Market's Panicking")
