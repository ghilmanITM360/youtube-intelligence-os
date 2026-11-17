#!/usr/bin/env python3
"""Builds STIRRING_TEA_ASSET_PROMPTS.md from the data below. Re-run after editing; counts are computed, never typed.
Usage: python3 build_asset_prompts.py   (writes next to this file)"""
import re, os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "STIRRING_TEA_ASSET_PROMPTS.md")
PROJ = os.path.dirname(HERE)
MASTER = os.path.join(HERE, "inputs", "ALIEN_MASTER_001.png")
MASTER_SHA = "12b1f42ea48d0eb88c1b0fd63237904fd547d478fc7bf8a03bfdd67e3833ad9c"
ORIG = "/Users/ghilmankhan/Downloads/Minimalist alien science mascot.png"
OUTDIR = os.path.join(HERE, "assets")   # where Codex writes finished files

# ---------------------------------------------------------------- script
V3 = {
 "B01": "Could you boil a cup of water just by stirring it? Short answer: no. But the spoon does try.",
 "B02": "Stirring really does add energy. The swirl rubs the water against itself, and that friction turns motion into heat. So the idea is sound. The problem is the amount.",
 "B03": "Take a quarter liter of water at twenty degrees. Boiling is a hundred. Lifting it those eighty degrees takes about eighty-four thousand joules. Do that in two minutes, and you need seven hundred watts going in. That's seven old hundred-watt light bulbs, or about what a microwave draws to heat a mug. In horse terms, about one horsepower.",
 "B04": "Even dropping the water over Niagara Falls warms it only about a tenth of a degree.",
 "B05": "Now the spoon. A hard stir adds well under one watt: less than a hundredth of one of those bulbs. Seven hundred needed, under one delivered. The water warms a hair, until the cup leaks that heat away as fast as the spoon adds it.",
 "B06": "So stir faster, far faster than any hand: tens of thousands of strokes a second, and the water cavitates. Pressure drops behind the spoon and vapor bubbles form. That looks like boiling, but it's low pressure, not heat. And the splashing spreads the water out, so it cools even faster.",
 "B07": "Someone actually measured tea: stirring it, dipping the spoon, or leaving it alone all cool it at about the same rate.",
 "B08": "So, ordinary spoon, open cup? No. The needle stays near room temperature, however hard you stir. A spoon is for dissolving sugar. Boiling is not in its job description.",
}
WIN_FULL = {"B01":(0,4.4),"B02":(4.4,11.7),"B03":(11.7,26.4),"B04":(26.4,29.8),"B05":(29.8,39.7),"B06":(39.7,52.8),"B07":(52.8,57.9),"B08":(57.9,66.4),"B09":(66.4,68.0)}
WIN_60 = {"B01":(0,4.5),"B02":(4.5,12),"B03":(12,26.5),"B05":(26.5,36),"B06":(36,49),"B08":(49,59),"B09":(59,60)}
BEAT_NAME = {"B01":"Hook and early verdict","B02":"Stirring adds energy","B03":"Energy and power ladder","B04":"Niagara comparison","B05":"The spoon adds under one watt","B06":"Faster stirring: cavitation and splash","B07":"Measured tea cooling","B08":"Answer and sugar","B09":"Final hold"}
FULL_ONLY = {"B04","B07"}
def wc(s): return len(s.split())
W_FULL = sum(wc(v) for v in V3.values())
W_60 = sum(wc(v) for k, v in V3.items() if k not in FULL_ONLY)
KOKORO_S = 67.4  # measured ffprobe 67.397 s, af_heart speed 1.35, pauses trimmed

# ---------------------------------------------------------------- global locks
STROKE_STAGE = 7        # px on the 1080x1920 canvas
ART_SCALE = 0.78        # alien: master-scale px -> stage px (master outline ~9 px -> 7 px)
INK, CANVAS, RED = "#0C0C0C", "#FFFFFF", "#D7263D"
GREY1, GREY2, MINT = "#E4E4E4", "#C4C4C4", "#E3FCDE"
STYLE = ("Flat 2D hand-drawn black monoline ink illustration in the style of a whiteboard explainer: ONE uniform line weight, "
         "slightly wobbly hand-drawn line, round line caps, near-black ink #0C0C0C, flat fills only (white or light grey #E4E4E4 / #C4C4C4), "
         "no gradients, no shading, no texture, no glow, no drop shadow, no 3D, no cel shading, no thick-thin calligraphic variation, no sketchy double lines. "
         "Red #D7263D ONLY where the object is hot or it marks the answer. "
         "The look is the xkcd What If whiteboard look: the page is overwhelmingly PURE WHITE #FFFFFF, at least 85 percent of any canvas stays empty white; light grey only for small water or accent areas, never large grey or coloured areas, no background scenery. ")
NEG = ("Do not draw any text, letters, numbers, logos or watermark. Do not copy any existing comic, channel, mascot, title card or book illustration. "
       "No photo realism. No real person.")
ALPHA = ("Output a true-alpha RGBA PNG with a fully transparent background (ask the image tool for a transparent background and keep its alpha; "
         "do not paint a white, grey, black or checkerboard background).")
ALIEN_LOCK = ("Character = ALIEN_MASTER_001 (reference image 1): pale-mint head #E3FCDE with a black outline, tall rounded-triangle egg shape wider at the top and narrowing to a soft point at the chin, "
              "two large solid-black tilted almond eyes, one short flat black mouth line, a single-stroke stick body (one line each for neck, torso, arms, legs), no drawn hands or feet, no clothes, no hair, no glow. ")

ASSETS = []
def A(id, fn, kind, typ, beats, cut, purpose, prompt="", refs="", preserve="", change="", layer="", anchors="", out="", checks=""):
    ASSETS.append(dict(id=id, fn=fn, kind=kind, typ=typ, beats=beats, cut=cut, purpose=purpose, prompt=prompt, refs=refs,
                       preserve=preserve, change=change, layer=layer, anchors=anchors, out=out, checks=checks))

# kinds: ART unique artwork | POSE | STATE | COMP compositor element | REF reference sheet | PIPE derived by code
# typ: GEN (image model) | VEC (drawn in code/SVG) | TEXT (typeset layer) | PIPE (pipeline)

# ================================================================ PIPELINE + CHARACTER
CHK_CHAR = ("Silhouette matches the master head contour (egg wider at top, soft chin point); eyes are solid black tilted almonds in the master positions; one short flat mouth line; "
            "mint fill #E3FCDE; stroke weight equals the master (about 9 px at the 1536 px sheet scale); stick body single-stroke; NO glow, NO halo, NO shading; "
            "head height is 0.37 of figure height; alpha inside the head is 255 (no holes).")
A("PIPE-01","inputs/ALIEN_MASTER_001.png","PIPE","PIPE","all","60s","Registered copy of the supplied alien PNG; exact path, hash and measurements.",
  prompt="No generation. Copy the supplied PNG to inputs/ALIEN_MASTER_001.png (done), verify SHA-256 "+MASTER_SHA+", never edit it.",
  out="1024x1536 RGBA PNG (as supplied)", checks="SHA-256 equals the value above; file opens as RGBA 1024x1536.")
