# ORIGINAL PRODUCTION PACKAGE — derived from the o3FQcd91MIs pattern (v2)

Separate from the forensic record (`state_spec_76.md`). **This package contains no source characters, logos, photos, illustrations, names or script.** It describes a *system* to build a NEW video. Every number below that came from the source is MEASURED (see `key_facts.json`); creative choices are RECOMMENDATIONS.

## 1. Reusable art-direction system
- **Canvas:** one flat near-white field `#FCFCFC` for ~84% of runtime; dark UI-card field `#1E2021`; section fields allowed only for definition cards and two full-bleed scenes (tan `#DEBA9B/#EFD2B2` + sky `#CBE9F9`; beige `#E1D4B3` + grey `#5D5C5B`); two black types — hold black `#110F10` (long holds) and pure `#000000` (2-frame dip). (MEASURED palette from the source; pick your own hues if you want a distinct brand, keep the *roles*.)
- **Line:** one marker weight (~6–8 px at 1280×720) with slight wobble; never vector-perfect.
- **Fill:** flat, no gradient, no shadow; one accent colour per state maximum (gold, green, red, orange).
- **Negative space:** median 4% of pixels covered on character states; keep ≥90% empty on white-canvas states.
- **Mixed media rule:** crude drawn characters + crisp real-looking evidence cards/photos is the contrast engine; evidence cards are rectangular, unframed, 25–60% of frame width.

## 2. Original character / illustration design principles
- LEAD: oversized circle head (≈ 1/3 body height), 3–5 hair marks, dot eyes, one-line mouth, thin stick body. Build ≥10 swap-in poses: neutral-arms-out, grin+prop-hold, hands-on-hips smug, crouch, flex, phone-to-ear (large), distressed (sweat marks), scowl, wave, cheer. **Pose changes are whole-asset swaps; no rig.**
- FOIL: distinct silhouette (different hair shape) with 3 poses (worried shrug, frown, neutral).
- Supporting heads: round heads only (no bodies) for group gags (5 expressions).
- Sage/meme figure and gag props are separate transparent PNGs; every prop ≤ 25% of frame height unless the beat is the prop itself.
- Faces: expression is carried by mouth line + brow marks only. Keep identical eye dot size across poses (continuity).

## 3. Typography, colour, layout, spacing rules
- Two typefaces (licensed): (a) rounded casual sans for statements/questions (~3.5–5% frame height); (b) hand-script for name tags, section captions, asides (~3–6%); micro-text asides ~1.2–1.5% only when the narration also says them.
- Name tag: script text top-left of head with a short arrow to the head, offset ~0.05 frame width.
- Question cards: single centred line, baseline at y≈0.50, margin ≥ 0.07 frame width each side.
- Two-line build: the second line sits ~0.07–0.12 frame height below the first and appears on a LATER cut (never animated in).
- Contrast: black on `#FCFCFC` ≈ 19:1; dark UI cards white on `#1E2021`. Minimum readable text 1.2% frame height; anything smaller must be spoken.
- Layout grid: subject low-centre-left (x 0.12–0.40); prop/evidence at right (x 0.45–0.75); end card title top-centre.

## 4. Scene / state specifications
See `original_prompts.md` (76 prompts, one per state, with per-state reconstruction requirements) and `state_spec_76.csv` for the forensic source facts that justify each. Style families used (count of states): F1 Pose-on-canvas (character + name tag) ×8, F10 Gag prop alone ×7, F11 End card ×1, F2 Pose + prop ×9, F3 Hand-drawn chart doodle ×4, F4 Text-only card ×15, F5 Evidence / UI card ×13, F6 Photo insert ×10, F7 Time-skip / split ×4, F8 Black beat ×3, F9 Full-bleed illustrated scene ×2.

## 5. Image-generation guidance
- Generate characters/props as isolated transparent-PNG layers with the STYLE anchor + the per-state prompt; reject any output with shading, gradients, photographic skin, or real brand marks.
- Keep a seed/reference sheet of LEAD (one approved head) and image-to-image from it for all poses to hold continuity.
- Evidence cards: build in a design tool or HTML mock-up with correct, cited data; never generate numbers with an image model.
- Photos: use licensed stock/own shoots; keep them small and rectangular.
- QA each asset at 100% zoom for outline weight consistency (±20%).

