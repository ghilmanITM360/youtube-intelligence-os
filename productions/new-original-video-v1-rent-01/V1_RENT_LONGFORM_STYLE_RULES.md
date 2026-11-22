# V1 Rent: reusable long-form production rules (what worked in R4)

Date 2026-11-21. Applies to the V1 Rent series and any landscape long-form for this channel project. Principles come from `CHANNEL_VISUAL_AUDIT/CHANNEL_001/22_LONGFORM_VISUAL_DNA.md`; this file records how they were applied and what to repeat. Status of evidence: the proof and the full 75 s were independently reviewed (`out_r4/PROOF_INDEPENDENT_REVIEW.md`, `out_r4/FULL_SEGMENT_INDEPENDENT_REVIEW.md`); the host art is a **provisional placeholder** until Codex delivers `codex_art/v2_rig/` (see `CODEX_HANDOFF_V2_LONGFORM_RIG.md`).

## Workflow that avoided another style-discovery loop
1. Read doc 22 before storyboarding or briefing art.
2. Re-block narration by meaning into beats (R4: 26 beats over 75 s, median 2.7 s, min 1.4, max 5.0). One focal subject per beat; the beat table lives in the renderer (`tools/v1r4_render.py`, `--storyboard` writes `STORYBOARD_R4_75s.md`).
3. Prove the system on a 15-20 s cut that ends on a silence, review it independently, fix, then scale. Rendering is cheap (75 s in about 15 s); the cost is review time, so review the proof, not every iteration.
4. Fixed the reviewer's P1/P2 items before scaling; kept R3 untouched as the baseline.

## Rules confirmed in use
| Area | Rule used | Note |
|---|---|---|
| Canvas | `#FDFDFD` default; the room plate in 1 beat (the "why does rent feel bigger" question) | host stays thin-bodied inside it |
| Host | separate body (3 poses) and head (5 drawings) layers, anchors in `rig_anchors.json`; any head on any body | head about 0.33 of figure height; no lip sync; head swap at a meaningful word |
| Time | content quantised to 24 fps steps inside a 30 fps file; pop = 3 frames (0.6, 1.1, 1.0 scale); draw-on for circles/arrows/brackets in 5 steps | data bars appear instantly (no growth through unlabeled heights) |
| Cuts | hard cut at every beat boundary; no idle bob; no continuous motion | still-frame share 86-87%, same range as the references |
| Graphics | flat wobbly-outlined shapes, red hand-drawn circle/arrow on the key figure, numbers at final value only | no rolling counters |
| Type | Marker Felt for labels and callouts, Helvetica 44 px for source tags; labels at least 5% of frame height (54 px), most 64+ | source tags need to be larger than first attempt (38 px was too small on phone) |
| Sources | every number carries its tag on the same beat; "derived" values labelled | claim register is the single source |
| Layout | host left (neck x 330-470), graphics right; source tags move bottom-right when the host is on the left, bottom-left otherwise | keep chart labels clear of the tag line |

## Defects found by review and how they were fixed (so they are not repeated)
- A hand-drawn bracket overlapped the top of the numbers and read as a strike-through. Keep annotations clear of numerals; place them over labels or the axis.
- Label appeared before the word it names ("typical" at 7.3 s). Time every label to the word in `t2_words_merged.json`.
- Bars with a pop animation showed partial heights. Data shapes use an instant appearance.
- Source tags 2.7% of frame height. Use 44 px at 1080p.

## Limits to remember
- The host art is a code-drawn stand-in. Final proportions and stroke must be re-checked when Codex files arrive (acceptance list in the handoff).
- Doc 22 rests on two host appearances and a pixel-level sample; do not over-fit (for example, 17-35 cuts per 75 s is a guide measured with a pixel-difference metric that also counts big pop-ins; our 25 beat cuts are real cuts, while the same metric reads higher because of pop-ins).
- No audience test.

## Second review round (full 75 s) and fixes
Independent review of the first full render: PASS WITH FIXES (`out_r4/FULL_SEGMENT_INDEPENDENT_REVIEW.md`). Fixed in `V1_RENT_R4_0-75s_v2.mp4`; the fixes were checked by me on stills, **not re-reviewed independently**.
- Brush font made "7" read as "1" (2.7% looked like 2.1%). Numerals now use Chalkboard SE Bold; keep hand-lettered type for words and an unambiguous face for digits.
- Red circles cut through numerals: circle size comes from the measured text width, centred slightly below the text box centre (`numcirc`).
- Shelter group raised clear of the source tag; U+2212 minus replaced by the word "minus" (Marker Felt has no glyph); source tag held through the repeat of the 2.8/2.7 chart.
- Five pop-ins retimed to the spoken word (MEASURES 29.8, ruler 29.85, "Not a" 64.5, "?" 31.5, "one piece" 38.3).
- Open P3 (not fixed): host drawn at three scales and thick torso (placeholder rig, final art to fix); room beat is 4.6 s against the 1-3 s guide; equal tiles at 38.0-39.9 s could imply equal weights; slope line at 71.4-75 s is unlabelled; check Marker Felt/Chalkboard font licences before publishing.

## Segment 2 (75-122.3 s) additions
- Fonts: Apple Marker Felt/Chalkboard SE replaced by OFL Patrick Hand and Caveat Brush (`FONT_LICENCE_NOTE.md`). Numerals in Patrick Hand (crossbar 7).
- Educational graphics that worked: mini houses for the sample, lease paper, panel chips, a month stepper, a drawn radical, a fraction, chips with arrows for a chain. Source tag on every beat, same two lines.
- Illustrative graphics must say so ("illustration, not to scale") and must not imply a real proportion (3 of 12 houses, not 5 of 12).
- A stepping animation needs 0.5 s per state and no blank lead-in; cut to a big number at the spoken word.
- Independent review of R4 v3 and R5 (`out_r5/INDEPENDENT_QA_R4v3_R5.md`): PASS WITH FIXES on both; the P2 fixes are in R4 v4 and R5 v2 and were checked by me on stills only.