A("PIPE-02","assets/chr/ALIEN_HEAD_CLEAN.png","PIPE","PIPE","all","60s","Head and neck cutout of the master with the baked glow halo removed; the reference for every generation.",
  prompt=("Code step, no image model: load ALIEN_MASTER_001, keep pixels with alpha >= 200 inside the head box x 337..643, y 139..509 plus the neck line below it; "
          "set every other pixel to alpha 0 (this removes the faint baked glow halo, which is NOT part of the character); re-save RGBA PNG at 1024x1536. "
          "Measured on the master: head solid bbox x 337..643, y 139..~494 (306 wide x ~356 tall), head centre x 490, neck line x ~494 (about 9 px wide) starting y ~500, "
          "left eye bbox x 377..477 y 276..354, right eye bbox x 531..620 y 269..353, mouth about x 490..527 y ~414, mint fill (227,252,222), outline 7-10 px."),
  refs="PIPE-01", out="1024x1536 RGBA PNG", anchors="HEAD_TOP (490,139); CHIN (490,494); NECK_TOP (494,500)",
  checks="No pixel with alpha 1..199 outside the antialiased outline; head interior alpha 255; no visible halo when composited over #0C0C0C.")

def view(id, fn, name, desc, extra=""):
    A(id, fn, "ART", "GEN", "model sheet", "60s", f"Model-sheet view: {name}.",
      prompt=(STYLE+ALIEN_LOCK+f"Full-figure {name} of the alien standing, relaxed, arms hanging, {desc}. NO floor line, NO ground, NO shadow, NO platform under the feet: the two legs simply end in free line ends. Figure height 962 px on a 1536x1536 canvas: head top y=140, chin y=496, shoulders y=520, hip y=760, feet y=1102, figure axis x=768. "
              "Proportions: head 0.37 of height, torso 0.25, legs 0.355, arm length 375 px (upper 185 + forearm 190). Stroke 9 px. "+extra+ALPHA+" "+NEG),
      refs="ALIEN_MASTER_001 as reference image 1; ALIEN_HEAD_CLEAN (PIPE-02) as reference image 2", preserve="head contour, eye shape and placement, mouth position, mint fill, stroke weight",
      change="body and view angle only", layer="z30 (character)", anchors="HEAD_TOP (768,140) CHIN (768,496) SHOULDER (768,520) HIP (768,760) FEET (768,1102)",
      out="1536x1536 RGBA PNG, transparent", checks=CHK_CHAR)
view("CHR-V01","assets/chr/CHR_V01_front.png","front","facing the camera, eyes and mouth visible, symmetrical")
view("CHR-V02","assets/chr/CHR_V02_three_quarter.png","three-quarter (head turned about 35 degrees to the right)","body turned about 35 degrees, far eye smaller and closer to the head edge, mouth line shifted right")
view("CHR-V03","assets/chr/CHR_V03_profile.png","profile facing right","head in pure side profile: one eye as a narrow almond on the front edge, egg shape seen from the side with a soft chin point, short mouth line at the front","The profile head must keep the same height (356 px) and the same top-heavy egg volume.")
view("CHR-V04","assets/chr/CHR_V04_back.png","back view","head seen from behind: plain mint egg with outline, no eyes, no mouth, neck line below")

def expr(id, name, desc):
    A(id, f"assets/chr/CHR_{id[-3:]}_expr_{name}.png", "STATE", "GEN", "model sheet", "60s", f"Expression head: {name}.",
      prompt=(STYLE+ALIEN_LOCK+f"Head and neck only, front view, expression '{name}': {desc}. Keep the master head contour and eye placement; only the mouth line and eye angle/size may change, by at most 12 px. "
              "Canvas 1024x1536, same head position as the master (head top y=139). Stroke 9 px. "+ALPHA+" "+NEG),
      refs="ALIEN_HEAD_CLEAN (PIPE-02)", preserve="head outline, fill, eye shape, eye centres to within 8 px",
      change=f"mouth line and eye tilt for '{name}' only", layer="z31 (head swap over a pose)", anchors="CHIN (490,494) HEAD_TOP (490,139)",
      out="1024x1536 RGBA PNG, transparent", checks=CHK_CHAR+" Only the mouth/eye angle differs from the master.")
expr("CHR-X01","neutral","exactly the master face: short flat mouth line, eyes level")
expr("CHR-X02","curious","mouth becomes a tiny open round 'o' about 14 px wide, eyes tilted 4 degrees more upward")
expr("CHR-X03","surprised","mouth a larger 'o' about 26 px, eyes 8 percent larger")
expr("CHR-X04","deadpan","mouth a flat line 20 percent longer, eyes level and slightly smaller (flat, unimpressed)")
expr("CHR-X05","smug","mouth line with the right end curled up 8 px, eyes level")
expr("CHR-X06","worried","mouth a short wavy line, eyes tilted 6 degrees downward at the outer corners")

def grip(id, name, desc):
    A(id, f"assets/chr/CHR_{id[-3:]}_grip_{name}.png", "REF", "GEN", "model sheet", "60s", f"Hand-grip reference: {name}.",
      prompt=(STYLE+f"Close reference sheet, 1536x768, white-transparent: the end of a single-stroke stick arm (the channel draws NO hands, so the 'grip' is the arm line ending in a short curl of 26 px that wraps the prop). {desc} "
              "Draw three versions side by side: front, side, three-quarter. Stroke 9 px. "+ALPHA+" "+NEG),
      refs="CHR-V01", preserve="arm stroke weight and round cap", change="grip shape only", layer="reference only",
      anchors="WRIST (arm end) marked by a small + only in the review contact sheet",
      out="1536x768 RGBA PNG", checks="No fingers, no hand shape; the curl overlaps the prop by 10-18 px; stroke equals the arm stroke.")
grip("CHR-G01","spoon_side","The arm ends in a curl around a spoon handle seen from the side.")
grip("CHR-G02","spoon_top","The arm ends in a pinch (two 14 px strokes) at the top of a spoon handle, for lifting the spoon out.")
grip("CHR-G03","point","The arm ends in a straight pointing stroke (no hand), 20 px beyond the wrist.")
grip("CHR-G04","pinch_cube","The arm ends in a pinch around a small sugar cube of 34 px.")
A("CHR-MS01","assets/chr/CHR_MS01_model_sheet.png","PIPE","PIPE","model sheet","60s","Model sheet contact: 4 views, 6 expressions, 4 grips on one board for review.",
  prompt="Code step: tile CHR-V01..V04, CHR-X01..X06, CHR-G01..G04 on #FFFFFF with ID captions (caption text only on this review board), draw the anchor crosses and a 0.37 head-ratio ruler.",
  refs="CHR-V01..V04, CHR-X01..X06, CHR-G01..G04", out="3200x2400 RGB PNG", checks="All 14 tiles present; head heights agree within 3 percent; anchors line up across views.")

# ---- poses
POSE_BASE = ("Full-figure single pose of the alien on a transparent 1536x1536 canvas, NO floor line, NO ground, NO shadow under the feet, same scale as the model sheet: head top y=140, chin y=496, shoulders y=520, hip y=760, feet y=1102, figure axis x=768, feet baseline y=1102. "
             "Arm length 375 px. No prop is drawn in the hand: the arm ends at the marked WRIST anchor where the compositor places the prop. Stroke 9 px. ")
