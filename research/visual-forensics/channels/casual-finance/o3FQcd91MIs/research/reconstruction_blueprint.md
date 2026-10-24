# Reconstruction blueprint — NEW ORIGINAL production system derived from o3FQcd91MIs

Source video: `o3FQcd91MIs` · sha256 prefix `82ab2b63` · 1280×720 · CFR 30 fps · 277.93 s · 8,338 frames.
Mode: `RECONSTRUCTION` (on top of `DEEP + CT_SCAN`). The source was viewed natively (76 state frames + 12 frame-by-frame transition windows). This blueprint specifies a **new original asset and motion system** that reproduces the *pattern*, never the artwork, characters, names, logos, photographs or script of the source. Every rule below carries an evidence label.

> Legal / originality guardrail: do not reuse "Dave", "Eve", the exact joke props, the third-party photos, brand logos, film posters, or the script. Replace with an original cast, original gags and licensed or self-made imagery. Third-party screenshots (quote cards, news articles, forum posts) in the source are evidence of *format*, not assets to copy.

## 1. Canvas and global specs (MEASURED)

| Parameter | Value | Label |
|---|---|---|
| Frame | 1280×720, 30 fps CFR, H.264 | MEASURED |
| Default canvas | near-white `#FCFCFC`, ≈90–94% of pixels in character states | MEASURED (k-means, 10 frames) |
| Dark UI cards | `#1E2021` field (search / quote / AI-overview captures) | MEASURED |
| Hard black beat | `#110F10` (not pure `#000`), 3 full-frame holds | MEASURED |
| Section colour fields | light blue `#90B7F9` (definition card); beach scene tan `#DEBA9B`/`#EFD2B2` + sky `#CBE9F9`; restaurant-chain beige `#E1D4B3` | MEASURED |
| Skin tone (cartoon) | `#F2D5B6`–`#EED1B7` | MEASURED |
| Accent colours | gold trophy `#EAAD2B`, green chart `#4FAE57`, red `#E53A2D`/`#E62B2C` (flames, X, subscribe) | MEASURED |
| Content coverage | median 4.05% non-canvas pixels on white-canvas states (extreme negative space) | MEASURED |
| Camera | none (no pan/zoom/shake); "zoom" is a hard scale replace | OBSERVED + MEASURED |

## 2. Asset system to build (all original)

1. **Lead character** — flat-colour stick figure with oversized round head, 3–5 mark hair, dot eyes, single-line mouth, irregular wobbly black outline (≈6–8 px), no shading. Build 8–10 expression/pose PNGs (neutral, grin, smug, distressed, flexing, phone-on-ear, shrug, crouch, cheering, scowl) as **separate transparent layers** so each cut swaps a whole pose (no skeletal rig needed). *Evidence: Dave appears in 25 of 47 shots, ~142 s on screen; poses change only at hard cuts.* (OBSERVED)
2. **Foil character** — second stick figure with a different silhouette cue (bob hair) and 3 poses (worried shrug, frown, neutral). (OBSERVED function: reacts / delivers the "rigged" complaint.)
3. **Labels** — handwritten name tag + hand-drawn arrow pointing at the subject's head; handwritten script for names and asides, rounded comic-style sans for typed statements (OBSERVED; font identity INFERRED, not claimed). Use two licensed fonts: one hand-script, one rounded sans.
4. **Hand-drawn data graphics** — axes + coloured polyline charts with a legend (square swatch → label), red circle annotation, thick brush arrows, red X, time-skip caption ("N months later" + thick arrow), zig-zag split divider. Draw in one brush so the lines read as one hand.
5. **Props / gags** — trophy+ribbon, toddler+flame, coin blob, film-poster-sized photo card, certificate plaque, snowman+snowflakes, flames, pile of money, poker table, jagged chart + letter "B" doodle. Rule: one gag prop per sentence, drawn or sourced to match the same outline weight.
6. **Evidence cards** — captured/real UI cards (dark-mode search box, stock quote card, definition card, AI overview, news article, spreadsheet, forum post). For a new original video: create your own accurate mock-ups or licensed screenshots with correct figures. Never fabricate data.
7. **Full-bleed illustrated scenes** — two hand-drawn environments (restaurant by the sea, restaurant counter) with the lead character inserted; each ~3–6 s; used for the emotional payoff of an A/B contrast.
8. **Third-party photo inserts** — small rectangular cut-out photos used as "evidence/comedy" beats (3–6 per video, 1.5–6 s each). Use licensed or original replacements.
9. **Black beats** — 2.1–3.3 s full-frame `#110F10` holds, **before and after** the central question card (S010 / S011 / S012 / S014).
10. **End card** — title + hand-note with arrow pointing at social icons + character beside a red subscribe button.

