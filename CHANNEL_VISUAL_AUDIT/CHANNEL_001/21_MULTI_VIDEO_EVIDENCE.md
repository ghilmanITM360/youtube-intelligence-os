# 21 MULTI-VIDEO EVIDENCE — CH001 (T1 numeric pass; 4 selected + 2 holdouts + reference)

Method: ffmpeg decode at 6 fps (cuts, palette, bands) and 4 fps (row-ink profile per 5% of height); numpy only. Tools/raw: `MULTI_VIDEO_MEASUREMENTS/` (an.py, prof.py, multi.json). **Numeric only: no frame was viewed, no shot-level blueprint, no scene taxonomy per video.** This is a T1 pass, NOT a deep analysis; deep_analysis_done stays "no" in the register.

| Video | Role | Res | Dur s | Bg | Cuts/10s | Static frac | Content band (% height) | Caption band 65-75% | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 10nEByVLya0 | reference (deep) | 1080x1920 | 55.3 | #FDFDFD | 1.6 | 0.60 | 35-65 | yes (dark 0.09 at 40-50 is in-band art) | baseline |
| 33NVvWsGt9k | selected | 1080x1920 | 49.5 | #FCFCFC | 0.4 | 0.92 | 35-60 | **absent** | near-static; green/orange accents |
| 1eTwFcXq1iw | selected | 1080x1920 | 89.5 | #FDFDFD | 0.9 | 0.76 | 35-75 | yes | plus ~2% ink on every row (side element/border?) and a dmax 89.6 hard cut (likely full-frame change) |
| 02f598d4 | selected | 360x640 | 67.2 | #FDFDFD | 1.3 | 0.80 | 20-60 | text at 65-75 (weak) | low-res re-upload (SnapYT) |
| 3132dfa8 | selected | 720x1280 | 62.8 | #FDFDFD | **5.1** | 0.71 | **full height** (5-95) | none separable | dense, dark ink 5-14% every band; different family |
| xdF8HOwCgTU | holdout | 1080x1920 | 91.2 | #FCFCFC | 0.5 | 0.81 | 35-65 | **absent** | skin-tone accents |
| zLvSl1irqtU | holdout | 1080x1920 | 47.8 | #FDFDFD | 0.8 | 0.90 | 35-65 | **absent** | green + orange accents |

## Holdout prediction test (rules from 10nEByVLya0 only)
| Prediction (from 05/13) | Holdout xdF8 | Holdout zLv | Verdict |
|---|---|---|---|
| bg #FDFDFD | #FCFCFC | #FDFDFD | PASS (2/2, +-1 level) |
| art confined to ~35-65% height | 35-65 | 35-65 | PASS (2/2) |
| burned-in caption block at y~1353 | absent | absent | **FAIL (0/2)** |
| cut rate ~1.6/10 s (accept 0.8-3.2) | 0.5 | 0.8 | **FAIL/borderline (0.5 out, 0.8 at edge)** |
| static fraction ~0.6 | 0.81 | 0.90 | FAIL (more static) |