def pose(id, name, desc, wrist, purpose, expr_default="CHR-X01"):
    A(id, f"assets/pose/POSE_{id[-2:]}_{name}.png", "POSE", "GEN", "shots", "60s", purpose,
      prompt=(STYLE+ALIEN_LOCK+POSE_BASE+f"Pose '{name}': {desc} "+ALPHA+" "+NEG),
      refs="CHR-V01, CHR-V02, CHR-V03, ALIEN_HEAD_CLEAN (PIPE-02), CHR-MS01", preserve="head contour, eyes, mouth, fill, stroke weight, limb lengths, feet baseline y=1102, axis x=768 (or the stated foot axis)",
      change=f"limb angles and head turn only: {name}", layer="z30 (character); head swap layer z31; prop layers z25-z29",
      anchors=f"FEET (768,1102) HIP (768,760) SHOULDER (768,520) CHIN (768,496) WRIST {wrist}", out="1536x1536 RGBA PNG, transparent",
      checks=CHK_CHAR+" Limb lengths equal the model sheet (arm 375, leg ~342); only one arm/leg angle set differs; feet stay on the baseline; the wrist anchor is within 6 px of the stated point.")
pose("CHR-P01","stand_neutral","standing front view, arms hanging, head level, looking at the camera.","(640,760) hanging","Opening and idle narrator stance.")
pose("CHR-P02","present_right","standing three-quarter, the right arm raised to point up and to the right toward a diagram (forearm at 30 degrees above horizontal), head turned to follow it.","(1090,335)","Presenting a diagram or ruler in the upper panel.")
pose("CHR-P03","look_down_cup","standing three-quarter facing right, head tilted down 25 degrees toward a cup at table height, arms hanging, eyes angled down.","(640,760)","Looking at the cup.")
pose("CHR-P04","reach_to_mug","three-quarter facing right, right arm extended forward and slightly up (wrist at shoulder height + 60 px) to reach the mug, left arm hanging.","(1130,560)","Reaching toward the mug or spoon.")
pose("CHR-P05","grip_spoon_ready","three-quarter facing right, right arm bent, forearm vertical, the wrist held above the mug rim (wrist 33 px above the neutral grip point) so a spoon can hang down; arm ends in the spoon-grip curl (CHR-G01).","(1050,420)","Gripping the spoon before it enters the water.")
pose("CHR-P06","stir_slow_A","three-quarter facing right, right arm out with the wrist LEFT of the mug axis (60 px left of the neutral grip point N=(1050,453)), elbow low, relaxed, head tilted toward the cup.","(990,453)","Slow stir, position A.")
pose("CHR-P07","stir_slow_B","exactly pose stir_slow_A but the wrist moved 120 px to the RIGHT (60 px right of the neutral grip point N); body, head and legs identical to stir_slow_A to the pixel.","(1110,453)","Slow stir, position B (alternates with A).")
pose("CHR-P08","stir_hard_A","three-quarter facing right, leaning forward 8 degrees, right arm out with the wrist far LEFT (80 px left of N), shoulders tense, the head slightly shaking (draw 2 short motion ticks beside the head).","(970,453)","Vigorous stir, position A.")
pose("CHR-P09","stir_hard_B","exactly stir_hard_A but the wrist 160 px to the RIGHT (80 px right of N), the same lean; the head ticks mirrored.","(1130,453)","Vigorous stir, position B.")
pose("CHR-P10","lift_spoon","three-quarter facing right, right arm raised so the wrist is 120 px above N (spoon pulled out of the cup), head following it, arm ends in the lift pinch (CHR-G02).","(1050,333)","Lifting the spoon out of the cup.")
pose("CHR-P11","check_dial","three-quarter facing right, left arm extended toward a dial at the right, arm ending in a pointing stroke (CHR-G03), head turned to the dial, eyes toward it.","(1130,470)","Checking the thermometer dial.")
pose("CHR-P12","final_shrug","front view, both arms raised to the sides with the forearms bent up (shrug), head tilted 6 degrees, deadpan.","(540,400) and (996,400)","Final deadpan reaction.","CHR-X04")
pose("CHR-P13","sugar_drop","three-quarter facing right, right arm extended over the mug with the wrist 170 px above N so the cube is just over the rim, ending in the cube pinch (CHR-G04), left arm hanging, head tilted down.","(1050,285)","Dropping a sugar cube in.")
pose("CHR-P14","profile_look_up","profile facing right, standing still, head tilted up 30 degrees, both arms hanging; figure drawn at the same 962 px height (the compositor scales it to 22 percent for a scale-figure on the Niagara view).","(640,760) hanging","Tiny scale figure watching the falls.")

# ================================================================ PROPS AND ENVIRONMENT
PROP = ("Generate at 2x the stage size so a 14 px stroke becomes 7 px. Flat side elevation, no perspective. ")
def prop(id, fn, kind, beats, cut, purpose, subject, size, stage, anchors, checks, refs="", layer="", preserve="", change="", bg="alpha"):
    p = STYLE + subject + " " + PROP + (ALPHA if bg=="alpha" else "Fill the whole canvas with flat #FFFFFF (no transparency).") + " " + NEG
    A(id, fn, kind, "GEN", beats, cut, purpose, prompt=p, refs=refs, preserve=preserve, change=change, layer=layer, anchors=anchors,
      out=f"{size} {'RGBA PNG, transparent' if bg=='alpha' else 'RGB PNG on #FFFFFF'}; stage size {stage}", checks=checks)

prop("MUG-R01","assets/ref/MUG_R01_sheet.png","REF","reference","60s","Mug reference sheet: three views to lock the outline.",
     "Reference sheet of ONE ceramic mug (no tea): side view with the handle on the RIGHT, top-down view (rim circle, handle), three-quarter view. Mug 230 px wide x 260 px tall body (stage size), straight slightly tapered walls, rounded bottom corners, C-shaped handle 75 px wide. Draw an inner dashed line at the 90 percent fill height.",
     "2400x900","n/a (reference)","n/a","Same mug in all three views; handle on the right in side view; rim and base proportions agree.")
prop("MUG-01","assets/prop/MUG_01_back_fill.png","ART","B01,B02,B05,B06,B07,B08","60s","Mug back layer: white-filled glass-walled mug body that hides what is behind it.",
     "Side elevation of the mug from MUG-R01, handle on the right, drawn as a see-through ceramic mug: only the outer outline, a white fill, a thin rim line at the top. No water, no spoon. Width 230 (+75 handle), height 260.",
     "1000x640","230x260 body + 75 handle","BASE (center bottom) at x=660,y=1370 stage; RIM_Y 1110; WATERLINE_REST 1150; INNER_LEFT 560; INNER_RIGHT 760",
     "Outline closed, fill opaque white, handle on the right; base sits exactly on the baseline row; no water drawn.",
     refs="MUG-R01", layer="z10",preserve="outline of MUG-R01 side view")
prop("MUG-02","assets/prop/MUG_02_front_outline.png","ART","B01,B02,B05,B06,B07,B08","60s","Mug front outline layer drawn over water and spoon so the walls stay crisp.",
     "Exactly the mug outline of MUG-01 as line art only (no fill), transparent inside, so it can be placed above the water and the spoon.",
     "1000x640","same as MUG-01","identical to MUG-01 (same pixel coordinates)","Line positions identical to MUG-01 within 1 px (overlay test); interior fully transparent.",
     refs="MUG-01", layer="z20", preserve="every outline pixel of MUG-01", change="remove the fill only")