## 6. Motion / animation instructions (measured style = stepped)
- Interpolation: **hold (stepped) only**. No ease, no tween, no scale animation, no camera.
- A state change is one frame: frame N shows the old composition, frame N+1 the new. Additive elements appear on the cut frame with everything else unchanged (13 of 75 boundaries were purely additive).
- A 'zoom' is a swap to a larger-scale asset on one frame.
- Optional creative extension (NOT in the source): 4–6-frame ease-ins would look different from the measured style; apply only if the brand wants to diverge.

## 7. Transition timing, entry / hold / exit
- Entry: hard replace on the frame where the key word begins or up to 0.2 s before it (measured median lead −0.05 s, 63 of 78 events within ±0.2 s; ASR-only).
- Hold: state median 3.37 s, p10 1.6 s, p90 5.6 s; fastest state 20 frames (0.67 s). Cold open 24 changes/min, settling to 12–19/min.
- Exit: next hard replace; no fade/dissolve anywhere. Black holds: enter and exit by hard replace; hold 2.1–3.3 s; the voice continues.
- One special transition: 2 pure-black frames (`#000000`) then a new full-bleed scene — use sparingly as an 'arrival' beat.

## 8. Layering and compositing (per state)
Bottom→top: (1) canvas/field colour; (2) full-bleed scene if any; (3) evidence card or photo; (4) character layer; (5) props/gags; (6) arrows/circles/X marks (red, hand-drawn); (7) text (script then sans); (8) micro-asides. All layers hard-cut; no masks needed. Export each layer as PNG with alpha; keep canvas colour exact.

## 9. Narration-to-visual alignment procedure
1) Lock the voiceover first. 2) Auto-transcribe with word timestamps for a rough cue sheet (treat as ±0.2 s). 3) Place each hard cut on the cue word frame, then nudge 0–3 frames earlier for 'visual before word' beats (10 of 78 source events led by >0.2 s). 4) Have a human listen end-to-end and confirm sync and pronunciation before sign-off (not done for the source).

## 10. Editing timeline (derived from the source's measured structure)
CFR 30 fps, 1280×720. Frames/PTS below are the SOURCE's timings, offered as a pacing template (frame i has PTS (i+1)/30). Replace content, keep rhythm.

