import sys; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('YST8eMG3_Z8',2624)
A.scenes([
(0,"OECD issuance chart scales small-large-small; red '29T', money bag and a handwritten aside pop/write on","headline; bond-issuance chart; red 29T text; money bag; handwritten aside; caption","SS_ISSUANCE_CHART,TY_RED_29T,PR_BAG,TY_RED_NOTE","Scale of borrowing: 29 trillion dollars in 2026, 4 trillion more than two years ago"),
(267,"Host at a desk with a 'CF' laptop beside a PDF-viewer panel scrolling through the OECD Global Debt Report","headline; host; desk and laptop; PDF-viewer panel (scrolling); caption","CH_HOST,PR_DESK,SS_PDF_VIEWER,SS_REPORT_PAGES","The OECD publishes a 200-page report; reading it is a chore"),
(615,"Detective-hat figure with a magnifier","headline; figure; caption","CH_DETECTIVE","Turn to the report's takeaways"),
(678,"OECD text page with a growing yellow highlight; small thinking figure pops in at the lower right","headline; text page; highlight; small figure; caption","SS_OECD_TEXT,OV_HIGHLIGHT,CH_FIG","Nearly 80% of borrowing does not pay for anything new"),
(887,"Green US-map character with 'Actual useful things' and a 'Boring!' bubble","headline; map character; green text; bubble; caption","CH_USMAP,TY_GREEN_NOTE,OV_BUBBLE","Roads and schools are the useful things the money is not buying"),
(939,"Bearded 'DEBT' paper character (loop jitter)","headline; debt-paper character; caption","CH_DEBTMAN","Just moving the old pile of debt forward"),
(1011,"OECD text page with a growing yellow highlight; thinking figure pops in at the lower right","headline; text page; highlight; figure; caption","SS_OECD_TEXT,OV_HIGHLIGHT,CH_FIG","Refinancing cost: $13.5 trillion last year, about $14.5 trillion this year"),
(1298,"Figure at a green chalkboard: 'NOT even!'","headline; figure; blackboard; chalk text; caption","CH_FIG,PR_BLACKBOARD,TY_RED_NOTE","It doesn't arrive evenly"),
(1347,"Three 'DEBT' papers; one turns into a red block, later 'PAY IN 2027'","headline; three debt papers; red block; text; caption","PR_DEBTDOC,TY_RED_NOTE","A third of fixed-rate debt comes due by 2027"),
(1477,"Lone worried figure","headline; figure; caption","CH_LONE","Why the timing matters: when it was borrowed"),
(1538,"Line chart with two curves (US comparison)","headline; chart; caption","SS_INTEREST_CHART","Similar to the United States situation just covered"),
(1623,"OECD text page with an orange highlight and 'DEBT' paper icons","headline; text page; highlight; debt papers; caption","SS_OECD_TEXT,OV_HIGHLIGHT,PR_DEBTDOC","60% of the debt maturing by 2027 was issued in 2021 or earlier"),
(1904,"Bar/area chart page: linear zoom into the lower right; figure with pointer appears","headline; chart (zoom); figure; caption","SS_OECD_FIG,CH_FIG","Rates on new debt are about 2 points above the maturing debt"),
(2119,"OECD text page: small push-in, pointing figure rises in; highlight; 'DEBT' paper and money bag pop","headline; text page (push-in); figure; highlight; debt paper; money bag; caption","SS_OECD_TEXT,CH_FIG,OV_HIGHLIGHT,PR_DEBTDOC,PR_BAG","A third of developed-world debt is swapped one maturity at a time"),
(2338,"Lone worried figure: 'and we're already seeing it happen'","headline; figure; caption","CH_LONE","Turn: it is already happening"),
(2387,"OECD text page with a stepwise yellow highlight and sticky notes ('20%')","headline; text page; highlight; sticky notes; caption (end)","SS_OECD_TEXT,OV_HIGHLIGHT,PR_NOTES","One fifth of fixed-rate bonds outstanding in 2025 were issued above 4%")])
# S01
A.event("S01",27,81,"SCALE_TWEEN","bond-issuance chart","Chart grows from a small thumbnail (f26) to a large size by ~f45, holds to ~f63, then returns to the small size by f81; exact keyframes not measured.","SE001; ev_01",conf="MEDIUM")
A.event("S01",102,102,"POP_IN","red '29T' text","Red hand-lettered '29T' appears beside the chart in one frame.","SE002; d1",conf="HIGH")
A.event("S01",121,121,"POP_IN","money bag","Money bag appears next to '29T' in one frame.","SE003; d1",conf="HIGH")
A.event("S01",148,222,"TEXT_WRITE_ON","handwritten aside 'and the trend of incomprehensibly large numbers continues'","Rotated handwritten note grows in four bursts (f148-168, f176-188, f197-205, f216-222) while the narration reaches '$4 trillion more'.","SE004-007; d1",conf="MEDIUM")
A.event("S01",266,266,"HARD_CUT_REPLACE","29T, bag and aside removed","Overlays disappear one frame before the stage cut at f267; the chart alone is on screen at f266.","SE008; ev_01",conf="MEDIUM",amb="partial removal one frame before the cut")
# S02
A.event("S02",295,408,"SCREEN_RECORDING_INSERT","PDF-viewer panel","Panel content scrolls from the report cover through title, OECD logo, foreword, editorial, table and executive-summary pages; the thumbnail strip highlight follows (f296-f324 observed). Smooth over f307-408 with no zoom (net scale 1.0 measured).","SE009-010; d2",conf="MEDIUM",label="PLAUSIBLE_HYPOTHESIS",mclass="SCREENREC",amb="viewer chrome and moving thumbnail highlight are observed; whether this is a recorded scroll or a keyframed tall image is not provable")
A.E[-1]["measure"]="camera_306_409.json"; A.E[-1]["easing"]="not applicable: page content is replaced, so the zoom/pan fit is meaningless (net scale 1.0)"
A.event("S02",419,482,"SCREEN_RECORDING_INSERT","PDF-viewer panel","Viewer jumps to a blue chart page and scrolls through chart/table pages in bursts (f419-450, f459-482).","SE011-012; ev_01",conf="LOW",label="PLAUSIBLE_HYPOTHESIS",mclass="SCREENREC",amb="mechanism as above")
A.event("S02",488,560,"SCREEN_RECORDING_INSERT","PDF-viewer panel","Further page changes: single-frame jumps at f488 and f515, bursts f495-505 and f533-560.","SE013-017; ev_01",conf="LOW",label="PLAUSIBLE_HYPOTHESIS",mclass="SCREENREC",amb="mechanism as above")
A.event("S02",524,527,"POSE_SWAP","host","Host changes from the worried reading pose to a slumped pose with X-shaped eyes and open mouth over four intermediate frames; pose then holds through the scene.","SE016; d4",conf="HIGH")
A.event("S02",567,613,"SCREEN_RECORDING_INSERT","PDF-viewer panel","Last page changes (f567-579, f589-600) and a chart page scaling in the viewer at f607-613 before the cut.","SE018-021; ev_02",conf="LOW",label="PLAUSIBLE_HYPOTHESIS",mclass="SCREENREC",amb="mechanism as above")
# S04
A.event("S04",687,795,"HIGHLIGHT_SWEEP","yellow highlight on the borrowing sentence","Yellow area grows from f687 to ~95 % of its maximum at f795 (172 px at 180-px analysis size), monotone fraction 0.96, tracking the narration of the sentence.","color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S04",814,814,"POP_IN","small thinking figure","Figure with hand to chin appears at the lower right in one frame.","SE023; d5",conf="HIGH")
# S05
A.event("S05",917,917,"OVERLAY_POP","bubble 'Boring!'","Speech bubble appears on the map character in one frame.","SE025; d5",conf="HIGH")
# S06
A.event("S06",952,1010,"CHARACTER_LOOP_ANIMATION","bearded debt-paper character","Beard and face outline jitter subtly across 59 frames (f951-1005 sampled); looks like a short pose-swap loop, amplitude small.","SE027; d3",conf="LOW",amb="mechanism and loop length not measured")
# S07
A.event("S07",1017,1130,"HIGHLIGHT_SWEEP","yellow highlight on the refinancing sentence","Yellow area grows from f1017 to ~95 % of maximum at f1130 (138 px), monotone fraction 0.91.","color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S07",1154,1154,"POP_IN","thinking figure","Figure with hand to chin appears at the lower right in one frame (different pose from S04).","SE028; d5",conf="HIGH")
# S08
A.event("S08",1315,1315,"OVERLAY_POP","chalkboard text 'NOT even!'","Text appears on the board and the figure's arm moves to point at it, both in one frame.","SE030; d5",conf="HIGH")
# S09
A.event("S09",1374,1374,"POP_IN","red block","The left debt paper is replaced by a solid red block in one frame.","SE032; d5",conf="HIGH")
A.event("S09",1428,1428,"OVERLAY_POP","'PAY IN 2027' on the red block","White block text appears in one frame.","SE033; d5",conf="HIGH")
# S12
A.event("S12",1634,1865,"HIGHLIGHT_SWEEP","orange highlight on the 60 % sentence","Orange area grows from f1634 to ~95 % of maximum at f1865 (317 px), monotone fraction 0.91; the slowest highlight in this video (231 frames).","color_orange",conf="MEDIUM",label="MEASURED")
A.E[-1]["measure"]="color_orange.json"
# S13
A.event("S13",1938,1990,"CAMERA_SCROLL_ZOOM","chart page","Linear zoom to 1.689x over 54 frames with the image shifting left and up (toward the lower right); scale, pan_x and pan_y all fit linear.","camera_1937_1991",conf="HIGH",label="MEASURED",geo="net scale x1.689; image shift (-66.8,-32.9) px at 180-px analysis size")
A.E[-1]["easing"]="linear (SUPPORTED, margin 0.058)"; A.E[-1]["measure"]="camera_1937_1991.json"
A.event("S13",1989,1991,"POP_IN","pointing figure","Figure with a pointer appears at the lower right within three frames (absent at f1988, present at f1991).","SE038; d3",conf="MEDIUM")
# S14
A.event("S14",2138,2146,"CAMERA_PUSH_IN","text page","Page enlarges about 1.29x over 9 frames; ease type ambiguous (linear vs smoothstep).","camera_2137_2146",conf="MEDIUM",label="MEASURED",geo="net scale x1.288 about stage centre; shift (+1.6,+6.4) px at 180-px analysis size")
A.E[-1]["easing"]="AMBIGUOUS (linear best, margin 0.016, 9 samples)"; A.E[-1]["measure"]="camera_2137_2146.json"
A.event("S14",2143,2146,"CHARACTER_RISE_IN","pointing figure","Figure with pointer is absent through f2142 and fully on screen at f2146.","SE040; d3",conf="MEDIUM")
A.event("S14",2154,2235,"HIGHLIGHT_SWEEP","yellow highlight on the maturing-debt sentence","Yellow area grows from f2154 to ~95 % of maximum at f2235 (75 px), monotone fraction 0.89.","color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S14",2272,2272,"POP_IN","'DEBT' paper","Paper appears at the left in one frame.","SE043; d5",conf="HIGH")
A.event("S14",2302,2302,"POP_IN","money bag","Money bag appears on the paper in one frame.","SE044; d5",conf="HIGH")
# S16
A.event("S16",2387,2603,"HIGHLIGHT_SWEEP","yellow highlight on the 2025 bond sentence","Highlight is already present (285 px) at the cut and grows in steps (f2461, f2520, f2595-2619) to 545 px by f2623.","color_yellow",conf="MEDIUM",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.write(headline="Everybody's Fighting Over the Same Pile of Debt")
