# WI-0081 lens audit (xkcd What If visual forensics) — 2026-11-15
Lens = HUMANCRAFT_ALIGNMENT §6 + STYLE_BIBLE v2: white plate, one 8 px monoline, flat grey fills only, red only for marks, 1-frame pops, no gradients/halos, stage props readable at 1080x1920.
Measured by assets/qa/audit_lens.py -> audit_lens.csv (read-only).

## Measured facts
- Head fit is GOOD on all 26 CHR files: head height 337-339 px (target 338), top y 149-151 (target 150), axis x 767-769 (X: 490). So heads never jump between swaps.
- Only the FEET differ: P poses end at y 1056-1140 (target 1102); outliers P14 1260 (+158), P12 1056 (-46), P03 1140 (-38). V views: V01 1005, V02 1140, V03 1206, V04 1226 (reference views, not shot layers).
- Because head is the anchor and legs are single lines, a 20-47 px leg-length difference (2-5% of figure) is invisible in a 1-frame swap. Proposed owner decision: P-pose feet tolerance 6 -> 50 px, head-anchored; P14 is the only true reject for length.
- Real rejects (content, not alignment): P04 halo, P08 baked motion marks, P11 baked dial, P14 legs too long.
- Plates NIA-01/03 and TBL-01 are RGB (not alpha) -> must sit on pure white, no grey wash; check they do not make the frame <85% white.
- Props that fail the lens: MUG-01 vs MUG-02 outline mismatch, WTR-01/02/03 grey fills differ (WTR-01 only 0.5% ink, nearly empty), SPN-02/03 do not share a silhouette, RUL-01 (0.65% ink) and THR-01 (0.12% ink) are hairlines -> unreadable at 320 px.
- Draft stills S01/S16 draw a ground line and a table; the xkcd lens has no floor line (NO floor line rule). S07/S16/S21 show a stray "W" label (compositor bug).
- MSK-01 is empty (0.0% ink) — code asset, must be fixed by me.

## Who does what (75 / 25)
- 75% IMAGE assets (Codex only): all CHR-*, MUG/WTR/SPN/THM/JUG/HRS/CAV/FLM/BLB/CLK/MWV/NIA/TBL/RUL/THR.
- 25% CODE (Claude): 19 VEC (arrows, red marks, brackets, dots, sugar, X, circle, chart, rulers), 20 TEXT layers, MSK-01, and all motion: 1-frame pops, 6-frame linear dissolves, constant-speed write-ons, hard-landing pans. No bounce/overshoot (0/13 windows in the reference).
