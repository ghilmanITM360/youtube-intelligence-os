# Codex handoff V2: V1 Rent long-form host rig (thin body + large original head)

Date 2026-11-21. Owner: Codex makes the illustration assets only. Claude owns storyboard, charts, type, animation, render, QA.
**Supersedes the character part of `CODEX_HANDOFF.md` and `codex_art/HANDOFF.md`** (the detailed clothed, shaded renter is NOT the target any more). Do not touch or overwrite anything in `v1_assets/approved/`.

## Read first (required, in this order)
1. `CHANNEL_VISUAL_AUDIT/CHANNEL_001/22_LONGFORM_VISUAL_DNA.md` (principles L1-L11, rules in section 4).
2. `V1_RENT_STYLE_FIDELITY_AUDIT.md` sections 3, 5 (geometry table).
Do NOT start from the old detailed-clothing specification. Do NOT open, trace, copy or redraw the reference channel's frames or character; work only from the numbers below. The result must be our own recognisable character.

## Character (original, fictional)
The same early-30s American renter as the approved art, reduced to the long-form rig: dark side-parted curls, warm skin tone, simple dot or small-oval eyes, one-line mouth variations, a single olive overshirt hint, dark jeans, small white sneakers. No resemblance to a real person. Identity must read the same in all 5 heads and 3 bodies (same hair shape, same skin colour, same line weight).

## Proportions (hard numbers, figure height H = head + body = 1800 px)
| Part | Target |
|---|---|
| Head height | 0.34 H = about 610 px; head width about 0.36 H = about 650 px (round, slightly wider than tall is fine) |
| Body (neck to sole) | about 0.66 H = about 1190 px |
| Body line weight (arms, legs) | about 2.5% of H = about 45 px, round caps, hand-drawn slight wobble |
| Torso | one narrow slab or thick line, width about 4-5% of H (80-90 px), olive `#5B6B3A` fill, ink outline |
| Head outline | about 1.6% of H = about 29 px, ink `#1F2430` |
| Hands | simple small circles or mitts, about 70 px |
| Feet | small white rounded shoes with ink outline |
Flat fills only: no gradients, no shading, no glow, no texture. Palette: ink `#1F2430`, olive `#5B6B3A`, skin warm tone of your choice (keep it constant), hair dark, jeans dark ink, white `#FFFFFF`. A small coral `#E8604C` is allowed only if a pose needs it (do not add it to the body).

## Deliverables (transparent PNG, RGBA, tight crop plus a 40 px margin; draw at 2x and downsample is fine)
Separate head and body layers.

| File | Content | Canvas |
|---|---|---|
| `rig_body_down.png` | arms hanging relaxed, standing, facing front | 1300 x 1300 |
| `rig_body_shrug.png` | both palms up, shoulders raised (a shrug) | 1300 x 1300 |
| `rig_body_point.png` | right arm (viewer's right) extended horizontally pointing out of the figure; left arm down | 1500 x 1300 |
| `rig_head_neutral.png` | calm, small flat mouth | 700 x 700 |
| `rig_head_smile.png` | small smile | 700 x 700 |
| `rig_head_worried.png` | brows up and in, wavy or small down mouth | 700 x 700 |
| `rig_head_surprised.png` | eyebrows high, small round mouth ("o") | 700 x 700 |
| `rig_head_smirk.png` | one-sided smirk, one brow up (the "this is odd" face) | 700 x 700 |
| `rig_anchors.json` | for each body: `neck` = (x, y) in the body canvas where the head's chin anchor sits; for each head: `chin` = (x, y) in the head canvas; both measured, in px | n/a |

Anchor rule: every head must fit every body with the same `chin` position, so Claude can swap any head onto any body. The neck stub on the body may sit under the head; the head's lower edge overlaps it.

Optional (only if cheap): `rig_body_hold.png`, the same body with one hand held out flat (palm up, nothing in it) so Claude can place a bill in it.
Not needed: lip sync, mouth-open variants, 3/4 views, clothing detail, shadows, backgrounds (the existing approved room plate is reused for a few beats).

## Acceptance (Claude checks at 1080p and at phone size)
1. Measured: head height / figure height between 0.31 and 0.38; body line 2-3% of H; outline within 1.2-2.2% of H.
2. Any head on any body: alignment within 6 px at the anchors.
3. Five heads read as five different emotions at 200 px height without labels.
4. One identity across all files (hair, skin, olive overshirt).
5. Clean alpha, no halo on white (`#FDFDFD`) and on the approved cream room.
6. Stroke looks hand-drawn (slight wobble), not a perfect geometric vector.
One correction round per failed asset. Put files in `codex_art/v2_rig/` with originals preserved, SHA-256 listed in a `qa/validation.json`, and say what each file's real pixel size and generation size are (as in the last batch).

## Status of the pipeline until these arrive
Claude has built a **provisional placeholder rig** (procedurally drawn, same file names and anchors, in `v1r4_assets/provisional/`) to prove the long-form grammar. The renderer reads `v1r4_assets/rig/` first and falls back to the placeholder, so Codex files drop in with no code change. The placeholder is not final art and is not claimed as Codex output.
