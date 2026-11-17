# Visual CT scan — wBLVmEZV2Oc "How high could the magnitude of Earthquakes go?" (Short)

- Channel: xkcd's What If? `UC6IxnFzHofFJ5X2PycSMsww` (@xkcd_whatif); format SHORT (listed on /shorts tab, census 2026-11-04T01:43Z); published 2025-06-24 (first public Short).
- Source: `xkcd Channel/How high could the magnitude of Earthquakes go？ [wBLVmEZV2Oc].mp4`, sha256 `ffff4ea9…38f5b1`, 1080x1920 h264, 24/1 CFR, time_base 1/12288, 1,583 decoded frames, 65.958 s. A second local copy (corpus SRC04, YTDown 1080p) has different bytes (`61e3f985…`) and was not used.
- Mode: DEEP with frame-precise onsets. Status: **VISUAL_ANALYSIS_PARTIAL** (listening BLOCKED; 184 of 250 activity frames sampled rather than viewed; art review at tile scale). Reviewer: primary analyst (this session).

## 1. Coverage (MEASURED / OBSERVED)
All 1,583 frames measured (low-res global diff + full-res sparse-ink diff). 63 segments: 32 HOLD states (1,333 frames, each below the calibrated per-frame threshold and first-vs-last drift check; settled frame viewed) and 31 ACTIVITY events (250 frames; 66 viewed in tiles, 17 activities viewed at every frame). 20 periodic I-frame requantisation frames (every 168 frames = 7 s GOP) were absorbed as encoder artifacts by rule (no pixel changed ≥150, max diff <80); not visually viewed. See `coverage.json`.

## 2. Structure (OBSERVED)
5 shots (true composition swaps), 63 states/events. Mean shot length is not meaningful here: SH003 (8.54–55.67 s) is one continuous "magnitude ruler" diagram that carries 47 s of escalation.

| Time (s) | Shot | Narration (ASR, uncertified) | Visual job |
|---|---|---|---|
| 0–5.1 | SH001 | "The Richter scale, which has technically been replaced by the Moment Magnitude scale, measures the strength…" | Title + detailed seismograph; red strike-through write-on on RICHTER SCALE (1.46–1.79), corrected title typed on (2.00–2.33), seismograph swapped to "shaking" drawing with vibration ticks (3.46) |
| 5.1–8.5 | SH002 | "…somewhere between 3 and 9…" | Media collage (newspaper 3.5, phone 4.8, TV '8 on the Richter scale' / 'Uhm, actually…'); red circles mark the numbers (6.50–6.67) |
| 8.5–55.7 | SH003 | "…10 as the top… 0 as the bottom… no top or bottom… magnitude 9… 10… 11… 15… 18…" | Blank ruler → labels 10 and 0 pop on → cross-dissolve to an endless −20…35 ruler with a pause-to-read footnote (12.58–12.79) → ruler trucks left (14.96) → red hatching above 10 "might as well be" (16.63) → ruler parked at left edge with an arrow marker (18.29) → each magnitude = title swap + ruler scroll + one illustrative object + annotation pops |
| 55.7–58.7 | SH004 | "…the Death Star caused a magnitude 18 earthquake on Alderaan." | Cutaway TV joke frame (bun-haired anchor + sphere icon) |
| 58.7–65.96 | SH005 | "…the expanding cloud of space debris would be faster and hotter." | Back to spine layout, MAGNITUDE >18; 140-frame slow ruler scroll; final swap to more dispersed debris with radial speed lines; ends on a held drawing, no end card |

## 3. xkcd-specific findings (this video only)
- **Premise bounding:** the question is not spoken as "what if"; it opens on a correction joke (struck title) and a misconception collage, then states the bound ("there is no top or bottom") visually as a ruler that runs off both frame edges. (OBSERVED; function INFERRED)
- **Reasoning → visual steps:** one persistent measuring instrument (ruler spine, left 5–10 % of width) plus a moving arrow is the escalation device; each step adds exactly one object (globe, fault block, faulted globe, damaged globe, vapour ring, debris) and at most one annotation. (OBSERVED)
- **Labels/scale:** dimension arrow "3500 Km" (30.08 s) and dated epicentre labels (21.42 s) pop on as single frames after the object; numbers on screen match the ASR quantities (9.0–9.1/9.1–9.3; 3,500 km; 10^32 J). Narrated "half way around the world" is shown only as a fault line on a globe (no label). (OBSERVED)
- **Reveal timing:** write-ons occur for corrections and titles (strike, typed title, typed energy line, red hatching); objects and annotations are instant pops. Visual onsets fall near the matching ASR word (e.g. strike at 1.458 s, ASR "technically been replaced" 1.14–2.34 s), but sync is ASR_UNCERTIFIED. (OBSERVED onset / INFERRED sync)
- **Jokes:** deadpan relief stick figure "PHEW!" with crossed-out wave (44.88 s, "couldn't cause any tsunamis"); pop-culture cutaway (55.67 s); "BYE BYE EARTH" text gag; "UHM, ACTUALLY…" pedant gag. Stick figures appear only in jokes/insets, not as presenters. (OBSERVED)
- **Camera vs drawing vs cut:** cuts = full recomposition on the same off-white canvas (4 in 66 s); camera = ruler truck/scroll with the canvas otherwise static (G0022, G0026, G0034, G0040, G0044, G0052, G0060); drawing animation = write-on strokes or state swaps (shake marks, fractures). (OBSERVED)
- **Shorts compression:** 66 s, one continuous diagram for 72 % of runtime; no hook text card, no captions burned in, no end card. (OBSERVED)

## 4. Art direction (MEASURED palette; OBSERVED style)
Background exact `#F7F7F7`; 95.5 % of settled pixels in the brightest bin, black ink ~2.7 %, light grey fills (bin `#D0D0D0`) ~1 %; red accent (bin ~`#D03040`) in 7 of 32 holds, used only for correction/emphasis marks (strike, circles, hatching, epicentre rings). Mean dark-ink coverage per settled state 3.2 % (max 7.5 %). Hand-lettered all-caps titles; one small serif footnote block (only non-hand-lettered text). Objects (seismograph, fault block, globes) are drawn with far more detail than the stick figures — a deliberate contrast between diagram fidelity and minimal characters. Typeface identity, drawing software and layer structure are UNAVAILABLE from pixels.

## 5. Audio (UNAVAILABLE as listening)
faster-whisper small.en ASR: 20 segments covering 0–65.5 s; agrees with the catalog plaintext captions at word-sequence ratio 0.978 (264 of 271 caption words matched; `asr/asr_vs_catalog_caption.json`). ebur128 integrated −16.2 LUFS, LRA 1.7 LU, true peak −2.6 dBFS (MEASURED levels only). Music/SFX presence, delivery and pauses: UNAVAILABLE (no listening capability).

## 6. Counterexamples / uncertainties
- Onset of the red circle on the TV "8" is not bracketed (between f160 and f204; possibly coincident with absorbed frame f168). UNRESOLVED.
- G0022/G0026 motions: title fade + ruler translate could also be implemented as a zoom/crop; labelled as apparent truck (alternative: layer translate).
- 184 activity in-between frames were sampled, not viewed (write-on order inferred from first/last tiles).

## 7. Attention hypotheses (INFERRED, no metrics)
High-contrast red is reserved for "this is wrong / look here" marks, so it plausibly directs the eye to the corrected term and the misconception numbers. The persistent ruler arrow gives a constant progress cue across the escalation. No retention, CTR or gaze data exist for this video.
