import sys, json; sys.path.insert(0,'scripts')
from author_lib import *
A=Author('gGNVpOo7BK8',2236)
A.scenes([
(0,"Headline 'the secret exit we had to built for them'; host at a green blackboard 'What can they do?' then 'Two alternatives:'","headline; host; blackboard; caption","PR_BLACKBOARD,CH_HOST","Two things Japan can do with its bonds"),
(105,"'SELL' with a paper and a red SALE tag; a red line draws; a small Japan-map character pops; a shop video clip and 'PAWN' pop: 'it can sell them or it can pawn them'","headline; paper; red line; map character; video clip; caption","PR_DOC,OV_REDLINE,CH_JAPAN,PHOTO_CLIP","Sell or pawn"),
(174,"Large Japan-map character with a paper and a yellow tag: 'Japan's choice was to start selling'","headline; map character; paper; tag; caption","CH_JAPAN,PR_DOC","Japan chose to sell"),
(242,"Money bags pop in one by one beside a thin Japan-map character: 'Japan spent a record amount of money'","headline; map character; bags; caption","CH_JAPAN,PR_BAGS","A record amount of money"),
(289,"Large Japan-map character with a paper and yellow tag: 'sold American debt to do it'","headline; map character; paper; caption","CH_JAPAN,PR_DOC","Sold American debt"),
(338,"Japan-map character alone, bubble 'This is fine!': 'and told the entire world it meant business'","headline; map character; bubble; caption","CH_JAPAN,OV_BUBBLE","It meant business"),
(406,"Worried host alone: 'and not only did Japan's way not work'","host; caption","CH_HOST","Japan's way did not work"),
(473,"US-map character: 'it also was now America's problem'","map character; caption","CH_USMAP","America's problem"),
(499,"Giant US-map character close-up: 'America's problem'","map character (close-up); caption","CH_USMAP","America's problem"),
(530,"Federal Reserve building alone: 'there's a tool at the Federal Reserve'","building; caption","PR_BANK","A tool at the Fed"),
(584,"Fed building and a Japan-side building with a paper; paper and a bag move: 'where a foreign government can hand over its American bonds, take dollars'","two buildings; paper; bag; caption","PR_BANK,PR_BLDG,PR_DOC,PR_BAG","A foreign government hands over bonds and takes dollars"),
(702,"Green palm-leaf card with red 'TWO WEEKS LATER': 'and buy the bonds back later'","title card; caption","FX_TIMECARD","Time passes before the buy-back"),
(747,"Buildings again; bags and paper trade places: 'at a slightly higher repurchase price'","two buildings; bags; paper; caption","PR_BANK,PR_BLDG,PR_BAG,PR_DOC","Slightly higher repurchase price"),
(816,"Shop video clip at the top above a bag and paper: 'it's a pawn shop for governments'","video clip; bag; paper; caption","PHOTO_CLIP,PR_BAG,PR_DOC","A pawn shop for governments"),
(872,"Host at a green blackboard: 'the official name for it is the Foreign and International Monetary Authorities repo facility'","host; blackboard; caption","CH_HOST,PR_BLACKBOARD","The official name"),
(1027,"Small green bills: 'Repo Facility ... these are liquidity tools'","bills; caption","PR_CASH","Liquidity tools for central banks"),
(1063,"Icon collage (bills, calendar, buildings, paper) pops together: 'short-term repurchase agreements'","icon collage; caption","PR_CASH,PR_BANK,PR_CALENDAR,PR_DOC","Short-term repurchase agreements"),
(1160,"Host alone: 'here's how it works'","host; caption","CH_HOST","Here's how it works"),
(1196,"Japan-side building with a $100 paper that moves; the Fed building pops at the right: 'hands over $100 in US bonds... the Fed gives them $100 in cash'","two buildings; $100 paper; caption","PR_BLDG,PR_BANK,PR_DOC","$100 in bonds for $100 in cash"),
(1480,"Gold card 'THE NEXT DAY': 'then the next day'","title card; caption","FX_TIMECARD","The next day"),
(1511,"Buildings with bills that move; green '$101' pops: 'the Bank of Japan buys those bonds back'","two buildings; bills; green $101; caption","PR_BLDG,PR_BANK,PR_CASH,TY_GREEN","Bonds bought back for $101"),
(1618,"Green '$1' with the host pointing: 'for $101 and the repurchase price'; a '$1 =' coin and the Fed building pop","green text; host; coin; building; caption","TY_GREEN,CH_HOST,PR_COIN,PR_BANK","The $1 difference is the Fed's interest"),
(1805,"Host alone: 'the whole reason for the facility'","host; caption","CH_HOST","The reason for the facility"),
(1851,"US-map character and Japan-map character with bubbles; a bag drifts: 'is to give foreign countries quick access to dollars so they aren't forced onto the open market'","map characters; bubbles; bag; caption","CH_USMAP,CH_JAPAN,OV_BUBBLE,PR_BAG","Quick access to dollars"),
(2031,"Japan-map character with sunglasses and cash: 'a way to raise dollars'","map character; cash; caption","CH_JAPAN,PR_CASH","A way to raise dollars"),
(2092,"'US BONDS FOR SALE' stall with papers; a red X crosses it: 'without ever becoming a seller'","stall; papers; red X; caption","PR_STALL,PR_DOC,OV_REDX","Without becoming a seller"),
(2141,"US-map and Japan-map characters with bubbles and a bag: 'it's what you build for a creditor you cannot afford to lose'","map characters; bubbles; bag; caption","CH_USMAP,CH_JAPAN,OV_BUBBLE,PR_BAG","A creditor you cannot afford to lose")])
A.event("S01",30,30,"CAPTION_CHUNK_CHANGE","blackboard text","Board text changes from 'What can they do?' to 'Two alternatives:' in one frame.","SE001; ev_01",conf="HIGH")
A.event("S02",105,121,"STROKE_REVEAL","red vertical line","Red vertical line draws beside the 'SELL' paper over ~17 frames (red area 0 to 343 px).","SE002; color_red",conf="HIGH",label="MEASURED",amb="progress fitted by pixel count only")
A.event("S02",133,133,"POP_IN","small Japan-map character","Small Japan-map character appears at the right in one frame.","SE003; ev_01",conf="HIGH")
A.event("S02",151,157,"VIDEO_CLIP_INSERT","shop clip and 'PAWN'","Shop clip and 'PAWN' text appear at f151; the clip region updates at f151, f154 and f157 (3-frame cadence) and then holds to the cut f174.","SE004; clip-region mean abs diff",conf="MEDIUM",label="MEASURED",mclass="INDET",amb="source clip not identified")
A.event("S03",203,203,"OVERLAY_POP","yellow tag on the paper","Small yellow tag appears on the paper in one frame (+114 yellow px).","SE008; color_yellow",conf="MEDIUM",label="MEASURED")
A.event("S04",242,275,"POP_IN","money bags","Money bags pop in one by one beside the character over 34 frames.","SE009; ev_01",conf="MEDIUM")
A.event("S06",375,375,"OVERLAY_POP","bubble 'This is fine!'","Bubble appears beside the Japan-map character in one frame.","SE012; ev_01",conf="MEDIUM")
A.event("S10",530,530,"POP_IN","Federal Reserve building","Fed building appears in one frame after the giant map character.","SE016; ev_01",conf="HIGH")
A.event("S10",531,575,"SCALE_TWEEN","Federal Reserve building","Building grows from a small icon to about twice its size over ~46 frames while the caption is typed (ink area in the stage rows, fit below).","SE016; extent_529_577",conf="HIGH",label="MEASURED")
A.E[-1]["measure"]="extent_529_577.json"; A.E[-1]["easing"]="ease_out_cubic (SUPPORTED, margin 0.073; ink area, indicative)"
A.event("S11",601,619,"PROP_DRIFT","paper","Paper moves from the Japan-side building toward the Fed building over ~19 frames.","SE018; ev_01",conf="MEDIUM",amb="path and easing not measured")
A.event("S11",660,678,"PROP_DRIFT","bag","Bag moves from the Fed building toward the Japan-side building over ~19 frames.","SE019; ev_01",conf="MEDIUM",amb="path and easing not measured")
A.event("S13",747,760,"PROP_DRIFT","bags and paper","Bags and paper start trading places between the buildings (14 frames).","SE021; ev_01",conf="MEDIUM",amb="path and easing not measured")
A.event("S13",769,808,"PROP_DRIFT","bags and paper","Further movement of bags and paper between the buildings over ~40 frames.","SE022; ev_01",conf="LOW",amb="path and easing not measured; several props move")
A.event("S14",816,867,"VIDEO_CLIP_INSERT","shop clip","Shop clip at the top updates every third frame (f816, 819, 822, 825, 828, 831, 840, 841, 846, 852, 855, 858, 861, 864, 867), i.e. a ~10 fps source, with a hold at f832-839.","SE023; clip-region mean abs diff",conf="MEDIUM",label="MEASURED",mclass="INDET",amb="source clip not identified")
A.event("S17",1127,1127,"POP_IN","calendar and agreement paper","Calendar and an agreement paper appear in the collage in one frame.","SE034; ev_02",conf="MEDIUM")
A.event("S19",1284,1343,"PROP_DRIFT","$100 paper","The $100 paper moves from the Japan-side building to the right over ~60 frames.","SE038; ev_02",conf="MEDIUM",amb="path and easing not measured")
A.event("S19",1352,1352,"POP_IN","Fed building","Fed building appears at the right in one frame.","SE039; ev_02",conf="HIGH")
A.event("S19",1431,1469,"PROP_DRIFT","$100 paper","The $100 paper moves to the Fed building over ~39 frames.","SE041; ev_02",conf="MEDIUM",amb="path and easing not measured")
A.event("S21",1533,1567,"PROP_DRIFT","bills","Bills move between the buildings over ~35 frames.","SE044; ev_02",conf="MEDIUM",amb="path and easing not measured")
A.event("S21",1567,1567,"OVERLAY_POP","green '$101'","Green '$101' appears beside the Fed building in one frame (+60 green px).","color_lgreen",conf="HIGH",label="MEASURED")
A.event("S22",1728,1728,"POP_IN","'$1 =' coin","Coin appears after '$1 =' in one frame (+71 green px).","SE046; color_lgreen",conf="MEDIUM",label="MEASURED")
A.event("S22",1769,1769,"POP_IN","Fed building","Fed building appears in one frame.","SE047; ev_02",conf="HIGH")
A.event("S24",1892,1892,"OVERLAY_POP","bubble text","Bubble text changes in one frame.","SE050; ev_02",conf="MEDIUM",amb="bubble wording read at 360p")
A.event("S24",1937,1959,"PROP_DRIFT","bag","Bag drifts from the US-map character toward the Japan-map character over ~22 frames.","SE051; ev_02",conf="MEDIUM",amb="path and easing not measured")
A.event("S26",2121,2122,"OVERLAY_POP","red X","Red X appears across the stall within two frames (+550 red px) and is removed at the cut f2141.","SE056; color_red",conf="HIGH",label="MEASURED")
A.event("S27",2182,2198,"OVERLAY_POP","bubble text","Bubble text changes twice over ~16 frames (wording read at 360p).","SE059; ev_02",conf="MEDIUM",amb="bubble wording read at 360p")
A.fill_small(172)
A.E=[e for e in A.E if not (e['op']=='UNRESOLVED_CHANGE' and ('HARD' in e['desc'] or 'CUT' in e['desc'] or 'BIG_POP' in e['desc']) and any(e['f0']-2<=s['f0']<=e['f1']+2 for s in A.S))]
A.write(headline="the secret exit we had to built for them")
a=json.load(open('videos/gGNVpOo7BK8/review/assets.json'))
for x in a:
    if x['asset_id']=='TY_HEADER': x['f1']=406
json.dump(a,open('videos/gGNVpOo7BK8/review/assets.json','w'),indent=1)
