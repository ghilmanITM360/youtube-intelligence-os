# Release Metadata Issue — v1.0.0

**Recorded, not fixed.** Per instruction, v1.0.0 was not altered during this
review. This is a release-maintenance item for a separate patch release; it
must not be bundled with Test A work.

## The inconsistency

`releases/production_intelligence_brain-v1.0.0/BRAIN_MANIFEST.json`:

```
project_status    = "COMPLETE_VALIDATED"
release_status    = "PREPARING"
release_frozen_at = null
```

The Test A protocol expected `STATUS = COMPLETE_VALIDATED / FROZEN`. The
release therefore describes itself as still being prepared while being used,
and published by hash, as a frozen artefact.

## Why the first pass proceeded, and why this revision did too

Everything except the two string fields indicates a frozen, validated release:

- `validator/validate_brain.py` returns `RESULT: PASS` with zero failures. Run
  before and after the first pass, and again after this revision.
- Every declared count matches the protocol exactly: 7864 words, 604 sentences,
  200 shots, 581 states, 438 motions, 448 assets, 1421 A/V events
  (581 STATE_CHANGE + 438 MOTION_START + 402 MOTION_END).
- `RELEASE_MANIFEST.json` declares 50 files with zero hash or size mismatches.
- The distributed ZIP is sealed by a published SHA-256:
  `05e3277199efc1a8e780db87b9e25f9e294496091be45d2d0f36afe760539270`.

A published archive hash is a stronger freeze guarantee than a status string,
so the release was treated as **frozen-by-hash**. No test stop was triggered.
The first pass recorded this in `TEST_A_MANIFEST.json.brain_status_note`.

## What a fix would involve — for a future v1.0.1, not now

1. Set `release_status` to `FROZEN` and `release_frozen_at` to the real freeze
   timestamp.
2. Re-hash `BRAIN_MANIFEST.json` and update its entry in
   `RELEASE_MANIFEST.json`.
3. Re-build and re-hash the distribution ZIP, publishing a new
   `.sha256` alongside it.
4. Re-run `validator/validate_brain.py` and record the result.
5. Release as **v1.0.1**, leaving v1.0.0 and its published hash intact so that
   Test A's first pass and this revision remain reproducible against the exact
   artefact they were run on.

## Scope boundary

Do not perform steps 1–5 as part of Test A. Changing v1.0.0's bytes would
invalidate the provenance of both the blind first pass and this revision.
Re-running Test A against a patched v1.0.1 is a separate decision, and if it is
taken, the blind pass cannot be re-run blind.
