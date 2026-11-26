# Apollo 11 retroreflector (LRRR)

**Future reuse:** Lunar laser ranging; optics. **Source production:** Slot 07 V3 (`07-video-productions/SLOT07_lunar-laser-ranging`). **Library built:** 2026-11-26 from the locked V3 project; the project files were cloned, not moved.

**Status meanings:** `APPROVED_IN_FILM` = used in the owner-accepted Slot 07 V3 film and passed Claude's measured tests (owner visual acceptance of Slot 07 V3, 2026-11-26); it is not a blanket approval for every future shot. `CANDIDATE` = generated and partly tested, not used in the final film. `REJECTED` = failed a test; listed so nobody reuses it.

| File | Status | Size | Role | Provenance | sha256 (first 16) |
|---|---|---|---|---|---|
| `UE_RETROREFLECTOR_ASSEMBLY_001.png` | APPROVED_IN_FILM | 1024x1536 | reflector layer of the carry interaction, with the composited 10x10 cube array | Codex B5PR + Claude composite of the cube array | 44318a4e05a7bacb |
| `UE_RETROREFLECTOR_CUBE_ARRAY_001.png` | APPROVED_IN_FILM | 1254x1254 | 100 corner-cube instances on the measured recess grid | Codex cube parts (batch 0b) placed by Claude | 394e16655f8caefa |
| `UE_RETROREFLECTOR_CUBE_ARRAY_001_instances.json` | APPROVED_IN_FILM | 8936 B | instance centres (exact count and registration) | Claude | 47963840fe90c1f6 |
| `UE_RETROREFLECTOR_FRAME_MASTER_34.png` | CANDIDATE | 1500x1000 | 3/4 frame master | Codex batch 2 | 811bd9be8910876a |
| `B5PR2 cube-grid edit` | REJECTED |  | IoU 0.327: whole object re-rendered larger and moved | runs/_rejected |  |
| `R2b side-view fix` | REJECTED |  | tilt regressed 23.6 -> 14.7 deg | runs/_rejected |  |

## Code and rigging

uemotion/optics.py (corner-cube ray paths, antiparallel exit rays), animation/proofs/p07.py, p13.py

The engine snapshot is in [`05-animation-engine/uemotion/`](../../../05-animation-engine/uemotion/); the scene files named above are in the Slot 07 project `animation/`.

## Validation results

P13: exit rays antiparallel to entry (dot = -1.0 for three rays), cube-face to cutaway registration 0.05 px - PASS. In film: 0:38-0:51.

## Licensing

- Generated for this channel with Codex image generation (OpenAI) from public-domain NASA reference photos; no third-party character, logo or text. Use under the OpenAI terms of the owner account (owner to confirm commercial terms).

## Reference evidence

`REFERENCE_INDEX_retroreflector.md` (copied) lists every reference photo with its source URL, licence and what it influenced. The photos stay in the project at `codex_handoff/references/retroreflector/` (reference use only; several are CC BY-SA and are never shown in a film).

## Usage

1. Copy the files you need into the new project's `assets/` (keep the `UE_` name; record it in the project's asset manifest with this sha256).
2. Read the rig JSON (if any) for z-order and pivots; never re-measure by eye.
3. Re-run the matching proof test (above) in the new scene before using it in a cut.
4. A new angle or pose is an **edit of the master** through Codex (see `02-production-playbooks/CLAUDE_CODEX_ASSET_PRODUCTION_PROTOCOL.md`), never a fresh text-only generation.

## Known limitations

Panel tilt about 23 deg from the ground (AS11-40-5952). Only the 3/4 view is approved; the side view is a candidate, and the top view was dropped.
