"""HIIT After 60 — V3 motion correction (V2 project_v2.py kept). Engine: ../../tools/anim_v3.py + rig.py.
V3: two-leg gait + contralateral arms (rig.RunRig), ground marks at stance-foot speed, red opening headline bar.
python3 project_v3.py [render|test A B|still t1 t2 ...|srt]
Flow per beat: setup -> primary action -> explanation -> reaction/highlight -> reading hold -> next idea.
Compositions: S01-S03 one outdoor stage (no cuts) / S04-S06 one clinic stage / S07-S08 one park stage.
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../tools"))
from anim_v3 import Video3 as Video, INK, CORAL, TEAL, ARIAL
import rig

# Caption text: only machine-verified corrections (see animation/v2/CAPTION_VERIFICATION.md). Index -> shown text.
FIX = {0: "…or", 1: "high-intensity", 2: "", 8: "7", 71: "avoided", 72: "in"}
v = Video("01_HIIT_AFTER_60", "HIIT_After_60_V3_REVIEW.mp4",
          music_chords=[(261.6, 329.6, 392.0), (174.6, 220.0, 261.6), (196.0, 246.9, 293.7), (220.0, 261.6, 329.6)],
          music_seg=2.0, voice="source_audio/voice_v2_paced.wav", word_fix=FIX,
          cue_breaks={50, 59, 62, 73, 82})  # phrase-level cue ends (raw ASR word indices)
w = v.w
G = 1285                                   # ground line (world px)
RUN = (0.6, 20, rig.RunRig(lift=64, arm_amp=26))   # 0.6 s gait cycle (~200 steps/min, interval effort), V3 rig
b2 = w("However") - 0.12                   # outdoor -> concern beat
b4 = w("So") - 0.14                        # cut to clinic
b5 = w("Or", after=16) - 0.14
b6 = w("it", after=21.5) - 0.12
b7 = w("But") - 0.14                       # cut to park
b8 = w("That's") - 0.1
END = v.duration
v.bar = dict(lines=["HIIT AFTER 60", "TOO INTENSE?"], until=w("It's") - 0.1)   # = end of the opening scene

# ---------------- S01-S03 outdoor stage: hook, benefit, concern ----------------
S1 = v.scene("S01", 0, w("It's") - 0.1, [("HIIT", CORAL), (" after 60?", INK)])
S2 = v.scene("S02", S1["end"], b2, [("Good for the ", INK), ("heart", CORAL)])
S3 = v.scene("S03", b2, b4, [("Existing ", INK), ("heart disease?", CORAL)], label="the speaker's concern")
park_y = G - 362 * 1.2
v.group(S1, "park", 0, park_y, 1.2, until=b4, part_opts={"tree": dict(skip=True)})
# hook: hard/easy intensity contrast readable at frame 0, the rest of the pattern builds with "interval training"
BX, BY, BS = 120, 386, 1.2
v.group(S1, "intervals", BX, BY, BS, until=S2["start"] + 0.05, exit="fade", z=2, part_opts={
    "caption": dict(skip=True), "baseline": dict(), "work-1": dict(),
    "rest-1": dict(at=v.aw("intensity"), enter="wipe_up"),
    "work-2": dict(at=w("interval"), enter="wipe_up", sfx="tick"),
    "rest-2": dict(at=w("training."), enter="wipe_up"),
    "work-3": dict(at=w("training.") + 0.22, enter="wipe_up", sfx="tick")})
v.text(S1, "example: hard + easy intervals", 760, 668, 34, (95, 95, 95), at=v.aw("intensity"), enter="fade",
       until=S2["start"] + 0.05, exit="fade", z=3)              # explanation + "not a prescription" boundary in one label
sam_run = v.character(S1, "sam-run-warm", 60, G - 574 * 1.1, 1.1, run=RUN, until=b2, z=5,
                      speed=[(b2 - 0.7, 0.55)])                    # eases off before stopping at "However"
v.marks(sam_run, G)
v.group(S1, "score7", 650, 690, 0.82, at=w("7"), enter="pop", sfx="chime", until=S2["start"] + 0.05, exit="fade",
        z=6, part_opts={"attribution": dict(skip=True)})
v.text(S1, "speaker's rating", 650 + 164 * 0.82, 690 + 300 * 0.82, 36, INK, at=w("7") + 0.15, enter="fade",
       until=S2["start"] + 0.05, exit="fade", z=6)
v.cam(S2["start"] + 0.7, 1.06, 420, 1000, dur=0.7)       # gentle push-in once the hook graphics have cleared
# benefit: the heart grows out of Sam's chest (connected object), then pulses on the two cardio words
chest = (60 + 200 * 1.1, G - 574 * 1.1 + 300 * 1.1)
heart = v.layer(S2, "heart", chest[0] - 200 * 0.12, chest[1] - 200 * 0.12, 0.12, at=w("heart,"), enter="fade",
                until=b4, z=6, sfx="pop", moves=[(w("heart,"), w("heart,") + 0.55, dict(x=760 - 150, y=840 - 150, s=0.75), "out")],
                loop=("pulse", 0.07, [w("cardiovascular"), w("conditioning.")]))
heart["ref_s"] = 0.75
v.layer(S3, "question", -10, -175, 0.42, at=w("concern"), enter="pop", sfx="pop", parent=heart, z=7)
v.character(S3, "sam-concern-concern", 60, G - 592 * 1.1, 1.1, z=5)

# ---------------- S04-S06 clinic stage: supervision, caution, the speaker's advice ----------------
S4 = v.scene("S04", b4, b5, [("Supervised ", CORAL), ("care", INK)], label="the speaker's advice")
S5 = v.scene("S05", b5, b6, [("Why the ", INK), ("caution?", CORAL)])
S6 = v.scene("S06", b6, b7, [("Heart disease? ", INK), ("Avoid it", CORAL)], label="the speaker's view")
v.cam(b4, 1.0, 540, 1000, dur=0.01)                     # hard cut resets the frame
cy = G - 436 * 1.2
v.group(S4, "clinic", 0, cy, 1.2, until=b7, sfx="whoosh", part_opts={
    "plant": dict(skip=True), "window": dict(dx=400, dy=-60)})      # window between the two people, plant removed (V1 overlap)
v.character(S4, "nora-point-explain", -20, G - 592 * 1.1, 1.1, enter="slide_l", at=b4 + 0.1, until=b5, z=5)
v.character(S5, "nora-open-concern", -20, G - 592 * 1.1, 1.1, until=b7, z=5)
v.character(S4, "sam-stand-warm", 650, G - 592 * 1.1, 1.1, until=w("higher"), z=5)
v.character(S5, "sam-concern-concern", 650, G - 592 * 1.1, 1.1, at=w("higher"), until=b7, z=5)
v.cam(b5 + 0.75, 1.08, 528, 1060, dur=0.7)               # reframe on the two people while the risk is explained
v.cam(b6 + 0.6, 1.0, 540, 1000, dur=0.6)                # widen again to make room for the callback graphic
# callback to the hook pattern: the same hard/easy bars, dimmed when the speaker advises avoiding HIIT with heart disease
v.group(S6, "intervals", 540 - 350 * 0.72, 430 - 28 * 0.72, 0.72, at=b6 + 0.15, enter="wipe_up", z=3,
        part_opts={"caption": dict(skip=True)},
        moves=[(w("avoided"), w("avoided") + 0.6, dict(o=0.22), "out")])

# ---------------- S07-S08 park stage: endurance for normal patients, verdict ----------------
S7 = v.scene("S07", b7, b8, [("Endurance", CORAL), (" + stamina", INK)], label="for normal patients")
S8 = v.scene("S08", b8, END + 0.1, [("Speaker's rating: ", INK), ("7/10", CORAL)])
v.group(S7, "park", 0, park_y, 1.2, until=END + 0.1, sfx="whoosh")
v.marks(v.character(S7, "sam-run-warm", -40, G - 574 * 1.1, 1.1, run=RUN, until=b8, z=5,
                    moves=[(b7, b8, dict(x=230), "linear")]), G)        # runs into the frame: travel, not a static bob
v.character(S8, "sam-stand-warm", 230, G - 592 * 1.1, 1.1, until=END + 0.1, z=5)
v.group(S7, "stopwatch", 690, 520, 0.7, at=w("endurance"), enter="pop", sfx="pop", until=b8, exit="fade", z=6,
        part_opts={"hands": dict(loop=("spin", 90), pivot=v.part_center("stopwatch", "dial"))})
v.group(S8, "score7", 680, 520, 0.9, at=w("7", after=29), enter="pop", sfx="chime", until=END + 0.1, z=6,
        part_opts={"attribution": dict(skip=True)})

print("timing", round(v.bar["until"], 3), round(b2, 3), round(b7, 3), round(b8, 3), file=sys.stderr)
if __name__ == "__main__":
    v.main(sys.argv)
