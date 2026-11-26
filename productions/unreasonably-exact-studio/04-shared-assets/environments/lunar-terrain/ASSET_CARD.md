# Lunar terrain

**Future reuse:** Moon scenarios. **Source production:** Slot 07 V3 (`07-video-productions/SLOT07_lunar-laser-ranging`). **Library built:** 2026-11-26 from the locked V3 project; the project files were cloned, not moved.

**Status meanings:** `APPROVED_IN_FILM` = used in the owner-accepted Slot 07 V3 film and passed Claude's measured tests (owner visual acceptance of Slot 07 V3, 2026-11-26); it is not a blanket approval for every future shot. `CANDIDATE` = generated and partly tested, not used in the final film. `REJECTED` = failed a test; listed so nobody reuses it.

| File | Status | Size | Role | Provenance | sha256 (first 16) |
|---|---|---|---|---|---|
| `UE_LUNAR_TERRAIN_MASTER_001.png` | APPROVED_IN_FILM | 1024x1536 | lunar surface master; Claude splits it into parallax bands in code | Codex run B3M (refs AS11-40-5952, AS15-85-11451, AS12-46-6813 attached with -i) | fbd12a91924dd30e |

## Code and rigging

animation/proofs/common.py and p13.py (band split; parallax factors stars .08, ridge .30, ground .75, array 1.0)

The engine snapshot is in [`05-animation-engine/uemotion/`](../../../05-animation-engine/uemotion/); the scene files named above are in the Slot 07 project `animation/`.

## Validation results

Claude measured: horizon at row 398 (26 %), clear foreground, shadows to the right. P13 parallax ratios equal the layer factors (PASS). In film: 0:38-0:51.

## Licensing

- Generated for this channel with Codex image generation (OpenAI) from public-domain NASA reference photos; no third-party character, logo or text. Use under the OpenAI terms of the owner account (owner to confirm commercial terms).

## Reference evidence

`REFERENCE_INDEX_moon.md` (copied) lists every reference photo with its source URL, licence and what it influenced. The photos stay in the project at `codex_handoff/references/moon/` (reference use only; several are CC BY-SA and are never shown in a film).

## Usage

1. Copy the files you need into the new project's `assets/` (keep the `UE_` name; record it in the project's asset manifest with this sha256).
2. Read the rig JSON (if any) for z-order and pivots; never re-measure by eye.
3. Re-run the matching proof test (above) in the new scene before using it in a cut.
4. A new angle or pose is an **edit of the master** through Codex (see `02-production-playbooks/CLAUDE_CODEX_ASSET_PRODUCTION_PROTOCOL.md`), never a fresh text-only generation.

## Known limitations

One sun direction (upper left) is baked in. Native 1024x1536; wider pans need an outpainted plate.