prop("WTR-01","assets/prop/WTR_01_rest.png","STATE","B01,B05,B08","60s","Water at rest: flat grey fill with a level surface line.",
     "The water body inside the mug: flat #E4E4E4 fill from the waterline to the inner bottom, the surface is one straight horizontal line, nothing else (no ripples, no bubbles). Waterline 40 px below the rim (stage y=1150).",
     "1000x640","inner shape only","WATERLINE y=1150; clip to MSK-01","Fill touches the inner walls without overlap; surface perfectly level; no marks.",refs="MUG-01",layer="z12")
prop("WTR-02","assets/prop/WTR_02_swirl_light.png","STATE","B02,B05,B08","60s","Water with a gentle swirl and a slight surface dip (early stir).",
     "Same water body as WTR-01 with three curved swirl lines inside it (spiral arcs, same ink weight) and the surface dipped 10 px at the center and raised 6 px at the walls. Nothing else.",
     "1000x640","same","WATERLINE center y=1160, wall y=1144; clip to MSK-01","Three swirl lines only; fill and silhouette identical to WTR-01 except the surface dip.",
     refs="WTR-01", layer="z12", preserve="water fill color and inner shape", change="add 3 swirl lines and a 10 px surface dip")
prop("WTR-03","assets/prop/WTR_03_vortex.png","STATE","B06","60s","Strong vortex: deep central dip and five swirl lines (hard stir).",
     "Same water body with a deep funnel dip of 60 px at the center, wall rise 24 px, five tight spiral lines; the surface is a smooth V-shaped curve. No droplets.",
     "1000x640","same","WATERLINE center y=1210, wall y=1126; clip to MSK-01","Funnel is the largest change vs WTR-02; fill color unchanged; water stays inside the mug.",
     refs="WTR-02", layer="z12", change="deepen the dip, add 2 swirl lines")
prop("WTR-04","assets/prop/WTR_04_splash.png","STATE","B06","60s","Splash droplets leaving the mug (overlay above the rim).",
     "Overlay only: 10 water droplets (teardrops and small circles, flat #E4E4E4 with ink outline) in arcs leaving the rim, 5 to the left and 5 to the right, plus 2 short motion ticks. Nothing else.",
     "1000x640","drawn above y=1110","droplet origin at the rim y=1110, x 580 and 740","Droplets outside the mug silhouette only; none overlap the handle.",
     layer="z22", refs="MUG-02")
prop("SPN-01","assets/prop/SPN_01_upright.png","ART","B01,B02,B05,B08","60s","Spoon upright in the water (neutral stir position).",
     "A teaspoon in side view: long straight handle, oval bowl at the bottom end, no pattern. Stage size 340 px long, bowl 44 px wide, handle 10 px wide, vertical.",
     "200x800","340x50","GRIP at 60 percent from the top (the neutral wrist N lands here); BOWL_CENTER at the bottom; pivot at the grip","Handle straight, bowl an oval of 2:1, one outline, white fill.",
     layer="z15", refs="WTR-01")
prop("SPN-02","assets/prop/SPN_02_tilt_left.png","STATE","B02,B08","60s","Spoon tilted 20 degrees to the left (stir position A).",
     "Exactly SPN-01 rotated 20 degrees counter-clockwise about its grip point. Transparent canvas with the same size.",
     "400x800","same","pivot at the GRIP; angle -20","Identical shape to SPN-01 except rotation; no re-draw differences.",refs="SPN-01",change="rotate -20 degrees about the grip")
prop("SPN-03","assets/prop/SPN_03_tilt_right.png","STATE","B02,B08","60s","Spoon tilted 20 degrees to the right (stir position B).",
     "Exactly SPN-01 rotated 20 degrees clockwise about its grip point.",
     "400x800","same","pivot at the GRIP; angle +20","Identical shape to SPN-01 except rotation.",refs="SPN-01",change="rotate +20 degrees about the grip")
prop("SPN-04","assets/prop/SPN_04_blur_pair.png","STATE","B05,B06","60s","Fast-stir spoon: two faint copies and speed marks.",
     "SPN-01 shown at two positions 40 px apart (the second copy outline only 50 percent opacity ink), with 4 short horizontal speed lines on the trailing side. Nothing else.",
     "600x800","same","pivot at the GRIP of the leading copy","Leading copy identical to SPN-01; speed lines on one side only.",refs="SPN-01")
prop("SPN-05","assets/prop/SPN_05_resting_rim.png","STATE","B01,B09","60s","Spoon laid across the mug rim at rest.",
     "SPN-01 rotated to 75 degrees from vertical, bowl dipping 20 px inside the rim on the left, handle resting over the right rim, as if laid across the mug.",
     "800x300","same","RIM contact points at x=560 and x=760, y=1110","Spoon touches the rim at two points, not floating; same spoon shape.",refs="SPN-01,MUG-02",change="rotate and place on the rim")
prop("SPN-06","assets/prop/SPN_06_wet_lift.png","STATE","B02","60s","Spoon lifted with three drips.",
     "SPN-01 upright with three small drips falling from the bowl (teardrops) and a short wet line on the bowl.",
     "200x900","same","GRIP at 60 percent","Drips below the bowl only; spoon unchanged.",refs="SPN-01")
prop("THM-R01","assets/ref/THM_R01_sheet.png","REF","reference","60s","Dial-thermometer reference sheet.",
     "Reference sheet of a kitchen dial thermometer: front face (round dial 150 px with tick marks, a needle, a short stand), side view (thin body), and the probe cable. No numbers.",
     "2000x800","n/a","n/a","Dial round; tick marks evenly spaced over 270 degrees; no numbers drawn.")
prop("THM-01","assets/prop/THM_01_dial_base.png","ART","B01,B02,B05,B08,B07","60s","Dial base: round face, tick ring, stand (needle drawn separately).",
     "Front view dial thermometer: circle 150 px diameter, 24 short tick marks around 270 degrees (0 at lower left, full scale at lower right), a small hub circle at the center, a short stem and flat foot of 60 px. No needle, no numbers.",
     "400x560","150 dial + stem, 150x225","DIAL_CENTER (75,75) of the dial; PIVOT = DIAL_CENTER; FOOT_BASELINE at table y=1370","Needle absent; ticks symmetric; no text.",layer="z8",refs="THM-R01")
prop("THM-02","assets/prop/THM_02_needle.png","STATE","B01,B02,B05,B07,B08","60s","Needle layer; rotated about the hub for every temperature state.",
     "A single thin needle with a tiny round tail, 60 px long (stage), pointing straight up. Transparent canvas 200x200 with the hub at the center.",
     "200x200","60 long","PIVOT = hub (100,100); 20 C = -108 deg from the up axis; one-hair move = +1.5 deg; 100 C = +108 deg","Hub at the exact center; needle straight; same stroke as the dial.",layer="z9",refs="THM-01")
