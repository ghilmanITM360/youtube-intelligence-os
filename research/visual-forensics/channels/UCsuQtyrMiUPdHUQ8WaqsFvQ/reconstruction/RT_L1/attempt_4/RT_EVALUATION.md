# RT_L1 attempt 4 - evaluation (ACCEPTANCE_RT_v1, sha c0ee184e)
Measured 10/10 PASS (RT_EVALUATION.json): ink 0.0999, yellow 0.545, stroke 12.0 px, hold 1.18 s, single-frame 0.952, events 42/min, 21/23 intended matched (0.913), 0 unexplained.
Observed (primary opened SHEET_01..04 once each):
- V1 PASS original snail-like mascot, thick outline, flat fills, no gradient/shadow.
- V2 PASS single-frame swaps; only multi-frame transition is dip G0020.
- V3 PASS word-by-word stacked title, slots reserved (G0004/G0006/G0008), all in frame.
- V4 PASS red X G0018.
- V5 PASS final 5 MORE MINUTES joke; no end card.
- V6 FAIL: nothing is cut off (edge ink 0 on frames 99,440,830,1250,1349,1499, measured; the apparent bottom clipping at sheet scale is the tile label bar, see below), but overlaps hurt readability: MON badge over T tile and "!!" over F/S tiles (G0038-39), Z over MINUTES (G0042-43), SAT SUN over sun (G0030-31), 1 over DAY OFF (G0020-21).
RESULT attempt 4: FAIL (V6). Fix request: collisions only.
Tool limit found here: pe_sheets.py draws its 22 px label bar OVER the tile (line 38), hiding the bottom 22/270 = 8.1% of a landscape frame and 22/480 = 4.6% of a portrait frame in every contact sheet. Audit: campaign/SHEET_LABEL_BAND_AUDIT.json.
