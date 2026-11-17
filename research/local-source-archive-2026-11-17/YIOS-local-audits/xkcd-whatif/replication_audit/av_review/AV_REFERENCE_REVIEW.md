# AV reference review — 5 xkcd What If references (2026-11-14)
Full timestamped rows (narrator ASR / visible change / ledger function / measured sound / dB / stage): `REF5_TIMELINE_ROWS.csv` (103 rows). Human audio timecodes: `AUDIO_HUMAN_PASS_TIMECODES.csv`.

## Verification & status (labels: OBSERVED = measured/decoded; INFERRED = my reading; UNKNOWN)
| Video | ID verified | Visual | Transcript | Audio | Status |
|---|---|---|---|---|---|
| 8fADp43wJwU high-view long (304 s) | filename ID + manifest SHA-256 recomputed = MATCH | ledger 29 shots (prior review) + 12-frame sheet re-viewed this pass | faster-whisper small.en (prior), ASR segments merged per shot | NOT_LISTENED; silencedetect + per-shot mean dB only | VISUAL+TRANSCRIPT MAPPED, AUDIO PENDING HUMAN |
| Z_xJ40QXu7Q typical long (236 s) | MATCH | ledger 24 shots only; **no frames re-viewed this pass** | ASR merged | NOT_LISTENED | MAPPED FROM LEDGER, VISUAL RE-VIEW NOT DONE |
| 9VG0yqq_PHM recent long (162 s) | MATCH | ledger 10 shots + 12-frame sheet re-viewed | ASR merged | NOT_LISTENED | VISUAL+TRANSCRIPT MAPPED, AUDIO PENDING |
| FkUNHhVbQ1Q Mars long (267 s) | MATCH | ledger 28 shots + 12-frame sheet re-viewed | ASR merged | NOT_LISTENED | VISUAL+TRANSCRIPT MAPPED, AUDIO PENDING |
| 2p305nzcVQE Mars Short (106 s, 1080x1920) | MATCH | ledger 12 shots + 12-frame sheet re-viewed | ASR merged | NOT_LISTENED | VISUAL+TRANSCRIPT MAPPED, AUDIO PENDING |
Nothing here is "full AV sign-off". Audio listening is BLOCKED_CAPABILITY for this session; ASR is not listening. All 5: 24 fps, AAC audio; 4 are 1920x1080, Short is 1080x1920.

## Measured sound facts (OBSERVED, machine only)
- Per-shot mean level during narration sits in a narrow band, −18.0…−21.9 dB, median ≈ −19 dB in all five → constant voice level; no measured level step at cuts. Whether a music/ambience bed exists under the voice is UNKNOWN.
- Every long ends with a red end card whose mean level is ≈ −31 dB (−31.1…−32.0), i.e. ≈12 dB lower than speech; narration stops before the card (silences 292.2–293.9 / 223.8–225.6 / 150.6–152.3 / 256.7–257.3 s). Short ends with 0.8 s trailing silence then a one-frame blank (−72.8 dB).
- Only 1–3 silences ≥0.35 s per video: narration is essentially continuous. Pauses are not used as a beat device (INFERRED from ASR+silencedetect).

