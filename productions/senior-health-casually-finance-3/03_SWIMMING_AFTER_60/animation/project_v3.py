"""Swimming After 60 — V3 motion correction (from project_v2.py; V2 untouched). Engine: ../../tools/anim_v3.py + rig.py.
V3: arms/legs redrawn every frame by rig.SwimRig (alternating crawl, 6-beat kick, water fx at contacts); red opening bar.
python3 project_v3.py [render|test A B|still t1 t2 ...|srt]
One pool stage, no cuts: June swims freestyle across the pool the whole time (parented body: limbs cannot detach);
the explanation builds above the water: heart -> endurance -> whole-body labels -> joint question -> rating.
"best exercise" stays the speaker's attributed view; the joints sentence stays verbatim and is framed as a question.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../tools"))
from anim_v3 import Video3 as Video
from anim_v2 import INK, CORAL, TEAL
import rig

# small.en tokens are lower-case/unpunctuated and split "9.5": restore casing/punctuation only (no word changes).
FIX = {0: "Swimming,", 1: "I'll", 4: "9.5", 5: "", 8: "10.", 9: "It's", 18: "heart,", 19: "best", 23: "fitness,",
       27: "endurance,", 32: "body,", 33: "so", 37: "joints,", 42: "joints.", 43: "So", 44: "I'll", 47: "9.5", 48: "",
       51: "10."}
v = Video("03_SWIMMING_AFTER_60", "Swimming_After_60_V3_REVIEW.mp4",
          music_chords=[(174.6, 220.0, 261.6), (130.8, 164.8, 196.0), (146.8, 174.6, 220.0), (116.5, 146.8, 174.6)],
          music_seg=2.4, word_fix=FIX, cue_breaks={8, 14, 18, 23, 27, 32})
w = v.w
END = v.duration
b2, b3 = w("It's") - 0.1, w("best", after=5.5) - 0.12
b4, b5 = w("it", after=9.5) - 0.08, w("so", after=11) - 0.1
b6 = w("So", after=14) - 0.05

S1 = v.scene("S01", 0, b2, [("Swimming", TEAL), (" after 60?", INK)], label="and your heart?")
S2 = v.scene("S02", b2, b3, [("Good for the ", INK), ("heart", CORAL)], label="the speaker's view")
S3 = v.scene("S03", b3, b4, [("Heart fitness", CORAL), (" + ", INK), ("endurance", TEAL)], label="the speaker's view")
S4 = v.scene("S04", b4, b5, [("Whole-body", CORAL), (" movement", INK)])
S5 = v.scene("S05", b5, b6, [("What about the ", INK), ("joints?", CORAL)], label="the speaker's point")
v.bar = dict(lines=["SWIMMING AFTER 60", "HEART BENEFITS?"], until=b2)   # opening hook, ends with sentence 1
S6 = v.scene("S06", b6, END + 0.1, [("Speaker's rating: ", INK), ("9.5/10", CORAL)])

# ---- pool: water drawn again in front at 55% so submerged limbs read as under water
WT = 880                                 # water top (px)
PX, PY, PS = 0, WT - 144 * 1.2, 1.2
v.layer(S1, "pool", PX, PY, PS, part="water", until=END + 0.1, z=0)
v.layer(S1, "pool", PX, PY, PS, part="ladder", until=END + 0.1, z=0)
v.layer(S1, "pool", PX, PY, PS, part="water", o=0.55, until=END + 0.1, z=8)
v.layer(S1, "pool", PX, PY, PS, part="edge", until=END + 0.1, z=9)
v.layer(S1, "pool", PX + 60, PY, PS, part="ripples", until=END + 0.1, z=9,
        moves=[(0, END, dict(x=PX + 60 - 14 * END), "linear")])

# ---- swimmer: invisible root carries travel; rig.SwimRig draws alternating arms + flutter kick each frame
SS = 1.0
SY = WT - 160 * SS                       # waterline through the torso (asset y 160)
root = v.swimmer(S1, "june-swim-warm", 250, SY, SS, per=1.5, rg=rig.SwimRig(), until=END + 0.1,
                 moves=[(0, END, dict(x=90), "linear")])   # swims left (head-first); SwimRig.bounce = gentle rise/fall

# ---- hook: small beating heart above the swimmer (cardio relevance at frame 0), rating on "9.5"
small = v.layer(S1, "heart", 300 - 200 * 0.16, -60 - 200 * 0.16, 0.16, parent=root, until=w("heart,"), z=10,
                loop=("pulse", 0.14, [i * 0.55 for i in range(10)]))
v.group(S1, "score95", 700, 470, 0.8, at=w("9.5"), enter="pop", sfx="chime", until=b2 + 0.05, exit="fade", z=10,
        part_opts={"attribution": dict(skip=True)})
v.text(S1, "speaker's rating", 700 + 164 * 0.8, 470 + 300 * 0.8, 36, INK, at=w("9.5") + 0.15, enter="fade",
       until=b2 + 0.05, exit="fade", z=10)

# ---- heart: the small heart grows out of its place above the swimmer into the explanation space
th = w("heart,")
hx, hy, _, _, _, _, _ = v.state(small, th)
HX, HY, HS = 760, 600, 0.7
v.layer(S2, "heart", hx, hy, 0.16, at=th, until=b4 + 0.05, exit="fade", z=10, sfx="pop",
        moves=[(th, th + 0.55, dict(x=HX - 200 * HS, y=HY - 200 * HS, s=HS), "out")],
        loop=("pulse", 0.07, [w("cardiovascular")]))
v.group(S3, "stopwatch", 300, 600 - 200 * 0.6, 0.6, at=w("best", after=7.5), enter="pop", sfx="pop", until=b4 + 0.05,
        exit="fade", z=10, part_opts={"hands": dict(loop=("spin", 90), pivot=v.part_center("stopwatch", "dial"))})

# ---- whole body: labels attached to the moving swimmer, one per word, camera closer on the swimmer
for word, txt, dx, dy in (("uses", "arms", 70, 270), ("whole", "legs", 560, 290), ("body,", "core", 330, 40)):
    v.text(S4, txt, 0, 0, 44, TEAL, at=w(word), enter="pop", until=b5 + 0.05, exit="fade", z=11, parent=root)
    v.layers[-1].update(x=dx - v.layers[-1]["pivot"][0], y=dy - v.layers[-1]["pivot"][1])
v.cam(b4 + 0.5, 1.1, 480, 920, dur=0.5)
v.cam(b5 + 0.5, 1.0, 540, 900, dur=0.5)

# ---- joints: verbatim sentence, neutral visual (healthy joint, highlight on each spoken "joints")
v.group(S5, "joint", 540 - 200 * 0.75, 640 - 200 * 0.75, 0.75, at=b5 + 0.1, enter="pop", sfx="soft",
        until=b6 + 0.05, exit="fade", z=10,
        part_opts={"ring": dict(loop=("pulse", 0.08, [w("joints,"), w("joints.")]))})

# ---- rating returns
v.group(S6, "score95", 540 - 164 * 1.0, 480, 1.0, at=w("9.5", after=15), enter="pop", sfx="chime", until=END + 0.1,
        z=10, part_opts={"attribution": dict(skip=True)})

if __name__ == "__main__":
    v.main(sys.argv)
