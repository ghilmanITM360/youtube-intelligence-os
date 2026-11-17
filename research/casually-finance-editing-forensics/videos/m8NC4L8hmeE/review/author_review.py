import sys, json; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('m8NC4L8hmeE',1502)
A.scenes([
(0,"Phone showing a LinkedIn post by 'Mr. Finance' with a bubble 'Yo everyone' that grows a second line and an '@YouTube' tag: 'it's like your old boss posting about you on LinkedIn'","phone; post; bubble; caption","PR_PHONE,SS_LINKEDIN_POST,OV_BUBBLE","A LinkedIn post that tags the employer"),
(85,"Host close-up holding a phone: 'tagging your current employer'","host (close-up); phone; caption","CH_HOST,PR_PHONE","Tagging your current employer"),
(108,"Grey-haired official with 'wtf man' and 'no bro code' captions; red caption 'And Bessent didn't take it well' is typed","official; red typed caption; captions","CH_OFFICIAL,TY_RED","And Besant didn't take it well"),
(147,"Two figures side by side; a news-headline card slides in from the top: 'Druckenmiller and Besant aren't just two guys who know each other. They are mentor and protege'","two figures; news card; caption","CH_OFFICIAL,CH_FIG,SS_NEWS_CARD","Mentor and protege"),
(272,"Photo of Stanley Druckenmiller with a red arrow label; the photo shrinks to the top, a LinkedIn profile card slides in and enlarges, a host with sunglasses rises","photo; label; profile card; host","PHOTO_PERSON,OV_REDARROW,SS_LINKEDIN_PROFILE,CH_HOST","A billionaire hedge fund manager"),
(407,"Red 'The lore' title with a briefcase figure and text: 'Scott Bessent got his start in finance working for Stanley Druckenmiller'","title; figure; text","TY_RED,CH_OFFICIAL","The lore"),
(489,"Dark text box with a yellow-highlighted line and the host pointing: 'He hired Scott Bessent at Soros in 1991'","text box; host; caption","SS_YAHOO_TEXT,OV_HIGHLIGHT,CH_HOST","He hired Besant at Soros in 1991"),
(560,"Two figures with a bubble 'Who tf are you lol': 'So this isn't a critic the Treasury Secretary can wave off'","two figures; bubble; caption","CH_OFFICIAL,CH_FIG,OV_BUBBLE","Not a critic he can wave off"),
(634,"Big host in the foreground and a small official; a Wall Street Journal page appears, a bubble 'I thought you better than this', red 'wrong'","host; official; WSJ page; bubble; red word","CH_OFFICIAL,SS_WSJ_PAGE,OV_BUBBLE,TY_RED","This is the man he learned the job from"),
(752,"Host with a microphone: 'He answered'","host; microphone; caption","CH_HOST,PR_MIC","He answered"),
(805,"Host with a microphone, then a G20 poster and a 'Greetings from Asheville' postcard: 'a week later, on television, from a G20 meeting'","host; G20 poster; postcard; caption","CH_HOST,SS_G20_POSTER,PHOTO_POSTCARD","A week later, on television"),
(853,"Speech bubble with a quote 'Stan's a great investor. He changes his mind a lot, and he doesn't like losing money' that scrolls with a yellow highlight growing; official below","bubble; quote text (pan); highlight; official","OV_BUBBLE,SS_CNBC_QUOTE,OV_HIGHLIGHT,CH_OFFICIAL","Stan changes his mind a lot and doesn't like losing money"),
(1042,"'NICKNAME ALERT' heading that flips style over a video clip of a dog with a glowing cone","heading; video clip","TY_RED,PHOTO_CLIP","Nickname alert"),
(1138,"Two grey-haired figures, one laughing, 'XDDD'","two figures; caption","CH_OFFICIAL","He called him by his nickname"),
(1162,"Text bubble from a Druckenmiller article with a yellow highlight; official below: 'the market price is information and you're supposed to listen to it'","bubble text page; highlight; official; caption; red word","SS_ARTICLE_BUBBLE,OV_HIGHLIGHT,CH_OFFICIAL,TY_RED","The market price is information"),
(1287,"Quote bubble with a re-drawn yellow highlight; official below: 'the price is an opinion and policy doesn't take orders from opinions' (red 'opinion')","bubble quote; highlight; official; caption; red word","SS_CNBC_QUOTE2,OV_HIGHLIGHT,CH_OFFICIAL,TY_RED","The price is an opinion"),
(1402,"Official with sunglasses and crossed arms: 'If Besant isn't going to listen to the market' and a tiny 'I do what I want boo'","official; captions","CH_OFFICIAL","If he doesn't listen to the market"),
(1459,"'SUPER DUPER PLAN! CLASSIFIED' document with a magnifying glass that moves toward it; worried figure: 'then what exactly is the plan?'","document; magnifier; figure; caption","PR_DOC,PR_MAGNIFIER,CH_FIG","What exactly is the plan?")])
A.event("S01",25,25,"CAPTION_CHUNK_CHANGE","post bubble text","Bubble text grows a second line ('CF sucks lolol') in one frame.","SE001; ev_01",conf="MEDIUM")
A.event("S01",61,61,"CAPTION_CHUNK_CHANGE","post bubble text","A third line ('@YouTube') is added to the post in one frame.","SE002; ev_01",conf="MEDIUM")
A.event("S03",108,141,"TEXT_WRITE_ON","red caption 'And Bessent didn't take it well'","Red caption is typed in steps (red area 85 px at f108, 286 at f112, 405 at f121, 631 by f141), removed at the cut f147.","SE005; color_red",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_red.json"
A.event("S04",213,222,"SLIDE_IN","news-headline card","News-headline card slides in from the top over ~10 frames.","SE015; ev_01",conf="MEDIUM")
A.event("S05",272,309,"SCALE_TWEEN","Druckenmiller photo","Photo and its red arrow label shrink and move to the top over ~38 frames (label red area 90 px at f272).","SE018; ev_01",conf="MEDIUM",amb="scale and easing not measured")
A.event("S05",292,309,"SLIDE_IN","LinkedIn profile card","Profile card slides in from the lower right over ~17 frames.","SE018; ev_01",conf="MEDIUM")
A.event("S05",332,332,"CHARACTER_RISE_IN","host with sunglasses","Host with sunglasses rises from the lower right (visible from f332).","SE019; ev_01",conf="MEDIUM")
A.event("S05",335,349,"CAMERA_SCROLL_ZOOM","LinkedIn profile card","Profile card enlarges and moves up over ~14 frames.","SE019; ev_01",conf="MEDIUM",label="DIRECTLY_OBSERVED",amb="geometry not measured")
A.event("S08",591,591,"OVERLAY_POP","bubble 'Who tf are you lol'","Bubble appears above the two figures in one frame.","SE032; ev_02",conf="HIGH")
A.event("S09",685,693,"SLIDE_IN","Wall Street Journal page","WSJ page appears from the right edge over ~9 frames.","SE037; ev_01",conf="MEDIUM")
A.event("S09",714,714,"OVERLAY_POP","bubble 'I thought you better than this'","Bubble appears above the small official in one frame.","SE040; ev_01",conf="HIGH")
A.event("S09",736,736,"OVERLAY_POP","red 'wrong'","Red 'wrong' appears under the caption in one frame (0 to 282 red px) and is removed at the cut f752.","SE; color_red",conf="HIGH",label="MEASURED")
A.event("S11",823,833,"SLIDE_IN","G20 poster and postcard","G20 poster is on screen by f822 and the 'Greetings from Asheville' postcard enters at the lower right between f825 and f832 (red area 507 to 908 px).","SE049; color_red",conf="MEDIUM",label="MEASURED",amb="poster onset not isolated")
A.event("S12",864,1034,"HIGHLIGHT_SWEEP","yellow highlight on the quote","Yellow area grows from 0 to 3136 px over ~171 frames while the quote text scrolls left (f864-922: 0 to 1260 px; f924-1004: to 2395 px; f1009-1034: to 3136 px).","color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S12",896,1004,"CAMERA_SCROLL_ZOOM","quote text in the bubble","Quote text pans left by about 185 px (analysis size) over ~111 frames with a 1.03x scale; x pan linear (SUPPORTED, margin 0.053), scale ease-in-out (SUPPORTED, margin 0.048).","camera_895_1006",conf="HIGH",label="MEASURED",geo="net scale x1.028; image shift (-185.1,-1.3) px at 180-px analysis size")
A.E[-1]["easing"]="pan x linear (SUPPORTED, margin 0.053); scale ease_in_out_smoothstep (SUPPORTED, margin 0.048)"; A.E[-1]["measure"]="camera_895_1006.json"
A.event("S13",1042,1086,"VIDEO_CLIP_INSERT","dog clip","Clip region updates on f1045, 1047, 1050, 1052, 1054, 1057, 1059, 1062, 1064, 1066, 1069, 1071, 1074, 1076, 1078, 1081, 1083 and 1085 (alternating 2- and 3-frame gaps = ~10 updates per second on a 24 fps timeline) and then holds to the cut f1138; the glow flashes red-orange at f1045, f1054-1060 and f1076-1085.","clip-region mean abs diff; color_red",conf="MEDIUM",label="MEASURED",mclass="INDET",amb="source clip not identified")
A.event("S13",1048,1084,"OPACITY_FADE","'NICKNAME ALERT' heading","Heading flips between thin red and bold dark-red lettering about every 12 frames (thin at f1042-1048, bold f1054-1060, thin f1066-1072, bold f1078-1084).","SE054; ev_02",conf="MEDIUM",label="DIRECTLY_OBSERVED",mclass="INDET",amb="style flip, not a fade; period read from sampled frames")
A.event("S14",1138,1138,"POP_IN","two laughing figures","Two figures replace the clip scene in one frame (stage 3.3 % of frame).","SE055; ev_02",conf="HIGH")
A.event("S15",1173,1244,"HIGHLIGHT_SWEEP","yellow highlight on the bubble text","Yellow area grows from 0 to 423 px over f1173-1201 and to 770 px by f1244 (72 frames).","color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S16",1315,1398,"HIGHLIGHT_SWEEP","re-drawn yellow highlight","Yellow area is reset to 150 px at the start of the scene and grows to 714 px over f1315-1398 (84 frames).","color_yellow",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="color_yellow.json"
A.event("S16",1340,1344,"OVERLAY_POP","red 'opinion'","Red word 'opinion' appears in the caption within five frames.","SE062; ev_02",conf="MEDIUM")
A.event("S18",1459,1489,"POINTER_TRANSLATE","magnifying glass","Magnifying glass moves from the left toward the document over ~31 frames (path and easing not measured).","SE073; ev_02",conf="MEDIUM",amb="path and easing not measured")
A.fill_small(172)
A.E=[e for e in A.E if not (e['op']=='UNRESOLVED_CHANGE' and ('HARD' in e['desc'] or 'CUT' in e['desc'] or 'BIG_POP' in e['desc']) and any(e['f0']-2<=s['f0']<=e['f1']+2 for s in A.S))]
A.write(headline=None)
