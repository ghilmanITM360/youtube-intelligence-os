import sys; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('ZDoeEd8fMdo',2455)
A.scenes([
(0,"'GIGANTIC BUSINESS' office building shrinks, engine photo and a hand with a speech bubble pop in","headline; building sign; photo; hand; bubble; caption","PR_BLDG,PHOTO_ENGINE,OV_BUBBLE","Grown companies are bolting old aircraft engines to the ground for power"),
(181,"Latitude Media article page: yellow highlight grows, turbine photo pops, red dotted line draws","headline; article; highlight; photo; red dotted line; caption","SS_LATITUDE_PAGE,OV_HIGHLIGHT,PHOTO_TURBINE,OV_REDLINE","Two developers reportedly paid $25 million just to reserve a place in line"),
(370,"US electricity-sources stack chart with a red circle on 'natural gas 40.8 %'; US-map character and a lightning character pop in","headline; chart; red circle; map character; lightning character; caption","SS_EIA_CHART,OV_REDCIRCLE,CH_USMAP,CH_LIGHTNING","Gas turbines produce roughly 40 % of America's electricity"),
(483,"Large photo of a gas turbine","headline; photo; caption","PHOTO_TURBINE","Among the most complex machines on Earth"),
(583,"Figure at a green blackboard: 'Now THAT is exclusive'","headline; figure; blackboard; caption","CH_FIG,PR_BLACKBOARD","Only a handful of companies can build one"),
(668,"Text page with three manufacturer logos and a yellow highlight","headline; text page; logos; highlight; caption","SS_MARKET_TEXT,LOGO_GEVERNOVA,LOGO_SIEMENS,LOGO_MITSUBISHI,OV_HIGHLIGHT","Three manufacturers control over three quarters of the global market"),
(778,"Lone figure; GE Vernova logo pops beside its head","headline; figure; logo; caption","CH_FIG,LOGO_GEVERNOVA","One of them is GE Vernova"),
(833,"Utility Dive article on the GE Vernova backlog with a turbine icon and an 'I want a nice big turbine' bubble","headline; article; turbine icon; bubble; caption","SS_UTILITYDIVE,PR_TURBINE,OV_BUBBLE","Backlog from 80 to 116 gigawatts"),
(966,"Teal-header company page with a worried man at lower right: red ellipse draws on the phrase, yellow highlight grows","headline; page; man; red ellipse; highlight; caption","SS_GE_PAGE,CH_MAN,OV_REDCIRCLE,OV_HIGHLIGHT","Largely sold out through the end of 2028"),
(1118,"Text page with a man pointing at the lower left: yellow highlight grows to f1270, then smokestack factories pop in","headline; text page; highlight; man; factories; caption","SS_CAPACITY_TEXT,OV_HIGHLIGHT,CH_MAN,PR_FACTORY","In 2024 developers ordered nearly 3x more turbine capacity than factories can produce in a year"),
(1394,"Tech-company logos and manufacturer logos with speech bubbles ('A SUPERCALIFRAGILLION DOLLARS!!!', 'Pls stop making up numbers', 'WE CAN'T!!!')","headline; logos; bubbles; caption","LOGO_BIGTECH,LOGO_GEVERNOVA,OV_BUBBLE","It doesn't matter how many zeros Big Tech puts on the check"),
(1573,"Lone worried figure: 'but it's not just the gas turbines either'","headline; figure; caption","CH_LONE","The problem is broader than turbines"),
(1645,"Transformers poster crossed out with a red X and 'not you'; the picture slides out","headline; picture; red X; text; caption","PHOTO_TRANSFORMERS,OV_REDX","Transformers, the grid machines, not the movie"),
(1688,"Transformer lead-time bar chart with power poles; man and red '30%' pop in","headline; bar chart; poles; red arrow; man; red 30 %; caption","SS_TRANSFORMER_CHART,PR_POLE,CH_MAN,TY_RED","Transformers take over 2.5 years with a 30 % supply shortage"),
(1899,"Lone figure: 'new transmission lines?'","headline; figure; caption","CH_LONE","Transmission lines"),
(1941,"Permitting-reform text page: 1.89x ease-out zoom, yellow highlight, papers and an angry man pop in","headline; text page (zoom); highlight; papers; angry man; caption","SS_PERMIT_TEXT,OV_HIGHLIGHT,PR_PAPER,CH_MAN","6.5 years to complete due to permitting delays and a mountain of other BS"),
(2119,"Typed 'You are...' with a red queue number and a server icon","headline; typed text; red number; server; caption","TY_TYPED,TY_RED,PR_SERVER","It's not a single waitlist, it's the entire supply chain"),
(2199,"Power pole; US-map character sits on the wire","headline; pole; wire; map character; caption","PR_POLE,CH_USMAP","American energy supply"),
(2276,"Chart page with a red arrow and a Netflix logo","headline; chart; red arrow; logo; caption","SS_CHART,OV_REDARROW,LOGO_NETFLIX","Tech moves at Netflix speeds"),
(2349,"Turtle carrying a pole: 'moving at the speed of Blockbuster'","headline; turtle; pole; caption (end)","CH_TURTLE,PR_POLE","Infrastructure moves at the speed of Blockbuster")])
A.event("S01",69,69,"MORPH_REARRANGE","building","Building and sign shrink to about a third of their size and move left in one frame.","SE001; ev_01",conf="HIGH")
A.event("S01",88,88,"POP_IN","engine photo","Photo appears to the right of the building in one frame.","SE002; ev_01",conf="HIGH")
A.event("S01",128,128,"POP_IN","hand with bubble","Hand and a speech bubble (text not verified at this size) appear in one frame.","SE003; ev_01",conf="HIGH")
A.event("S02",187,262,"HIGHLIGHT_SWEEP","yellow highlight on the reservation sentence","Yellow area grows from f187 to ~95 % of maximum at f262 (827 px at analysis size), monotone fraction 0.97.","color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S02",287,287,"POP_IN","turbine photo","Photo appears at the top right in one frame.","SE005; ev_01",conf="HIGH")
A.event("S02",322,352,"STROKE_REVEAL","red dotted line","Red dotted line draws left to right under the highlight; red area reaches 95 % at f348 (183 px at analysis size, monotone 1.0) and the last pixels settle by f352.","color_red",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_red.json"
A.event("S03",411,411,"OVERLAY_POP","red circle","Red circle appears on the 'natural gas 40.8 %' block in one frame (region-consistent).","SE008; ev_01",conf="MEDIUM")
A.event("S03",434,434,"POP_IN","US-map character","US-map character appears at the right edge in one frame.","SE009; ev_01",conf="MEDIUM")
A.event("S03",453,453,"POP_IN","lightning character","Small lightning character appears at the left in one frame.","SE010; ev_01",conf="MEDIUM")
A.event("S06",678,689,"POP_IN","manufacturer logos","GE Vernova logo at f678, then Siemens and Mitsubishi logos at f689.","SE017-018; ev_01",conf="MEDIUM")
A.event("S06",724,760,"HIGHLIGHT_SWEEP","yellow highlight","Yellow area grows from f724 to ~95 % of maximum at f760 (305 px), monotone 1.0.","color_yellow",conf="MEDIUM",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S07",796,796,"POP_IN","GE Vernova logo","Logo appears beside the figure's head in one frame.","SE021; ev_01",conf="MEDIUM")
A.event("S08",875,875,"OVERLAY_POP","bubble 'I want a nice big turbine'","Speech bubble appears in one frame.","SE023; ev_01",conf="MEDIUM")
A.event("S09",1016,1044,"STROKE_REVEAL","red ellipse","Red ellipse is drawn around the phrase over ~29 frames.","SE026; ev_01",conf="MEDIUM",amb="progress not tracked")
A.event("S09",1020,1106,"HIGHLIGHT_SWEEP","yellow highlight","Yellow area grows from f1020 to ~95 % of maximum at f1106 (316 px), monotone 0.97.","color_yellow",conf="MEDIUM",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S09",1091,1103,"EXPRESSION_SWAP","man","Man's face changes over 13 frames (worried to alarmed) at the lower right.","SE027; ev_01",conf="MEDIUM")
A.event("S10",1118,1282,"HIGHLIGHT_SWEEP","yellow highlight","Highlight present at the cut and grows to ~95 % of maximum at f1270 (585 px), monotone 0.99; final pixels settle by f1281.","color_yellow",conf="MEDIUM",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S10",1285,1285,"POP_IN","smokestack factories","Factory pictures appear at the upper corners in one frame.","SE029; ev_01",conf="MEDIUM")
A.event("S11",1443,1443,"CAPTION_CHUNK_CHANGE","speech bubble text","Bubble text changes to 'A SUPERCALIFRAGILLION DOLLARS!!!' in one frame.","SE034; ev_01",conf="HIGH")
A.event("S11",1475,1475,"OVERLAY_POP","bubble 'Pls stop making up numbers'","Second speech bubble appears in one frame.","SE035; ev_01",conf="MEDIUM")
A.event("S11",1521,1521,"OVERLAY_POP","bubble 'WE CAN'T!!!'","Third speech bubble appears in one frame.","SE036; ev_01",conf="MEDIUM")
A.event("S13",1661,1679,"PROP_DRIFT","Transformers picture","Red X and 'not you' text appear at f1661; the picture then slides out to the right over ~16 frames.","SE039; ev_01",conf="MEDIUM")
A.event("S14",1733,1733,"POP_IN","power poles","Poles appear at both sides of the bar chart in one frame.","SE041; ev_02",conf="MEDIUM")
A.event("S14",1820,1820,"POP_IN","man and '30%'","Man with red '30%' appears at the right in one frame.","SE044; ev_02",conf="MEDIUM")
A.event("S16",1941,1996,"CAMERA_SCROLL_ZOOM","permitting text page","Page enlarges 1.89x about the stage centre over 56 frames, ease-out cubic (scale and pan_x agree).","camera_1941_1996",conf="HIGH",label="MEASURED",geo="net scale x1.893 about stage centre")
A.E[-1]["easing"]="ease_out_cubic (SUPPORTED, margin 0.093)"; A.E[-1]["measure"]="camera_1941_1996.json"
A.event("S16",1974,2049,"HIGHLIGHT_SWEEP","yellow highlight","Yellow area grows from f1974 to ~95 % of maximum at f2049 (184 px), monotone 0.99, starting while the zoom is still settling.","color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S16",2065,2104,"POP_IN","paper stacks and angry man","Paper stacks pop in at f2019, f2065 and f2078 and the angry man with a red headband at f2104.","SE047-054; ev_02",conf="MEDIUM")
A.event("S17",2122,2134,"TEXT_WRITE_ON","typed 'You are...'","Text appears letter by letter over 13 frames (Y, You, You ar, You are).","SE055; ev_02",conf="HIGH")
A.event("S17",2153,2153,"OVERLAY_POP","red queue number","Red '198576 is queue' appears in one frame.","SE056; ev_02",conf="MEDIUM")
A.event("S18",2249,2249,"POP_IN","US-map character","US-map character appears on the wire in one frame.","SE061; ev_02",conf="HIGH")
A.event("S19",2276,2334,"POINTER_TRANSLATE","red arrow","Red arrow travels along the chart over ~59 frames; the Netflix logo pops in over f2313-2316.","SE062; ev_02",conf="LOW",amb="path and logo timing not separated")
A.write(headline="the clock on ai we can't control")