## 3. Motion grammar (MEASURED — the most important finding)

- **87 of 89** measured change episodes are **single-frame** replacements (1/30 s); the other two are a 2-frame codec-refresh episode (36.03 s) and the 3-frame black dip below. There is **no tweening/easing, no continuous motion, no camera move** inside any state (all residual changes ≤0.06% of pixels are periodic codec refresh, see coverage.json).
- Therefore the "animation" is **stepped composition replace**: the editor places a new still composition on the cut frame; entrances (pop-in of a prop, arrow, text line) are *the new frame*, never an animated move.
- The only multi-frame *content* event is a **2-frame full-black dip** (frames 7233–7234, 241.13–241.17 s) between the "outperformer" close-up and the full-bleed restaurant scene.
- **Reconstruction rule R-M1:** set every layer's keyframes with *hold* (stepped) interpolation; cut layers on frame boundaries; no easing curves, no scale animation. (Adding eased motion would break the measured style.)
- **R-M2:** "text reveal" = whole line appears on one frame (sometimes the first part, then the second part on a later cut); never a typewriter or wipe.
- **R-M3:** "zoom" = same character art swapped at a larger scale and offset on one frame (S001.0→S001.1 frame 40→41).
- **R-M4:** state-change density ≈ 3.7 s average (median state 3.35 s, mean 3.63 s; p10 1.57 s, p90 5.63 s). Opening runs faster (24 changes/min in 0–15 s, 20 in 15–30 s) and settles to 12–19/min.

## 4. Editorial timeline blueprint (derived from the 47-shot / 76-state structure)

Target: 270–285 s explainer; 16 narrative beats. Per beat: duration, visual device, state changes.

| Beat | Time window (source) | Visual device to reproduce (original assets) | States |
|---|---|---|---|
| Hook / character intro | 0–30 s | blank canvas → character + tag; scale-up cut; badge prop; arrow to gag prop; chart; coin gag; flex gag; pop-culture poster prop; quote caption; cloaked figure; phone-call pose | 12 |
| Escalation | 30–51 s | split-screen divided by zig-zag (two scenes at once); time-skip caption; brand logo drop with curved arrow; two arrow-line text cards ("strategy → …", "risk → …"); second character delivers complaint | 6 |
| Twist | 51–63 s | time-skip caption + meme photo; distressed pose + red falling chart; dark-mode search-box card with the query | 3 |
| Central question | 64–68 s | one centred question line on blank canvas | 1 |
| Explanation / analogy | 69–83 s | dark definition card + silhouette evolution strip; concept chart with the character's marker | 2 |
| Evidence | 83–96 s | stock-chart quote card; same concept chart with red circle; hand-drawn two-line comparison with legend | 4 |
| Counter-argument | 97–121 s | desk character + two quoted terms; large pose with long name tag; stock card with red-circled ratio; food photo; foil figure; quote card on black with large red quote glyph | 9 |
| Evidence / stakes | 121–153 s | long-run chart card; shrinks beside "17 Years"; framed certificate gag with snowman; AI-overview card; stacked three-line formula text; certificate with red X + flames | 13 |
| Central question 2 | 154–157 s | two stacked question lines on cream | 2 |
| Option 1 / Option 2 | 157–185 s | note-caption pose; news article with red-boxed chart + character on cash pile; poker table of faces; three photo pops; "rigged" two-character exchange | 9 |
| Payoff set-up | 185–197 s | black 3.3 s → answer question card → black 2.1 s → cheer pose + chart doodle + "B" → black 2.7 s | 5 |
| Definition + example | 197–241 s | question card; definition card (roller-coaster drawing); brand wordmark + value; second handwritten line; spreadsheet capture; "why does this matter" card; repeated cheer; small/large pose | 8 |
| Contrast scenes | 241–266 s | full-bleed scene A (up market) → complaint pair → full-bleed scene B (down market) → equals-sign portrait → equals-sign forum post | 5 |
| Takeaway + end card | 266–278 s | gag prop alone; closing line alone; end card | 3 |

## 5. Per-distinct-state generation prompts (templates)

