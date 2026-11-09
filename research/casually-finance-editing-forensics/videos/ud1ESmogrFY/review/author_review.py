import sys; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('ud1ESmogrFY',2603)
A.scenes([
(0,"Grey ghost-like figure with red eyes turns black: 'the single biggest threat'","headline; figure; caption","CH_SHADOW","The single biggest threat to America"),
(110,"US-map and papers crossed out, then a Strait map crossed out and a robot with an AI bubble pop in","headline; maps; papers; red X; robot; bubble; caption","SS_MAPS,PR_PAPER,OV_REDX,CH_ROBOT","It isn't the debt, the Strait of Hormuz or the AI bubble itself"),
(209,"Small figure under the headline; 'ENERGY' title and props pop around it","headline; figure; ENERGY title; props; caption","CH_FIG,TY_EMPHASIS,PR_BARREL","It's energy"),
(245,"Lone figure; the persistent headline is gone from this cut on: 'in the way you're probably thinking'","figure; caption","CH_FIG","Not energy in the way you're thinking"),
(308,"Two children with cards; black screens with two eye dots flicker in and out","children; black frames; caption","CH_FIG","It's not blackouts or your utility bill"),
(355,"Boy holding a paper beside an empty speech bubble that fills with a document","boy; bubble; document; caption","CH_FIG,OV_BUBBLE,PR_DOC","Your monthly utility bill"),
(411,"Green US-map character; a roulette table and a growing pile of chips pop in","map character; roulette table; chips; caption","CH_USMAP,PR_ROULETTE,PR_CHIPS","America has pushed all its chips to the centre of the table"),
(542,"Roulette wheel alone; a robot rises in at the left","wheel; robot; caption","PR_ROULETTE,CH_ROBOT","The bet is that AI arrives on schedule"),
(636,"Robot with a teal bubble of tech logos; the bubble pops with sparkles","robot; bubble; logos; sparkles; caption","CH_ROBOT,OV_BUBBLE,LOGO_BIGTECH","If something's gonna pop the AI bubble"),
(702,"'ENERGY' title with a lightning character","ENERGY title; lightning character; caption","TY_EMPHASIS,CH_LIGHTNING","It's energy"),
(723,"Lone figure: 'and here's the thing about all those bubble takes'","figure; caption","CH_FIG","The bubble takes"),
(790,"Three arguing figures with rows of question marks; a red X crosses them out","figures; question marks; red X; caption","CH_FIGS,OV_REDX","They argue about the wrong question"),
(883,"Orange room with a figure and 'is it gonna LAST? / BROKE' boards: linear pull-back reveals a laptop screen","room; boards; figure; laptop frame; caption","SS_VIDEO_ROOM,CH_FIG,PR_COMPUTER","Whether AI is here to stay, will revolutionise every industry"),
(1052,"Figure beside a dark chatbot window with a green logo: 'a chatbot that can't count the letters in strawberry'","figure; chat window; logo; caption","CH_FIG,SS_CHATBOT","A chatbot that can't count the letters in strawberry"),
(1124,"Laptop with the video room again: 'is maybe about to take your job'","laptop; video room; caption","PR_COMPUTER,SS_VIDEO_ROOM","Maybe about to take your job"),
(1177,"Figure and a woman's photo: 'but that was never the right question'","figure; photo; caption","CH_FIG,PHOTO_WOMAN","That was never the right question"),
(1229,"Green US-map character at the roulette table; a small robot pops in at the top right","map character; roulette; robot; caption","CH_USMAP,PR_ROULETTE,CH_ROBOT","The real bet isn't whether AI works"),
(1293,"Lightning character beside a machine with a 'Well uhh, this is taking a while' bubble","lightning character; machine; bubble; caption","CH_LIGHTNING,PR_SERVER,OV_BUBBLE","It's whether we can physically deliver it on time"),
(1394,"Empty stage with a tiny falling figure","tiny figure; caption","CH_TINY","Whether the AI future can arrive"),
(1444,"Futuristic-city picture 'Us very, very soon:' with money bags either side and a robot peeking in","picture; text; bags; robot; caption","PHOTO_CITY,PR_BAGS,CH_ROBOT","Fast enough to justify the insane prices we're paying"),
(1560,"Purple Thanos figure with a snap-ready glove, a bill and newspaper","Thanos; bill; newspaper; caption","CH_THANOS,PR_CASH","Money is disappearing into AI faster than Thanos can snap"),
(1709,"Conference photograph with a figure at the right","photo; figure; caption","PHOTO_CONF,CH_FIG","The fastest and largest build-out in history"),
(1790,"Dark article screenshot with a bill: headlines swap three times","article; bill; caption","SS_ARTICLE,PR_CASH","Yet nobody's making any money"),
(1858,"Lone figure: 'which is fine'","figure; caption","CH_FIG","Which is fine"),
(1883,"Close-up face: 'which is fine for now'","face; caption","CH_FIG","For now"),
(1905,"Investor figure with a falling red graph and a small robot","figure; red graph; robot; caption","CH_FIG,OV_REDLINE,CH_ROBOT","Investors will happily fund losses"),
(1968,"Man with a basket and a 'Oh but the MONEY we'll make!' bubble with hearts","man; basket; bubble; hearts; caption","CH_MAN,OV_BUBBLE","As long as they think a payoff is coming"),
(2038,"Blank stage with a typed 'B'; a man with a basket appears, then tech logos, a bank with money bags, a data-centre icon and red arrows","text; man; basket; logos; bank; bags; data-centre icon; arrows; caption","TY_TYPED,CH_MAN,LOGO_BIGTECH,PR_BANK,PR_BAGS,PR_SERVER,OV_REDARROW","But eventually the investors, companies and lenders need the payoff to show up"),
(2177,"Figure with a 'Can't wait for my money babe!' bubble","figure; bubble; caption","CH_FIG,OV_BUBBLE","Need that payoff to actually show up"),
(2211,"Giant 'OR IT'S OVER' text behind a face","text; face; caption","TY_EMPHASIS,CH_FIG","Show up, or it's over"),
(2251,"Money bag: 'eventually the capital has to come home with a return'","money bag; caption","PR_BAG","Capital has to come home with a return"),
(2348,"Tech-logo bubble pops with sparkles: 'that's how the AI bubble pops'","logos; sparkles; caption","LOGO_BIGTECH","That's how the AI bubble pops"),
(2399,"Robot with red eyes; it topples off the stage","robot; caption","CH_ROBOT","It's not when it fails"),
(2441,"Green US-map character beside a clock whose hands turn: 'but when it's late'","map character; clock; caption","CH_USMAP,PR_CLOCK","But when it's late"),
(2478,"Figure with a money bag: 'when the capital starts to get sick of waiting'; a bubble 'Pick this, I'm out' and the second figure spinning away","figures; bag; bubble; caption (end)","CH_FIG,PR_BAG,OV_BUBBLE","Capital gets sick of waiting and decides to go somewhere else")])
A.event("S03",219,244,"POP_IN","ENERGY title and props","'ENERGY' title and its props (derricks, bags, a machine) appear around the figure over ~26 frames while the headline stays.","SE015; ev_01",conf="MEDIUM",amb="props not individually timed")
A.event("S05",315,315,"HARD_CUT_REPLACE","black frame","Stage replaced by a black frame with two white eye dots for 4 frames (f315-318).","SE020; ev_01",conf="HIGH")
A.event("S05",319,319,"HARD_CUT_REPLACE","children return","The two children return in one frame (f319-321).","SE021; ev_01",conf="HIGH")
A.event("S05",322,322,"HARD_CUT_REPLACE","black frame","Black frame with eye dots returns and stays until the cut at f355 (33 frames).","SE021; ev_01",conf="HIGH")
A.event("S06",392,392,"POP_IN","document in the bubble","Document appears inside the speech bubble in one frame.","SE024; ev_01",conf="MEDIUM")
A.event("S07",424,424,"POP_IN","roulette table","Roulette table appears under the map character in one frame.","SE025; ev_01",conf="HIGH")
A.event("S07",453,475,"POP_IN","chip pile","Chip pile grows around the table over ~24 frames.","SE026; ev_01",conf="LOW",amb="step timing not tracked")
A.event("S08",584,612,"CHARACTER_RISE_IN","robot","Robot appears at the lower left (f584) and grows into view over ~28 frames.","SE030; ev_01",conf="MEDIUM")
A.event("S12",859,859,"OVERLAY_POP","red X","Red X appears across the three figures in one frame.","SE042; ev_01",conf="HIGH")
A.event("S13",883,976,"CAMERA_SCROLL_ZOOM","orange room","Linear pull-back to 0.79x with a downward image shift of about 48 px (analysis size) over 94 frames, linear on scale, pan_x and pan_y (SUPPORTED).","camera_883_976",conf="HIGH",label="MEASURED",geo="net scale x0.786; image shift (+0.8,+48.0) px at 180-px analysis size")
A.E[-1]["easing"]="linear (SUPPORTED, margins 0.025-0.041)"; A.E[-1]["measure"]="camera_883_976.json"
A.event("S13",992,1033,"CAMERA_SCROLL_ZOOM","room on a laptop","Second linear pull-back to 0.57x over 42 frames (scale and pan_x linear, SUPPORTED; pan_y ambiguous) reveals that the orange room is on a laptop screen; scale total over both moves is about 0.45x.","camera_992_1033",conf="HIGH",label="MEASURED",geo="net scale x0.572; image shift (+34.8,+4.8) px at 180-px analysis size")
A.E[-1]["easing"]="linear (SUPPORTED, margin 0.020 scale, 0.032 pan_x)"; A.E[-1]["measure"]="camera_992_1033.json"
A.event("S17",1291,1291,"POP_IN","small robot","Small robot appears at the top right in one frame.","SE061; ev_02",conf="HIGH")
A.event("S18",1351,1351,"OVERLAY_POP","bubble 'Well uhh, this is taking a while'","Speech bubble appears next to the machine in one frame.","SE061; ev_02",conf="MEDIUM")
A.event("S23",1809,1809,"POP_IN","article panel replaced","Dark article panel is swapped (Google-logo headline) in one frame; further swaps at f1820 and f1844.","SE076; ev_02",conf="MEDIUM")
A.event("S23",1820,1820,"POP_IN","article panel replaced","Article panel swapped in one frame.","SE077; ev_02",conf="MEDIUM")
A.event("S23",1844,1844,"POP_IN","article panel replaced","Article panel swapped in one frame.","SE080; ev_02",conf="MEDIUM")
A.event("S28",2140,2140,"POP_IN","data-centre icon","Data-centre icon appears between the logos and the bank in one frame; red arrows follow at f2142.","SE094; ev_03",conf="HIGH")
A.event("S30",2213,2213,"OVERLAY_POP","'OR IT'S OVER' text","Giant hand-lettered text appears behind the face in one frame.","SE096; ev_03",conf="HIGH")
A.event("S31",2304,2332,"SCALE_TWEEN","coin with X","Orange coin with a white X grows/settles at the right of the money bags over ~29 frames.","SE069; ev_03",conf="LOW",amb="growth inferred from the stage-change series and overview")
A.event("S32",2349,2382,"OVERLAY_CLIP_LOOP","sparkle particles around the logo bubble","Small particles move around the tech-logo bubble every 1-3 frames over ~34 frames and a larger change lands at f2382 (2,700 stage px); whether this is a pre-rendered particle clip or hand keyframes is not resolved.","SE070; px series",conf="LOW",label="PLAUSIBLE_HYPOTHESIS",amb="mechanism not measured")
A.event("S33",2418,2425,"ROTATION","robot","Robot tilts and falls off the lower left over ~8 frames.","SE103; ev_03",conf="MEDIUM",amb="rotation angle not measured")
A.event("S34",2443,2478,"ROTATION","clock hands","Clock hands turn from about 6 o'clock to about 3 o'clock over ~35 frames while the narration says 'but when it's late'.","SE104-106; ev_03",conf="LOW",amb="hand angles read from sheet frames, not tracked")
A.event("S35",2573,2573,"OVERLAY_POP","bubble 'Pick this, I'm out'","Speech bubble appears in one frame.","SE112; ev_03",conf="HIGH")
A.event("S35",2577,2586,"ROTATION","second figure","Second figure spins away toward the upper left over ~10 frames and leaves the frame.","SE112; ev_03",conf="MEDIUM")
A.fill_small(172)
A.write(headline="it's boring, but it's what bursts the bubble")
