"""Swimming After 60 — editable animation project (scene/layer/keyframe data). Engine: ../../tools/anim.py
python3 project.py [render|test A B|still t1 t2 ...]"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../tools"))
from anim import Video, INK, CORAL, TEAL

v = Video("03_SWIMMING_AFTER_60", "Swimming_After_60_V1_REVIEW.mp4",
          music_chords=[(174.6, 220.0, 261.6), (130.8, 164.8, 196.0), (146.8, 174.6, 220.0), (116.5, 146.8, 174.6)],
          music_seg=2.4)
w = v.w
v.caption_overrides = {round(w("9"), 2): "9.5", round(w(".5"), 2): "",  # ASR splits "9.5" into two tokens
                       round(w("9", after=15), 2): "9.5", round(w(".5", after=15), 2): ""}
# Contradictory joints sentence (MEDICAL_CLAIMS S5, same in both ASR runs): verbatim, amber.
v.amber_spans = [(w("without"), w("joints", after=13.5, end=True))]

# Swimmer limbs: small swings about shoulder/hip only (straight-limb rotation, no elbow bending).
SHOULDER_F, SHOULDER_R, HIP_F, HIP_R = (215, 160), (228, 135), (432, 182), (432, 160)


def pool_swim(S, px, py, ps, ss, sx=None):
    """Pool + swimmer with the waterline through the swimmer's torso: water part drawn again at 55%
    opacity in front, so the submerged limbs read as under water (fixes the 'floating on top' state)."""
    water_top = py + 144 * ps
    sy = water_top - 160 * ss
    sx = px + 25 * ps if sx is None else sx  # hand inside pool wall, feet clear of ladder
    v.layer(S, "pool", px, py, ps, part="water")
    v.layer(S, "pool", px, py, ps, part="ladder")
    v.group(S, "june-swim-warm", sx, sy, ss, part_opts={  # no whole-body bob: limbs must stay attached
        "front-arm": dict(pivot=SHOULDER_F, loop=("swing", 6, 1.2)),
        "rear-arm": dict(pivot=SHOULDER_R, loop=("swing", -5, 1.2)),
        "front-leg": dict(pivot=HIP_F, loop=("swing", 4, 0.5)),
        "rear-leg": dict(pivot=HIP_R, loop=("swing", -4, 0.5))})
    v.layer(S, "pool", px, py, ps, part="water", o=0.55)
    v.layer(S, "pool", px, py, ps, part="ripples", moves=[(S["start"], S["end"], dict(x=px - 12 * (S["end"] - S["start"])))])
    v.layer(S, "pool", px, py, ps, part="edge")


S = v.scene("S01", 0, 2.88, [("Swimming", TEAL), (" after 60?", INK)])
pool_swim(S, 45, 760, 1.1, 1.1)
v.layer(S, "score95", 660, 360, 0.95, at=w("9"), enter="pop", sfx="chime")

S = v.scene("S02", 2.88, 5.92, [("Heart", CORAL), (" fitness", INK)], cam=(1.0, 1.04))
pool_swim(S, 45, 760, 1.1, 1.1)
v.layer(S, "heart", 640, 330, 0.85, at=w("heart"), enter="pop", sfx="pop")

S = v.scene("S03", 5.92, 10.16, [("Fitness", CORAL), (" + ", INK), ("endurance", TEAL)], cam=(1.0, 1.05))
v.layer(S, "june-stand-warm", 40, 640, 1.3)
v.layer(S, "heart", 640, 330, 0.85, moves=[(5.95, 6.4, dict(x=660, y=470, s=0.8))],
        loop=("pulse", 0.06, [w("cardiovascular")]))
v.group(S, "stopwatch", 660, 880, 0.8, at=w("endurance"), enter="pop", sfx="pop",
        part_opts={"hands": dict(loop=("spin", 120), pivot=v.part_center("stopwatch", "dial"))})

S = v.scene("S04", 10.16, 11.88, [("Whole-body", CORAL), (" movement", INK)], cam=(1.0, 1.06), cam_center=(540, 960))
pool_swim(S, 45, 760, 1.1, 1.1)

S = v.scene("S05", 11.88, 14.82, [("Joints ", INK), ("still move", CORAL)], cam=(1.0, 1.03))
pool_swim(S, 150, 470, 0.85, 0.95, sx=165)
v.group(S, "joint", 340, 900, 0.85, at=w("joints"), enter="pop", sfx="pop",
        part_opts={"ring": dict(at=w("joints"), enter="pop", loop=("pulse", 0.06, [w("joints", after=13.5)]))})

S = v.scene("S06", 14.82, v.duration, [("Speaker's verdict: ", INK), ("9.5/10", CORAL)], cam=(1.0, 1.02))
v.layer(S, "june-stand-warm", 40, 640, 1.3)
v.layer(S, "score95", 640, 700, 1.1, at=w("give", after=15), enter="pop", sfx="chime")

if __name__ == "__main__":
    v.main(sys.argv)
