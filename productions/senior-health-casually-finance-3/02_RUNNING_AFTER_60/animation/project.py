"""Running After 60 — editable animation project (scene/layer/keyframe data). Engine: ../../tools/anim.py
python3 project.py [render|test A B|still t1 t2 ...]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../tools"))
from anim import Video, INK, CORAL, TEAL

v = Video("02_RUNNING_AFTER_60", "Running_After_60_V1_REVIEW.mp4",
          music_chords=[(196.0, 246.9, 293.7), (146.8, 185.0, 220.0), (164.8, 196.0, 246.9), (130.8, 164.8, 196.0)],
          music_seg=2.2)
w = v.w
# ASR-uncertain, medically material wording (R3, R7): amber, verbatim, never silently corrected.
v.amber_spans = [(w("muscular"), w("system.", end=True)), (w("extraction"), w("blood", end=True))]

SAM = dict(x=20, y=640, s=1.3)
RUN = dict(x=120, y=600, s=1.3, loop=("bob", 7, 0.42))


def park(S, t0, t1):  # path/grass fixed, tree drifts left: runner stays in place, feet never slide
    v.group(S, "park", 20, 960, 1.15, part_opts={"tree": dict(moves=[(t0, t1, dict(x=20 - 28 * (t1 - t0)))])})


S = v.scene("S01", 0, 2.7, [("Running", CORAL), (" after 60?", INK)])
park(S, 0, 4.64)
v.layer(S, "sam-run-warm", **RUN)
v.layer(S, "score7", 650, 380, 1.0, at=w("7"), enter="pop", sfx="chime")

S = v.scene("S02", 2.7, 4.64, [("A very ", INK), ("good", CORAL), (" exercise", INK)])
park(S, 0, 4.64)
v.layer(S, "sam-run-warm", **RUN)
v.layer(S, "heart", 660, 400, 0.8, at=w("good"), enter="pop", sfx="pop")

S = v.scene("S03", 4.64, 11.36, [("Knees", CORAL), (" and ", INK), ("ankles?", CORAL)], cam=(1.0, 1.06))
v.layer(S, "sam-concern-concern", **SAM)
v.group(S, "joint", 640, 480, 0.9, at=w("problems"), enter="pop", sfx="pop",
        part_opts={"ring": dict(at=w("knees,"), enter="pop", loop=("pulse", 0.05, [w("knees,") + 0.4]))})
v.layer(S, "shoe", 660, 1000, 0.7, at=w("ankles"), enter="rise", sfx="soft")

S = v.scene("S04", 11.36, 14.42, [("In ", INK), ("moderation", CORAL)], cam=(1.0, 1.03))
v.layer(S, "nora-open-explain", 40, 620, 1.3)
v.group(S, "stopwatch", 650, 560, 0.85, at=w("provided"), enter="pop", sfx="pop",
        part_opts={"hands": dict(loop=("spin", 90), pivot=v.part_center("stopwatch", "dial"))})

S = v.scene("S05", 14.42, 19.66, [("Speaker's limit: ", INK), ("3x a week", CORAL)], cam=(1.0, 1.05))
v.layer(S, "nora-point-concern", 30, 700, 1.25)
v.group(S, "calendar", 520, 520, 1.25, at=w("not"), enter="pop", sfx="pop",
        part_opts={"days": dict(at=w("3"), enter="wipe", sfx="tick"), "note": dict(at=w("week"), enter="rise")})
v.layer(S, "shoe", 660, 1060, 0.6, at=w("distance"), enter="rise", sfx="soft")

S = v.scene("S06", 19.66, 24.04, [("With a ", INK), ("normal heart", CORAL)], cam=(1.0, 1.04))
v.layer(S, "sam-stand-warm", **SAM)
v.layer(S, "heart", 640, 560, 0.95, at=w("normal"), enter="pop", sfx="pop", loop=("pulse", 0.06, [w("cardiac")]))

S = v.scene("S07", 24.04, 28.44, [("Oxygen", TEAL), (" and the ", INK), ("heart", CORAL)], cam=(1.0, 1.04))
v.group(S, "lungs", 60, 560, 1.05, part_opts={"oxygen": dict(at=w("oxygen"), enter="pop", sfx="pop")})
v.layer(S, "heart", 650, 640, 0.85, at=w("maximum"), enter="pop", sfx="pop")
v.layer(S, "arrow", 380, 960, 0.75, at=w("extraction"), enter="wipe", sfx="soft")

S = v.scene("S08", 28.44, v.duration, [("Endurance", CORAL), (" + stamina", INK)], cam=(1.0, 1.03))
park(S, 28.44, v.duration)
v.layer(S, "sam-run-warm", **RUN)
v.group(S, "stopwatch", 650, 400, 0.8, at=w("endurance"), enter="pop", sfx="pop",
        part_opts={"hands": dict(loop=("spin", 120), pivot=v.part_center("stopwatch", "dial"))})

if __name__ == "__main__":
    v.main(sys.argv)