## Question → payoff chains (INFERRED from ASR + ledger + frames)
**Toaster / freezer (9VG0yqq_PHM)** — 0–8 s podcast question on a Q-card; 30–45 title card; 45–57 temperature axis (toaster ≫ freezer in absolute temperature, ~600 °C drawn as orange glow vs frost); 57–63 burnt toast; 75–105 fridge cutaway with red arrows: COP≈3 (E_out/E_in), toaster COP≈1, ~1000 W vs ~100 W → **consequence drawn as an energy-flow diagram**; 116–147 Winnipeg −20 °C night: the toaster still glows (state swap day→night grey) → punchline "to a toaster, all weather is cold" (147.6 s). Sound: continuous voice, ≈−19 dB.
**Last light (8fADp43wJwU)** — 0–8.7 Q card; 8.7–20.7 humans removed (red dotted figure on dark board = "gone"); 20.7–73 grid power fails (coal, nuclear, fuel-energy bar chart); 79–172 off-grid sources in turn (geothermal pipe room with rust, "<3 YEARS"; wind; hydro dam; batteries self-discharge); 172–220 solar call boxes; 228–285 radium/radioactive glow → cesium-137 tank "fade but keep same blue colour" (285 s payoff); end card 293.7. Consequence shown as **same object degrading with a time label**.
**Billion-story building (Z_xJ40QXu7Q, ledger-only)** — 0–20 Q (age-4½ asker); 34–58 tower strength/wind; 58–80 elevators/sky-lobby; 80–97 money; 97–151 "GOAL 1,000,000,000" scale; 151–183 centrifugal force (swing carousel → globe → Earth/Moon equal-effect); 183–221 orbit/escape-speed payoff ("view from the roof" 221.6); end 225.5.
**Mars oceans (FkUNHhVbQ1Q)** — 0–9.8 Q card + comment pile + chalkboard Earth/Mars; 9.8–22.8 red title card; 22.8–60 Mars water is frozen, Curiosity temps, phase diagram (red 0.06 atm line vs triple point); 60–127 water column dumped into Gale Crater, lake forms, Mt. Sharp island (map zoom); 127–171 coast/valley flooding, rover swept down slope, Hellas breakthrough, Perseverance hit by ice-rock waterfall (167–171 two-frame rover state change); 203–257 Olympus Mons, before/after planets, greenhouse reversal last line; end card 257.1.

## Mars pair: long (FkUNHhVbQ1Q) vs Short (2p305nzcVQE) — `MARS_PAIR_NARRATION_MAP.csv`
Method: ASR word-window alignment, all 41 Short segments matched ≥60 % (INFERRED; timings are ASR-estimated).
- **Narration kept: 41 % of long words.** Same voice track excerpt, re-sequenced.
- **Cut from long (≥8 words):** 0–7 s Q intro + 28 words; 30–60 Curiosity temps + phase diagram; 67–74 Arctic comparison; 106–111; 121–162 (trickle freezes, Phoenix/Viking, "I'm a big fan of maps", Valles Marineris, landers carried south = 41 s); 171–195 coastline chatter; 204–222 Olympus Mons/before-after; 229–243.
- **Moved:** the question sentence ("How would Mars change as the water accumulated?") plays at Short 11 s, not 8 s of the long; Short opens with the recap line ("In the previous What If…") that sits at long 11.8 s; the "ice-topped water" sentence order preserved.
- **Added/redrawn for 9:16:** no Q card, no comment pile, no red title card, no end card (ends on a one-frame blank); new cold open = label "PREVIOUSLY ON 'WHAT IF'" + chalkboard + stick figure; every wide scene re-composed to portrait (sky band on top, black ground below, subject kept centred); maps become landscape panels with the figure beneath; Gale-crater lake map rebuilt as a tall single-subject image; talking-figure presence kept in map beats; red cap on the water column kept (colour continuity).
- Chain preserved in Short: frozen Mars → water column in crater → elevation map → crater lake → Hellas/Perseverance waterfall → flow stops/ice layer → greenhouse caveat. The Short ends on an unresolved "Except maybe none of this would happen" hook, not the long's closing line (INFERRED: loop/retention device; UNKNOWN whether intended).
Rule extracted: a Short is a **re-sequenced excerpt with portrait re-composition**, not a re-edit of the long's frames.

## Diagnostic lessons used for the pilot (2 reference scenes)
1. Toaster COP diagram (75–105 s): cause drawn as **red arrows with a quantity label** → pilot adds red apex ticks + numbers.
2. Last-light rust scene (99–110 s): consequence shown as the **same object changed + a time/quantity label** → pilot keeps the same ball/mat and shows the shrinking apex staircase.