prop("THM-03","assets/prop/THM_03_probe_cable.png","ART","B01,B02,B05,B08","60s","Probe cable: thin line from the dial into the mug.",
     "A thin smooth curved line (single stroke) from the dial stand at the right, over the mug's right rim, down into the water ending with a small probe tip 100 px below the waterline along the right inner wall. White gap where it passes behind the handle.",
     "600x700","approx 300x350","START at the dial base (885,1300); RIM_CROSS (770,1112); PROBE_TIP (748,1255)","Line single-stroke, crosses the rim at one point, probe stays on the right wall away from the spoon path.",layer="z11",refs="MUG-01,THM-01")
prop("TBL-01","assets/env/TBL_01_stage.png","ART","B01,B02,B05,B08,B09","60s","Stage plate: floor line, table top, legs (fixed camera for every stage shot).",
     "Full-frame portrait plate 1080x1920 (generate at 2160x3840): flat pure-white #FFFFFF canvas with a long thin floor line at y=1700, a rectangular table side view with a 14 px (stage 7 px) top slab at y=1370 from x=420 to x=1080 (cropped by the frame), two plain legs down to the floor, and nothing else in the upper 70 percent.",
     "2160x3840","1080x1920","FLOOR y=1700; TABLE_TOP y=1370; table left edge x=420","Floor and table are straight lines; the upper area is empty; table top at exactly y=1370 on the downscaled plate.",bg="canvas",layer="z0",
     preserve="n/a")

# ---- science graphics
prop("RUL-01","assets/sci/RUL_01_watt_ruler.png","ART","B02,B03,B04,B05,B06,B07,B08,B09","60s","Persistent vertical watt ruler (the anchor; ticks only, labels are text layers).",
     "A tall thin vertical ruler: one straight 7 px spine line 1100 px tall with 9 long ticks every 100 px (0..800 W) and 8 short ticks between them, ticks to the right of the spine. No text, no numbers.",
     "300x2300","60x1100","ZERO at the bottom (30,2280)/2; 100 W per 125 px stage (0-800 W over 1000 px); spine x=90 stage","Spine straight, tick spacing exactly even (100 W = 125 px), 0 at the bottom.",layer="z40 (persistent overlay, above scenes, below pops)")
prop("THR-01","assets/sci/THR_01_temp_ruler.png","ART","B03","60s","Temperature ruler strip 20 to 100 C (ticks only).",
     "A vertical thermometer-style scale bar: rounded rectangle 36 px wide, 560 px tall, 17 ticks every 5 C from 20 to 100 on the right, bulb at the bottom. White fill, no red, no numbers.",
     "300x1300","36x560 + bulb","20C at the bottom tick y=1210/2, 100C at the top tick; 7 px stage per C","Tick spacing even; range ends at both labelled ends; no red (red gap is a compositor bracket).",layer="z14")
prop("JUG-01","assets/sci/JUG_01_quarter_litre.png","ART","B03","60s","Quarter-liter measuring jug with water to the 250 ml mark.",
     "A transparent measuring jug in side elevation with a spout at the left and a handle at the right, graduation ticks (no numbers) at 50 ml steps, flat #E4E4E4 water to the 250 ml tick.",
     "700x900","240x300","WATERLINE = 250 ml tick; base on y=1370 or panel baseline","Water level exactly at the tick marked 250; handle on the right.",layer="z14")
prop("CLK-01","assets/sci/CLK_01_clock.png","ART","B03","60s","Clock icon with a 2-minute sector.",
     "A round analog stopwatch: circle 150 px, a small top button, 12 ticks, one hand pointing at 12, and a flat #C4C4C4 pie sector from 12 to 4 o'clock (the 2-minute-of-6 sector is only an icon).",
     "400x460","150x170","CENTER (75,85)","Sector from 12 to 4; hand at 12; no numbers.",layer="z16")
prop("BLB-01","assets/sci/BLB_01_bulb.png","ART","B03,B05","60s","Old incandescent bulb (seven are tiled to make 700 W).",
     "An old incandescent light bulb, base down: round glass 70 px, screw base 34 px, filament drawn as a small zigzag, no glow, no light rays, no red.",
     "300x420","70x100","BASE_BOTTOM (150,420); tiles at 60 px spacing; 100 W under the first via a label","Bulb recognizable at 100 px height; no glow.",layer="z16")
prop("MWV-01","assets/sci/MWV_01_microwave.png","ART","B03","60s","Small microwave with a mug inside (same ruler height as 700 W).",
     "A small countertop microwave in front elevation: a rectangular body 200 x 130 px, a door window on the left with a mug silhouette inside, a control panel strip with three buttons on the right, a short cord. No text, no glow.",
     "600x440","200x150","BASE (300,430)","Door window shows a mug; panel on the right; no text.",layer="z16")
prop("HRS-01","assets/sci/HRS_01_horse.png","ART","B03","60s","Original horse silhouette for 'about one horsepower'.",
     "An original simple horse drawn as a side-view monoline outline with white fill, standing, 220 px wide: oval body, four straight legs, curved neck, small head, a short tail and mane as 3 strokes. Do NOT draw any comic, mascot or book illustration; plain generic horse.",
     "700x640","220x200","HOOF_BASELINE (350,620)","Four legs, one tail, one mane tuft; not a copy of any published horse drawing.",layer="z16")

prop("NIA-01","assets/sci/NIA_01_falls_wide.png","ART","B04","full-cut-only","Niagara wide plate: cliff, crest, base pool (water curtain drawn separately).",
     "A tall portrait panel 1080x810 (generate at 2160x1620): flat #FFFFFF sky, a rocky cliff on the left and right drawn as WHITE-filled outline shapes with a few thin hatch lines (no grey fill, the panel stays mostly white), a horseshoe-shaped crest at the top and a pool at the bottom with flat #E4E4E4 water. Leave the center column (x 360..720) EMPTY for the water curtain layer.",
     "2160x1620","1080x810","CREST_Y 120; POOL_SURFACE_Y 700; FALL_HEIGHT 580 px","Center column empty; crest y=120 and pool y=700 on the downscaled plate; flat fills only.",bg="canvas",layer="z0")
prop("NIA-02","assets/sci/NIA_02_water_curtain.png","STATE","B04","full-cut-only","Descending water curtain overlay.",
     "A vertical curtain of falling water 360 px wide x 580 px tall: flat #E4E4E4 with 9 thin vertical streak lines of varying length, a ragged top edge and an unfinished (fading) bottom edge. Nothing else.",
     "720x1160","360x580","TOP (540,120); BOTTOM (540,700)","Streaks vertical; top ragged; width matches the NIA-01 empty column.",layer="z5",refs="NIA-01")
prop("NIA-03","assets/sci/NIA_03_cup_at_foot.png","ART","B04","full-cut-only","Close view: a cup of water at the foot of the falls.",
     "Close panel 1080x810 (generate 2160x1620 with a flat #FFFFFF background): the bottom of a waterfall seen from the side: a very light curtain (white with a few streak lines) entering from the top, a flat-water pool, and a plain cup sitting at the pool edge with water in it, the cup 160 px tall. Nothing red.",
     "2160x1620","1080x810","CUP_BASE (540,700); CURTAIN_X 300..540","Cup outline closed; water in the cup flat grey; curtain enters from the top edge.",bg="canvas",layer="z0",refs="NIA-01,MUG-01")
