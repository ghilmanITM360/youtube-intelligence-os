# Apollo astronaut

**Future reuse:** Space exploration. **Source production:** Slot 07 V3 (`07-video-productions/SLOT07_lunar-laser-ranging`). **Library built:** 2026-11-26 from the locked V3 project; the project files were cloned, not moved.

**Status meanings:** `APPROVED_IN_FILM` = used in the owner-accepted Slot 07 V3 film and passed Claude's measured tests (owner visual acceptance of Slot 07 V3, 2026-11-26); it is not a blanket approval for every future shot. `CANDIDATE` = generated and partly tested, not used in the final film. `REJECTED` = failed a test; listed so nobody reuses it.

| File | Status | Size | Role | Provenance | sha256 (first 16) |
|---|---|---|---|---|---|
| `UE_APOLLO_ASTRONAUT_CARRY_REFLECTOR_001.png` | APPROVED_IN_FILM | 1024x1536 | astronaut layer of the carry/set-down interaction, hidden parts painted | Codex B5PA (layer cut of B5P; restack IoU 0.983) | ac068dbc36b13356 |
| `UE_APOLLO_ASTRONAUT_MASTER_001.png` | CANDIDATE | 1024x1536 | standing 3/4 master, visor down, anonymous: the reference for every derived pose | Codex B5M | 7ed3ea9fb7800430 |
| `UE_APOLLO_ASTRONAUT_TORSO_NOARMS_001.png` | CANDIDATE | 1024x1536 | arm rig: torso layer | Codex B5L | f2911528d653bf92 |
| `UE_APOLLO_ASTRONAUT_ARM_NEAR_001.png` | CANDIDATE | 1024x1536 | arm rig: near arm with overlap sleeve | Codex B5L | 70352512f4759a24 |
| `UE_APOLLO_ASTRONAUT_ARM_FAR_001.png` | CANDIDATE | 1024x1536 | arm rig: far arm | Codex B5L | 54384d3eebde0a15 |
| `UE_APOLLO_ASTRONAUT_ARMS_RIG_003.json` | CANDIDATE | 1203 B | arm rig pivots and skinning (rig v2) | Claude | 3abf34b3dc4e1cb4 |
| `B5L2 shoulder cap` | REJECTED |  | no alpha 0 anywhere, noise over the canvas | runs/_rejected |  |

## Code and rigging

animation/proofs/p05.py (arm rig v2, deformation at the shoulder), p06.py (carry, grip lock, set-down)

The engine snapshot is in [`05-animation-engine/uemotion/`](../../../05-animation-engine/uemotion/); the scene files named above are in the Slot 07 project `animation/`.

## Validation results

P06 (in film): glove-to-bar error 0.000, lands on the master pose, release after touch-down, ballistic dust - PASS. P05 arm rig v2: shoulder gap PASS (worst 86 px of 15,361) but P05 is NOT in the final cut, so the arm rig stays CANDIDATE.

## Licensing

- Generated for this channel with Codex image generation (OpenAI) from public-domain NASA reference photos; no third-party character, logo or text. Use under the OpenAI terms of the owner account (owner to confirm commercial terms).

## Reference evidence

`REFERENCE_INDEX_astronaut.md` (copied) lists every reference photo with its source URL, licence and what it influenced. The photos stay in the project at `codex_handoff/references/astronaut/` (reference use only; several are CC BY-SA and are never shown in a film).

## Usage

1. Copy the files you need into the new project's `assets/` (keep the `UE_` name; record it in the project's asset manifest with this sha256).
2. Read the rig JSON (if any) for z-order and pivots; never re-measure by eye.
3. Re-run the matching proof test (above) in the new scene before using it in a cut.
4. A new angle or pose is an **edit of the master** through Codex (see `02-production-playbooks/CLAUDE_CODEX_ASSET_PRODUCTION_PROTOCOL.md`), never a fresh text-only generation.

## Known limitations

One suit (Apollo 11 A7L, anonymous, visor down), one 3/4 angle. No walk cycle, no face. New angles must be edits of the master (UE_APOLLO_ASTRONAUT_MASTER_001), not new text-only generations.
