# Style guide: Finance Short 01 (Phase 2)

An original 2D outlined flat-illustration explainer style. It takes general clarity and motion principles from finance explainers: one relationship per beat, progressive reveals, and props acting as actors. It copies none of Casually Finance's characters, line quality, scenes, thumbnails or artwork. That channel's peach round stick-host and white hand-drawn field aren't used. This style uses navy structure lines, flat cel shading, a warm-brown angular shopper and a navy "explainer stage".

## Palette (tokens in `build/style.py`)

| Role | Token | Hex | Rule |
|---|---|---|---|
| Structure, outlines, text | ink | `#142A38` | All outlines and primary text |
| Offer / repayment path / Remy | teal | `#147D83` (dk `#0E646A`, lt `#4FA9A6`, pale `#CFE7E2`) | Paid-in-full branch, payments, true 0% panel |
| Conditional charge / deferred interest | coral | `#F16850` (dk `#C94B37`, pale `#FBD3C9`) | Interest receipt, IF, charged states, remainders |
| Paper | paper | `#FFF5DF` (dk `#E9D9BA`, dkr `#D3C09C`) | Documents, collar, cuffs, signs |
| Time | gold | `#E8BC62` (pale `#F6E3B4`) | Calendars, clock, back-trace arrow |
| Stage | navy `#142A38`, mid `#1B3744`, dk `#091D29` | | Explainer backgrounds (Phase 1 thumbnail world) |
| Neutrals | wall `#F3E6CF`, floor `#C98F5E`, wood `#9C6440`, plant `#3E8E6E`, sage `#9DBFAE`, slate `#34505F` | | Environments and clothing only |
| Sofa | plum `#7E5A7A` / `#654662` / `#9A7896` | | Deliberately outside the semantic roles |

Meaning is always carried by words or symbols as well, never by colour alone. Coral is reserved for the conditional charge. Don't use coral for decoration.

## Line and shading

- Outline width (at 1080-wide frame scale 1): characters 8, hands 6.5, props 7, fine interior detail 3–5. Joins and caps are round.
- Construction is base fill → interior shade shapes → outline stroked on top. This hides shade leaks.
- One cel shade per material, on the back (screen-left) planes, with light from the upper right. Highlights are short strokes (hair, sweater, cheek), never gradients.
- Appendages (thumbs, fingers) are filled closed and stroked open at the base, so they grow out of the palm.

## Typography

- Avenir Next 800 for headlines, labels and captions; 700 for body lines inside props. All text stays live `<text>`.
- Phone minimums at 1080 width: captions 56 px, labels 26–40 px, prop fine print ≥15 px (decorative only, like "Illustrative offer").
- Label pills are rounded capsules, ink or role-colour fill, paper or ink text.

## Layout (1080×1920)

- Headline / label zone y 200–420. Main visual y 420–1300. Caption plate y ≈ 1330–1530.
- Avoid essential content below y ≈ 1600 and right of x ≈ 960 (Shorts UI).
- Vary staging on purpose: wide store, counter medium, macro switch, explainer stage, home wide, push-in. Don't fall back to a repeated host-left / card-right slide.
- Explainer-stage scenes keep Remy as a reactor in a lower corner (scale 0.55–0.75). Story scenes use full-body or waist-up Remy (scale 0.62–1.4).

## Environment kits

Store (showroom), checkout (counter medium), living room, navy stage, paper macro. Each is layered (bg / mid / floor / fg) with one-point perspective floors. Kits carry no text, prices, rates, dates or brands.

## Financial-accuracy rules baked into the art

- No dollar amounts, APR values, balances or real dates anywhere. All charts are schematic and labelled as such.
- The deferred-interest offer never says "0%". "TRUE 0% INTRO APR" appears only in the comparison panel, with "Interest may start after the promo period".
- Balance-history interest chips shrink with the balance carried. The art never shows interest on the original principal after payments.
- "WAIVED" appears only on the paid-in-full + terms-met path. The alternative path is labelled ALTERNATIVE, so the same shopper doesn't appear to take both paths.

## Motion vocabulary (for the animation phase)

REVEAL_STEP, POP_IN (6–10 f, scale 0.85→1), SLIDE_IN (10–18 f), MATCH_SCALE, MASK_FILL (receipt print, balance fill), DIRECTED_TRANSFER (coins, receipt drop), STAMP_HIT (scale 1.6→1 in 5 f + settle), TRACE_REVEAL (stroke-dash), COMPARE_BUILD, LABEL_HIGHLIGHT, POSE_EXPRESSION_SWITCH (step, 4–8 f angle blend), WALK_CYCLE, CAMERA_REFIT (18–30 f), SCENE_EXIT. Charts never overshoot their end states.
