# kNry0bf7eC0 — visual-only closure (contract v1; LOCAL ONLY)
Source: `source_manifest.json` path, sha256 cb6eb61d…221f re-computed this pass (match), 606 frames, 1080x1920, 24/1 CFR.
Reused: rv1 state_ledger (17 segments, frame-precise onsets), FULL_FRAME_MEASUREMENTS (606 rows), rv1 every-frame activity views (8/8).
New: `closure_v1/` native frames (22 listed frames only), hold sheets at 1/2 scale (`holds_0*.jpg`, viewed), native text crops (`text_native.png`, viewed), change crops (`crop_38_39.png`, `crop_71_72.png`, viewed), `checks.json`, `activity_curves.csv`.

## V4 timing — resolutions
| Seg | rv1 | Native resolution (OBSERVED, frames 38/39/40) |
|---|---|---|
| G0002 f39 (1.625 s) | UNRESOLVED_MINOR_CHANGE, LOW | **WIRE_POP**: a power cable pops on in 1 frame — runs from the lamp arm up the pole (second line beside the pole) to the panel, plus a coiled filament inside the lamp head. 11,884 px changed (native, >=12), bbox x352–563, y886–1919; next frame 2 px. Event class GRAPHIC → OBJECT_STATE_POP. |
Unviewed activity frames per rv1: 0. Unresolved after closure: 0.

## V5 motion
All 8 activities are single-frame pops/cuts (activity_curves.csv: change on frame f only, f+1 = 0–6 px). Hold stillness: max within-hold change 797 px (f72, G0003) and 181 px (f168, G0007); f71/f72 viewed — grain/encoder residue around the lamp glow, no drawn change. Every other hold <= 8 px.

## V6 creative — corrections to rv1 (rv1 files unchanged)
- VS002 is **not** "same composition as G0001": it adds the cable and filament (G0002).
- VS003 damage = black **stipple speckles** on the panel (not cobwebs); VS004 adds black **drip streaks** running from the panel down the pole and along the cable.
- VS006 "INFERRED camera drift during hold": **REFUTED** — phase correlation G0009→G0011 shift (0.0, 0.0) px; only the label is added. All same-shot hold pairs shift <= 0.01 px.
- VS008/VS009 story: the hanging mains bulb is lit (rays) in VS008 and **goes dark** in VS009 while the solar lamp stays lit with a cone — the payoff is the light-source comparison.
- Text (native read): `~100 YEARS` (white, hand-lettered caps, tilde, G0010 onward); `HELP` (black caps on the call box, every SH002/SH003 state); sign fragment `…MAS!` with sun-burst (cropped by left frame edge). No other text.
- Palette (measured, rv1): achromatic only; canvas #4C4C4C with film-grain noise; soft radial white glows (lamp, ground) — gradient glows are used, contrary to "flat fills" defaults (DARK_FIELD + GLOW classes).
- Continuity: pole, panel, lamp and call-box geometry identical across SH002 states; the SH001 close-up and SH002/SH003 wides are re-drawn at new scale (cut, not zoom: no intermediate frames).
Shot cuts verified (before/after native frames): f215→f217 (SH001→SH002), f442→f444 (SH002→SH003).
