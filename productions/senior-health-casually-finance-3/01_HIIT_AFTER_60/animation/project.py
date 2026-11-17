"""HIIT After 60 — editable animation project (scene/layer/keyframe data). Engine: ../../tools/anim.py
python3 project.py [render|test A B|still t1 t2 ...]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../tools"))
from anim import Video, INK, CORAL

v = Video("01_HIIT_AFTER_60", "HIIT_After_60_V1_REVIEW.mp4",
          music_chords=[(261.6, 329.6, 392.0), (174.6, 220.0, 261.6), (196.0, 246.9, 293.7), (220.0, 261.6, 329.6)],
          music_seg=2.0)
w = v.w
# Disputed medical wording (MEDICAL_CLAIMS H5/H6): shown amber, never silently corrected.
v.amber_spans = [(w("mortality"), w("mobility", end=True)), (w("awarded"), w("to", after=22.0, end=True) - 0.2)]
v.caption_overrides = {round(w("awarded"), 2): "avoided/awarded"}  # base vs small.en ASR disagreement at ~21.9 s

SAM = dict(x=20, y=640, s=1.3)  # Sam keeps one stage position across S01-S03/S05 so pose swaps read as continuity

S = v.scene("S01", 0, 3.24, [("HIIT", CORAL), (" after 60?", INK)])
v.group(S, "intervals", 155, 330, 1.1, part_opts={
    "work-1": dict(at=w("high"), enter="rise", sfx="tick"), "rest-1": dict(at=w("intensity"), enter="rise"),
    "work-2": dict(at=w("interval"), enter="rise", sfx="tick"), "rest-2": dict(at=w("training."), enter="rise"),
    "work-3": dict(at=w("training.") + 0.3, enter="rise", sfx="tick")})
v.layer(S, "sam-run-warm", **SAM, loop=("bob", 7, 0.42))
v.layer(S, "score7", 640, 780, 1.0, at=w("seven"), enter="pop", sfx="chime")

S = v.scene("S02", 3.24, 7.72, [("Good for the ", INK), ("heart", CORAL)])
v.layer(S, "sam-run-warm", **SAM, until=w("good"), loop=("bob", 7, 0.42))
v.layer(S, "sam-stand-warm", **SAM, at=w("good"))
v.layer(S, "heart", 640, 470, 0.95, at=w("heart"), enter="pop", sfx="pop", loop=("pulse", 0.06, [w("cardiovascular")]))
v.layer(S, "arrow", 420, 700, 0.8, at=w("conditioning."), enter="wipe", sfx="soft")

S = v.scene("S03", 7.72, 13.36, [("Existing ", INK), ("heart disease?", CORAL)], cam=(1.0, 1.05))
v.layer(S, "sam-concern-concern", **SAM)
v.layer(S, "heart", 640, 470, 0.95, moves=[(7.75, 8.25, dict(x=680, y=800, s=0.75))],
        loop=("pulse", 0.06, [w("cardiovascular", after=11)]))
v.layer(S, "question", 640, 420, 0.65, at=w("concern"), enter="pop", sfx="pop")

S = v.scene("S04", 13.36, 16.2, [("Supervised ", CORAL), ("care", INK)], cam=(1.0, 1.03))
v.group(S, "clinic", 45, 830, 1.1)
v.layer(S, "sam-stand-warm", 560, 640, 1.2)
v.layer(S, "nora-point-explain", 60, 610, 1.2, at=w("So"), enter="slide_l", sfx="pop")

S = v.scene("S05", 16.2, 21.26, [("Risk ", CORAL), ("needs context", INK)], cam=(1.0, 1.06))
v.layer(S, "sam-concern-concern", **SAM)
v.layer(S, "question", 620, 680, 0.85, at=w("avoid"), enter="pop", sfx="pop", loop=("swing", 3, 2.4))

S = v.scene("S06", 21.26, 24.34, [("Not one rule ", INK), ("for everyone", CORAL)])
v.layer(S, "nora-open-concern", 40, 620, 1.3)
v.layer(S, "heart", 640, 700, 0.8, at=w("cardiovascular", after=22), enter="pop", sfx="pop")

S = v.scene("S07", 24.34, 28.9, [("Endurance", CORAL), (" + stamina", INK)], cam=(1.0, 1.04))
v.group(S, "park", 20, 960, 1.15, part_opts={"tree": dict(moves=[(24.34, 28.9, dict(x=-260))])})
v.layer(S, "sam-run-warm", 120, 600, 1.3, loop=("bob", 7, 0.42))
v.group(S, "stopwatch", 660, 400, 0.75, at=w("stamina"), enter="pop", sfx="pop",
        part_opts={"hands": dict(loop=("spin", 120), pivot=v.part_center("stopwatch", "dial"))})

S = v.scene("S08", 28.9, v.duration, [("Speaker's verdict: ", INK), ("7/10", CORAL)], cam=(1.0, 1.02))
v.layer(S, "nora-open-warm", 40, 620, 1.3)
v.layer(S, "score7", 640, 700, 1.1, at=w("giving"), enter="pop", sfx="chime")

if __name__ == "__main__":
    v.main(sys.argv)
