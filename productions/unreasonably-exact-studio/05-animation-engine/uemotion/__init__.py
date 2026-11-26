"""uemotion: deterministic, time-function based 2D/2.5D motion primitives for the Lunar Laser Ranging short.

Every drawn element is a pure function of time (no frame-to-frame state), so any clip can be re-rendered at any fps,
at any --scale, in any order, in parallel. Three clocks are kept separate (see timeline.ClockSet):
narration_t (seconds on the master voice recording), anim_t (clip-local time), model_t (the physical light-travel clock).
Import submodules explicitly: from uemotion import canvas, easing, ...
"""