| State | Start f | End f | Hold (s) | Family | Entry | Prompt id |
|---|---:|---:|---:|---|---|---|
| S001.0 | 0 | 40 | 1.3667 | F1 | start of video (f0) | P-S001.0 |
| S001.1 | 41 | 173 | 4.4333 | F2 | FULL_COMPOSITION_REPLACE (hard cut) | P-S001.1 |
| S001.2 | 174 | 245 | 2.4 | F2 | ADDITIVE_ELEMENT_ENTRY (existing content unchanged) | P-S001.2 |
| S001.3 | 246 | 301 | 1.8667 | F3 | FULL_COMPOSITION_REPLACE (hard cut) | P-S001.3 |
| S001.4 | 302 | 398 | 3.2333 | F3 | ADDITIVE_ELEMENT_ENTRY (existing content unchanged) | P-S001.4 |
| S001.5 | 399 | 490 | 3.0667 | F10 | FULL_COMPOSITION_REPLACE (hard cut) | P-S001.5 |
| S001.6 | 491 | 543 | 1.7667 | F2 | FULL_COMPOSITION_REPLACE (hard cut) | P-S001.6 |
| S001.7 | 544 | 649 | 3.5333 | F6 | FULL_COMPOSITION_REPLACE (hard cut) | P-S001.7 |
| S001.8 | 650 | 738 | 2.9667 | F6 | ADDITIVE_ELEMENT_ENTRY (existing content unchanged) | P-S001.8 |
| S001.9 | 739 | 768 | 1.0 | F6 | ADDITIVE_ELEMENT_ENTRY (existing content unchanged) | P-S001.9 |
| S001.10 | 769 | 913 | 4.8333 | F6 | FULL_COMPOSITION_REPLACE (hard cut) | P-S001.10 |
| S001.11 | 914 | 998 | 2.8333 | F2 | FULL_COMPOSITION_REPLACE (hard cut) | P-S001.11 |
| S001.12 | 999 | 1121 | 4.1 | F7 | FULL_COMPOSITION_REPLACE (hard cut) | P-S001.12 |
| S001.13 | 1122 | 1230 | 3.6333 | F7 | FULL_COMPOSITION_REPLACE (hard cut) | P-S001.13 |
| S001.14 | 1231 | 1281 | 1.7 | F7 | ADDITIVE_ELEMENT_ENTRY (existing content unchanged) | P-S001.14 |
| S001.15 | 1282 | 1354 | 2.4333 | F4 | FULL_COMPOSITION_REPLACE (hard cut) | P-S001.15 |
| S001.16 | 1355 | 1405 | 1.7 | F4 | FULL_COMPOSITION_REPLACE (hard cut) | P-S001.16 |
| S001.17 | 1406 | 1540 | 4.5 | F1 | FULL_COMPOSITION_REPLACE (hard cut) | P-S001.17 |
| S001.18 | 1541 | 1672 | 4.4 | F7 | FULL_COMPOSITION_REPLACE (hard cut) | P-S001.18 |
| S001.19 | 1673 | 1805 | 4.4333 | F3 | FULL_COMPOSITION_REPLACE (hard cut) | P-S001.19 |
| S002.0 | 1806 | 1917 | 3.7333 | F5 | FULL_COMPOSITION_REPLACE (hard cut) | P-S002.0 |
| S003.0 | 1918 | 2061 | 4.8 | F4 | PARTIAL_REPLACE (some content persists) | P-S003.0 |
| S004.0 | 2062 | 2185 | 4.1333 | F5 | FULL_COMPOSITION_REPLACE (hard cut) | P-S004.0 |
| S005.0 | 2186 | 2509 | 10.8 | F5 | PARTIAL_REPLACE (some content persists) | P-S005.0 |
| S005.1 | 2510 | 2665 | 5.2 | F5 | FULL_COMPOSITION_REPLACE (hard cut) | P-S005.1 |
| S005.2 | 2666 | 2784 | 3.9667 | F5 | FULL_COMPOSITION_REPLACE (hard cut) | P-S005.2 |
| S005.3 | 2785 | 2894 | 3.6667 | F3 | FULL_COMPOSITION_REPLACE (hard cut) | P-S005.3 |
| S005.4 | 2895 | 2985 | 3.0333 | F1 | FULL_COMPOSITION_REPLACE (hard cut) | P-S005.4 |
| S005.5 | 2986 | 3034 | 1.6333 | F4 | ADDITIVE_ELEMENT_ENTRY (existing content unchanged) | P-S005.5 |
| S005.6 | 3035 | 3097 | 2.1 | F4 | ADDITIVE_ELEMENT_ENTRY (existing content unchanged) | P-S005.6 |
| S005.7 | 3098 | 3183 | 2.8667 | F1 | FULL_COMPOSITION_REPLACE (hard cut) | P-S005.7 |
| S005.8 | 3184 | 3275 | 3.0667 | F5 | FULL_COMPOSITION_REPLACE (hard cut) | P-S005.8 |
| S005.9 | 3276 | 3389 | 3.8 | F6 | FULL_COMPOSITION_REPLACE (hard cut) | P-S005.9 |
| S005.10 | 3390 | 3495 | 3.5333 | F2 | FULL_COMPOSITION_REPLACE (hard cut) | P-S005.10 |
| S006.0 | 3496 | 3635 | 4.6667 | F6 | FULL_COMPOSITION_REPLACE (hard cut) | P-S006.0 |
| S007.0 | 3636 | 3820 | 6.1667 | F5 | FULL_COMPOSITION_REPLACE (hard cut) | P-S007.0 |
| S007.1 | 3821 | 3928 | 3.6 | F5 | ADDITIVE_ELEMENT_ENTRY (existing content unchanged) | P-S007.1 |
| S007.2 | 3929 | 4057 | 4.3 | F10 | FULL_COMPOSITION_REPLACE (hard cut) | P-S007.2 |
| S008.0 | 4058 | 4312 | 8.5 | F5 | FULL_COMPOSITION_REPLACE (hard cut) | P-S008.0 |
| S009.0 | 4313 | 4332 | 0.6667 | F4 | FULL_COMPOSITION_REPLACE (hard cut) | P-S009.0 |
| S009.1 | 4333 | 4380 | 1.6 | F4 | ADDITIVE_ELEMENT_ENTRY (existing content unchanged) | P-S009.1 |
| S009.2 | 4381 | 4446 | 2.2 | F4 | ADDITIVE_ELEMENT_ENTRY (existing content unchanged) | P-S009.2 |
| S009.3 | 4447 | 4548 | 3.4 | F10 | FULL_COMPOSITION_REPLACE (hard cut) | P-S009.3 |
| S009.4 | 4549 | 4608 | 2.0 | F10 | PARTIAL_REPLACE (some content persists) | P-S009.4 |
| S009.5 | 4609 | 4665 | 1.9 | F4 | FULL_COMPOSITION_REPLACE (hard cut) | P-S009.5 |
| S009.6 | 4666 | 4716 | 1.7 | F4 | FULL_COMPOSITION_REPLACE (hard cut) | P-S009.6 |
| S009.7 | 4717 | 4805 | 2.9667 | F2 | FULL_COMPOSITION_REPLACE (hard cut) | P-S009.7 |
| S009.8 | 4806 | 5035 | 7.6667 | F5 | FULL_COMPOSITION_REPLACE (hard cut) | P-S009.8 |
| S009.9 | 5036 | 5101 | 2.2 | F2 | FULL_COMPOSITION_REPLACE (hard cut) | P-S009.9 |
| S009.10 | 5102 | 5258 | 5.2333 | F10 | FULL_COMPOSITION_REPLACE (hard cut) | P-S009.10 |
| S009.11 | 5259 | 5305 | 1.5667 | F6 | FULL_COMPOSITION_REPLACE (hard cut) | P-S009.11 |
| S009.12 | 5306 | 5353 | 1.6 | F6 | ADDITIVE_ELEMENT_ENTRY (existing content unchanged) | P-S009.12 |
| S009.13 | 5354 | 5397 | 1.4667 | F6 | ADDITIVE_ELEMENT_ENTRY (existing content unchanged) | P-S009.13 |
| S009.14 | 5398 | 5552 | 5.1667 | F1 | FULL_COMPOSITION_REPLACE (hard cut) | P-S009.14 |
| S010.0 | 5553 | 5652 | 3.3333 | F8 | BLACK_HOLD_ENTRY | P-S010.0 |
| S011.0 | 5653 | 5721 | 2.3 | F4 | BLACK_HOLD_EXIT | P-S011.0 |
| S012.0 | 5722 | 5783 | 2.0667 | F8 | BLACK_HOLD_ENTRY | P-S012.0 |
| S013.0 | 5784 | 5903 | 4.0 | F2 | BLACK_HOLD_EXIT | P-S013.0 |
| S014.0 | 5904 | 5983 | 2.6667 | F8 | BLACK_HOLD_ENTRY | P-S014.0 |
| S015.0 | 5984 | 6042 | 1.9667 | F4 | BLACK_HOLD_EXIT | P-S015.0 |
| S016.0 | 6043 | 6186 | 4.8 | F5 | FULL_COMPOSITION_REPLACE (hard cut) | P-S016.0 |
| S017.0 | 6187 | 6486 | 10.0 | F10 | FULL_COMPOSITION_REPLACE (hard cut) | P-S017.0 |
| S017.1 | 6487 | 6594 | 3.6 | F4 | ADDITIVE_ELEMENT_ENTRY (existing content unchanged) | P-S017.1 |
| S017.2 | 6595 | 6920 | 10.8667 | F5 | FULL_COMPOSITION_REPLACE (hard cut) | P-S017.2 |
| S017.3 | 6921 | 6961 | 1.3667 | F4 | FULL_COMPOSITION_REPLACE (hard cut) | P-S017.3 |
| S017.4 | 6962 | 7068 | 3.5667 | F2 | FULL_COMPOSITION_REPLACE (hard cut) | P-S017.4 |
| S017.5 | 7069 | 7159 | 3.0333 | F1 | FULL_COMPOSITION_REPLACE (hard cut) | P-S017.5 |
| S017.6 | 7160 | 7232 | 2.4333 | F1 | FULL_COMPOSITION_REPLACE (hard cut) | P-S017.6 |
| S018.0 | 7235 | 7404 | 5.6667 | F9 | BLACK_DIP_2F_THEN_REPLACE | P-S018.0 |
| S019.0 | 7405 | 7566 | 5.4 | F1 | FULL_COMPOSITION_REPLACE (hard cut) | P-S019.0 |
| S020.0 | 7567 | 7654 | 2.9333 | F9 | PARTIAL_REPLACE (some content persists) | P-S020.0 |
| S021.0 | 7655 | 7804 | 5.0 | F6 | FULL_COMPOSITION_REPLACE (hard cut) | P-S021.0 |
| S021.1 | 7805 | 7990 | 6.2 | F5 | FULL_COMPOSITION_REPLACE (hard cut) | P-S021.1 |
| S021.2 | 7991 | 8102 | 3.7333 | F10 | FULL_COMPOSITION_REPLACE (hard cut) | P-S021.2 |
| S021.3 | 8103 | 8169 | 2.2333 | F4 | FULL_COMPOSITION_REPLACE (hard cut) | P-S021.3 |
| S021.4 | 8170 | 8337 | 5.6 | F11 | FULL_COMPOSITION_REPLACE (hard cut) | P-S021.4 |