prop("NIA-04","assets/sci/NIA_04_impact_splash.png","STATE","B04","full-cut-only","Impact splash overlay where the curtain meets the pool.",
     "Overlay: a splash crown of 14 droplets and spray lines fanning out each side of an impact point, flat #E4E4E4 and ink outline. Nothing else.",
     "900x400","450x200","IMPACT_POINT (450,190)","Symmetric fan, droplets distinct.",layer="z6",refs="NIA-02")
prop("NIA-06","assets/sci/NIA_06_zoom_scale.png","ART","B04","full-cut-only","Zoomed thermometer scale strip: the 0.12 C change, exaggerated and tagged illustrative.",
     "A tall zoom-in thermometer scale strip 200 px wide x 600 px tall, a magnifier-style circle frame, 12 fine ticks (every 0.01 C) with every fifth tick longer. No numbers.",
     "400x1200","200x600","TICK_0 at bottom; 12 ticks to the top","Ticks even; magnifier circle closed; no numbers.",layer="z17")

prop("CAV-01","assets/sci/CAV_01_spoon_closeup.png","ART","B06","60s","Spoon close-up plate for cavitation (spoon moving through water).",
     "A close-up cutaway of water (flat #E4E4E4 rectangle 620x420 px with a straight surface line) and a spoon bowl moving to the RIGHT seen from the side (the bowl as a 2:1 oval, handle going up and out of the water), with 3 horizontal speed lines behind it. No bubbles in this layer.",
     "1400x900","700x450","SPOON_BOWL_TRAILING_EDGE (left edge of the bowl) at (250,260)","Spoon moves to the right; bubbles absent (they are CAV-02); speed lines behind the bowl.",layer="z14",refs="SPN-01")
prop("CAV-02","assets/sci/CAV_02_bubbles.png","STATE","B06","60s","Vapor bubbles on the low-pressure side of the moving spoon (trailing edge).",
     "Overlay only: 11 small bubbles of varying size (circle outlines, white fill, 8 to 34 px) clustered in a thin wake directly BEHIND the left (trailing) edge of the spoon bowl, plus 2 bubbles at the bowl tip; none in front of the bowl and none at the bottom of the container.",
     "700x450","same as CAV-01","CLUSTER ORIGIN = SPOON_BOWL_TRAILING_EDGE (250,260), spread to x=90","All bubbles are behind the trailing edge (low-pressure region), none ahead of the bowl or on the container floor.",layer="z18",refs="CAV-01")
prop("CAV-03","assets/sci/CAV_03_heated_pot.png","ART","B06","60s","Comparison panel: heat-driven boiling (pot on a flame, bubbles rising from the heated bottom).",
     "A pot of water on a flame in side view: pot 300x240 px, flat #E4E4E4 water, a red #D7263D flame (3 teardrop shapes) under the pot, 9 bubbles (circle outlines) rising from the pot bottom to the surface, 4 short steam wisps. Red only on the flame.",
     "900x800","450x400","FLAME_CENTER (225,330); BOTTOM_BUBBLE_ROW y=290","Flame red, bubbles start at the bottom (heat) not at a moving object; only the flame is red.",layer="z14")
prop("FLM-01","assets/sci/FLM_01_flame.png","ART","B06","60s","Flame icon for the crossed-out flame under the cavitation bubbles.",
     "A single flame icon, three red #D7263D teardrop tongues with ink outline, 80 px tall.",
     "300x300","80x80","BASE (150,300)","Red only; three tongues; no glow.",layer="z19")

# ================================================================ COMPOSITOR VECTOR ELEMENTS
def vec(id, fn, beats, cut, purpose, spec, anchors, checks, kind="COMP", layer="z50", typ="VEC", state=False):
    A(id, fn, "STATE" if state else kind, typ, beats, cut, purpose,
      prompt="Draw in code (SVG/PIL), no image model. "+spec, anchors=anchors, layer=layer,
      out="SVG source + transparent PNG at stage size" if typ=="VEC" else "editable text layer (compositor)", checks=checks)
vec("HEAT-01","assets/vec/HEAT_01_red_ticks.png","B02","60s","Two red ticks leaving the swirl into the water (motion becomes heat).",
    "Two short red #D7263D strokes 24 px long, 7 px weight, round caps, each with a small arrowhead pointing outward from the swirl into the water; wobble +-1.5 px.","ORIGIN at the swirl edge (610,1190); direction 40 and 70 degrees","Red only; two ticks; 1-frame pop.")
vec("HLS-01","assets/vec/HLS_01_heat_out_arrow.png","B05,B06","60s","Wide red wavy 'heat out' arrow rising from the open mug top (state: normal).",
    "A wavy upward red #D7263D arrow 120 px tall, 36 px wide, 7 px stroke, three wave crests, arrowhead at the top.","BASE (660,1100) above the rim","Rises from the open top; wavy; red.")
vec("HLS-02","assets/vec/HLS_02_heat_out_wide.png","B06","60s","Wider 'heat out' arrow after splashing (state change).",
    "Same as HLS-01 but 220 px wide with 5 wave lines fanned out, 7 px stroke.","BASE (660,1100)","Visibly wider than HLS-01 (about 1.8x); same weight.",state=True)
vec("HLS-03","assets/vec/HLS_03_spoon_in_tiny.png","B05","60s","Tiny red 'spoon in' arrow beside the mug (nearly invisible by design).",
    "A very short red arrow 28 px long, 7 px stroke, pointing into the swirl.","TIP at the swirl edge (610,1190)","Much shorter than HLS-01 (roughly one fifth the length).")
vec("DOT-01","assets/vec/DOT_01_tiny_dot.png","B05","60s","Tiny dot near zero on the watt ruler (spoon's power).",
    "A solid black dot 12 px diameter placed 2 px above the ruler zero.","ZERO of RUL-01","Dot is far below the 100 W tick.")
vec("RDC-01","assets/vec/RDC_01_red_circle.png","B03,B05","60s","Red callout circle: pops in one frame and holds.",
    "A hand-wobbled red #D7263D ellipse, no fill, 7 px stroke, parameterised by center and size; path wobble +-2 px.","center on the referent (700 W tick; dot)","GFX-004: red pixel count in the ROI goes from 0 to >200 in one frame and the next two frames stay within +-5 percent.")
vec("BRK-01","assets/vec/BRK_01_red_gap_bracket.png","B03","60s","Red bracket marking the 80-degree gap on the temperature ruler.",
    "A vertical red #D7263D bracket 7 px stroke spanning y of 20 C to 100 C on THR-01, to the right of the ticks.","spans THR-01 ticks 20..100","Spans exactly the two end ticks.")
vec("ARR-01","assets/vec/ARR_01_leader_arrow.png","B03,B04,B06","60s","Black leader arrow with a curve, used for labels.",
    "Black curved leader line 7 px with a small open arrowhead; length parameter.","from label to referent","Same stroke weight; arrowhead open.")
vec("STR-01","assets/vec/STR_01_red_strike.png","B01","60s","Red strike across BOIL (the early verdict).",
    "A single red #D7263D straight strike line 7 px through the center of the word layer 'BOIL', 8 px longer each side.","centered on TXT-02","Draws on in 4-8 frames or pops in 1 frame per the rules; wobble +-1.5 px.")
