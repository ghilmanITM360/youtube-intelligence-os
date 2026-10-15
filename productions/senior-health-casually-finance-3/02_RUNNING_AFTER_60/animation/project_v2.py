"""Running After 60 — V2 editable animation project. Engine: ../../tools/anim_v2.py (V1 project.py/anim.py untouched).
python3 project_v2.py [render|test A B|still t1 t2 ...|srt]
One park stage throughout (no hard cuts): Sam runs -> stops on the caution -> Nora joins for moderation ->
heart/lungs/O2 build out of Sam's chest -> heart returns to his chest and he runs on. Original audio, no pacing edit.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../tools"))
from anim_v2 import Video, INK, CORAL, TEAL

# Machine-verified caption corrections (animation/v2/CAPTION_VERIFICATION.md). Index -> shown text.
FIX = {28: "musculoskeletal", 29: "", 76: "VO₂", 83: "", 84: "blood,"}
v = Video("02_RUNNING_AFTER_60", "Running_After_60_V2_REVIEW.mp4",
          music_chords=[(196.0, 246.9, 293.7), (146.8, 185.0, 220.0), (164.8, 196.0, 246.9), (130.8, 164.8, 196.0)],
          music_seg=2.2, word_fix=FIX, cue_breaks={16, 20, 24, 42, 49, 75, 80, 84, 88})
w = v.w
G, SC = 1285, 1.1
RUN = (0.6, 20)
END = v.duration
b2, b3 = w("Running", after=2.5) - 0.1, w("However,") - 0.1
b4, b5 = w("Running", after=11) - 0.15, w("not") - 0.12
b6, b7 = w("So") - 0.12, w("Running", after=24) - 0.1
b8 = w("and", after=28.3) - 0.05
SAMX = 60
chest = lambda x: (x + 200 * SC, G - 592 * SC + 300 * SC)

S1 = v.scene("S01", 0, b2, [("Running", CORAL), (" after 60?", INK)], label="and your heart?")
S2 = v.scene("S02", b2, b3, [("A very ", INK), ("good", CORAL), (" exercise", INK)])
S3 = v.scene("S03", b3, b4, [("Knees", CORAL), (" and ", INK), ("ankles?", CORAL)], label="the speaker's caution")
S4 = v.scene("S04", b4, b5, [("In ", INK), ("moderation", CORAL)])
S5 = v.scene("S05", b5, b6, [("3 runs ", CORAL), ("a week?", INK)], label="the speaker's suggestion")
S6 = v.scene("S06", b6, b7, [("With a ", INK), ("normal heart", CORAL)], label="the speaker's view")
S7 = v.scene("S07", b7, b8, [("Oxygen", TEAL), (" + ", INK), ("heart", CORAL)])
S8 = v.scene("S08", b8, END + 0.1, [("Endurance", CORAL), (" + stamina", INK)])

v.group(S1, "park", 0, G - 362 * 1.2, 1.2, until=END + 0.1, part_opts={
    "tree": dict(dx=330, until=b3, moves=[(0, b3, dict(x=-820), "linear")])})  # parallax: passes behind Sam, leaves frame
v.group(S8, "park", 400, G - 362 * 1.2, 1.2, part_opts={"path": dict(skip=True), "grass": dict(skip=True),
        "tree": dict(at=b8 + 0.45, until=END + 0.1, moves=[(b8 + 0.45, END, dict(x=40), "linear")])})

# ---- hook + benefit: Sam already running at frame 0, a small heart beating on his chest = the heart question
sam_run = v.character(S1, "sam-run-warm", -20, G - 574 * SC, SC, run=RUN, until=b3, z=5,
                      moves=[(0, b3 - 0.3, dict(x=SAMX), "out")], speed=[(b3 - 0.8, 0.55)])
v.layer(S1, "heart", 200 * SC - 200 * 0.16, 300 * SC - 200 * 0.16, 0.16, parent=sam_run, z=6, until=b3,
        loop=("pulse", 0.12, [0.0, 0.55, 1.1, 1.65, 2.2, 2.75, 3.3]))
v.group(S1, "score7", 640, 560, 0.82, at=w("7"), enter="pop", sfx="chime", until=b2 + 0.05, exit="fade", z=6,
        part_opts={"attribution": dict(skip=True)})
v.text(S1, "speaker's rating", 640 + 164 * 0.82, 560 + 300 * 0.82, 36, INK, at=w("7") + 0.15, enter="fade",
       until=b2 + 0.05, exit="fade", z=6)
v.cam(b2 + 0.6, 1.05, 400, 1050, dur=0.6)

# ---- caution: Sam stops; a ring on his own knees -> ankles -> whole legs; a joint close-up linked by an arrow
sam = v.character(S3, "sam-concern-concern", SAMX, G - 592 * SC, SC, until=b4, z=5)
ring = v.layer(S3, "joint", 220 - 202 * 0.6, 522 - 201 * 0.6, 0.6, part="ring", parent=sam, at=w("knees,"),
               enter="pop", sfx="pop", z=7, moves=[(w("ankles"), w("ankles") + 0.4, dict(y=621 - 201 * 0.6), "out"),
                                                   (w("musculoskeletal"), w("musculoskeletal") + 0.5,
                                                    dict(x=220 - 202 * 1.45, y=560 - 201 * 1.45, s=1.45), "out")])
v.group(S3, "joint", 620, 560, 1.0, at=w("problems"), enter="pop", sfx="soft", z=6, until=b4, exit="fade",
        part_opts={"ring": dict(skip=True)})
v.layer(S3, "arrow", 330, 852, 1.0, at=w("knees,") + 0.05, enter="wipe", z=6, until=b4, exit="fade")
v.text(S3, "bones · joints · muscles", 760, 1080, 40, TEAL, at=w("musculoskeletal"), enter="fade", z=7,
       until=b4, exit="fade")
v.cam(b3 + 0.5, 1.0, 540, 1000, dur=0.5)                   # widen so legs, ring and close-up all stay in frame

# ---- moderation: Nora joins from her side; the calendar shows the SPEAKER'S suggestion, not a universal cap
v.character(S4, "sam-stand-warm", SAMX, G - 592 * SC, SC, until=b8 + 0.45, z=5)
v.character(S4, "nora-open-explain", 600, G - 592 * SC, SC, at=w("provided"), enter="slide_r", until=b6, exit="fade", z=5)
v.group(S5, "calendar", 540 - 200 * 0.9, 420, 0.9, at=b5 + 0.1, enter="pop", sfx="pop", z=6, until=b6, exit="fade",
        part_opts={"note": dict(skip=True), "days": dict(at=w("3"), enter="wipe", sfx="tick")})
v.layer(S5, "shoe", 430, 700, 0.45, at=w("distance"), enter="fade", z=6, until=b6, exit="fade", sfx="soft",
        moves=[(w("distance") + 0.1, w("moderate,"), dict(x=520), "out")])   # a short, moderate distance

# ---- normal heart -> heart grows out of Sam's chest; VO2: lungs above it, O2 dots travel down into the heart
cx, cy = chest(SAMX)
HX, HY, HS = 720, 800, 0.7
heart = v.layer(S6, "heart", cx - 200 * 0.16, cy - 200 * 0.16, 0.16, at=w("heart,", after=20), enter="fade", sfx="pop",
                until=b8 + 0.55, z=6, loop=("pulse", 0.07, [w("cardiac"), w("blood,")]),
                moves=[(w("heart,", after=20), w("heart,", after=20) + 0.55, dict(x=HX - 200 * HS, y=HY - 200 * HS, s=HS), "out"),
                       (b8, b8 + 0.5, dict(x=cx - 200 * 0.16, y=cy - 200 * 0.16, s=0.16, o=0.0), "inout")])
LX, LY, LS = 720, 560, 0.62
v.group(S7, "lungs", LX - 200 * LS, LY - 200 * LS, LS, at=w("VO₂"), enter="pop", sfx="pop", until=b8 + 0.3, exit="fade",
        z=6, part_opts={"oxygen": dict(skip=True)})
v.layer(S7, "lungs", LX - 200 * LS, LY - 200 * LS, LS, part="oxygen", at=w("oxygen"), enter="fade", z=7,
        until=w("blood,") + 0.4, exit="fade",
        moves=[(w("extraction"), w("blood,"), dict(y=HY - 200 * LS - 30), "inout")])   # O2 moves into the heart
v.cam(b7 + 0.7, 1.08, 640, 860, dur=0.7)                   # push in on the linked diagram
v.cam(b8 + 0.6, 1.0, 540, 1000, dur=0.6)

# ---- endurance: heart returns to his chest, Sam runs on
v.character(S8, "sam-run-warm", SAMX, G - 574 * SC, SC, run=RUN, at=b8 + 0.45, until=END + 0.1, z=5,
            moves=[(b8 + 0.45, END, dict(x=SAMX + 260), "linear")])
v.group(S8, "stopwatch", 680, 520, 0.7, at=w("endurance"), enter="pop", sfx="pop", until=END + 0.1, z=6,
        part_opts={"hands": dict(loop=("spin", 90), pivot=v.part_center("stopwatch", "dial"))})

if __name__ == "__main__":
    v.main(sys.argv)
