# Earth

**Future reuse:** Spaceflight, tides, orbital mechanics. **Source production:** Slot 07 V3 (`07-video-productions/SLOT07_lunar-laser-ranging`). **Library built:** 2026-11-26 from the locked V3 project; the project files were cloned, not moved.

**Status meanings:** `APPROVED_IN_FILM` = used in the owner-accepted Slot 07 V3 film and passed Claude's measured tests (owner visual acceptance of Slot 07 V3, 2026-11-26); it is not a blanket approval for every future shot. `CANDIDATE` = generated and partly tested, not used in the final film. `REJECTED` = failed a test; listed so nobody reuses it.

| File | Status | Size | Role | Provenance | sha256 (first 16) |
|---|---|---|---|---|---|
| `UE_EARTH_SURFACE_001.png` | APPROVED_IN_FILM | 4096x2048 | cloud-free surface map (equirectangular); lighting applied in code | NASA Blue Marble class map; Claude assembled/upscaled (labelled resampled) | 40e9d6a21e019a0a |
| `UE_EARTH_NIGHT_LIGHTS_001.png` | APPROVED_IN_FILM | 4096x2048 | city lights, shown only on the night side (terminator mask in code) | NASA Black Marble | d08bd9579652620c |
| `UE_EARTH_CLOUDS_001.png` | APPROVED_IN_FILM | 4096x2048 | wrap-safe cloud layer (alpha), drifts 0.1-0.3 deg/s in code | Codex cloud tiles (batch 1 + run B1c) composited by Claude | 283ba3171d6ece3c |
| `earth_clouds_proc_4096x2048.png` | REJECTED |  | Claude procedural clouds: blobby, smeared land at partial alpha | not copied; stays in the project as a rejected file |  |
| `batch1 polar patches` | REJECTED |  | invented coastlines | not copied (geography must come from NASA maps) |  |
| `batch1 atmos_slice_*.png` | CANDIDATE |  | atmosphere slice layers; not registered with each other; not used | codex_handoff/deliveries/batch1/ |  |

## Code and rigging

uemotion/space.py (globe sphere mapping, one film-wide sun direction, terminator, atmosphere rim, night-light mask)

The engine snapshot is in [`05-animation-engine/uemotion/`](../../../05-animation-engine/uemotion/); the scene files named above are in the Slot 07 project `animation/`.

## Validation results

P01 (Earth rotation lighting): lit side constant while spinning, sun from the left, no antimeridian seam (5.12 vs 2.39), no pole pinch, clouds drift 15 deg - all PASS. P02 one-sun test PASS. In film: 0:09-0:35, 1:18-1:36.

## Licensing

- Generated for this channel with Codex image generation (OpenAI) from public-domain NASA reference photos; no third-party character, logo or text. Use under the OpenAI terms of the owner account (owner to confirm commercial terms).
- NASA imagery, public domain (NASA media usage guidelines); NASA does not endorse; no NASA logo used.

## Reference evidence

`REFERENCE_INDEX_earth.md` (copied) lists every reference photo with its source URL, licence and what it influenced. The photos stay in the project at `codex_handoff/references/earth/` (reference use only; several are CC BY-SA and are never shown in a film).

## Usage

1. Copy the files you need into the new project's `assets/` (keep the `UE_` name; record it in the project's asset manifest with this sha256).
2. Read the rig JSON (if any) for z-order and pivots; never re-measure by eye.
3. Re-run the matching proof test (above) in the new scene before using it in a cut.
4. A new angle or pose is an **edit of the master** through Codex (see `02-production-playbooks/CLAUDE_CODEX_ASSET_PRODUCTION_PROTOCOL.md`), never a fresh text-only generation.

## Known limitations

Polar regions come from the NASA map (not repainted). Day/night only; no seasons or axial tilt in the renderer. 4096x2048 is enough for a globe up to ~600 px radius; close-ups need a higher-resolution source.