vec("XOUT-01","assets/vec/XOUT_01_red_x.png","B06","60s","Red cross over the flame (heat is not the cause of these bubbles).",
    "Two crossing red strokes 7 px, 70 px square.","over FLM-01","Pops in 1 frame; red.")
vec("MSK-01","assets/vec/MSK_01_mug_clip.png","B02,B05,B06","60s","Alpha clip mask equal to the mug's inner shape (clips water and spoon).",
    "Filled path equal to the inner outline of MUG-01, 3 px inset, hard edge.","same coordinates as MUG-01","Water never draws outside the inner walls.",kind="COMP",layer="mask")
vec("EXP-01","assets/vec/EXP_01_triptych_plate.png","B07","full-cut-only","Three-panel plate for STIR / DIP / NOTHING (dividers).",
    "Three equal vertical panels 1080x810 stage canvas split by two 7 px black vertical dividers at x=360 and x=720, pure white background #FFFFFF.","panel centers x=180, 540, 900","Dividers straight, equal widths.",kind="COMP",layer="z0")
vec("EXP-02","assets/vec/EXP_02_dip_arrow.png","B07","full-cut-only","Up-down double arrow for the DIP panel.",
    "A black vertical double-headed arrow 90 px tall, 7 px stroke.","above the DIP mug","Heads symmetric.",kind="COMP")
vec("CHT-01","assets/vec/CHT_01_cooling_graph.png","B07","full-cut-only","Schematic cooling graph (illustrative): three nearly identical decaying curves, dip slightly lower.",
    "Axes 7 px (x labelled time, y temperature as text layers); three exponential-decay curves from the same start point; STIR and NOTHING overlap within 2 px, DIP ends 6 px lower; stroke 7 px, curve colors ink / #848484 / #C4C4C4. Tagged 'illustrative' via TXT-14. Drawn from a formula T = T_room + (T0-T_room) exp(-t/tau), NOT from data.","panel 1080x810, origin (140,700)","Curves start together; ends differ by under 6 px; the illustrative tag is present.")
vec("SUG-01","assets/vec/SUG_01_sugar_cube.png","B08","60s","Sugar cube (isometric-free flat square with 3 dot grains).",
    "A 34 px square, 7 px stroke, white fill, three 4 px grain dots; flat.","at the CHR-P13 pinch","Square, flat, three dots.",kind="ART",layer="z25")
vec("SUG-02","assets/vec/SUG_02_cube_half.png","B08","60s","Sugar cube half dissolved (state).",
    "Same cube drawn 60 percent size with a crumbled right edge and 3 loose grain dots below it.","above the waterline then in water","Smaller than SUG-01; crumbled edge.",state=True,layer="z25")
vec("SUG-03","assets/vec/SUG_03_crumbs.png","B08","60s","Sugar crumbs near the spoon (state).",
    "Five 4-6 px grain dots clustered near the bowl; no cube outline.","at the spoon bowl","Only grains remain.",state=True,layer="z25")
vec("SUG-04","assets/vec/SUG_04_dissolved.png","B08","60s","Dissolved: two faint grey swirl marks (state).",
    "Two short curved grey #C4C4C4 strokes in the water, no cube, no grains.","in the water at the bowl","No cube or grains remain.",state=True,layer="z25")

# ================================================================ TEXT LAYERS
TXT_FONT = ("All-caps rounded hand-printed monoline face, same stroke weight as the ink (7 px at 1080 wide), a licensed face the owner picks (candidate: an OFL hand-print caps face; do NOT use a font that imitates the source channel's exact lettering). ")
def txt(id, text, beats, cut, anchor, note="", color="ink"):
    A(id, f"text/{id}.txt", "COMP", "TEXT", beats, cut, f"Text layer: {text}",
      prompt=TXT_FONT+f"String: {text}. Colour {color}. Editable layer, never baked.", anchors=anchor, layer="z60 (above all art)",
      out="editable text layer in the compositor (no PNG)", checks=("Text equals the narration/number checked in section 2; "+note) if note else "Text equals the narration/number checked in section 2; baseline 7 px weight; readable at 320 px width.")
txt("TXT-01","BOIL BY STIRRING?","B01","60s","chip at the top (540,160); max 18 characters; pops at f<=6","")
txt("TXT-02","BOIL","B01","60s","word layer inside TXT-01 (x 220..420); STR-01 strikes it","")
txt("TXT-03","W","B02","60s","top of RUL-01 (90,150)")
txt("TXT-04","84 kJ","B03","60s","in the red gap beside THR-01; idealised energy to reach 100 C (see 2.3)")
txt("TXT-05","2 min","B03","60s","beside CLK-01")
txt("TXT-06","700","B03","60s","at the 700 W tick of RUL-01, red #D7263D",color="red")
txt("TXT-07","100","B03","60s","below the first bulb of seven")
txt("TXT-08","+0.12 C (idealized)","B04","full-cut-only","beside NIA-03 cup, a book estimate for a 51 m fall; tag 'idealized'")
txt("TXT-09","< 1 W","B05","60s","beside DOT-01; a rough estimate (book 1e-7 W, my 7 mW), shown only as '< 1 W'")
txt("TXT-10","TENS OF THOUSANDS / S (BOOK'S ESTIMATE)","B06","60s","above SPN-04 (the book's figure; see correction C4)")
txt("TXT-11","LOW PRESSURE","B06","60s","on the same frame as CAV-02 bubbles pop")
txt("TXT-12","NOT BOILING","B06","60s","on the CAV-02 bubbles, same frame as the crossed flame")
txt("TXT-13","STIR / DIP / NOTHING","B07","full-cut-only","three labels, one above each mug in EXP-01")
txt("TXT-14","ILLUSTRATIVE","B04,B07","full-cut-only","small caps tag on NIA-06, CHT-01, and the three-needle drop")
txt("TXT-15","NO.","B08","60s","next to the mug, red, 1-frame pop",color="red")
txt("TXT-16","ABOUT 51 M","B04","full-cut-only","beside the height bracket on NIA-01 (the Horseshoe figure; sources range 48-57 m)")
txt("TXT-17","20 C / 100 C / 250 ML","B03","60s","scale ends on THR-01 and the jug; typeset as separate layers")
txt("TXT-18","SPOON IN / HEAT OUT","B05","60s","one label per arrow, same frame as each arrow pops")
txt("TXT-19","ABOUT 1 HP","B03","60s","at the horse")
txt("TXT-20","ABOUT 700 W (COOKING POWER)","B03","60s","at the microwave; the output rating, not wall draw (see correction C1)")
vec("NIA-05","assets/vec/NIA_05_height_bracket.png","B04","full-cut-only","Black bracket for the falls height on the wide plate.",
    "A vertical black bracket 7 px stroke spanning crest to pool on NIA-01 on the left side, with two short end caps.","spans y=120..700 at x=170","Bracket ends at crest and pool surface.",kind="COMP")

