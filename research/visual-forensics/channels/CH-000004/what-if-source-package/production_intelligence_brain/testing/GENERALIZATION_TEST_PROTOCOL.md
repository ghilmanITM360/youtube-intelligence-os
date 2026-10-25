# Generalization Test Protocol

Purpose: test whether the frozen v1.0.0 brain **generalizes** the production grammar it learned from the 14-video corpus, rather than memorizing it. A passing test on the 14 training videos proves nothing here — the corpus must be genuinely unseen.

**Do not run this protocol against any of the 14 source videos.** See §"No training leakage" below.

**Never modify the frozen v1.0.0 brain as part of running this protocol.** Test outputs are recorded in `testing/`, never merged back into `01_master_data/`, `02_production_dna/`, `03_reconstruction_system/`, `04_patterns/`, or `05_blueprints/`.

## Two modes

### Mode A — Unseen Script

Input: a new narration script only (no reference video). Fill in `UNSEEN_SCRIPT_INPUT_TEMPLATE.md`.

Given only that script, the brain (using only its frozen artifacts — `02_production_dna/`, `03_reconstruction_system/`, `04_patterns/`, `05_blueprints/` — never the original 14 source videos) must produce:

1. Sentence segmentation
2. Key concepts
3. Visual beat plan
4. Shot plan
5. State plan
6. Asset requirements
7. Motion decisions
8. Audio-anchor decisions
9. CapCut vs. I2V decisions (per `03_reconstruction_system/DECISION_RULES.md`)
10. Reconstruction plan

This tests whether the production grammar was actually learned, independent of any specific reference footage.

### Mode B — Unseen Reference Video

Input: an unseen reference video. Fill in `UNSEEN_VIDEO_INPUT_TEMPLATE.md`.

Procedure, in order:

1. **Freeze a blind prediction first** — using only the narration/script or early evidence (e.g. first few seconds), predict the production grammar (shot plan, state plan, motion decisions, etc.) the same way Mode A does. Record the prediction before looking at the rest of the video.
2. **Then independently forensically analyze** the unseen video (same methodology used to build the original 14-video corpus: shots, states, motions, assets, audio events, AV sync).
3. **Compare** predicted production grammar vs. observed production grammar using the metrics below.

The frozen v1.0.0 brain is not modified during this comparison.

## Metrics

Quantitative:
- Shot-count error
- State-count error
- Visual-change timing error
- Motion-decision precision
- Motion-decision recall
- Asset-category match rate
- CapCut-vs-I2V decision agreement rate
- Keyword/visual-anchor timing error
- Static-hold duration error
- Transition-type agreement

Qualitative (reviewed by a human, recorded as free text in the test result):
- Visual style fidelity
- Production logic soundness
- Over-animation
- Under-animation
- Invented behavior (anything the brain asserts with no basis in its frozen artifacts)
- Reference fidelity (Mode B only)

## No training leakage

Before running any test:

1. Compute `TEST_INPUT_SHA256` for the candidate video (or script, script-only mode).
2. Compare it against every `SHA256` value in `SOURCE_VIDEO_INDEX.csv`.
3. If it matches any row, the input is **not** eligible — pick different material.
4. Record the computed hash and the non-match check result in the test result (see `TEST_RESULT_SCHEMA.json`, field `training_overlap_check`).

## Recording results

Every test run produces one JSON file conforming to `TEST_RESULT_SCHEMA.json`, stored under `testing/results/` (created on first real run — does not exist yet, since no unseen test has been executed).

## Status

No unseen test has been executed yet. This protocol is ready; awaiting a genuinely unseen script or reference video from the user.
