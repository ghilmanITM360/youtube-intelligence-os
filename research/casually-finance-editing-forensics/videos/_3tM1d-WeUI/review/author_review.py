import sys; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('_3tM1d-WeUI',2575)
A.scenes([
(0,"Data-centre icon with a growing 'FEED ME, MY ELECTRICAL MOTHER' bubble and a red block","headline; data-centre icon; bubble; red block; caption","PR_SERVER,OV_BUBBLE","Data centres want power now, guaranteed, forever"),
(178,"PJM logo, then a green US-map pops in and '67M' appears","headline; logo; map; red text; caption","LOGO_PJM,CH_USMAP,TY_RED","PJM is the largest US grid operator, serving 67 million people"),
(305,"PJM logo, '67M' and a purple PJM-territory map","headline; logo; red text; territory map; caption","LOGO_PJM,TY_RED,SS_PJM_MAP","13 states from Chicago to Washington"),
(394,"Five stick figures, one highlighted: 'roughly 1 in 5 Americans'","headline; figures; caption","CH_PEOPLE","One in five Americans"),
(454,"House and building icons pop in one after another, then the PJM logo","headline; house/building icons; logo; caption","PR_HOUSE,PR_BLDG,LOGO_PJM","Your lights depend on PJM's decisions"),
(581,"PJM logo with a microphone: bubbles 'I'm bout to drop a BANGER!', 'READY?!', then '*crickets*' text and 'So uh...'","headline; logo; microphone; bubbles; crickets text; caption","LOGO_PJM,PR_MIC,OV_BUBBLE","PJM's biggest decision happens at an event nobody watches"),
(846,"PJM logo with a microphone, power-plant and wind-turbine icons and 'sure' text","headline; logo; microphone; plant icons; caption","LOGO_PJM,PR_MIC,PR_PLANT,PR_WIND","Once a year PJM pays plants to promise electricity on the worst days"),
(922,"Lone figure with a huge 'TRUST ME BRO' text that shrinks to fit","headline; figure; text; caption","CH_FIG,TY_EMPHASIS","It's a billion-dollar pinky promise"),
(1046,"Photo of a snowy tree: 'a January freeze'","headline; photo; caption","PHOTO_SNOW","January freeze"),
(1084,"Photo of a heat-wave sun: 'or an August heat wave'","headline; photo; caption","PHOTO_HEAT","August heat wave"),
(1127,"Lone figure with small coins: 'that insurance was dirt cheap'","headline; figure; coins; caption","CH_FIG,PR_CASH","Insurance was dirt cheap"),
(1214,"Energy-consumption bar chart with a man leaning on it: 'because American electricity demand flatlined for 20 years'","headline; bar chart; man; red arrow; caption","SS_ENERGY_CHART,CH_MAN,OV_REDARROW","Demand flatlined for 20 years"),
(1317,"PJM logo and microphone with '*crickets*' texts; then the stage empties and a data-centre icon slides in from the right: 'then the data centers arrived'","headline; logo; microphone; crickets text; data-centre icon; caption","LOGO_PJM,PR_MIC,PR_SERVER","The capacity auction is boring; then the data centres arrived"),
(1504,"Sad lone figure: 'not one at a time'","headline; figure; caption","CH_LONE","Not one at a time"),
(1546,"Twelve data-centre icons scattered: 'by the dozen'","headline; icons; caption","PR_SERVER","By the dozen"),
(1576,"Data-centre icon with blue lightning bolts, then small-city icons and the bar chart","headline; icon; bolts; city icons; caption","PR_SERVER,FX_BOLTS,PR_BLDG","Buildings that swallow as much electricity as a small city"),
(1680,"US energy-consumption bar chart with a red box on the recent bars","headline; bar chart; red box; caption","SS_ENERGY_CHART,OV_REDBOX","A system designed for a world where demand barely grew"),
(1793,"PJM price line chart: a worried man pops in and out, red 'Max $325' with an ellipse","headline; line chart; man; red text; red ellipse; caption","SS_PJM_PRICE_CHART,CH_MAN,TY_RED,OV_REDCIRCLE","PJM paid the maximum price allowed under federal law"),
(2022,"Second PJM chart with a moving red arrow","headline; line chart; red arrow; caption","SS_PJM_SUPPLY_CHART,OV_REDARROW","But there still wasn't enough power supply to go around"),
(2105,"Sad lone figure: 'and that's the physical reality of the grid'","headline; figure; caption","CH_LONE","The physical reality of the grid"),
(2170,"Money bags with a gas-turbine photo, then a bar chart and a permitting text page swap in at the right","headline; bags; photo/chart/text panel; caption","PR_BAGS,PHOTO_TURBINE,SS_TRANSFORMER_CHART,SS_PERMIT_TEXT","All that money can't summon a turbine, a transformer or a transmission line"),
(2326,"Siemens Energy, GE Vernova and Mitsubishi Power logos; bubble 'Booked and busy, sorry!' and calendar icons pop","headline; logos; bubble; calendars; caption","LOGO_SIEMENS,LOGO_GEVERNOVA,LOGO_MITSUBISHI,OV_BUBBLE,PR_CALENDAR","Manufacturers are booked years out"),
(2432,"PJM chart with a red arrow; a man pops in at the end","headline; chart; red arrow; man; caption (end)","SS_PJM_SUPPLY_CHART,OV_REDARROW,CH_MAN","The grid failed to buy what it needed and paid full price")])
A.event("S02",196,196,"POP_IN","green US map","US map appears at the right in one frame.","SE002; ev_01",conf="HIGH")
A.event("S02",246,246,"OVERLAY_POP","red '67M'","Red '67M' appears at the left in one frame.","SE004; overview",conf="MEDIUM")
A.event("S05",470,470,"POP_IN","house and building icons","Second house/building pair appears in one frame; further pairs at f484 and between f543 and f558.","SE009-011; ev_01",conf="MEDIUM")
A.event("S05",559,561,"POP_IN","PJM logo","PJM logo appears above the icons by f561 (absent at f558).","SE011; ev_01",conf="MEDIUM")
A.event("S06",601,601,"OVERLAY_POP","bubble 'I'm bout to drop a BANGER!'","Speech bubble appears in one frame.","SE013; ev_01",conf="HIGH")
A.event("S06",638,638,"OVERLAY_POP","bubble 'READY?!'","Bubble text swaps to 'READY?!' in one frame.","SE014; overview",conf="MEDIUM")
A.event("S06",678,678,"OVERLAY_POP","'*crickets*' texts","Two small '*crickets*' text items appear and the bubble is removed in one frame.","SE015; ev_01",conf="HIGH")
A.event("S06",715,715,"CAPTION_CHUNK_CHANGE","'*crickets*' texts","Cricket texts change position/wording in one frame.","SE016; ev_01",conf="LOW")
A.event("S06",742,742,"OVERLAY_POP","bubble 'So uh...'","New speech bubble appears in one frame.","SE017; overview",conf="MEDIUM")
A.event("S08",954,1000,"SCALE_TWEEN","lone figure","Figure shrinks to about half its width (0.133 to 0.067 of the frame width) over ~30 frames before the 'TRUST ME BRO' text takes the stage; ink-extent fit ease-in quad (SUPPORTED, margin 0.149; ink counts are mixed with the incoming text after f988).","extent_954_1000",conf="MEDIUM",label="MEASURED")
A.E[-1]["easing"]="ease_in_quad (SUPPORTED, margin 0.149; indicative)"; A.E[-1]["measure"]="extent_954_1000.json"
A.event("S08",982,996,"SCALE_TWEEN","'TRUST ME BRO' text","Text starts oversized and cropped by the frame edges (f982) and shrinks to fit the width by f996.","SE023; ev_01",conf="MEDIUM",amb="scale path not tracked")
A.event("S09",1046,1084,"CAMERA_SCROLL_ZOOM","snowy-tree photo","Photo shifts by about (+27,+52) px at analysis size with ~1.01x scale over 39 frames, ease-in quad (SUPPORTED, margin 0.132); tracked shift may include image-content change.","camera_1046_1084",conf="LOW",label="MEASURED",geo="net scale x1.01; image shift (+26.9,+52.0) px at 180-px analysis size")
A.E[-1]["easing"]="ease_in_quad (SUPPORTED, margin 0.132; tentative)"; A.E[-1]["measure"]="camera_1046_1084.json"
A.event("S12",1214,1286,"POINTER_TRANSLATE","red arrow above the bars","Red arrow glides right from x = 0.555 to 0.690 of the frame width over 73 frames, linear (SUPPORTED, margin 0.047), moving from the 2000s bars to the last bar while the narration says 'flatlined'; the man at the lower left stays still.","blob_1214_1286",conf="HIGH",label="MEASURED")
A.E[-1]["easing"]="linear (SUPPORTED, margin 0.047)"; A.E[-1]["measure"]="blob_1214_1286.json"
A.event("S16",1580,1665,"OVERLAY_CLIP_LOOP","blue lightning bolts","Blue bolts flicker and change position beside the data-centre icon every 1-3 frames over ~85 frames; whether this is a pre-rendered loop or hand keyframes is not resolved.","SE036; ev_01",conf="LOW",label="PLAUSIBLE_HYPOTHESIS",amb="mechanism and loop length not measured")
A.event("S16",1666,1679,"POP_IN","small-city icons","Small green building icons appear at the top right in steps between f1666 and f1676.","SE036; ev_01",conf="MEDIUM")
A.event("S23",2433,2478,"POINTER_TRANSLATE","red arrow","Red arrow moves toward the chart's right end over ~46 frames (x from 0.733 to 0.796 and y from 0.467 to 0.501 of the frame size), linear on both axes.","blob_2432_2478",conf="MEDIUM",label="MEASURED")
A.E[-1]["easing"]="linear (SUPPORTED, margin 0.029 x, 0.027 y)"; A.E[-1]["measure"]="blob_2432_2478.json"
A.event("S13",1458,1475,"SLIDE_IN","data-centre icon","Icon enters from the right edge over 18 frames.","SE033; ev_01",conf="MEDIUM")
A.event("S18",1840,1840,"POP_IN","worried man","Man appears at the lower right of the chart in one frame; he is removed at f1937.","SE038; ev_02",conf="HIGH")
A.event("S18",1947,1947,"OVERLAY_POP","red 'Max $325' and ellipse","Red label and ellipse appear at the chart's peak (first seen by f1950).","SE040; overview",conf="MEDIUM")
A.event("S19",2022,2065,"POINTER_TRANSLATE","red arrow","Red arrow moves toward the right end of the line over ~44 frames; ease type ambiguous.","blob_2021_2066",conf="LOW",label="MEASURED")
A.E[-1]["easing"]="AMBIGUOUS (ease_out_quad, margin 0.004-0.006)"; A.E[-1]["measure"]="blob_2021_2066.json"
A.event("S21",2220,2220,"POP_IN","gas-turbine photo","Photo appears beside the money bags in one frame.","SE044; ev_02",conf="HIGH")
A.event("S22",2371,2371,"OVERLAY_POP","bubble 'Booked and busy, sorry!'","Speech bubble appears next to the logos in one frame.","SE048; ev_02",conf="HIGH")
A.event("S22",2377,2386,"POP_IN","calendar icons","Six calendar icons pop in around the logos between f2377 and f2386.","SE049; ev_02",conf="MEDIUM")
A.event("S23",2507,2507,"POP_IN","man","Man appears at the lower right of the chart in one frame.","SE051; ev_02",conf="HIGH")
A.write(headline="ai now faces a severe power shortage")
