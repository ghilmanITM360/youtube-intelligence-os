# Moon

**Future reuse:** Lunar missions, tides, distance explanations. **Source production:** Slot 07 V3 (`07-video-productions/SLOT07_lunar-laser-ranging`). **Library built:** 2026-11-26 from the locked V3 project; the project files were cloned, not moved.

**Status meanings:** `APPROVED_IN_FILM` = used in the owner-accepted Slot 07 V3 film and passed Claude's measured tests (owner visual acceptance of Slot 07 V3, 2026-11-26); it is not a blanket approval for every future shot. `CANDIDATE` = generated and partly tested, not used in the final film. `REJECTED` = failed a test; listed so nobody reuses it.

| File | Status | Size | Role | Provenance | sha256 (first 16) |
|---|---|---|---|---|---|
| `UE_MOON_GLOBE_001.png` | APPROVED_IN_FILM | 4096x2048 | equirectangular Moon map; near side faces Earth in code | NASA LROC/SVS Moon map; Claude upscaled (labelled) | adc28e955cec346c |
| `UE_MOON_GLOBE_001_notes.json` | APPROVED_IN_FILM | 703 B | source and processing notes | Claude | 61fba227bcc2163a |

## Code and rigging

uemotion/space.py (same globe renderer and sun direction as Earth)

The engine snapshot is in [`05-animation-engine/uemotion/`](../../../05-animation-engine/uemotion/); the scene files named above are in the Slot 07 project `animation/`.

## Validation results

P02 one-sun test and parallax factors PASS; P03 opening uses it. In film: 0:00-0:10, 0:11-0:35, 1:28-1:36.

## Licensing

- NASA imagery, public domain (NASA media usage guidelines); NASA does not endorse; no NASA logo used.

## Reference evidence

`REFERENCE_INDEX_moon.md` (copied) lists every reference photo with its source URL, licence and what it influenced. The photos stay in the project at `codex_handoff/references/moon/` (reference use only; several are CC BY-SA and are never shown in a film).

## Usage

1. Copy the files you need into the new project's `assets/` (keep the `UE_` name; record it in the project's asset manifest with this sha256).
2. Read the rig JSON (if any) for z-order and pivots; never re-measure by eye.
3. Re-run the matching proof test (above) in the new scene before using it in a cut.
4. A new angle or pose is an **edit of the master** through Codex (see `02-production-playbooks/CLAUDE_CODEX_ASSET_PRODUCTION_PROTOCOL.md`), never a fresh text-only generation.

## Known limitations

Albedo map only (no height map), so terminator relief is painted by the shading model, not by real topography.
