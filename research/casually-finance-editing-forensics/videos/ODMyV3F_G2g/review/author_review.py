import sys, json; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('ODMyV3F_G2g',1953)
A.scenes([
(0,"Detective-hat host with a magnifier at the lower left; a US-map character, a Japan-map character with a yen note and a black photo pop in or slide in","host; map characters; yen note; photo","CH_HOST,CH_USMAP,CH_JAPAN,PR_CASH,PR_PHOTO","The only evidence is a photograph"),
(174,"Hand-lettered 'To do:' note filling the frame","note; text","PR_NOTE","A handwritten to-do list"),
(202,"Small to-do note at the lower right; a portrait of the Treasury Secretary with a flag and seal pops in, a red 'Scott Bessent' label and arrow appear and the portrait enlarges","note; portrait; label; seal","PR_NOTE,PHOTO_PORTRAIT,OV_REDARROW,LOGO_TREASURY","In front of the Secretary of the Treasury"),
(389,"Photo of the desk with a name plate and the handwritten note; the host points; the photo enlarges 1.85x","photo (zoom); host","PHOTO_DESK,CH_HOST","One line legible across the room"),
(495,"White frame; a Reuters article with the photo enters from the left; '11:33 July 31st' and a photographer with a long lens slide in","article; text; photographer","SS_REUTERS,CH_PHOTOGRAPHER","Taken at 11:33 on July 31st"),
(709,"News card enters from the top; host with chin on hand; red '1998' pops; the US-map character slides in from the right","news card; host; red text; map character","SS_NEWS_CARD,CH_HOST,TY_RED,CH_USMAP","First time since 1998"),
(901,"Desk photo at the top; a 'buy milk' notepad pops under it; red arrows and 'essentially the same'","photo; notepad; red arrows; text","PHOTO_DESK,PR_NOTE,OV_REDARROW","The receipt was a doodle on a notepad"),
(975,"Host alone, then DEBT papers pop above him one after another","host; DEBT papers","CH_HOST,PR_DEBTDOC","What makes this interesting"),
(1115,"Host with '30 years', DEBT papers and a bag; a dark news card 'Treasury yield tops 5.19%' enters from the top","host; DEBT papers; bag; news card","CH_HOST,PR_DEBTDOC,PR_BAG,SS_NEWS_CARD","Highest 30-year rate since 2007"),
(1217,"US-map and Japan-map characters side by side; the Japan character jumps onto the US character; green bond papers pop one by one; a globe character pops","map characters; bond papers; globe character","CH_USMAP,CH_JAPAN,PR_BOND,CH_EARTH","The country we're propping up holds the most American debt"),
(1359,"Host alone","host","CH_HOST","So the question becomes"),
(1400,"Small host at a laptop; a US-map character with a red mark pops at the top; a red question mark appears","host; laptop; map character; red question mark","CH_HOST,PR_LAPTOP,CH_USMAP,TY_RED","Why are we doing this? What are we buying?"),
(1491,"A person behind a newspaper rises from the bottom","person; newspaper","CH_FIG,PR_NEWSPAPER","The story that gets reported"),
(1540,"Red-brown arch shape","shape","PR_ARCH","The story underneath"),
(1572,"Red-brown arch with the word 'TRUTH'","shape; text","PR_ARCH,TY_TRUTH","Rarely the same one"),
(1612,"Host with an equals sign; a red slash crosses it","host; sign; red slash","CH_HOST,PR_EQUALS,OV_REDSLASH","The two stories are not the same"),
(1663,"Collage of map characters, cash, shield, bags and a globe character","characters; props","CH_USMAP,CH_JAPAN,CH_EARTH,PR_CASH,PR_BAGS,PR_SHIELD","Of everything in this story"),
(1704,"Host under a black box that grows, then fades into the desk photo; an official peeks in and a 'DON'T LOOK!' bubble pops","host; black box; photo; official; bubble","CH_HOST,PR_BLACKBOX,PHOTO_DESK,CH_OFFICIAL,OV_BUBBLE","The only thing that told you what was happening was a to-do list")])
A.event("S01",28,28,"POP_IN","US-map character","US-map character appears at the upper left in one frame.","SE001; ev_01",conf="HIGH")
A.event("S01",109,118,"POP_IN","Japan-map character and yen note","Japan-map character and a yen note appear beside the US-map character within ten frames.","SE004; ev_01",conf="MEDIUM",amb="exact frame within f109-118 not isolated")
A.event("S01",131,148,"PROP_DRIFT","black photo","Black photo slides in from the lower right to the host's right over 18 frames.","SE005; ev_01",conf="MEDIUM",amb="path and easing not measured")
A.event("S03",237,237,"POP_IN","portrait with flag","Portrait with a flag appears in one frame (red flag area 0 to 160 px).","SE008; color_red",conf="HIGH",label="MEASURED")
A.event("S03",259,259,"POP_IN","Treasury seal","Seal appears on the portrait in one frame.","SE009; ev_01",conf="HIGH")
A.event("S03",285,286,"OVERLAY_POP","red label and arrow","Red 'Scott Bessent' label and arrow appear within two frames (red area 171 to 277 px).","SE; color_red",conf="MEDIUM",label="MEASURED")
A.event("S03",309,347,"CAMERA_SCROLL_ZOOM","portrait","Portrait enlarges 1.29x and moves up by about 84 px (analysis size) over ~39 frames; pans linear (SUPPORTED, margin 0.021-0.030), scale linear AMBIGUOUS (margin 0.013).","camera_309_347",conf="MEDIUM",label="MEASURED",geo="net scale x1.286; image shift (-3.3,-84.4) px at 180-px analysis size")
A.E[-1]["easing"]="linear (pans SUPPORTED, scale AMBIGUOUS)"; A.E[-1]["measure"]="camera_309_347.json"
A.event("S04",389,430,"CAMERA_SCROLL_ZOOM","desk photo","Photo enlarges 1.85x with a shift of (-18.7,+125.6) px at analysis size over ~43 frames, linear on scale and both pans (SUPPORTED, margin 0.038-0.041).","camera_388_432",conf="HIGH",label="MEASURED",geo="net scale x1.854; image shift (-18.7,+125.6) px at 180-px analysis size")
A.E[-1]["easing"]="linear (SUPPORTED, margin 0.038-0.041)"; A.E[-1]["measure"]="camera_388_432.json"
A.event("S05",501,514,"SLIDE_IN","Reuters article","Article card enters from the left edge and grows to full width over ~14 frames.","SE014; ev_01",conf="MEDIUM",amb="scale and path not measured")
A.event("S05",617,637,"SLIDE_IN","photographer","Photographer with a long lens slides in from the right over ~21 frames.","SE016; ev_01",conf="HIGH")
A.event("S06",709,725,"SLIDE_IN","news card","News card enters from the top over ~17 frames.","SE017; ev_01",conf="MEDIUM")
A.event("S06",739,739,"POP_IN","host","Host with chin on hand appears in one frame.","SE018; ev_01",conf="HIGH")
A.event("S06",763,764,"OVERLAY_POP","red '1998'","Red '1998' appears in two frames (0 to 193 red px), 50 ms before ASR '1998' (25.48 s).","color_red",conf="HIGH",label="MEASURED")
A.event("S06",817,870,"SLIDE_IN","US-map character","US-map character slides in from the right edge over ~54 frames.","SE020; ev_02",conf="MEDIUM",amb="path and easing not measured")
A.event("S07",928,928,"POP_IN","'buy milk' notepad","Notepad appears under the photo in one frame, at ASR 'a doodle' (30.88 s).","SE022; ev_02",conf="HIGH")
A.event("S07",946,946,"OVERLAY_POP","red arrows and 'essentially the same'","Red arrows and the words 'essentially the same' appear in one frame (0 to 213 red px).","SE023; color_red",conf="HIGH",label="MEASURED")
A.event("S08",1045,1045,"POP_IN","DEBT paper","DEBT paper appears above the host in one frame.","SE026; ev_02",conf="HIGH")
A.event("S08",1051,1051,"POP_IN","second DEBT paper","Second DEBT paper appears in one frame.","SE027; ev_02",conf="HIGH")
A.event("S09",1115,1143,"SLIDE_IN","news card","Dark news card enters from the top and shrinks toward the upper right over ~29 frames.","SE030; ev_02",conf="MEDIUM",amb="path and scale not measured")
A.event("S10",1247,1247,"POP_IN","Japan-map character on the US-map character","Japan-map character is drawn onto the US-map character in one frame.","SE032; ev_02",conf="HIGH")
A.event("S10",1284,1284,"POP_IN","first bond paper","First green bond paper appears above the characters in one frame.","SE033; ev_02",conf="HIGH")
A.event("S10",1291,1291,"POP_IN","second bond paper","Second bond paper appears in one frame.","SE034; ev_02",conf="HIGH")
A.event("S10",1297,1297,"POP_IN","third bond paper","Third bond paper appears in one frame.","SE035; ev_02",conf="HIGH")
A.event("S10",1340,1340,"POP_IN","globe character","Globe character appears above the stack in one frame.","SE036; ev_02",conf="HIGH")
A.event("S12",1440,1440,"POP_IN","US-map character","US-map character appears at the top in one frame.","SE039; ev_02",conf="HIGH")
A.event("S12",1462,1462,"OVERLAY_POP","red question mark","Red question mark appears beside the host in one frame (0 to 172 red px), 0.15 s before ASR 'buying' (48.88 s).","color_red",conf="HIGH",label="MEASURED")
A.event("S13",1491,1513,"CHARACTER_RISE_IN","newspaper reader","Person behind a newspaper rises from the bottom edge over ~23 frames.","SE041; ev_02",conf="HIGH")
A.event("S16",1636,1636,"OVERLAY_POP","red slash","Red slash appears across the equals sign in one frame (0 to 356 red px).","color_red",conf="HIGH",label="MEASURED")
A.event("S18",1704,1848,"SCALE_TWEEN","black box","Black box grows from a small rectangle to a frame-wide block over 145 frames (ink area linear, SUPPORTED, margin 0.049).","extent_1704_1848",conf="HIGH",label="MEASURED")
A.E[-1]["easing"]="linear (SUPPORTED, margin 0.049; ink area)"; A.E[-1]["measure"]="extent_1704_1848.json"
A.event("S18",1768,1788,"POSE_SWAP","host face","Host's face changes from neutral to a smile between f1768 and f1788.","SE047; ev_03",conf="MEDIUM",amb="exact frame not isolated")
A.event("S18",1831,1848,"POSE_SWAP","host face","Host's smile widens between f1831 and f1848.","SE047; ev_03",conf="MEDIUM",amb="exact frame not isolated")
A.event("S18",1849,1873,"OPACITY_FADE","black box into desk photo","Black box fades into the desk photo: mean gray of the upper stage rises from 137 to 193 at a constant ~2.4 levels per frame from f1849 to f1873 and then stays at 193.","gray mean series f1846-1900",conf="HIGH",label="MEASURED")
A.E[-1]["easing"]="linear (constant gray-level rate)"
A.event("S18",1900,1906,"CHARACTER_RISE_IN","official","Grey-haired official peeks in from the right edge over 7 frames.","SE048; ev_03",conf="HIGH")
A.event("S18",1907,1907,"OVERLAY_POP","bubble 'DON'T LOOK!'","Bubble appears beside the official in one frame, at ASR 'was ever supposed' (63.58 s).","SE048; ev_03",conf="HIGH")
A.fill_small(172)
A.E=[e for e in A.E if not (e['op']=='UNRESOLVED_CHANGE' and ('CUT' in e['desc'] or 'BIG_POP' in e['desc']) and any(e['f0']-2<=s['f0']<=e['f1']+2 for s in A.S))]
A.write(headline=None)
