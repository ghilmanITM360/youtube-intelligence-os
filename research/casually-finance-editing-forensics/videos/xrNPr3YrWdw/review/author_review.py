import sys; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('xrNPr3YrWdw',1992)
A.scenes([
(0,"Lone sad figure: 'They weren't wiped out by a crash'","headline; figure; caption","CH_FIG","Opens mid-argument: pensions were not wiped out by a crash"),
(48,"Blue building with a red sign; a certificate flutters away and a 'Pension? What pension?' bubble pops","headline; building; certificate; bubble; caption","PR_BLDG,PR_DOC,OV_BUBBLE","They just weren't offered anymore"),
(95,"PDF viewer on a Bureau of Labor Statistics table: page bursts, zoom to full page, buildings and certificate pop at the right","headline; PDF viewer then full-width table; red box; buildings; certificate; caption","SS_BLS_VIEWER,SS_BLS_TABLE,PR_BLDG,PR_DOC,OV_REDBOX","1985: 80 % of medium/large-company workers in defined-benefit plans; 2000: 36"),
(471,"PDF viewer on a chart page: zoom to the charts, red '14%' and a pointing figure pop","headline; PDF viewer (zoom); chart; red 14%; figure; caption","SS_PENSION_CHART,TY_RED,CH_FIG","Today the share is around 14 %"),
(549,"Lone smiling figure: 'which may just sound like a small paperwork change'","headline; figure; caption","CH_FIG","The change sounds small"),
(629,"Handwritten 'It isn't' on a blank stage, 'isn't' in red","headline; handwritten text; caption","TY_RED_NOTE","But it isn't small"),
(649,"Large certificate shrinks into the hand of a 'Dwight retires' figure; red timeline grows with bags, certificates and bond tags","headline; certificate; figure; red timeline; year labels; bags; certificates; bond tags; caption","PR_CHECK,CH_FIG,OV_TIMELINE,PR_BAG,PR_DOC,PR_BOND","Pension = a fixed amount on a fixed schedule, so the company has to buy something that matches the shape"),
(832,"'401(k) Plan' card slides left; striped building with red sign pops at the right","headline; card; building; caption","SS_401K_CARD,PR_BLDG","But under a 401(k) the company owes nothing past payday"),
(933,"EBRI/ICI bar chart with a pointing host that travels to the tall bars; photo, 401K paper and bond note pop; yellow underline grows","headline; chart; host with pointer; photo; paper; sticky note; highlight; caption","SS_EBRI_CHART,CH_HOST,PHOTO_MARKET,PR_DOC,PR_NOTES,OV_HIGHLIGHT","More than 70 % of 401(k) assets are in stocks, standalone bond funds about 5 %"),
(1258,"OECD logo","headline; logo; caption","LOGO_OECD","Introducing the OECD"),
(1352,"World map with member countries in orange","headline; map; caption","SS_OECD_MAP","An international organization of 38 developed countries"),
(1451,"Avengers logo","headline; logo; caption","LOGO_AVENGERS","The Avengers, but for economics"),
(1498,"Green US-map and a large green map character with a target and a red hat","headline; map characters; caption","CH_MAPS","Across its member countries"),
(1542,"OECD text page with a growing yellow highlight; bag, certificate and OECD logo icons below","headline; text page; highlight; bag; certificate; logo; caption","SS_OECD_TEXT,OV_HIGHLIGHT,PR_BAG,PR_DOC,LOGO_OECD","Pension funds' domestic bond holdings cut in half, 8 % in 2007 to 4 % last year"),
(1790,"Tiny figure under 'CHANGE' with red 'BIGGEST' dropping in","headline; figure; text; caption","CH_FIG,TY_EMPHASIS","The biggest change in structural demand"),
(1866,"Bond certificate with red '50 years!'","headline; bond certificate; red text; caption","PR_BOND,TY_RED","In the bond market in 50 years"),
(1915,"Woman on a phone with a 'Hello?' bubble","headline; figure; bubble; caption (end)","CH_WOMAN,OV_BUBBLE","Punchline: someone in HR named Susan")])
# S02
A.event("S02",73,93,"PROP_DRIFT","certificate","Certificate drifts up and to the right while rotating and leaves the frame over ~20 frames.","SE002; ev_01",conf="MEDIUM")
A.event("S02",89,89,"OVERLAY_POP","bubble 'Pension? What pension?'","Speech bubble appears in one frame.","SE002; ev_01",conf="HIGH")
# S03
A.event("S03",96,158,"SCREEN_RECORDING_INSERT","PDF viewer","Viewer page content changes in bursts (f113-115, f125-129, f139-143, f153-158) while the report is scrolled to the table; viewer toolbar and thumbnail strip visible.","SE003-006; d2",conf="LOW",label="PLAUSIBLE_HYPOTHESIS",mclass="SCREENREC",amb="viewer chrome is observed; recorded scroll versus keyframed tall image is not provable")
A.event("S03",184,203,"CAMERA_SCROLL_ZOOM","viewer to full-width table","Table page enlarges about 1.27x over ~20 frames while the viewer chrome exits to the left until the page fills the stage width.","camera_183_203",conf="MEDIUM",label="MEASURED",geo="net scale x1.266 about stage centre; shift (-17.1,-7.8) px at 180-px analysis size")
A.E[-1]["easing"]="AMBIGUOUS (smoothstep vs linear, margin 0.005)"; A.E[-1]["measure"]="camera_183_203.json"
A.event("S03",248,248,"POP_IN","small building","Small blue building appears at the right edge; the red outline on the '1985' row is present by this frame (absent at f202).","SE008; d2",conf="MEDIUM")
A.event("S03",266,266,"POP_IN","building group with sign","Larger building with a sign appears beside the table in one frame.","SE009; d2",conf="HIGH")
A.event("S03",326,326,"POP_IN","pension certificate","Certificate appears on the table's left in one frame.","SE010; d2",conf="MEDIUM")
# S04
A.event("S04",471,502,"CAMERA_SCROLL_ZOOM","viewer chart page","Viewer jumps to a chart page and the view enlarges about 1.28x over ~32 frames; scale fits linear, pans disagree because page content changes (f494-500).","camera_470_502",conf="MEDIUM",label="MEASURED",geo="net scale x1.275 about stage centre")
A.E[-1]["easing"]="linear scale (SUPPORTED, margin 0.038); pans inconsistent"; A.E[-1]["measure"]="camera_470_502.json"
A.event("S04",518,528,"CAMERA_SCROLL_ZOOM","viewer chart page","Further enlargement of about 1.41x over 10 frames; ease type ambiguous.","camera_518_528",conf="LOW",label="MEASURED",geo="net scale x1.405")
A.E[-1]["easing"]="AMBIGUOUS (smoothstep, margin 0.014; 10 samples)"; A.E[-1]["measure"]="camera_518_528.json"
A.event("S04",526,526,"POP_IN","red '14%' and pointing figure","Red hand-lettered '14%' and a figure with a pointer appear together in one frame.","SE014; ev_01",conf="HIGH")
# S06
A.event("S06",629,629,"POP_IN","handwritten 'It'","'It' appears with a cursor-like mark in one frame.","SE016; ev_01",conf="MEDIUM")
A.event("S06",632,632,"OVERLAY_POP","red 'isn't'","Red 'isn't' appears in one frame.","SE016; ev_01",conf="HIGH")
# S07
A.event("S07",673,690,"SCALE_TWEEN","certificate","Certificate shrinks and tilts over ~18 frames to a small icon, which is then held by the figure in S08.","SE018; ev_01",conf="MEDIUM",amb="shrink and rotation are bundled; not separately measured")
# S08
A.event("S07",698,784,"STROKE_REVEAL","red timeline","Red line grows from the 'Dwight retires' marker to the right edge: 8 px at f698, 134 px at f800 (analysis size), monotone fraction 1.0, in step with the labels 'Year 1' (f706), 'Year 15' (f724), 'Year 30' (f752), 'Year 35+' (f779).","color_red",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_red.json"
A.event("S07",706,713,"PROP_DRIFT","money bag","A bag appears at 'Year 1' and drops beside the figure over 8 frames.","SE019; d1",conf="MEDIUM")
A.event("S07",724,737,"PROP_DRIFT","money bag and certificate","Bag appears at 'Year 15' and drops beside a new certificate over ~14 frames.","SE020; d1",conf="MEDIUM")
A.event("S07",752,763,"PROP_DRIFT","money bag and certificate","Same drop at 'Year 30' (12 frames).","SE021; d1",conf="MEDIUM")
A.event("S07",779,786,"PROP_DRIFT","money bag and certificate","Same drop at 'Year 35+' (8 frames).","SE022; d1",conf="MEDIUM")
A.event("S07",801,801,"MORPH_REARRANGE","timeline set","Layout rebuilds in one frame: four bond tags appear above, the timeline moves up and bags and certificates re-seat below.","SE023; d1",conf="MEDIUM")
# S09
A.event("S08",868,890,"PROP_DRIFT","401(k) card","Card slides left by about 40 px (at 360 px width) over 23 frames.","SE025; d4",conf="MEDIUM")
A.event("S08",891,891,"POP_IN","striped building with red sign","Building appears at the right in one frame.","SE025; d4",conf="HIGH")
# S10
A.event("S09",970,970,"POP_IN","pointing host","Host head and arm appear at the lower left in one frame.","SE027; d3",conf="HIGH")
A.event("S09",972,1040,"HIGHLIGHT_SWEEP","yellow underline under the chart","Yellow area grows from about f972 to ~95 % of its maximum at f1040 (37 to 262 px at analysis size).","color_yellow",conf="MEDIUM",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S09",1052,1066,"POINTER_TRANSLATE","host and pointer arm","Host moves from the lower left to the right end of the chart over 15 frames and extends the arm to the tall bars (mouth open).","SE028; d3",conf="MEDIUM",amb="path not tracked")
A.event("S09",1148,1148,"POP_IN","stocks photo","Photo appears at the upper left in one frame.","SE029; d3",conf="HIGH")
A.event("S09",1180,1180,"POSE_SWAP","host and 401K paper","Host is back at the lower left (arm no longer on the bars) and a '401K' paper appears next to the photo, both by this frame.","SE031; d3",conf="MEDIUM",amb="host return path not detected between f1157 and f1179")
A.event("S09",1225,1225,"POP_IN","bond sticky note","Yellow 'BOND' note appears at the left edge in one frame.","SE032; d3",conf="HIGH")
# S15
A.event("S14",1553,1761,"HIGHLIGHT_SWEEP","yellow highlight on the pension-fund sentence","Yellow area grows from f1553 to ~95 % of maximum at f1761 (347 px at analysis size), monotone fraction 0.87.","color_yellow",conf="HIGH",label="MEASURED")
# S16
A.event("S15",1801,1841,"SCALE_TWEEN","'CHANGE' and red 'BIGGEST' text","'CHANGE' scales in from the top (f1801-1811); red 'BIGGEST' grows from 46 to 790 px (f1813-1825) and settles at 629 px by f1835, an area overshoot of about 26 % (indicative of an ease with overshoot).","SE042; color_red",conf="MEDIUM",label="MEASURED",amb="slide position and scale not separated; red area only")
A.E[-1]["measure"]="color_red.json"
# S17
A.event("S16",1895,1895,"OVERLAY_POP","red '50 years!'","Red hand-lettered text appears beside the bond note in one frame.","SE044; d3",conf="HIGH")
# S18
A.event("S17",1945,1945,"OVERLAY_POP","bubble 'Hello?'","Speech bubble appears in one frame.","SE046; d3",conf="HIGH")
A.event("S10",1259,1262,"UNRESOLVED_CHANGE","OECD logo","Four frames after the cut with changes of 0-9 px; mechanism not resolved.","SE033; ev_02",conf="LOW",label="MEASURED",mclass="INDET",amb="below the stage-change threshold")
A.write(headline="The Bond Market Lost It's Favorite Buyer")
