# Parallax components

**Future reuse:** General animation production. **Source production:** Slot 07 V3 (`07-video-productions/SLOT07_lunar-laser-ranging`). **Library built:** 2026-11-26 from the locked V3 project; the project files were cloned, not moved.

**Status meanings:** `APPROVED_IN_FILM` = used in the owner-accepted Slot 07 V3 film and passed Claude's measured tests (owner visual acceptance of Slot 07 V3, 2026-11-26); it is not a blanket approval for every future shot. `CANDIDATE` = generated and partly tested, not used in the final film. `REJECTED` = failed a test; listed so nobody reuses it.


## Code and rigging

uemotion/camera.py (Layer2_5D multiplane camera, push-in, tilt), uemotion/timeline.py (ClockSet: film/anim/model clocks)

The engine snapshot is in [`05-animation-engine/uemotion/`](../../../05-animation-engine/uemotion/); the scene files named above are in the Slot 07 project `animation/`.

## Validation results

P02 (stars .06, Moon .35, Earth 1.00 x near plane) and P13 (.08/.30/.75/1.0) measured ratios equal the factors - PASS.

## Licensing

- Project code written by Claude for this channel.

## Reference evidence

Code-drawn; the physics it shows is in the Slot 07 `SCIENTIFIC_CLAIMS_LEDGER.csv` and `scientific_model/`.

## Usage

1. Copy the files you need into the new project's `assets/` (keep the `UE_` name; record it in the project's asset manifest with this sha256).
2. Read the rig JSON (if any) for z-order and pivots; never re-measure by eye.
3. Re-run the matching proof test (above) in the new scene before using it in a cut.
4. A new angle or pose is an **edit of the master** through Codex (see `02-production-playbooks/CLAUDE_CODEX_ASSET_PRODUCTION_PROTOCOL.md`), never a fresh text-only generation.

## Known limitations

Rigid layers only; no mesh deformation in uemotion (the Slot 02 mesh warp lives in the V15 tools).