# ================================================================ SHOT MANIFEST
SHOTS = [
 ("S01",0.0,0.0,"B01","60s","table, mug (water at rest), spoon across rim, dial at 20 C","chip TXT-01 pops at f<=6; alien stands","-","TBL-01,MUG-01,WTR-01,MUG-02,SPN-05,THM-01,THM-02,THM-03,CHR-P01,CHR-X01,TXT-01"),
 ("S02",2.0,2.0,"B01","60s","S01 scene","red strike across BOIL; alien looks down","-","STR-01,TXT-02,CHR-P03"),
 ("S03",3.0,3.0,"B01","60s","S01 scene","alien reaches and takes the spoon; spoon enters; 3 swirl lines appear","spoon leaves the rim","CHR-P04,CHR-P05,CHR-P06,CHR-P07,SPN-01,SPN-02,SPN-03,WTR-02,MSK-01"),
 ("S04",5.0,4.5,"B02","60s","S03 scene","two red ticks leave the swirl and enter the water","-","HEAT-01"),
 ("S05",8.0,7.5,"B02","60s","S03 scene","spoon lifted with drips, needle moves one hair then holds","spoon leaves the water","CHR-P10,SPN-06,CHR-P11,THM-02,CHR-X02"),
 ("S06",10.5,10.5,"B02","60s","S05 scene","watt ruler pops at left and stays to the end","-","RUL-01,TXT-03"),
 ("S07",11.7,12.0,"B03","60s","ruler persists; hard cut to a diagram panel","jug beside the 20-100 C ruler, red gap","stage plate leaves","JUG-01,THR-01,BRK-01,TXT-17,CHR-P02,ARR-01"),
 ("S08",14.2,14.5,"B03","60s","S07","84 kJ label pops in the gap","-","TXT-04"),
 ("S09",17.0,17.5,"B03","60s","S07","clock with 2 min sector pops","-","CLK-01,TXT-05"),
 ("S10",19.0,19.5,"B03","60s","S07","red circle pops on the ruler at 700","-","RDC-01,TXT-06"),
 ("S11",20.5,21.0,"B03","60s","S07 + ruler","seven bulbs pop one per tick; 100 under the first","jug/clock fade out by hard swap","BLB-01,TXT-07"),
 ("S12",23.0,23.5,"B03","60s","ruler + circle","microwave replaces the bulbs at the same height","bulbs leave","MWV-01,TXT-20"),
 ("S13",24.8,25.5,"B03","60s","ruler","horse silhouette at the same height","microwave leaves","HRS-01,TXT-19"),
 ("S14",26.4,"-","B04","full-cut-only","ruler leaves for this cut","hard cut: wide falls with a tiny alien for scale and the height bracket","diagram leaves","NIA-01,NIA-02,NIA-05,TXT-16,CHR-P14,CHR-X03"),
 ("S15",28.2,"-","B04","full-cut-only","S14","close view: cup at the foot; splash on landing; zoom strip with the label +0.12 C (idealized)","wide view leaves","NIA-03,NIA-04,NIA-06,TXT-08,TXT-14"),
 ("S16",29.8,26.5,"B05","60s","ruler returns; stage plate","cut back to the stage; spoon blur; alien stirs hard","falls leaves","TBL-01,MUG-01,WTR-03,MUG-02,SPN-04,CHR-P08,CHR-P09,THM-01,THM-02,THM-03"),
 ("S17",31.2,28.0,"B05","60s","S16","tiny dot near zero on the ruler, far under 700","-","DOT-01,TXT-09"),
 ("S18",33.8,30.5,"B05","60s","S17","dot circled; one bulb pops beside it","-","RDC-01,BLB-01"),
 ("S19",36.5,33.5,"B05","60s","stage + ruler","two arrows on the mug: tiny spoon-in and equal heat-out; needle rises a hair","-","HLS-01,HLS-03,TXT-18,WTR-02,THM-02,CHR-P03,CHR-X06"),
 ("S20",39.7,36.0,"B06","60s","stage","spoon blurs with speed marks; label tens of thousands/s","-","SPN-04,TXT-10,CHR-P08,CHR-P09,WTR-03"),
 ("S21",42.5,39.0,"B06","60s","hard cut to a close-up panel","bubbles pop behind the trailing edge; label LOW PRESSURE on the same frame","stage leaves","CAV-01,CAV-02,TXT-11"),
 ("S22",46.0,42.5,"B06","60s","S21","pot-on-flame comparison panel pops left; NOT BOILING on the bubbles; flame crossed out","-","CAV-03,FLM-01,XOUT-01,TXT-12"),
 ("S23",48.5,44.5,"B06","60s","stage","splash droplets leave the mug; heat-out arrow widens","close-up leaves","WTR-04,HLS-02,WTR-03,TBL-01,MUG-01,MUG-02,CHR-P09"),
 ("S24",52.8,"-","B07","full-cut-only","ruler persists","three identical mugs: STIR / DIP / NOTHING, thermometers at the same height","stage leaves","EXP-01,EXP-02,TXT-13,MUG-01,MUG-02,WTR-01,SPN-01,THM-01,THM-02"),
 ("S25",55.0,"-","B07","full-cut-only","S24","all three needles drop to the same lower mark (dip a hair lower); optional schematic graph inset, tagged illustrative","-","CHT-01,TXT-14"),
 ("S26",57.9,49.0,"B08","60s","stage","cut to the opening mug, needle near 20 C; alien checks the dial","tri-panel leaves","TBL-01,MUG-01,WTR-01,MUG-02,SPN-05,THM-01,THM-02,THM-03,CHR-P11"),
 ("S27",61.0,52.5,"B08","60s","S26","sugar cube drops and dissolves at the spoon","-","CHR-P13,SUG-01,SUG-02,SUG-03,SUG-04,WTR-02,SPN-01"),
 ("S28",64.0,56.0,"B08","60s","S27","red NO. pops once; alien shrugs","-","TXT-15,CHR-P12,CHR-X04,CHR-X05"),
 ("S29",66.4,59.0,"B09","60s","final frame held, no end card, no CTA","-","-","-"),
]

# ---------------------------------------------------------------- checks
IDS = [a["id"] for a in ASSETS]
assert len(IDS) == len(set(IDS)), "duplicate id"
used = collections.Counter()
for s in SHOTS:
    if s[8] != "-":
        for i in s[8].split(","):
            assert i in IDS, ("manifest id missing", i, s[0]); used[i] += 1
unused = [i for i in IDS if used[i] == 0 and next(a for a in ASSETS if a["id"]==i)["kind"] not in ("REF","PIPE") and not i.startswith(("CHR-V","CHR-G"))]
assert not unused, ("unused assets", unused)

for s_ in SHOTS:
    if s_[4]=="60s" and s_[8]!="-":
        for i in s_[8].split(","):
            assert next(a for a in ASSETS if a["id"]==i)["cut"]=="60s", ("60s shot uses full-only asset", s_[0], i)
def cnt(**kw):
    return sum(1 for a in ASSETS if all(a[k]==v for k, v in kw.items()))
kinds = collections.Counter(a["kind"] for a in ASSETS)
typs = collections.Counter(a["typ"] for a in ASSETS)
n60 = sum(1 for a in ASSETS if a["cut"] == "60s")
nfo = sum(1 for a in ASSETS if a["cut"] == "full-cut-only")
gen_total = typs["GEN"]
n_tex = typs["TEXT"]; n_vec = typs["VEC"]

exec(open(os.path.join(HERE, "_md_sections.py")).read())
