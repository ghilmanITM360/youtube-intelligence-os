# Decision engine and held-out test
Model: predict a state's entering class (CUT, POP_IN, POSE, TEXT_SWAP, START, OTHER) from asset type of the state (CH_ character, OBJ_, GFX_, other) plus the previous state's class. Fit on 11 videos (2,923 states). Held out before fitting: 10nEByVLya0, Xkk9GnnJHBg, 7K991LgY3tc, SYSUh-oow6M (828 states). Script: `tools/decision_engine_heldout.py`.

| Result | Value |
|---|---|
| Held-out accuracy | 53.0% |
| Majority baseline (always CUT) | 47.8% |
| Per video | 44.3%, 52.4%, 61.3%, 39.2% |
| Duration error (MAE) vs global median | 0.845 s vs 0.861 s (no real gain) |

Strongest rules (train): after a POP_IN, a prop (OBJ/GFX) state is again POP_IN 61-64%; a character state after POP_IN is CUT 73%; plain CUT chains continue CUT 56%.

Verdict: the model is only about 5 points better than a constant guess, and the duration rule adds nothing. Communication-need mapping (number, process, comparison) is NOT built because `narrative_function` is "see report" in 2,148 of 2,195 shots; it would need new labelling. Reliability: low.
