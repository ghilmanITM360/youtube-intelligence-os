# Asset QA

QA date 2026-10-13. Reviewer: one agent (Claude). Method: rendered contact sheets plus close-up crops at 1–2× and an automated pass. **No independent human art director has reviewed this yet.**

## Automated checks (`qa/automated_qa.json`, `qa/text_inventory.csv`)

| Check | Result |
|---|---|
| 244 SVG sources well-formed (system `xmllint`) | PASS, 0 errors |
| 196 PNG exports present; pixel size recorded per asset | PASS |
| SHA256 for every SVG and PNG (`ASSET_REGISTER.csv`) | Recorded |
| Deterministic rebuild (two consecutive builds) | PASS: 0 hash changes across 244 assets |
| No `$<number>` or `<number>%` text, except "TRUE 0% INTRO APR" / "for the 0% period" in the comparison | PASS |
| Deferred-interest assets (offer, promo sign, receipt, ledger) never contain "0%" | PASS |
| Remy face-outline landmark path present in all 19 pose files | PASS |
| Every scene-layout asset ID resolves to a registered asset (automated check in build_assets.py) | PASS (0 unresolved) |

## Character consistency QA: Remy

| Item | Finding | Status |
|---|---|---|
| Head and facial identity | Same `FACE`, ear and nose geometry in every pose and expression (shared code, string-checked). Phase 1 reference head shown in `remy_expression_sheet.png` | PASS |
| Eye placement | Fixed centres (303,207)/(361,206); gaze offset ≤ 6 px | PASS |
| Hair shape | Mass, colour and screen-right sweep kept. Contour is rounder and more scalloped than the Phase 1 spikes | **PASS_WITH_NOTES: owner sign-off needed** |
| Body proportions | One rig; every pose re-poses the same parts; no per-shot redraws | PASS |
| Hand anatomy | v1 "claw" open hands and loop thumbs **rejected and rebuilt** (capsule fingers under the palm, open-stroke thumbs). Final set reads correctly at video scale | PASS_WITH_NOTES (stylised mittens, not portrait-detail hands) |
| Gripping gestures | Back/front sandwich verified on sheet, statement, card, pen and marker crops. Pen recoloured teal after it vanished into ink outlines | PASS |
| Character-object contact | Fingertip meets the IF lever (C04). Marker meets the calendar circle (C12). Coin starts at the fingertip (C06A). Sheet edges sit between thumb and fingers | PASS |
| Perspective | 3/4-right figure throughout. The 3/4 seated pose on a front-view sofa is cartoon licence | PASS_WITH_NOTES |
| Clothing | Teal sweater, cream collar and cuffs, slate trousers in all states | PASS |
| Outline thickness | Character 8, hands 6.5, props 7, fine 3–5 (scale-1 units); consistent at each scene scale | PASS |
| Expression readability | 15 presets read at contact-sheet scale. Phone-scale sheet shows big-shape expressions read; subtle brow differences (neutral vs soft) fade at 1/6 scale | PASS_WITH_NOTES |
| Camera-scale consistency | Stage reactor 0.55–0.75, store/home 0.62–0.85, close/medium 1.2–1.4, macro arm 2.4. Outlines scale with the rig (documented) | PASS |

**Associate:** distinct silhouette (bun, glasses, apron), consistent across 3 poses and 3 expressions. Shares Remy's limb and hand system, recoloured. PASS.

## Rework log: rejected or corrected during production

1. Open hands (v1) looked like claws, so they were rebuilt. Point/fist thumbs were closed loops, so they were rebuilt as open-stroke appendages.
2. Knee joints showed the shin cap, so the draw order was fixed (thigh over shin).
3. The sitting pose hid the thighs behind the torso. Fixed with a slot override (legs in `mid`).
4. Blush leaked outside the face outline. Moved inside.
5. Offer-sheet text overflowed the paper; it was re-laid out (NO INTEREST / IF / PAID IN FULL / WITHIN 12 MONTHS). Receipt header, flag label, calendar header and statement header overflows were also fixed.
6. **Balance-history diagram (v1):** the gold "trace back" curve ran along the chip tops and read as a quantitative trend line. **Rejected as potentially misleading** and replaced with a bracket into the receipt plus a timeline arrow under the axis.
7. Scene fixes:
   - C01A Remy too small; enlarged.
   - C06A/B month strip hidden by Remy's head; moved.
   - C07 Remy undersized; enlarged.
   - C12 label overlapped a calendar; moved.
   - C14 receipt floated against the wall; it now leans on the cushion.

## Financial-accuracy review of the artwork

| Item | Treatment |
|---|---|
| F2 | Offer labelled "Illustrative offer"; no brand or store name; the associate's badge is blank |
| F3 | Receipt grows from PURCHASE DAY and stays on a "NOT CHARGED YET" clip until the outcome |
| F4/F5 | Separate teal and coral paths; the coral path is labelled ALTERNATIVE |
| F6 | Bars decline with payments; interest chips scale with each month's balance; labelled "SCHEMATIC • NOT TO SCALE" |
| F7 | "MINIMUM PAID ≠ PROMO PAID OFF" is shown as a possible outcome (one example remainder), not a universal claim |
| F8 | Comparison keeps "Interest may start after the promo period" |
| F9 | Two date cards with no real dates |
| F10 | Final qualifier: "waived only if paid in full on time" |

## Known limitations and missing artwork

- **Audio gate:** APR is mispronounced in the MP3, so every timing is provisional (`audio_analysis/AUDIO_QA_REPORT.md`).
- **Art direction:** no human review. Illustration quality is clean, consistent flat vector work, but not bespoke hand-drawn caricature: limited secondary detail, simple hands, no torso turns or back views.
- **Animation coverage:**
  - The walk cycle has only 2 key poses.
  - The associate has 3 poses.
  - There is no delivery or "sofa arriving" sequence (S11 starts with the sofa in place).
  - There's no dedicated close-up of a hand flipping the IF switch beyond the C04 arm crop.
- Some diagram labels are 20–24 px and need phone re-checking. Text depends on Avenir Next.
- Hero frames are start/hero states. In-between states (coin positions, receipt print rows, balance fills) are prepared as separate assets and layers, but their motion is not verified until animation.