Intra-state element entries (cut inside a state): S007.1 at f3855 (128.5333 s): TEXT_ENTER: bold green percentage appears below the duration line; S009.2 at f4417 (147.2667 s): ICON_ENTER: tiny stick-figure icon appears right of the equals sign; S009.8 at f4916 (163.9 s): TEXT_ENTER: bold word appears above the cash-pile character.

## 11. Continuity constraints
- Same LEAD face construction in every pose; same outline weight; same canvas colour.
- Reuse (callbacks) are deliberate: prop alone at open and close; the 'answer' doodle twice; the two-character complaint twice; small-pose opening echoed before the final contrast; identical question card twice. Plan these as repeated assets, not new ones.
- Section grammar: single-line question card → explanation state(s) → evidence card → character reaction.
- Do not change position of a persistent element between consecutive states unless the beat is a swap.

## 12. Asset inventory (minimum build list)
- LEAD poses ≥10; FOIL poses 3; round-head set 5; gag props ≈25 (prize+banner, baby+flame, coin blob, flames, plaque+snowfall, cash pile, poker table+chips, laptop/desk character, hooded sage, etc. — all original); arrows (straight, curved, brush), circles, X; zig-zag divider; 2 full-bleed scenes; ≈12 evidence cards (UI, article, spreadsheet, definition, quote); ≈10 photo inserts; end card; 2 licensed fonts.

## 13. Production implementation recommendations
- Build in any NLE/compositor with a 30 fps CFR sequence; use *hold* keyframes or simply stacked clips cut on frames. A scripted route (Python + OpenCV/ffmpeg compositing from a JSON state list) is feasible because there is no motion: one JSON row per state (assets, positions, in-frame, out-frame).
- Budget: ~76 compositions for 4.6 min; roughly 60–80% reuse of character poses.
- QA: re-run the measurement pipeline (`measure_frames.py`, `episodes.py`) on your render; target ≥95% of episodes single-frame; I-frame refresh blips at ~4 s are encoder behaviour, not an edit.
- Originality review before publish; a human watches/listens end to end.
