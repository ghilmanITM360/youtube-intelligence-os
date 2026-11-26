# Observatory (with telescope rig)

**Future reuse:** Astronomy videos; scientific experiments. **Source production:** Slot 07 V3 (`07-video-productions/SLOT07_lunar-laser-ranging`). **Library built:** 2026-11-26 from the locked V3 project; the project files were cloned, not moved.

**Status meanings:** `APPROVED_IN_FILM` = used in the owner-accepted Slot 07 V3 film and passed Claude's measured tests (owner visual acceptance of Slot 07 V3, 2026-11-26); it is not a blanket approval for every future shot. `CANDIDATE` = generated and partly tested, not used in the final film. `REJECTED` = failed a test; listed so nobody reuses it.

| File | Status | Size | Role | Provenance | sha256 (first 16) |
|---|---|---|---|---|---|
| `UE_OBSERVATORY_SKY_MOUNTAINS_PLATE_001.png` | APPROVED_IN_FILM | 1024x1536 | background plate (z 0) | Codex B4P (edit of master B4M) | bb9bedfcdf5637f3 |
| `UE_OBSERVATORY_BUILDING_CLOSED_001.png` | APPROVED_IN_FILM | 1024x1536 | building, dome closed (z 30) | Codex B4L (layer cut of B4M) | b83f165e1b557cd7 |
| `UE_OBSERVATORY_BUILDING_SLIT_OPEN_001.png` | APPROVED_IN_FILM | 1024x1536 | building, slit open (z 30) | Codex B4L2 (one-defect edit; IoU 0.992 vs closed) | 453d36f0ccdcc359 |
| `UE_OBSERVATORY_SLIT_LEAF_LEFT_001.png` | APPROVED_IN_FILM | 1024x1536 | left shutter leaf (z 41, closed_dx 40) | Codex B4L | c37b91a4f36c8c6c |
| `UE_OBSERVATORY_SLIT_LEAF_RIGHT_001.png` | APPROVED_IN_FILM | 1024x1536 | right shutter leaf (z 41, closed_dx -25) | Codex B4L | 74bb830665be424c |
| `UE_OBSERVATORY_GROUND_RIDGE_001.png` | APPROVED_IN_FILM | 1024x1536 | foreground ridge (z 50) | Codex B4L | cfa99055b4e9b873 |
| `UE_TELESCOPE_TUBE_001.png` | APPROVED_IN_FILM | 1024x1536 | telescope tube (z 35), altitude pivot (490, 920), aperture (590, 700), clipped by the slit mask | Codex B4L | 7528ceb954159f74 |
| `UE_OBSERVATORY_RIG_002.json` | APPROVED_IN_FILM | 1108 B | rig: layer order, pivots, slit geometry (Claude-measured) | Claude | c2e1c9bf33c3f7f8 |
| `UE_OBSERVATORY_MASTER_001.png` | CANDIDATE | 1024x1536 | the master all layers were cut from: reference for future derived views (not itself in the film) | Codex B4M | 2c2a4344f9e16a9f |

## Code and rigging

animation/proofs/obs_rig.py (layer stack, shutter, mount slew with no overshoot, slit clip)

The engine snapshot is in [`05-animation-engine/uemotion/`](../../../05-animation-engine/uemotion/); the scene files named above are in the Slot 07 project `animation/`.

## Validation results

P04: telescope clipped by the slit, tube visible through the open slit, monotonic slew 40->6 deg, shutter opens before the slew - all PASS. In film: 0:00-0:10, 0:51-1:00.

## Licensing

- Generated for this channel with Codex image generation (OpenAI) from public-domain NASA reference photos; no third-party character, logo or text. Use under the OpenAI terms of the owner account (owner to confirm commercial terms).

## Reference evidence

`REFERENCE_INDEX_observatory.md` (copied) lists every reference photo with its source URL, licence and what it influenced. The photos stay in the project at `codex_handoff/references/observatory/` (reference use only; several are CC BY-SA and are never shown in a film).

## Usage

1. Copy the files you need into the new project's `assets/` (keep the `UE_` name; record it in the project's asset manifest with this sha256).
2. Read the rig JSON (if any) for z-order and pivots; never re-measure by eye.
3. Re-run the matching proof test (above) in the new scene before using it in a cut.
4. A new angle or pose is an **edit of the master** through Codex (see `02-production-playbooks/CLAUDE_CODEX_ASSET_PRODUCTION_PROTOCOL.md`), never a fresh text-only generation.

## Known limitations

All layers share one 1024x1536 canvas and one camera angle (3/4 front, low). The enclosure is a hemispherical dome; box enclosures need a new master. Telescope tube only (no mount close-up art).
