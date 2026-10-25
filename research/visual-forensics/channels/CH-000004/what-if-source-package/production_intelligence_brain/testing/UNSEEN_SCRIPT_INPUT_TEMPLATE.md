# Unseen Script Input — Test Template (Mode A)

Fill in every field before generating predictions. See `GENERALIZATION_TEST_PROTOCOL.md` Mode A.

## Input

- **Script text (verbatim, full):**

  ```
  <paste the full narration script here>
  ```

- **Script SHA-256:** `<sha256 of the exact script text file used>`
- **Source/author:** `<where this script came from — must not be one of the 14 training videos>`
- **Date received:** `<YYYY-MM-DD>`
- **Intended output format (resolution/aspect ratio):** `<must be supplied by the requester — the brain does not assume 1920x1080/16:9>`

## Training overlap check

- [ ] Confirmed this script is not a transcript of any of the 14 source videos in `SOURCE_VIDEO_INDEX.csv`.

## Brain artifacts consulted (frozen v1.0.0 only)

- `02_production_dna/*`
- `03_reconstruction_system/*`
- `04_patterns/*`
- `05_blueprints/*`

The original 14 source videos in `videos/` must NOT be consulted during generation.

## Required outputs (produce all 10, in order)

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

Record the completed outputs plus review notes in a `TEST_RESULT_SCHEMA.json`-conformant file under `testing/results/`.
