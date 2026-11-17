import sys; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('ji2qFfcgSB4',2377)
A.scenes([
(0,"Large US-map character with eyes fills the stage","headline; US map character; caption","CH_USMAP","Opens on the superpower: 'it's not just the United (States)'"),
(51,"Small UK-map character with a teacup; speech bubble 'STFU MY TEETH ARE FINE!'","headline; UK map character; teacup; bubble; caption","CH_UKMAP,PR_TEACUP,OV_BUBBLE","UK joke: the 'veneers-wearing lads across the pond'"),
(146,"Netherlands flag beside a spreadsheet table; bags pop; table zooms; host pops; red box and '2 TRILLION!'; euro note","headline; flag; table screenshot (zoom); money bags; host; red box + number; note; caption","PR_FLAG_NL,SS_PENSION_TABLE,PR_BAGS,CH_HOST,OV_REDBOX,TY_2TRILLION,PR_CASH","Netherlands: largest EU pension system, ~2 trillion euros overhaul"),
(479,"Pension-system text page with yellow highlight sweeping the key lines","headline; text page; highlight; caption","SS_PENSION_PAGE,OV_HIGHLIGHT","Evidence: first wave completed January 1st, 30 funds, 10 million members"),
(661,"'Defined benefit' building and document; then 'Defined contribution' figure and paper pop","headline; labels; building; document; figure; paper; caption","PR_BLDG,PR_DOC,CH_FIG,OV_LABELS","Old collective DB model vs new individual DC model"),
(829,"Netherlands flag with green map-shaped character; document, bag, bags and notes pop","headline; flag; green character; document; bags; notes; caption","PR_FLAG_NL,CH_NLMAP,PR_DOC,PR_BAG,PR_BAGS,PR_NOTES","Old rules: every promise matched with an asset"),
(965,"Bar chart of bond holders; green characters, host and money bag; red X on bag","headline; chart; green characters x2; host; bag; X circle; caption","SS_HOLDERS_CHART,CH_NLMAP,CH_HOST,PR_BAG,OV_XCIRCLE","They bought long German/French bonds and swaps regardless of yield"),
(1162,"Woman figure and green character; bubble 'Buy those bonds!'","headline; figure; green character; bubble; caption","CH_FIG,CH_NLMAP,OV_BUBBLE","A regulator told them to buy"),
(1242,"Text page with growing yellow highlight; green character; bubble","headline; text page; highlight; green characters; bubble; caption","SS_BOND_MARKET_PAGE,OV_HIGHLIGHT,CH_NLMAP,OV_BUBBLE","They came to own ~10 % of the entire German sovereign bond market"),
(1411,"Host at a blackboard: 'New rules =' then 'They DON'T have to'","headline; host; blackboard; caption","CH_HOST,PR_BLACKBOARD","Under the new rules they don't have to be a buyer"),
(1503,"Dutch central bank article with euro notes popping and a yellow highlight","headline; article page; euro notes; highlight; caption","SS_DNB_PAGE,PR_CASH,OV_HIGHLIGHT","DNB estimate: 100-150 billion euros of long-dated bonds and swaps could be unwound"),
(1740,"PIMCO table with host; red circle on the 115 figure; bills and a '30 year' tag","headline; table screenshot; host; red circle; bills; tag; caption","SS_PIMCO_TABLE,CH_HOST,OV_REDCIRCLE,PR_CASH,PR_TAG","PIMCO base case: 115 billion euros of 30-year demand vanishes"),
(2021,"Full-bleed teal wave illustration; small worried figure appears","wave illustration; figure; caption","PR_WAVE,CH_FIG","The biggest wave hasn't even hit yet"),
(2091,"ABP page; ABP logo; two documents; stack of bills; red '500B'; host with cash","headline; text page; logo; documents; bills; red number; host; caption","SS_ABP_PAGE,LOGO_ABP,PR_DOC,PR_CASH,TY_500B,CH_HOST","ABP, a third of the Dutch system, more than 500 billion euros, converts next January")])
A.event("S02",105,105,"OVERLAY_POP","bubble 'STFU MY TEETH ARE FINE!'","Speech bubble appears in one frame beside the UK character.","SE003",conf="HIGH")
A.event("S03",171,171,"POP_IN","money bag 1","First money bag appears in one frame under the flag.","SE005",conf="HIGH")
A.event("S03",180,180,"POP_IN","money bag 2","Second bag appears in one frame.","SE006",conf="HIGH")
A.event("S03",187,192,"POP_IN","money bag 3","Third bag appears at f187; minor shifts follow to f192 (settling or a second bag; unresolved).","SE007",conf="LOW",amb="settle vs second object")
A.event("S03",271,301,"CAMERA_SCROLL_ZOOM","flag and spreadsheet table","Group push-in: flag slides off the left edge while the table enlarges to ~2.07x over 31 frames with ease-out (decelerating); host then pops at f302.","SE009; camera_270_302",conf="HIGH",geo="net scale x2.07 about stage centre; tracked image-centre shift (+4,-43) px at 180-px analysis size")
A.E[-1]["easing"]="ease_out_quad (SUPPORTED, margin 0.05; scale, pan_x, pan_y all agree)"; A.E[-1]["measure"]="camera_270_302.json"
A.event("S03",302,302,"POP_IN","host figure","Host (stick figure with hair) appears in one frame at the left of the table (first seen f302; could be f301).","SE009 end; chk f300/f302",conf="MEDIUM")
A.event("S03",391,391,"OVERLAY_POP","red box and '2 TRILLION!'","Red box line around a table row plus the red number '2 TRILLION!' appear together; the host's face changes to an open mouth in the same frame.","SE011",conf="HIGH")
A.event("S03",410,410,"POP_IN","euro note","Green euro note appears beside the red number.","SE012",conf="HIGH")
A.event("S04",479,482,"OPACITY_FADE","page background tint","Page replaces the table at f479; background shows a cream tint f480-482 and is white by f483 (mechanism unresolved; possibly a short flash/blend).","SE013; chk f479-484",conf="LOW",mclass="INDET",amb="tint settle vs flash vs 4-frame blend")
A.event("S04",496,631,"HIGHLIGHT_SWEEP","yellow highlight on page text","Yellow highlight grows along the first lines in steps (f496, f515, f529) and then continuously to f631.","SE014-017; extent_495_640",conf="MEDIUM")
A.E[-1]["easing"]="AMBIGUOUS (smoothstep best, margin 0.011 over linear)"; A.E[-1]["measure"]="extent_495_640.json"
A.event("S05",749,749,"POP_IN","'Defined contribution' label, figure and paper","Right-hand 'Defined contribution' label with a figure and a paper appear in one frame beside the 'Defined benefit' building.","SE019",conf="HIGH")
A.event("S06",870,870,"POP_IN","document under the flag","Blue document appears under the flag.","SE021",conf="HIGH")
A.event("S06",912,912,"POP_IN","money bag","Bag appears beside the green character.","SE022",conf="HIGH")
A.event("S06",934,934,"POP_IN","bags and yellow notes","Two more bags and two yellow notes appear together.","SE023",conf="HIGH")
A.event("S07",1007,1007,"POP_IN","green character (left)","Left-hand green character appears under the chart.","SE025",conf="HIGH")
A.event("S07",1032,1032,"POP_IN","green character (right)","Second green character appears at the right.","SE026",conf="HIGH")
A.event("S07",1061,1061,"POP_IN","host figure","Host appears top-right above the chart.","SE027",conf="HIGH")
A.event("S07",1099,1099,"POP_IN","money bag on chart","Bag appears over the bars.","SE028",conf="HIGH")
A.event("S07",1141,1141,"OVERLAY_POP","red X circle on the bag","Orange/red X circle appears on the bag.","SE029",conf="HIGH")
A.event("S08",1188,1188,"OVERLAY_POP","bubble 'Buy those bonds!'","Bubble appears in one frame beside the woman.","SE031",conf="HIGH")
A.event("S09",1249,1323,"HIGHLIGHT_SWEEP","yellow highlight bar","Highlight grows left to right in steps (f1249, f1258, f1274, f1291, f1307, f1323) at roughly constant rate.","SE033-038; extent_1249_1330",conf="HIGH")
A.E[-1]["easing"]="linear (SUPPORTED, margin 0.037)"; A.E[-1]["measure"]="extent_1249_1330.json"
A.event("S09",1349,1349,"OVERLAY_POP","bubble 'Okay, you're the 3rd largest ...'","Bubble with small text appears beside the green character.","SE039",conf="MEDIUM")
A.event("S10",1446,1446,"OVERLAY_POP","blackboard text 'They DON'T have to'","Blackboard text replaces 'New rules =' in one frame.","SE041",conf="HIGH")
A.event("S11",1538,1538,"POP_IN","euro note 1","First note appears at top right.","SE043",conf="HIGH")
A.event("S11",1544,1544,"POP_IN","euro note 2","Second note appears.","SE044",conf="HIGH")
A.event("S11",1551,1551,"POP_IN","euro note 3","Third note appears.","SE045",conf="HIGH")
A.event("S11",1570,1640,"HIGHLIGHT_SWEEP","yellow highlight on the estimate sentence","Highlight starts at 'pension funds' (~f1580) and extends over two lines by ~f1640.","chk_f; extent_1570_1645",conf="MEDIUM")
A.E[-1]["easing"]="aggregate ink growth fits smoothstep (SUPPORTED) but two lines are summed; treat as indicative"; A.E[-1]["measure"]="extent_1570_1645.json"
A.event("S12",1903,1903,"OVERLAY_POP","red circle on '115'","Red circle appears around the 115 figure in the table.","SE047",conf="HIGH")
A.event("S12",1909,1909,"POP_IN","euro note","Bill appears at bottom-left.","SE048",conf="HIGH")
A.event("S12",1939,1939,"POP_IN","'30 year' tag","Yellow tag appears beside the bill.","SE049",conf="HIGH")
A.event("S12",1965,1965,"POSE_SWAP","host expression","Host face changes (mouth/brow) on 'simply vanishing'.","SE050",conf="MEDIUM")
A.event("S13",2053,2053,"POP_IN","small worried figure on the wave","Small figure appears at the wave crest.","SE052",conf="HIGH")
A.event("S14",2116,2116,"POP_IN","ABP logo","Blue 'ABP' wordmark appears in one frame.","SE054",conf="HIGH")
A.event("S14",2183,2183,"POP_IN","two documents","Two blue documents appear beside the logo.","SE055",conf="HIGH")
A.event("S14",2267,2267,"POP_IN","bill stack grows (1)","Another bill is added to the stack at the left (equal-size change).","SE056",conf="LOW",amb="count of bills at each step not resolved")
A.event("S14",2274,2274,"POP_IN","bill stack grows (2)","Another bill added.","SE057",conf="LOW",amb="count not resolved")
A.event("S14",2281,2281,"POP_IN","bill stack grows (3)","Another bill added.","SE058",conf="LOW",amb="count not resolved")
A.event("S14",2287,2287,"POP_IN","bill stack grows (4)","Another bill added (stack of four at f2306).","SE059",conf="LOW",amb="count not resolved")
A.event("S14",2306,2306,"OVERLAY_POP","red '500B'","Red '500B' text appears above the bills.","SE060",conf="HIGH")
A.event("S14",2333,2333,"POP_IN","host holding cash","Host figure with hand-drawn cash appears in front of the red text.","SE061",conf="HIGH")
A.write(headline="The World's Safest Market Is Breaking")
