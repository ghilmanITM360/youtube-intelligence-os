# Frozen rules v1 for the deep-VF held-out test (pre-registered before any held-out frame or table is viewed)

Frozen at the `date -u` stamp written into `FROZEN_RULES_v1.sha256`. Selection: `heldout_v7_selection.json` (seed 20261109).

## Honest exposure statement
- **No strictly fresh long-form video exists.** 45 long uploads are in the census, and 44 have a local source. Every one of those 44 has already been used: 24 are in the dev/held-out library, and 20 were in Pop-6 (quant-only, never visually reviewed). The one long with no local source is alkJ7xScBiw.
- In this session, two things were already seen for Pop-6 before this freeze:
  - frame 3 of every Pop-6 video (opening study);
  - the automated 1-frame share and the red title-card timing.
- Rules about the opening, the canvas colour, the title card or the 1-frame share are therefore **NOT tested** on Pop-6. Pop-6 is used only for viewed rules L1–L3 below.
- The 2 Shorts were never ingested, viewed or measured before this freeze.
- Pop-6 has no 2026 upload, so the **2026 long stratum is missing** from the held-out set.

## Held-out set
| Slot | Video | Why |
|---|---|---|
| Short A | U4cONnQxgvo | Seeded pick among fresh Shorts whose parent long is in the reviewed library (parent WH4g1ptJ-70) |
| Short B | X97DDWvxaqQ | Seeded pick among fresh Shorts with no caption text (no parent text match; most independent) |
| Long 2023–24H1 | e3uk7jU3RHo | Seeded per-period pick from Pop-6 |
| Long 2024H2 | UXA-Af-JeCE | Seeded per-period pick from Pop-6 |
| Long 2025H1 | X7sbn9LMZOg | Seeded per-period pick from Pop-6 |
| Long 2025H2 | U8F7UNK9jco | Seeded per-period pick from Pop-6 |

## Rules for Shorts (from the 20 dev/held-out library Shorts)
- **S1. No red title card.** No frame has mean R>150, G<110 and B<110. Dev: 0/20 Shorts had one; 44/44 longs did.
- **S2. Pops dominate.** The share of automated ACTIVITY segments lasting 1 frame is ≥ 0.44 (dev minimum).
- **S3. Canvas.** The off-white canvas (#F9F9F9 ±3) is the modal colour of the light frames.
- **S4. Dissolves and fades.** Every cross-dissolve or fade seen in the viewed windows lasts 6±1 frames and is linear.
- **S5. Red use (viewed).** Red ink appears only as marks, circles, strikes, labels or arrows. Red is never an object fill or a background.
- **S6. No photographs (viewed).** All imagery is line art with flat fills. Maps and grey textures are allowed.
- **S7. Density match (Short A only; dev n=1, Ny9m2l6h478 vs p2M8Y0z9Rl0 gave 26.7 vs 27.0/min).** On ASR sentences matched to the parent, the Short's event rate is within ±20% of the parent's rate on the same sentences. Short events come from the automated segments_v1 ACTIVITY count; the parent uses the same automated measure.

## Rules for longs (Pop-6 four; viewed rules only)
- **L1. Red use.** Same rule as S5. The red title card is excluded.
- **L2. No photographs.** Same rule as S6.
- **L3. Device restraint.** Holds are dead still: in the viewed sheet, no hold shows idle motion, bounce or shake. Camera moves (pan, zoom, scroll) make up ≤ 6% of automated ACTIVITY segments longer than 6 frames (dev reviewed share ≈ 6%), checked by viewing those segments.

## Pass rule
- A rule passes on a video if its check holds there. Rules marked "(viewed)" are judged on one viewed contact sheet per video, with one tile per automated HOLD segment, and are recorded with tile references.
- Overall verdict:
  - FROZEN_SET_HOLDS if ≥ 90% of the evaluated rule×video checks pass.
  - Otherwise list the failures, and only the failing category gets more samples.
