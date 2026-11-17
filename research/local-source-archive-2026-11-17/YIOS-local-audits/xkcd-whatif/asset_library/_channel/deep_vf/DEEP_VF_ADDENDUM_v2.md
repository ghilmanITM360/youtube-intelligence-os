# Deep-VF addendum v2 (rules v2, targeted held-out v8, silent proof; LOCAL ONLY)

This file supersedes addendum v1 where the two differ. The v1 files are not edited.

## 1. Corrections to v1
- **F3 title card (wrong in v1).** The 288 red frames in each long are **two cards**, not one 12.0 s title card:
  - a 2.0 s opening title card: 48 f in 43/44 longs;
  - a 10.0 s red end screen (credits and books): 240 f in 40/44 longs, running to the last frame.
  - All 44/44 local longs have both. Their total is exactly 288 f = 12.0 s in 40/44 longs (280–287 f in the other 4).
  - Shorts: 0/20 dev Shorts and 0/4 held-out Shorts have either card.
  - Evidence: `v2/title_card_durations.csv`, plus the viewed frames 175, 4800 and 4984 of 2LSyizrk8-0.
- **v1 S5/L1 ("red never a fill") was already false in dev.** Dev contains RED_SOLID fills: magma, fire, a red can, a laser, heat zones on maps.
- **v1 S6/L2 ("no photographs") was already false in dev.** 2LSyizrk8-0 uses blurred photos as a camera-resolution demo.
- **v1 L3 6% camera limit did not match dev.** On the same denominator (all automated activities), dev longs run 0–0.176.
- **v7 stays 19/23 = 82.6%, unchanged.**

## 2. Rules v2 and the v8 result
- **Rules:** `FROZEN_RULES_v2.md`, frozen 2026-11-08T20:41:49Z.
- **Results:** `heldout_v8/RESULTS.md`.

| Verdict | Score | Status | Caveats |
|---|---|---|---|
| Colour | 17/18 = 94.4% | HOLDS | 4 of the C2 passes are trivial (0 coloured tiles). The fail was zJNm: a saturated map classed PAINTED, a gap in the rule wording. |
| Journey/motion | 15/16 = 93.8% | HOLDS for ORDINARY/MAP_TOUR | **JOURNEY_LADDER arm UNTESTED** (no journey long in v8). The fail was zJNm: a Short film-strip scroll at 0.21 > 0.13. |
| Overall (targeted) | 32/34 = 94.1% | HOLDS | Not a fresh pass of the full ruleset. The 2026 long stratum is not covered. |

## 3. New measured tools (validated on dev)
- **`colour_classes.py`.** A native-colour class per frame. Exemplar sheets were viewed for each class.
  - Known misfires:
    - a thin red horizontal line can be classed RED_SOLID;
    - saturated maps fall into PAINTED_PLATE.
- **`motion_classes.py`.** Labels each motion as WHOLE_FRAME_CAMERA, RULER_SCROLL or OBJECT_MOTION.
  - Camera detection against dev reviewed labels: precision 0.92, recall 0.77.
  - Ruler detection was confirmed on e3uk (v7, used only as a tool check).

## 4. New findings this pass
1. **Every long has two cards.** There is a 2.0 s opening card and a 10.0 s closing card (see §1).
2. **DARK_FIELD is a core scene class, not an exception.** Space, night, underground and cross-section scenes make up 0–66% of states in longs and up to 78% in Shorts.
3. **Ladder without camera.** Jpy5 shows progress with a stepwise depth counter on a fixed map, plus red circle callouts. A ruler scroll (e3uk) is one option; relabelling is the other.
4. **Film-strip scroll device in Shorts** (zJNm): a whole-frame horizontal scroll of 12–15 f moves.
5. **The red-circle pop in our own proof confirms why grey detectors miss it.** The ROI red pixels go from 0 to 3576 in one frame, while the whole-frame luma diff is only 0.24.

## 5. Silent proof
- **Owner-authorized and rendered:** `proof_v1/PROOF_RESULTS.md`.
- **Both 16:9 and 9:16 pass:**
  - P1–P7;
  - the native-colour red-pop check;
  - the clip/overlap check.
- Attempt 1 failed frame review on three layout defects. Attempt 2 is clean.
- **Still pending:**
  - P8 (human playback review);
  - P9 (scorecard);
  - audio sync and final AV.

## 6. Sample size, deduplicated by video ID (no ID appears in more than one set)
| Set | Long | Shorts | Notes |
|---|---|---|---|
| Census | 45 | 46 | Local: 44 / 44 |
| **Reviewed** (frame-level state ledger, DEV + earlier quant held-outs) | 24 | 20 | About 11 Shorts are independent; the others are excerpts of library longs |
| Held-out sheet-level visual examination: v7 | 4 | 2 | Pop-6 longs had prior quant exposure |
| Held-out sheet-level visual examination: v8 | 4 | 2 | Jpy5/saj7 are partly exposed through library Shorts; zJNm art comes from dev WH4g |
| **Unique videos visually examined** | **32** | **24** | 56 IDs |
| **Visual gates passed** (held-outs, all evaluated rules of their version) | 6 | 1 | v7 under v1: UXA-Af-JeCE, X7sbn9LMZOg. v8 under v2: Jpy5, RgBY, saj7, PUtI, alBQ. Dev videos are training data, not gated. |
| **Full AV passed** | **0** | **0** | Listening is BLOCKED |

### Add another sample only if one of these triggers fires
| Trigger | Status | Next sample |
|---|---|---|
| Required format uncovered | **YES**: JOURNEY_LADDER (no fresh journey long), and the 2026 long stratum | 1 fresh 2026 long. The only candidate is alkJ7xScBiw (2026-10-27, "nuke in the Mariana Trench"), which has **no local source**. Acquiring it is an owner decision and out of scope for this pass. If it is not a journey video, the journey arm needs another source (none exists locally). |
| Revised rule failed | **YES**: Shorts (zJNm C2 map wording; M1 film-strip scroll) | Write rules v3: a MAP_FILL class, and a Short camera budget that counts the film-strip/scroll device. Then 2 fresh Shorts from the 20 still unused locally, preferring map- or scroll-heavy picks chosen by title. |
| A new finding changes a production decision | **YES** for the card correction (2 s opening card + 10 s end card, not a 12 s title card) and the DARK_FIELD scene class | No extra sample needed. These change the prompt pack / style bible (prompt pack v2 still to write). |

**Current answer.** About **33 long + 26 Shorts** in total:
- **already eligible:** 32 long + 24 Shorts examined;
- **still to add:** 2 Shorts (available locally) and 1 long (2026, needs acquisition);
- **additional, only if the 2026 long is not a journey video:** 1 more journey long.

Production can start on ORDINARY and MAP_TOUR formats now. The journey format should not be produced as a validated format yet.
