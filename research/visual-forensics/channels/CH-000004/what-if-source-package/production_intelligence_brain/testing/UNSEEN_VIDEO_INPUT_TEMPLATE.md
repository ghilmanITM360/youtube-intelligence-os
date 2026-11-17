# Unseen Reference Video Input — Test Template (Mode B)

Fill in every field. See `GENERALIZATION_TEST_PROTOCOL.md` Mode B. Complete step 1 (blind prediction) fully and record it **before** touching step 2 (forensic analysis) — do not look ahead.

## Input

- **Video filename:** `<filename>`
- **Video SHA-256:** `<sha256 of the video file>`
- **Source/provenance:** `<where this video came from>`
- **Date received:** `<YYYY-MM-DD>`
- **Narration script or early evidence available for the blind prediction:** `<paste what was available before forensic analysis>`

## Training overlap check

- [ ] Confirmed `Video SHA-256` above does not match any `SHA256` value in `SOURCE_VIDEO_INDEX.csv`.

## Step 1 — Blind prediction (frozen v1.0.0 brain artifacts only, no full-video viewing yet)

Same 10 outputs as Mode A, produced from the narration/early evidence only:

1. Sentence segmentation
2. Key concepts
3. Visual beat plan
4. Shot plan
5. State plan
6. Asset requirements
7. Motion decisions
8. Audio-anchor decisions
9. CapCut vs. I2V decisions
10. Reconstruction plan

**Freeze this prediction (timestamp it) before proceeding to step 2.**

- **Prediction frozen at:** `<ISO 8601 timestamp>`

## Step 2 — Independent forensic analysis of the full unseen video

Same methodology used to build the original 14-video corpus: shots, states, motions, assets, audio events, AV sync — produced independently of the step-1 prediction.

## Step 3 — Comparison

Score against every metric in `GENERALIZATION_TEST_PROTOCOL.md` §Metrics. Record quantitative + qualitative results in a `TEST_RESULT_SCHEMA.json`-conformant file under `testing/results/`.

The frozen v1.0.0 brain is not modified as part of this test.