Use these as image-generation / illustration prompts; every state in `visual_states.csv` maps to one of the families below (`literal_description` gives the per-state variant). Always keep the style anchor:

**STYLE ANCHOR (prefix to every prompt):** *"flat 2D hand-drawn doodle, near-white #FCFCFC background, thick wobbly black marker outline, solid flat colour fills with no shading or gradients, oversized round head stick figure, simple dot eyes and single-line mouth, lots of empty negative space, 16:9, transparent-PNG-ready layer"*.

| Family | States (examples) | Prompt template | Motion/camera | Continuity anchor |
|---|---|---|---|---|
| F1 Intro pose | S001.0, S017.5 | `[anchor] + lead character, arms out, small, low-centre, handwritten name tag top-left with arrow to head` | none; scale-up replace next cut | same face, same tag position |
| F2 Pose + prop | S001.1–S001.9, S009.7/S009.9 | `[anchor] + lead character at left holding {prop}, handwritten caption near head` | pop-in = new frame | prop scale ≈ head width |
| F3 Chart doodle | S001.3, S001.4, S005.3 | `[anchor] + hand-drawn axes, {color} polyline rising, tiny character beside` | stepped | legend swatches |
| F4 Text-only | S001.15/16, S003, S005.5/6, S009.0–2, S009.5/6, S011, S015, S017.3, S021.3 | `[anchor] + single centred line in rounded comic sans-like font, black on blank canvas` (second line adds on the next cut) | stepped | consistent font/size/baseline |
| F5 Evidence card | S002, S004, S005.1, S007.0/7.1, S008, S009.8, S016, S017.2, S021.1 | *original* accurate mock-up of a UI card, dark-mode or light, with legible figures | stepped | card width 35–60% of frame |
| F6 Photo insert | S001.7–S001.9 (poster), S001.18, S005.9, S009.11–13, S021.0 | licensed/original photo, rectangular cut-out on blank canvas, no border | stepped | one photo per beat, ≥1.5 s |
| F7 Time-skip / split | S001.12–S001.14, S001.18 | `[anchor] + thick black brush arrow pointing right, caption "N months later"` / zig-zag divider with two scenes | stepped | arrow style |
| F8 Black beat | S010, S012, S014 | solid `#110F10` full frame | hold 2.1–3.3 s | audio carries |
| F9 Full-bleed scene | S018, S020 | full-bleed hand-drawn scene with lead character inserted, location sign, section caption top-left | stepped | tan / beige palette |
| F10 Gag prop alone | S009.3, S009.4, S021.2 | single prop centred, optional red X + flame sprites | stepped | prop 20–30% height |
| F11 End card | S021.4 | title + hand-note + 3 icons + character + subscribe button | hold ≥5 s | brand title bold |

## 6. Editor/production steps

1. Record or script narration first (the visual edit follows the voice: ≈172 words/min in the source; this run's `audio_visual_alignment.csv`: median visual lag −0.073 s vs word start, 60 of 75 events within ±0.2 s; narration continues over black holds).
2. Build the asset library (§2). 3. Assemble beats on a 30 fps CFR timeline, one layer-set per state. 4. Place each cut on the frame where the key word begins (target |lag| ≤ 3 frames). 5. Use hold keyframes only. 6. Insert black beats around the central question. 7. Export H.264 1280×720 CFR 30, AAC 44.1 kHz.

## 7. Acceptance tests (QA)

- AT-1 No interpolated frames: mean abs-diff between consecutive frames must be exactly 0 except at cuts (re-run `measure_frames.py` + `episodes.py`; expect ≥ 90% of episodes single-frame).
- AT-2 State cadence within 3–4.5 s median; opening 20–25 changes/min in the first 30 s.
- AT-3 Negative space: median non-canvas content 3–6% on character states.
- AT-4 Palette within ΔE ≈ 6 of the measured tokens (§1) for canvas, black and accent colours.
- AT-5 Cut-to-word lag distribution: median within ±100 ms (ASR uncertainty ±100 ms).
- AT-6 No source art, names, logos, photos, or script reused (manual originality review).
- AT-7 A human watches/listens to the final cut end to end before any AV sign-off.

## 8. Limits

- Cartoon asset construction (line weight, exact fonts, easing) beyond frame-visible evidence is INFERRED.
- Sub-frame tweens, sub-0.06% pixel motion, and sound design cannot be established from this evidence.
- No human listening has been done; the audio part of the blueprint (voice pace, pauses) rests on ASR timing.