Result: bg and band rules generalise on 1080x1920 originals; **caption rule does not** (captions appear in 10nE and 1eTwFcXq1iw, not in 33NV/xdF8/zLv at the measured band; captions inside the art band are UNVERIFIED because no frame was viewed or OCR'd). Cut-rate is slower than the reference in 5 of 6 other videos.

## What changes in the rulebook
- 05_VISUAL_DNA: bg + band rules gain support (now 6 of 6 1080-ish videos for bg; 4 of 4 for band on 1080x1920). Palette: new accents seen (green #307030/#309050, orange #F09010, skin #F0D0B0, blue #3090B0/#50B0D0) = UNVERIFIED roles.
- 06/13: pacing is NOT one number; observed cuts/10s 0.4-5.1. Pacing must be a per-family parameter (decision-engine rule DE-pacing downgraded to hypothesis).
- 12/10: 3132dfa8 shows a full-bleed dense family (720x1280, 5.1 cuts/10 s) the reference does not cover.
- Per register trigger ("spot check reveals new family"): holdouts did reveal differences -> expand deep set by 3 (33NV, xdF8, zLv are now candidates for T2 visual-state extraction), do not call holdouts "blind" any more once used for fixes.

## Honest limits
Single numeric pass; no shot lists; "caption absent" = no dark ink in 65-75% band, not proven absent; static fraction counts frames with mean diff <1; cut = mean abs diff >18 at 6 fps (can miss soft cuts, can count fast motion). No audio used.

## T2 visual-state extraction (2026-11-20, numeric)
Method: 6 fps, ink-mask IoU vs state anchor < 0.80 starts a new state; per state t0/t1, ink fraction, bbox, saturated fraction. CSVs: `MULTI_VIDEO_MEASUREMENTS/states_<id>.csv`; script `states.py`. States are ink-change segments, NOT verified shots (motion inside a shot splits it; soft changes merge).
| Video | States | Mean dur s | Median dur s | Reading |
|---|---|---|---|---|
| 33NVvWsGt9k | 28 | 1.77 | 1.75 | slow, regular; talking-head-like beats |
| zLvSl1irqtU | 25 | 1.91 | 1.17 | slow |
| xdF8HOwCgTU | 85 | 1.07 | 0.83 | long (91 s) with steady state changes |
| 3132dfa8 | 78 | 0.81 | 0.17 | many sub-0.3 s states = continuous motion/animation family |
| 1eTwFcXq1iw | 129 | 0.70 | 0.50 | busiest; full-frame change at dmax 89.6 |
| 02f598d4 | 56 | 1.20 | 0.59 | low-res |
Reference 10nEByVLya0: 61 states in 55.4 s (mean 0.91 s). So state rate ranges 0.5-1.4 states/s except 3132dfa8 (continuous motion) - the reference sits mid-range, not typical of the slow 33NV/zLv pair.
Known defect: the `accent` column in the CSVs is a coarse 40-level quantisation with a hex-format overflow on some values (e.g. 7-digit strings); do NOT use it as palette evidence. Palette evidence remains the median-cut/quantised table in the T1 section.
Still not done for these videos: shot-by-shot blueprints, asset inventory, character/camera/edit grammar, any frame viewing. deep_analysis_done remains "no".

## OCR caption-position check (2026-11-20; tesseract CLI, frames sampled every 3 s, conf>60, alphabetic words >1 char; script `ocr.py`)
Word y-position histogram, 192-px bins over the 1920 height (bins 0-9; bottom caption zone = bins 6-7, y 1152-1536):
| Video | Frames / with text | Words | Words in bins 4-5 (y 768-1152, art band) | Words in bins 6-7 (y 1152-1536) | Verdict |
|---|---|---|---|---|---|
| 10nEByVLya0 (control) | 18/18 | 341 | 283 | 58 | bottom captions present (control OK) |
| 1eTwFcXq1iw | 28/30 | 289 | 144 (+47 in bin 3) | 98 | bottom captions present |
| 33NVvWsGt9k | 8/17 | 26 | 26 | 0 | **no bottom captions**; little text |
| xdF8HOwCgTU | 12/30 | 211 | 153 (+61 bin 3) | 2 | **no bottom captions**; text lives in art band/above |
| zLvSl1irqtU | 8/16 | 123 | 119 (+3 bin 3) | 1 | **no bottom captions** |
Conclusion (now OCR-supported, no longer "UNVERIFIED"): burned-in bottom caption block exists in 2 of 5 checked 1080x1920 videos (10nE, 1eTw). Holdout caption prediction stays FAIL 0/2, and the cause is real absence, not in-band captions. In-band text (labels/bubbles/numerals) is common (xdF8: 211 words in 12 frames) -> text-in-art is a separate asset class to characterise. Limits: 3 s sampling can miss short captions; OCR misses stylised fonts; control video detected only 58 bottom words, so recall is partial.
Rulebook consequence: 13/14 caption rule = family-conditional (captioned family: 10nE, 1eTw; uncaptioned: 33NV, xdF8, zLv). Novel scenes must declare family and not always add captions.

## Metric note (2026-11-20)
"Cuts/10 s" (mean abs diff >18) is area-sensitive and undercounts cuts in small-ink scenes (NS3/NS4 render 0.0 despite scheduled changes). Treat the T1 cut column as a coarse large-change count only; pacing parameter for rules = states/s (T2). Reference states/s: 10nE 1.10; 33NV 0.57; zLv 0.52; xdF8 0.93; 1eTw 1.44; 02f5 0.83; 3132dfa8 1.24 (continuous motion).

## T3 per-state measurement: 33NVvWsGt9k (28 states; `SCENE_BLUEPRINTS/33NVvWsGt9k_T3_state_measurements.csv`, script `t3.py`)
Per state at full 1080x1920: ink fraction, bbox, top-3 quantised colours of non-bg pixels, OCR text. Numeric + OCR only; no frame viewed; OCR text is noisy and only partly reliable.
Findings:
- **Different family from 10nE**: most states are large flat colour panels - green #309050 (S002-S006, S020; 54-83% of ink) and orange #F09010 (S012-S015, S017, S022-S023; 46-71%) - with black ink 11-44% over them. 10nE has white background with small coloured accents. So the same channel mixes (a) white-canvas drawn scenes and (b) full-panel meme/clip scenes.
- **Text is in-art dialogue/subtitle text** (OCR: "we like LET'S GOOOO!", "my time to SHINE", "I'm nervous", "oh yes! My specialty!", "Free? could try it then...", "INTERNATIONAL MONETARY ... EL SALVADOR", "$30"), not a bottom caption block. Topic: El Salvador / Bitcoin / IMF (story + meme-style character clips, S007-S011 skin-tone #F0B090 + beige #B09070 states look like a photo/clip scene).
- Colour roles per state: dark-dominant (#101010 30-87%) states S001, S007-S011, S016, S024-S028 (footage/photo/sketch-like); panel states S002-S006, S012-S015, S017-S023.
- Content band widens beyond 10nE: bbox y 712-1263 (10nE 655-1265) - similar vertical band; panels fill band width.
- Durations: median 1.67 s, range 0.33-3.83 s; hard reset between panels (S011->S012 0.33 s flash).
Rulebook impact: 05_VISUAL_DNA palette is NOT channel-wide - add "panel-fill" family with green/orange fills; 06 storyboard grammar must cover dialogue-panel scenes; assets 07/08 gain "third-party clip/meme panel" asset class (stand-ins only in recreations). Still no reconstruction test for this family (coverage gap).

## T3 per-state measurement: zLvSl1irqtU (25 states), xdF8HOwCgTU (85), 3132dfa8 (78) (same method/limits as 33NV; CSVs in SCENE_BLUEPRINTS/)
| Video | Dark-dominant states | Mean ink frac | Colours >30% of a state's ink (state count) | OCR text samples (noisy) | Family reading |
|---|---|---|---|---|---|
| zLvSl1irqtU | 10/25 | 0.045 | orange #F09010 (5), skin #F0D0B0 (3), green #307030 (2) | "become MILLIONAIRE!", "The Greater Fool Theory", "Understanding the Greater Fool Theory in..." | mixed: orange panels + title/slide text + drawn characters; slide-title cards |
| xdF8HOwCgTU | 41/85 | 0.050 | skin #F0D0B0 (16), red-orange #F05030 (8), orange (5) | "MicroStrategy" repeated across many states | character/face-driven with repeated brand/logo overlay text; long, many states |
| 3132dfa8 | 32/78 | **0.172** (3x denser) | skin (12), gold #D0B030 (7) | "US Secretary of the Treasury", "David ... Kennedy" | document/photo/news-montage family (screenshots with printed text), dense |
Cross-video summary (6 videos with per-state data incl. 33NV, excl. 10nE already deep): at least four distinct families: (A) white-canvas drawn story + bottom captions (10nE, 1eTw); (B) slow white-canvas with panels/character beats and no captions (33NV, zLv, xdF8); (C) dense document/photo montage (3132dfa8); (D) low-res re-upload (02f598d4, family unconfirmed). 10nE is one family out of >=3-4, which caps what a 10nE-only rulebook can claim.
Palette across videos: bg #FDFDFD/#FCFCFC constant; skin #F0D0B0 recurs (5 of 6 videos); orange #F09010 recurs (33NV, zLv, xdF8); green #307030/#309050 (33NV, zLv, 10nE); red-orange #F05030 (xdF8). Roles UNVERIFIED (no frame viewing).

## Unified family gate (gate.py, 2026-11-20) — correction of the "panel-fill" reading
`MULTI_VIDEO_MEASUREMENTS/gate.py FILE.mp4...` runs states/s, dark-ink share, bottom-caption, content rows and green/orange pixel share with one code path for refs and renders (render time for a 24 s scene is ~28 s, so rendering is not a bottleneck).
| Video | s/state | dark share of ink | caption | rows | green | orange |
|---|---|---|---|---|---|---|
| 33NV ref | 1.83 | 0.25 | no | 710-1180 | 0.005 | 0.002 |
| zLv ref | 1.91 | 0.21 | no | 720-1220 | 0.012 | 0.005 |
| xdF8 ref | 1.05 | 0.37 | no | 685-1220 | 0.000 | 0.002 |
| 10nE ref / v14 render | 0.55 / 0.53 | 0.32 / 0.27 | yes / yes | 655-1405 / 650-1405 | - | - |
| NS3 | 2.18 (ref 33NV 1.83: -19%, FAIL) | 0.12 | no | 695-1215 | 0 | 0 |
| NS4 | 0.69 | 0.19 | yes | 690-1380 | 0 | 0 |
| NS5 (old, full-width panels) | 1.87 | 0.24 | no | 695-1220 | **0.079** | **0.036** |
| NS5 (shrunk, k=0.45) | 1.87 | 0.55 (FAIL, ref 0.21-0.37) | no | 695-1220 | 0.014 | 0.006 |
**Finding:** reference green/orange regions are ~2-4% of frame (T3 ink_frac 0.017-0.047), not full-width panels; the NS5 v2 panels were ~10x too large. The family label "panel-fill" is therefore an over-reading: it is "coloured shape + black dialogue text". NS5 panels were shrunk (original art); green/orange share is now near the reference, but dark-ink share overshoots (text is too large relative to the shapes). Panel scale vs text share trades off (k=0.6: dark 0.45, green 0.025); stopped tuning to avoid another metric-chase loop. Open: reduce hand-font size and re-gate. Earlier NS5 "PASS" in NOVEL_SCENE_QA round 3 holds only for no-caption/band/state-rate.
**NS5 final (text 0.6x, dark box 0.5x):** s/state 1.87, dark share 0.23 (ref 0.21-0.37 PASS), no caption PASS, rows 755-1165 (ref 685-1220: narrower), green 0.015 / orange 0.007 (ref max 0.012 / 0.005: slightly high). The dark share was driven by two large dark boxes, not text (text 0.6x moved it 0.55 -> 0.54). Metric proxies now all near reference; still not independent evidence, no blind visual comparison.

### NS6 family C dense montage (render_novel4.py, original cards/charts/coins, 20 s, silent) vs 3132dfa8 via gate.py
| | s/state | dark share | rows | caption flag |
|---|---|---|---|---|
| 3132dfa8 ref | 0.79 | 0.42 | 125-1915 | True (dense content trips the 65-80% dark test; flag unreliable for family C) |
| NS6 | 0.80 (beat length 0.8 s set by construction) | 0.52 (+24%, FAIL) | 140-1900 | True (same artefact) |
First pass drift was too fast (0.17 s/state, every frame a new state); slowed to 0.12 px/frame. Proxy-only: no content semantics, no blind visual comparison, motion is linear drift (ref motion type unmeasured).

### NS6 dark-share tuning (stopped, not converged)
Dark share vs fill colour is a step function (dark = max channel <70): bars+coins (25,25,25)/(55,55,55) 0.49; both (85)/(90) 0.13; coins (50) + bars (85) 0.26; ref 0.42. Not matched; the reference's top colours (#303030 46%, #101010 31%) show real art uses mid-dark fills, so a fill-colour mix near (48) would be the next try. Proxy only.

### Audio as timing reference (internal; `audio_sync.py`, silencedetect -32 dB / 0.12 s vs visual-state boundaries, random baseline 5000 points)
| Video | family | boundaries | median dist to pause edge real / random | within 0.2 s real / random |
|---|---|---|---|---|
| 33NV | B | 26 | 0.12 / 0.53 | 0.62 / 0.28 |
| zLv | B | 24 | 0.20 / 0.58 | 0.50 / 0.24 |
| xdF8 | B? | 86 | 0.74 / 0.81 | 0.34 / 0.19 |
| 10nE | A | 100 | 0.72 / 0.71 | 0.27 / 0.22 |
| 1eTw | A | 126 | 0.40 / 0.38 | 0.37 / 0.33 |
**Finding (new, family-conditional hypothesis):** in the slow family B videos (33NV, zLv) visual state changes land on speech-pause edges well above chance; in the fast family A videos (10nE, 1eTw) they do not (boundaries fall inside speech, likely word-onset driven, which a pause detector cannot see). Rule candidate: family B cut on pauses; family A cut on word onsets (needs ASR word times, not measured). Caveats: 2 supporting videos, one threshold, correlation not causation, states are ink-change segments not verified shots.

### Word-onset test (`onset_sync.py`; Whisper word times: base for 4 videos, small_en for 10nE) — hypothesis NOT supported
| Video | fam | bounds | within 0.1 s of word onset real / random | within 0.1 s of word end real / random |
|---|---|---|---|---|
| 10nE | A | 100 | 0.62 / 0.56 | 0.51 / 0.59 |
| 1eTw | A | 126 | 0.67 / 0.59 | 0.57 / 0.62 |
| 33NV | B | 26 | 0.50 / 0.55 | 0.38 / 0.58 |
| zLv | B | 24 | 0.62 / 0.59 | 0.33 / 0.60 |
| xdF8 | B? | 86 | 0.65 / 0.60 | 0.53 / 0.63 |
Word density is ~3 words/s, so random points already sit within 0.1 s of an onset 55-60% of the time: the test has little power. Family A shows +6/+8 pts, inside sampling noise (SE ~0.05). Conclusion: the "family A cuts on word onsets" candidate is **unsupported**; no timing rule for family A is established. Family B: only the pause-edge alignment (previous section) stands. Word timestamps are Whisper-base grade (+-0.1-0.2 s), too coarse to resolve this at 6 fps state resolution.

## VISUAL QA CORRECTION (2026-11-20 evening) — first pass where pixels were actually viewed
Tooling: Read tool opens JPEG (PNG fails). `cmp_frames.py` (ref | render | diff), `contact_sheet.py`; sheets saved in `VISUAL_QA/`.
**Family taxonomy was wrong.** Numeric families A-D (white-canvas story / "panel-fill" / dense montage / low-res) came from ink statistics. Viewing 33NV, zLv, 3132dfa8, 1eTw, 02f598d4 shows ONE shared grammar:
white canvas, ONE focal subject per beat (photo plate / document screenshot / cartoon prop / stick figure), red-arrow + lettered annotation, thick black outlines, hard cuts + staggered pop-ins (bubble, second character, arrow ~0.6 s apart inside a beat).
Families differ mainly in CAPTION treatment: 3132 hand-lettered top lines with a red highlight word; 1eTw plain sans bottom caption (~67% H); 02f598d4 sans title on top + sans bottom caption; 33NV none (tiny dialogue in bubbles); 10nE Comic-style bottom caption.
Consequences: "green/orange panels" (B) are organic illustrated props (country-blob character, shop, coin mascot), not rectangles; "dense montage" (C) is not a random card pile; B/W third-party photos inflate the dark-ink share in C.
**Void:** NS5 (rectangles) and NS6 (random cards/charts) passed only numbers; they look nothing like the references. Their PASS/credit is void permanently.
**Replacements (render_novel5.py, original art only):**
| test | visual vs ref (viewed) | pacing s/state | other gate numbers | verdict |
|---|---|---|---|---|
| NS5_v2 retire-early (family B) | same grammar: blob character, house, stick man + bubble, coin mascot; ref props have richer detail | 2.00 (ref 1.83) | no caption OK, rows 665-1190 (ref 710-1180), dark 0.14 (ref 0.25), green 0.008 (ref 0.005) | grammar PARTIAL PASS; craft gap |
| NS6_v2 emergency-fund (family C) | same grammar: plate, badge+pot, man+bubble+2nd character, card+check, rotated plate+bubble; ref lettering/outlines heavier, characters more expressive | 1.20 (ref 0.79, 52% slow) | dark 0.06 vs 0.42 NOT comparable (ref plates are real B/W photos), rows 200-1425 (ref 125-1915) | grammar PARTIAL, pacing FAIL; not PASS |
Not tuned to numbers: dark share was deliberately NOT adjusted.
**Motion finding (E42):** ref motion is 24 fps content in a 30 fps file (every 5th frame in motion duplicates). Measured only in SH005; other shots not yet quantised.

## Independent review #1 + 24 fps census (2026-11-20)
Read-only vision subagent: 6 PASS / 16 PARTIAL / 2 FAIL on v19 (VISUAL_QA/independent_review_1.md); NS5_v2 FAIL, NS6_v2 PARTIAL-leaning-FAIL as same-channel. E42 generalised (dup_frames.py): 84 dup frames/16 segments in 10nE, v19 reproduced 7. Not yet measured on other videos.
