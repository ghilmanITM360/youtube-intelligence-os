import sys, json; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('H3PRCteue9Y',1885)
A.scenes([
(0,"Black-and-white portrait slides in at the upper left under 'The 60th US Secretary of the Treasury'; a red 'David Kennedy' label and arrow pop; a document page slides up with a yellow highlight; caption 'reportedly drew on the fund to buy an Oriental carpet for $8,000' (red '$8,000')","portrait; red label; document page (slide-in); highlight; caption","PHOTO_PORTRAIT,OV_REDARROW,SS_ESF_DOC,OV_HIGHLIGHT,TY_RED","The 60th Secretary reportedly bought a carpet from the fund"),
(235,"Treasury seal; a pot of cash slides in from the left; an Exchange Stabilization Fund page and a red arrow pop: 'the answer is a pot of money at the Treasury called the Exchange Stabilization Fund'","seal; pot; page; red arrow; caption","LOGO_TREASURY,PR_POT,SS_ESF_PAGE,OV_REDARROW","The Exchange Stabilization Fund"),
(364,"White frame, typed caption 'The Secretary of the Treasury can spend it without asking Congress'; a portrait with a flag slides in, a bubble 'I don't need y'all!' pops","caption; portrait with flag; bubble","PHOTO_PORTRAIT,OV_BUBBLE,TY_RED","He can spend it without asking Congress"),
(466,"Grey-haired official handing a paper to a red-haired figure; bubble 'Mr. President, could you sign this?': 'he just needs the President's signature'","two figures; paper; bubble; caption","CH_OFFICIAL,CH_FIG,PR_DOC,OV_BUBBLE","He just needs the President's signature"),
(520,"Grey credit card that turns gold and gets a green check: 'and the credit card opens up'","card; check; caption","PR_CARD,OV_CHECK","The credit card opens up"),
(576,"White frame with 'But why does it exist?'; a pot of cash rises from the bottom","caption; pot","PR_POT","But why does it exist?"),
(619,"Exchange Stabilization Fund web page that enlarges; the host pops in, a dollar sign and circular arrows pop: 'created with one goal, to stabilize the exchange value of the dollar'","web page (zoom); host; dollar sign; arrows; caption","SS_ESF_PAGE,CH_HOST,TY_DOLLAR,OV_ARROWS","Created to stabilize the exchange value of the dollar"),
(713,"Portrait of William Simon with a big empty bubble that fills with 'To stabilize, sure XDDDD': 'but throughout history, that's not what it tends to get used for'","portrait; bubble; caption","PHOTO_PORTRAIT,OV_BUBBLE","That's not what it gets used for"),
(803,"Dictionary entry for 'stabilize' with the host pointing; red caption 'wasn't as clearly defined as it should have been' and a red X","dictionary page; host; red caption; red X","SS_DICT_PAGE,CH_HOST,TY_RED,OV_REDX","The word stabilize wasn't clearly defined"),
(912,"Host, then a pot and the official pop; bubble 'And what if I used some for Clash Royale?' with a red 'no' and X: 'the fund tends to get spent on whatever the Secretary decides'","host; pot; official; bubble; red X","CH_HOST,PR_POT,CH_OFFICIAL,OV_BUBBLE,OV_REDX","Spent on whatever the Secretary decides"),
(1062,"'The 63rd Secretary of the Treasury': a portrait slides in, red 'William Simon' label, a document page slides in with highlights and red 'that cost $131,000'","caption; portrait; red label; document page; highlights; red text","PHOTO_PORTRAIT,OV_REDARROW,SS_ESF_DOC,OV_HIGHLIGHT,TY_RED","A 42-person trip costing $131,000"),
(1452,"Pot of cash: 'Once again, paid for by the Exchange Stabilization Fund'; the pot gets angry eyes and a bubble 'Are you bloody JOKING?!?'","pot; bubble; caption","PR_POT,OV_BUBBLE","Once again paid for by the fund"),
(1548,"Stick figure, then the official peeks in: 'You can think of it as the Secretary of the Treasury and President's personal piggy bank'","figure; official; caption","CH_FIG,CH_OFFICIAL","The personal piggy bank"),
(1617,"Official and the President at a desk; a pink piggy bank pops","figures; desk; piggy bank","CH_OFFICIAL,CH_PRESIDENT,PR_PIG","Secretary and President's piggy bank"),
(1665,"'He who shall NOT be named questioned!!!' with a strike-through; the official rises from the bottom","caption; official","CH_OFFICIAL,TY_RED","He who shall not be questioned"),
(1740,"Host with 'And I'm quoting'; a statute page slides in, red 'may NOT be reviewed' and yellow highlights appear","host; statute page; red text; highlights","CH_HOST,SS_STATUTE,TY_RED,OV_HIGHLIGHT","His decisions may not be reviewed")])
A.event("S01",1,33,"SLIDE_IN","portrait","Portrait slides in from the left edge over 33 frames.","SE001; ev_01",conf="HIGH",amb="path and easing not measured")
A.event("S01",78,78,"OVERLAY_POP","red 'David Kennedy' label","Red label and arrow appear beside the portrait in one frame (0 to 118 red px), 40 ms before ASR 'David' (2.64 s).","SE002; color_red",conf="HIGH",label="MEASURED")
A.event("S01",100,100,"CAPTION_CHUNK_CHANGE","caption 'reportedly drew on the fund to buy an Oriental carpet for $8,000'","Caption block appears at the lower right in one frame.","SE003; ev_01",conf="MEDIUM")
A.event("S01",114,172,"SLIDE_IN","document page","Document page enters from the right edge and enlarges over ~59 frames; a yellow highlight grows from 0 to 97 px over f139-164.","SE004; color_yellow",conf="MEDIUM",label="MEASURED",amb="page geometry not measured")
A.event("S02",255,269,"SLIDE_IN","pot of cash","Pot slides in from the left edge over 15 frames and cash piles into it (yellow area 858 to 3302 px).","SE007; color_yellow",conf="HIGH",label="MEASURED")
A.event("S02",315,315,"OVERLAY_POP","Exchange Stabilization Fund page and red arrow","Web page and a red arrow appear in one frame (red 0 to 160 px), 0.18 s after ASR 'Exchange' (10.32 s).","SE009; color_red",conf="HIGH",label="MEASURED")
A.event("S03",368,393,"SLIDE_IN","portrait with flag","The caption starts to type at f368 and the portrait with a flag slides in from the right edge from f372 to f393 (red stripe area 13 to 409 px).","SE011; color_red",conf="MEDIUM",label="MEASURED")
A.event("S03",438,438,"OVERLAY_POP","bubble 'I don't need y'all!'","Bubble appears under the portrait in one frame.","SE012; ev_01",conf="HIGH")
A.event("S05",546,565,"OPACITY_FADE","credit card","Card changes from grey to gold over ~13 frames (yellow area 0 to 3439 px at f546-558) and a green check appears and flashes at f560 and f565.","SE015-017; color_yellow",conf="MEDIUM",label="MEASURED",mclass="INDET",amb="colour change versus cross-fade not resolved")
A.event("S06",592,606,"CHARACTER_RISE_IN","pot of cash","Pot of cash rises from the bottom edge over ~15 frames (yellow area 0 to 3606 px).","SE019; color_yellow",conf="HIGH",label="MEASURED")
A.event("S07",619,648,"CAMERA_SCROLL_ZOOM","Exchange Stabilization Fund page","Page enlarges 1.55x with a shift of (+85.9,+110.1) px at analysis size over ~30 frames, linear on scale and both pans (SUPPORTED, margin 0.035-0.045).","camera_618_649",conf="HIGH",label="MEASURED",geo="net scale x1.546; image shift (+85.9,+110.1) px at 180-px analysis size")
A.E[-1]["easing"]="linear (SUPPORTED, margin 0.035-0.045)"; A.E[-1]["measure"]="camera_618_649.json"
A.event("S07",652,652,"POP_IN","host","Host appears at the upper right in one frame.","SE021; ev_02",conf="HIGH")
A.event("S07",668,695,"POP_IN","dollar sign and circular arrows","Dollar sign and circular arrows appear beside the host in three small steps (f668, f678, f695).","SE022-024; ev_02",conf="MEDIUM",amb="step contents read from small events")
A.event("S08",744,744,"OVERLAY_POP","empty bubble","Large empty bubble appears at the left in one frame; its text 'To stabilize, sure XDDDD' is filled in by f802.","SE026; ev_02",conf="HIGH")
A.event("S09",818,818,"SCALE_TWEEN","dictionary entry","Dictionary entry enlarges (the 'stabilize' headword grows) in one step.","SE028; ev_02",conf="MEDIUM",amb="step versus short tween not resolved")
A.event("S09",842,842,"OVERLAY_POP","red caption","Red caption 'wasn't as clearly defined as it should have been' starts to appear over the definition (0 to 61 red px at f842), 0.13 s after ASR 'wasn't' (27.94 s).","SE029; color_red",conf="HIGH",label="MEASURED")
A.event("S09",870,870,"OVERLAY_POP","red X","Red X appears across the definition in one frame (61 to 1291 red px), at ASR 'defined' (28.96 s).","SE030; color_red",conf="HIGH",label="MEASURED")
A.event("S10",931,931,"POP_IN","pot of cash","Pot of cash appears in one frame (yellow area +2447 px).","SE032; color_yellow",conf="HIGH",label="MEASURED")
A.event("S10",970,970,"POP_IN","official","Grey-haired official appears at the left in one frame.","SE033; ev_02",conf="HIGH")
A.event("S10",1005,1005,"OVERLAY_POP","bubble","Bubble 'And what if I used some for Clash Royale?' appears in one frame.","SE034; ev_02",conf="HIGH")
A.event("S10",1047,1047,"OVERLAY_POP","red 'no' and red X","Red 'no' and an X over the bubble appear in one frame (0 to 422 red px).","SE035; color_red",conf="HIGH",label="MEASURED")
A.event("S11",1064,1078,"SLIDE_IN","portrait","Portrait slides in from the left edge over ~15 frames.","SE037; ev_02",conf="HIGH",amb="path and easing not measured")
A.event("S11",1129,1129,"CAPTION_CHUNK_CHANGE","small caption 'his glasses were thick AF'","Small aside caption appears under the portrait in one frame (0 to 119 red px).","SE039; color_red",conf="HIGH",label="MEASURED")
A.event("S11",1159,1171,"SLIDE_IN","document page","Dark document page slides in from the left over 13 frames; shift (+100.8,+10.5) px at analysis size, ease-in-out (SUPPORTED, margin 0.030, scale 0.039).","camera_1159_1172",conf="MEDIUM",label="MEASURED",geo="net scale x1.013; image shift (+100.8,+10.5) px at 180-px analysis size")
A.E[-1]["easing"]="ease_in_out_smoothstep (SUPPORTED, margin 0.030-0.039; y pan AMBIGUOUS)"; A.E[-1]["measure"]="camera_1159_1172.json"
A.event("S11",1239,1315,"HIGHLIGHT_SWEEP","yellow highlights on the document","Two yellow sweeps: 111 to 185 px over f1239-1259 and 235 to 408 px over f1276-1315.","color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S11",1287,1287,"OVERLAY_POP","red 'that cost $131,000'","Red hand-lettered 'that cost $131,000' appears under the highlight in one frame (+99 red px), 0.16 s before ASR 'that' (43.06 s).","SE041; color_red",conf="HIGH",label="MEASURED")
A.event("S12",1497,1497,"OVERLAY_POP","bubble 'Are you bloody JOKING?!?' and angry eyes","Bubble appears and the pot gets angry eyes in one frame (yellow area -1325 px).","SE044; color_yellow",conf="HIGH",label="MEASURED")
A.event("S13",1578,1578,"CHARACTER_RISE_IN","official","Grey-haired official appears at the left edge.","SE046; ev_02",conf="MEDIUM",amb="peek-in versus pop not resolved")
A.event("S13",1610,1610,"CAPTION_CHUNK_CHANGE","caption 'and President's personal piggy bank'","Caption changes in one frame.","SE047; ev_02",conf="HIGH")
A.event("S14",1631,1631,"POP_IN","piggy bank","Pink piggy bank appears at the desk in one frame.","SE049; ev_02",conf="HIGH")
A.event("S15",1670,1693,"CHARACTER_RISE_IN","official","Official rises from the bottom edge over ~24 frames.","SE052; ev_03",conf="HIGH")
A.event("S16",1744,1772,"SLIDE_IN","statute page","Statute page slides in from the right and settles with a shift of (-123.2,+43.2) px at analysis size over ~29 frames, ease-in-out (SUPPORTED, margin 0.031-0.034).","camera_1743_1773",conf="HIGH",label="MEASURED",geo="net scale x1.015; image shift (-123.2,+43.2) px at 180-px analysis size")
A.E[-1]["easing"]="pan ease_in_out_smoothstep (SUPPORTED); scale ease_out_cubic"; A.E[-1]["measure"]="camera_1743_1773.json"
A.event("S16",1783,1787,"TEXT_WRITE_ON","red 'may NOT be reviewed'","Red hand-lettered 'may NOT be reviewed' is written in over 5 frames (0 to 554 red px), ending 50 ms before ASR 'may' (59.62 s) and removed at the end of the clip.","SE056; color_red",conf="HIGH",label="MEASURED")
A.event("S16",1784,1857,"HIGHLIGHT_SWEEP","yellow highlights on the statute","Yellow area grows from 0 to 67 px over f1784-1795 and from 139 to 227 px over f1840-1857.","color_yellow",conf="MEDIUM",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.fill_small(172)
A.E=[e for e in A.E if not (e['op']=='UNRESOLVED_CHANGE' and ('CUT' in e['desc'] or 'BIG_POP' in e['desc']) and any(e['f0']-2<=s['f0']<=e['f1']+2 for s in A.S))]
A.write(headline=None)
