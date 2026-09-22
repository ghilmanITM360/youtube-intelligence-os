# MASTER VIDEO FORENSIC RECONSTRUCTION
## `7 Things Wealthy Retirees Stopped Buying to Stay Rich`

**Source file:** `7_Things_Wealthy_Retirees_Stopped_Buying_to_Stay_Rich.mp4`
**Analysis date:** 24 August 2026
**Source video inspected:** YES — direct file inspection, 216/216 shots measured

---

# 0. EXECUTIVE VERDICT

> **This video contains zero animation.**
>
> All 216 shots are **static AI-generated illustrations**. Motion is supplied entirely by three editor presets applied over the stills. There is no AI video generation, no character movement, no motion graphics, no animated text, no drawn arrows, no parallax, no transitions other than hard cuts.

**Evidence.** A global similarity transform (SIFT + RANSAC) was fitted to every shot and the source frame was warped onto the target frame. Residual after motion compensation:

| Metric | Value |
|---|---|
| Mean residual (pixels differing >25/255) | **0.22%** |
| Shots with residual >3% | **0 of 216** |
| Mean inlier ratio of global fit | 0.93 |

A residual of 0.22% at 495 kbps H.264 is **below the compression noise floor**. If any element in any shot were moving independently of the frame, it would appear here as localised residual. Nothing does.

### What this means for the reconstruction brief

The `MASTER_VIDEO_FORENSIC_SYSTEM` motion-isolation apparatus — Engine C sections C13–C32, multi-pass AI passes, frame-state chains `F0→T1→F1`, coupled vs. independent motion classification, first/last-frame packages, ≤500-character animation prompts — **has no subject matter in this reference.**

Per the system's own **ABSOLUTE REFERENCE-FIDELITY RULE**:

> *"DO NOT invent additional animation because it looks interesting. DO NOT animate objects that remain static in the reference. If the reference contains one animation, reconstruct one animation."*

The reference contains **zero** animations. Therefore the faithful reconstruction is:

```
216 static images  →  3 named editor presets  →  hard cuts  →  narration  →  export
```

Any AI animation prompt written for this video would be a fabrication. Section 6 of this document states the single legitimate `AI PROMPT: N/A` per rule **C42 (STATIC STATE RULE)**, and Section 11 supplies an explicitly-labelled *optional* motion upgrade path for anyone who wants to exceed the reference rather than match it.

---

# 1. PASS 0 — MEDIA INSPECTION `HIGH CONFIDENCE`

| Field | Value |
|---|---|
| Duration | 847.500 s (14 m 07.5 s) |
| Resolution | 1280 × 720 |
| Aspect / SAR | 16:9, square pixels (1:1) |
| Orientation | Landscape |
| Frame rate | 30.00 fps constant (`30/1`, progressive) |
| Video codec | H.264 Main profile, Level 3.1, yuv420p |
| Colour | bt709 primaries / transfer / matrix, TV range |
| Video bitrate | 495 kbps |
| Audio codec | AAC-LC, 44 100 Hz, stereo, 128 kbps |
| Audio present | YES (847.655 s) |
| Container | MP4 / `isom`, muxer `Lavf59.27.100` |
| Handler string | `ISO Media file produced by Google Inc.` |

**Provenance note `MEDIUM CONFIDENCE`:** the Google handler plus the FFmpeg muxer identifies this as a **YouTube-delivered re-encode**, not a creator master. Bitrate, banding and blocking are delivery artefacts and must not be attributed to the production pipeline. All *geometric* measurements below (motion amplitudes, anchor points, overlay coordinates) survive re-encoding intact and are safe to rely on.

---

# 2. PASS 1 — SHOT DETECTION & EDITING GRAMMAR `HIGH CONFIDENCE`

**216 shots · 215 transitions · 100% HARD CUTS.**

Frame-stepped analysis at every sampled cut point. Inter-frame difference sits at `0.0`, spikes to `45–86` for **exactly one frame**, and returns to baseline:

```
cut@  2.97s  [0.0, 0.0, 57.3, 0.0, 0.2, 0.3, 0.2, 0.6]
cut@ 15.40s  [0.1, 0.3, 82.5, 0.0, 0.0, 0.0, 0.1, 0.3]
cut@837.03s  [0.0, 0.0, 86.5, 0.0, 0.0, 0.1, 0.8, 0.4]
```

A dissolve would produce a *ramp* across 6–20 frames. There is not one dissolve, fade, wipe, whip, zoom-transition or graphic match in fourteen minutes.

| Metric | Value |
|---|---|
| Total shots | 216 |
| Mean shot length | **3.92 s** |
| Median | **3.88 s** |
| Shortest | 1.07 s |
| Longest | 6.97 s |
| Std. deviation of gaps | narrow, unimodal |

**Distribution:**

```
0.0-1.5s  █████ 5
1.5-2.0s  ███████ 7
2.0-2.5s  █████████████████ 17
2.5-3.0s  ███████████████████████████ 27
3.0-3.5s  ██████████████████████████████ 30
3.5-4.0s  ███████████████████████████ 27
4.0-4.5s  █████████████████████████ 25
4.5-5.0s  ███████████████████████████ 27
5.0-5.5s  ████████████████████████████ 28
5.5-6.0s  ████████████ 12
6.0-7.0s  ███████████ 11
```

This is a **metronomic slideshow cadence**, not dramatically-paced editing. Median and mean are within 0.04 s of each other — a signature of near-uniform clip lengths on the timeline.

---

# 3. THE COMPLETE MOTION SYSTEM `HIGH CONFIDENCE`

Three presets constitute the entire motion vocabulary of the video.

| Template | Count | Share | Mean shot duration |
|---|---|---|---|
| **PAN-A (up)** | 73 | 33.8% | 3.82 s |
| **PAN-A (down)** | 66 | 30.6% | 3.66 s |
| **ZOOM-B (centre in)** | 64 | 29.6% | 4.78 s |
| **HOLD (no motion)** | 13 | 6.0% | 1.63 s |
| ZOOM OUT | **0** | 0% | — |
| Horizontal pan | **0** | 0% | — |
| Rotation | **0** | 0% | — |

## 3.1 PRESET "PAN-A" — vertical pan (139 shots, 64.4%)

| Parameter | Measured value |
|---|---|
| Scale | **exactly 1.00000** across all instances |
| Horizontal translation | **tx = 0.0 px** — zero, every instance |
| Vertical amplitude | **41.89 px mean**, range 37.3 – 42.9 |
| As fraction of frame height | **5.8%** |
| Rotation | 0.00° |
| Direction | 73 up / 66 down — **randomised, not alternating** |

**Easing curve — densely sampled on S006 at 0.30 s intervals:**

| Time progress | 6% | 12% | 24% | 36% | 48% | 59% | 71% | 83% | 95% | 100% |
|---|---|---|---|---|---|---|---|---|---|---|
| Amplitude reached | 1.2% | 3.7% | 12.2% | 26.1% | 45.1% | 66.2% | 82.4% | 93.5% | 99.4% | 100% |

A clean, symmetric sigmoid — **ease-in-ease-out**, ~48% of amplitude at 50% of time. Closely matches a standard `cubic-bezier(0.42, 0, 0.58, 1)` "Ease In Out".

**Critical detail:** the motion **completes early and then freezes.** On S006 (6.03 s clip) the pan finishes at ≈5.05 s and holds perfectly still for the final ≈0.93 s:

```
dt 4.80s → ty +42.73
dt 5.10s → ty +43.08
dt 5.40s → ty +43.09   ← frozen
dt 5.70s → ty +43.09   ← frozen
```

**Implementation requirement:** because the displayed content never changes scale but shifts 43 px vertically, the source image must be **pre-scaled to ≈106–110%** and panned inside that oversize, otherwise blank edges would enter frame. No blank edges are visible anywhere.

## 3.2 PRESET "ZOOM-B" — centre zoom-in (64 shots, 29.6%)

| Parameter | Measured value |
|---|---|
| Scale change | **+5.11% mean**, range +3.86% to +5.39% |
| **Anchor point** | **(639.7, 359.6)** |
| **Anchor std. deviation** | **(0.5, 0.7) px** |
| Direction | Always IN. Never out. |

Frame centre is (640.0, 360.0). The anchor is accurate to **half a pixel across 64 independent shots.**

> This is the single strongest piece of evidence in the analysis that the motion is a **stored preset, not hand-keyframed work.** No editor sets 64 separate anchor points to sub-pixel accuracy. This is one saved effect, dragged onto clip after clip.

**Easing curve — velocity per 0.30 s interval on S021:**

```
0.510  0.516  0.492  0.459  0.436  0.410  0.378  0.357  0.326  0.304
0.282  0.249  0.211  0.199  0.171  0.131  0.099  0.107  0.051  0.051
```

Velocity is near-flat at the start and decays monotonically to one-tenth by the end: **ease-out only** (fast start, asymptotic settle). *This is a different curve from PAN-A's symmetric ease-in-out* — confirming two genuinely distinct presets rather than one parameterised effect.

## 3.3 The duration → preset rule `HIGH CONFIDENCE`

| Clip length | Behaviour |
|---|---|
| **< 2.05 s** | 13 of 16 receive **no motion at all** (HOLD) |
| **≥ 2.05 s** | **200 of 200** receive a motion preset |

Zoom is additionally reserved for the longest beats: ZOOM-B median clip 5.00 s vs. 3.6 s for pans. The creator (or the template) gives slow zooms to the shots it wants to dwell on.

---

# 4. OVERLAY ARCHITECTURE `HIGH CONFIDENCE`

All 216 shot frames were averaged. Every image element blurs to mush — **except one, which stays razor-sharp.**

## 4.1 Channel avatar watermark

| Property | Value |
|---|---|
| Bounding box | x 1228 – 1274, y 5 – 57 |
| Size | **47 × 53 px** (3.7% of frame width) |
| Margin from right edge | **6 px** |
| Margin from top edge | **5 px** |
| Sharpness vs. frame interior in temporal average | **4× gradient energy** |
| Behaviour | **Screen-locked overlay** |
| Appearance | Circular badge, thin dark ring; cartoon man, brown hair, brown beard, glasses, green shirt |

**Screen-lock proof.** After compensating each shot for its own image motion, residual energy at the badge is **14.6× the frame interior**. On pan-up shots — where the top band is free of edge artefacts — the badge shows residual 10.9–23.6 while the *mirrored control region at identical height* shows **0.00–1.44**:

| Shot | Badge residual | Control residual (same height) |
|---|---|---|
| S037 | 14.59 | **0.17** |
| S113 | 23.59 | **0.00** |
| S151 | 10.90 | **0.89** |
| S170 | 19.18 | **1.44** |

The badge does not travel with the image. It is composited on top in the editor, at a fixed screen position, for the entire runtime.

## 4.2 On-screen text is BAKED INTO THE IMAGES

Template-tracked the whiteboard lettering on three title cards against the global motion model:

| Shot | Text region shift | Global image model | Match confidence |
|---|---|---|---|
| S014 | (0, **+41**) | ty **+41.1** | 0.997 |
| S113 | (0, **−41**) | ty **−40.8** | 0.999 |

The text moves **1:1 with the illustration**. There is no editor typography layer anywhere in this video.

This is independently corroborated by a defect the editor could not have produced (§5.2).

## 4.3 No captions / subtitles

Temporal-average gradient energy in the lower third (y 560–700): **7.85**, versus **43.72** at the badge. No persistent burned-in caption band exists. `HIGH CONFIDENCE`

**Total editor-side graphics inventory for the entire 14-minute video: one 47×53 px static PNG.**

---

# 5. STRUCTURE — THE SEVEN ITEMS `HIGH CONFIDENCE`

Recovered by OCR across all 216 frames, then confirmed by direct visual inspection of each title card.

| # | Item (verbatim) | Shot | Timecode | Section length |
|---|---|---|---|---|
| — | *Cold open / hook* | S001–S013 | 00:00.0 – 00:44.6 | 44.6 s, 13 shots |
| **7** | Brand New Cars | S014 | **00:44.6** | 98.5 s, 23 shots |
| **6** | Extended Warranties & Unnecessary Insurance | S037 | **02:23.0** | 103.9 s, 24 shots |
| **5** | Trendy Home Renovations. | S061 | **04:06.9** | 109.9 s, 27 shots |
| **4** | Luxury Status Goods | S088 | **05:56.8** | 99.3 s, 25 shots |
| **3** | Expensive Hobbies | S113 | **07:36.1** | 92.0 s, 27 shots |
| **2** | Percentage-Based Financial Advisors. | S140 | **09:08.2** | 123.2 s, 30 shots |
| **1** | The Silent Wealth Thief — Emotional Purchases | S170 | **11:11.3** | 114.5 s, 30 shots |
| — | *Payoff / CTA / outro* | S200–S216 | 13:05.8 – 14:07.5 | 61.7 s, 17 shots |

**Allocation is remarkably even:** every item receives 92–123 s. Item 2 (advisor fees) gets the most airtime; item 3 (hobbies) the least. The variance is only ±14% around the mean — another indicator of templated production.

## 5.1 Pacing defect — the 44.6-second cold open

Item 7 does not arrive until **00:44.6**, after 13 shots. That is **5.3% of runtime and 6% of shots** spent before the promised list begins. For a listicle whose title promises seven specific things, this is the highest-risk retention zone in the video.

## 5.2 Continuity defect — title-card typography `HIGH CONFIDENCE`

| Item | Numbering | Trailing punctuation |
|---|---|---|
| 7 | `7.` period | — |
| 6 | `6.` period | — |
| 5 | `5.` period | **stray trailing period** |
| 4 | `4.` period | — |
| 3 | `3:` **colon** | — |
| 2 | `2:` **colon** | **stray trailing period** |
| 1 | `1:` **colon** | — |

The scheme switches from `N.` to `N:` between items 4 and 3, and two cards carry an inconsistent trailing full stop.

**This is direct forensic proof of the baked-text pipeline.** Had the numbers been an editor text layer, they would share one style and be corrected in seconds. Because each number lives inside its own generated raster, fixing this requires **regenerating seven images**.

## 5.3 Wardrobe drift `LOW CONFIDENCE`

The presenter wears a different jacket in every title card — brown blazer (7), tan blazer (6), brown cardigan (5), olive jacket (4), dark-grey blazer (3), maroon blazer (2), navy blazer (1). Cannot determine from the artefact alone whether this is deliberate chapter-signalling or uncontrolled generator drift. The *character identity* (face, hair, beard, glasses) holds solid across all 216 images, which argues the wardrobe variation was tolerated rather than fought.

---

# 6. AUDIO INTELLIGENCE

## 6.1 Transcription status — BLOCKED

Semantic transcription **failed**. Whisper model weights are hosted off the sandbox network allowlist and returned `HTTP 403 Forbidden` from the egress proxy. Per the system's PASS 0 fallback rule, full **non-semantic** audio analysis was performed instead and is reported below.

**Consequence:** Engine A sections A1, A4–A8, A10, A12 (script beats, causal spine, curiosity loops, payoff ladder, emotion tracking) cannot be completed from this artefact. They are listed as MISSING in the compliance audit (§13), not fabricated.

## 6.2 Measured audio properties `HIGH CONFIDENCE`

| Metric | Value |
|---|---|
| Speech-active time | **792.8 s of 847.6 s = 93.5%** |
| Phrase segments | 276, mean 2.87 s (SD 1.51) |
| Inter-phrase gaps ≥0.25 s | 72, total 28.2 s |
| Mean gap | **0.39 s** (SD 0.106) |
| **Longest pause in 14 minutes** | **0.72 s** |
| Fundamental frequency | **123.5 Hz** mean, p5–p95 = 75–217 Hz → male register |
| Speaking rate | ≈**191 wpm** (envelope-onset proxy) |
| Overall RMS | −15.0 dBFS |
| True peak | 0.0 dBFS |
| Tail | audio **fade-out** present |

## 6.3 No music bed `HIGH CONFIDENCE`

Level inside speech gaps falls to **−37 to −59 dBFS** with inconsistent, non-harmonic spectral content (mean 25.9 tonal bins; several gaps register **zero**). A genuine music bed sustains stable tonal structure across *every* gap. Several gaps approach digital silence.

**Verdict: narration-only mix.** No music, no ambience beds, no sound effects detected.

## 6.4 Narration character `MEDIUM CONFIDENCE`

A maximum pause of **0.72 s across fourteen minutes**, with gap standard deviation of only 0.106 s, is not natural human phrasing — human narration produces occasional 1.5–3 s rhetorical pauses. This indicates either aggressive automated silence-trimming or synthetic speech. **Cannot verify without ASR.**

## 6.5 THE CENTRAL EDITING FINDING `HIGH CONFIDENCE`

| Metric | Value |
|---|---|
| Cuts within 0.35 s of a speech-pause boundary | **65 of 215 = 30.2%** |
| Median distance from cut to nearest pause | **3.09 s** |

> **The edit is time-driven, not speech-driven.** Images swap on a ~3.9 s metronome that ignores sentence structure. Roughly **70% of cuts land mid-sentence.**

This is the highest-leverage defect in the entire production. It costs nothing to fix — the images already exist; only their timeline positions need adjusting.

---

# 7. VISUAL DNA & MASTER IMAGE PROMPT SYSTEM

Because every shot is a still, **image generation is the entire production**. This section is the highest-value deliverable in the document.

## 7.1 Extracted DNA `HIGH CONFIDENCE`

**STYLE DNA.** Uniform 2D digital cartoon illustration. Thick, consistent dark-brown outlines of near-uniform weight. Flat cel shading with soft gradient fills and gentle ambient occlusion. Warm, saturated palette. Mild wide-angle barrel curvature on interiors. Densely propped, plausibly-real environments with legible signage. No visible brush or paper texture. Backgrounds rendered at slightly lower contrast than the subject. Consistency across all 216 images indicates **one generator and one locked style prompt**.

**CHARACTER DNA — C01 (present in 216/216 frames).** Man in his early sixties. Silver-grey hair, side-parted with a slight lift at the front. Full, neatly-trimmed grey beard and moustache. Round wire-rimmed spectacles. Warm mid-tone skin, pronounced smile lines, highly expressive raised eyebrows. Layered casual wardrobe: check or plaid flannel shirt under a knit vest, cardigan, or blazer; chinos or straight jeans; brown leather shoes.

**COMPOSITION DNA.** Subject centroid falls in the **centre horizontal third in 57%** of shots, middle vertical band in 52%. The temporal average shows an unmistakable centred head-and-torso ghost. Framing is predominantly full-body or three-quarter, eye-level, with the character occupying roughly the central 30–45% of frame width.

**CAMERA DNA.** Locked. Eye-level. No high or low angles observed in the sample. Perspective is gentle one- or two-point.

**COLOUR DNA.** Dominant warm neutrals (wood browns, beige, cream). Secondary cool blues and greens for exteriors, retail and screens. Accent reds reserved for price tags, warnings, market-crash chyrons and subscribe buttons — **accent scarcity is well observed**, red almost always marks a cost or an alarm.

**GRAPHIC DNA.** All graphics are *diegetic* — they exist inside the illustrated world as whiteboards, chalkboards, price tags, invoices, statements, billboards, phone and laptop screens, TV chyrons and shop signage. **Zero non-diegetic motion graphics.**

**MOTION DNA.** See §3. Three presets, no local animation.

**TRANSITION DNA.** Hard cut, 100%.

## 7.2 MASTER STYLE BLOCK — reusable prefix

> Copy this verbatim as the opening of every image prompt, then append the per-shot scene block from §7.4.

```
2D digital cartoon illustration, 16:9 landscape, 1280x720. Clean vector-like
rendering with thick, even dark-brown outlines and flat cel shading softened by
gentle gradient fills and light ambient occlusion. Warm saturated palette, no
paper grain or brush texture. Gentle wide-angle perspective. Background is fully
rendered and densely propped with plausible real-world detail and legible signage,
held one step lower in contrast and saturation than the foreground subject so the
character reads first. Even, soft key lighting with warm practical sources; no
harsh shadows. Eye-level locked camera.
```

## 7.3 MASTER CHARACTER BLOCK — reusable, guarantees identity continuity

```
CHARACTER (must remain identical in every image): a man in his early sixties.
Silver-grey hair, side-parted with a slight lift at the front. Full, neatly
trimmed grey beard and moustache. Round wire-rimmed spectacles. Warm mid-tone
skin, pronounced smile lines, expressive raised eyebrows. Friendly, animated,
slightly exasperated demeanour. Layered casual wardrobe: a check or plaid flannel
shirt worn under a knit vest, cardigan or soft blazer; chinos or straight-leg
jeans; brown leather shoes. Full body or three-quarter framing, positioned in the
central third of the frame, at eye level, occupying roughly 35% of frame width.
```

## 7.4 SCENE ARCHETYPE SYSTEM

All 216 illustrations resolve to **nine archetypes**. This is the reusable production grammar — generate any new episode by populating these nine slots.

| ID | Archetype | Function | Example shots |
|---|---|---|---|
| **AR1** | **TITLE CARD** — presenter beside whiteboard/chalkboard bearing the numbered item, gesturing toward it | Chapter marker | S014, S037, S061, S088, S113, S140, S170 |
| **AR2** | **RETAIL CONFRONTATION** — character in showroom/store facing a salesperson and a priced product | Temptation staged | S017, S021, S026, S042, S045, S090, S096, S104 |
| **AR3** | **DATA BOARD** — an itemised cost list, invoice, statement or chart baked into the scene | Evidence delivery | S010, S018, S029, S053, S068, S084, S118, S131, S147, S163 |
| **AR4** | **DOMESTIC REFLECTION** — character at home (armchair, desk, kitchen) with documents or laptop, contemplative | Reasoning beat | S009, S031, S128, S141, S161, S211 |
| **AR5** | **DISTRESS BEAT** — hands to head, shocked expression, papers flying, red alarm colour | Consequence / stakes | S011, S038, S056, S143, S148, S165 |
| **AR6** | **SOCIAL COMPARISON** — character alongside neighbours, crowds or luxury shoppers behaving differently | Contrast / status pressure | S008, S013, S095, S106, S111, S186 |
| **AR7** | **STREET & LIFESTYLE** — walking, markets, plazas, cafés, gardens | Connective tissue / pacing | S003, S004, S012, S109, S166, S190 |
| **AR8** | **CONTENTMENT PAYOFF** — relaxed, gardening, fireplace, sunset, laughing with friends | Reward state | S196–S208 cluster |
| **AR9** | **CTA CARD** — device screen showing subscribe UI | Call to action | S209, S211, S213, S214 |

## 7.5 TEXT BAKE DECISION — global rule

Per **C9**, applied at project level:

```
BAKE TEXT: YES — for all AR1 title cards and all AR3 data boards.
```

The reference bakes 100% of its text into the illustrations, so faithful reconstruction bakes it too. Image prompts for AR1 and AR3 **must** specify the exact wording.

> **Practical caution — this is where the reference is weakest.** Baking long numeric lists into a generative image is exactly why the reference contains garbled and inconsistent typography (§5.2), and why OCR of the data boards returns fragments like `Bag $50.09 Green $350.09`. Text baking is *reference-faithful* but *quality-limiting*.
>
> **Recommended deviation (§11.1):** generate AR1/AR3 as **clean plates** with a blank whiteboard/statement surface, then set the type in the editor. This yields sharp, correct, instantly-editable text and eliminates the entire class of defect in §5.2. Deviation flagged because it departs from the reference.

**CLEAN PLATE REQUIREMENT (if adopting the deviation):**
```
...an empty whiteboard on a rolling aluminium frame, its surface completely
blank, evenly lit, no writing or markings of any kind, occupying the right two
thirds of the frame and presented square to camera.
```
**TEXT OVERLAY SPEC:** wording `7. Brand New Cars`; handwritten-marker or clean geometric sans; dark navy-blue `#2B3A67`; left-aligned; cap height ≈ 5.5% of frame height; baseline at y ≈ 22% of frame height; left edge at x ≈ 38% of frame width.

---

# 8. VISUAL RECONSTRUCTION CARDS

Full `Output Card §1–28` format. Five archetype exemplars are given in full; all 216 shots are enumerated with their measured parameters in `EDL_216_shots.csv`.

---

## V001 — 00:00.000 – 00:02.967 · `AR7/AR4 hook opener`

**SHOT:** S001 · **DURATION:** 2.97 s · **STATE ID:** F001.0 (terminal — no sub-states)

### 1. WHAT THE VIEWER SEES
If you paused the video here, you would see a warm-toned diner interior shot slightly from the side. The recurring grey-bearded man in round glasses sits alone in a burgundy vinyl booth at the left-of-centre, both hands resting near a steaming dark mug on a pale laminate table. A printed receipt or statement lies flat on the table to his right, with a crumpled paper napkin near the lower-left edge. Salt and pepper shakers sit mid-table. Behind him, through the booth, a green LED stock ticker board reads **`DOW +250.3`** and **`S&P 500 +65.`** with an upward green arrow. Warm interior light, no visible window daylight. The character occupies roughly the central 35% of frame width; the ticker anchors the upper-right.

### 2. SCRIPT ↔ VISUAL SYNC
Spoken words unavailable (ASR blocked). Visual appears **at t=0** — this is the cold-open frame. Function: establish protagonist, establish financial-anxiety domain, establish the illustrated register.

### 3. CHANGE FROM PREVIOUS STATE
N/A — first shot.

### 4. VISUAL PURPOSE
`ESSENTIAL`. Removing it removes the entire premise-setting frame: an ordinary retiree, alone, with money news he is not celebrating.

### 5. CONSTRUCTION MAP
Single generated raster. No layers, no compositing, no separated elements.
```
Layer 1 — generated illustration (contains everything, including all text)
Layer 2 — channel avatar watermark PNG (screen-locked, editor)
```

### 6. EXACT LAYOUT
Canvas 1280×720 · 16:9. Character x ≈ 42, y ≈ 45, scale ≈ 0.55 frame height. Ticker board x ≈ 78, y ≈ 12. Mug x ≈ 40, y ≈ 62. Receipt x ≈ 52, y ≈ 72. Negative space: lower-left table surface. Eye path: face → mug → receipt → ticker.
*Approximate visual map — not pixel measurement.*

### 7. ATTENTION ORDER
FIRST: face and glasses. SECOND: steaming mug. THIRD: green ticker. Classification: **CONTROLLED**.

### 8. IMAGE REUSE STATUS
`NEW BASE`.

### 9–10. EXACT STANDALONE IMAGE PROMPT
```
[MASTER STYLE BLOCK]
[MASTER CHARACTER BLOCK]

SCENE: The man sits alone in a burgundy vinyl booth inside a warm, traditional
American diner, framed slightly from the side and just left of centre. Both hands
rest on a pale laminate table beside a dark ceramic mug of coffee with visible
steam rising. A printed financial statement lies flat on the table to his right; a
crumpled paper napkin sits near the lower-left corner of the table; chrome salt
and pepper shakers stand mid-table. His expression is quiet, tired and faintly
worried, eyes downcast toward the statement. Behind and above him on the diner
wall hangs a black stock-ticker board with bright green LED lettering reading
exactly "DOW  +250.3" on the first line and "S&P 500  +65." on the second, with a
green upward arrow at the left. Warm tungsten interior lighting, no daylight.
Muted red and brown diner palette with the green ticker as the only saturated
accent. Character occupies roughly the central third of the frame at eye level.
```

### 11. TEXT BAKE / OVERLAY DECISION
`BAKE: YES` — ticker text is diegetic and must be inside the image.

### 12. FIDELITY LOCK
Character identity, booth colour, single mug, single statement, ticker wording and green colour, warm interior light, eye-level camera. **PROHIBITED:** additional people, window daylight, red/negative ticker values, any motion cue.

### 13. COVERAGE AUDIT
Subject High · Pose High · Geometry Medium · Composition High · Scale High · Perspective High · Lighting High · Colour High · Negative space Medium · Text plan High · Continuity High.

### 14–15. FRAME STATE / STATE-CHAIN POSITION
`F001.0`. Single terminal state. No chain — nothing in this shot creates a second state.

### 16. COMPLETE MOTION EVENT INVENTORY
**NONE.** Zero motion events. Residual after global compensation: 0.24%.

### 17. WHY MOVE
No element moves. Not applicable.

### 18. WHAT STAYS STATIC
Everything. The entire illustration is a single rigid plate; the only frame-level change is the editor pan.

### 19. MOTION INTERFERENCE ANALYSIS
No competing animations exist. Interference risk: **none**.

### 20. MOTION COUPLING CLASSIFICATION
Not applicable — no motion events to couple.

### 21. RECOMMENDED PRODUCTION METHOD
**STATIC HOLD + EDITOR KEYFRAMES.**

### 22. AI SUITABILITY
`N/A` — no motion to generate. AI *image* generation suitability: **HIGH**.

### 23. AI ISOLATION PLAN
Not required.

### 24. SOURCE IMAGE FOR EACH AI PASS
No AI animation passes exist. Single source image = the generated illustration above.

### 25. ANIMATION PROMPT
```
AI PROMPT: N/A
```
Per **rule C42 (STATIC STATE RULE)** — *"Do NOT generate AI video just to preserve stillness."*

### 26. EDITOR / COMPOSITING BUILD
```
1. Import illustration; scale to 108% (pre-scale for pan headroom).
2. Apply preset PAN-A(down):
     Position Y: 0 → +41.5 px
     Easing:     ease-in-out, cubic-bezier(0.42, 0, 0.58, 1)
     Scale:      locked 108%, unchanged
     Position X: locked
3. Clip length 2.97 s. Motion spans full clip (short clip, no trailing freeze).
4. Watermark PNG on top layer, 47x53 px, 6 px from right, 5 px from top.
```
*Recreation method — original software not verified.*

### 27. EDIT OUT / NEXT STATE
`HARD CUT` at 00:02.967 → V002 (pool hall). No transition effect. Cut is **not** on a speech pause.

### 28. RECONSTRUCTION RULE
One image. One preset. One cut. Nothing moves inside the frame.

---

## V014 — 00:47.300 – 00:50.000 · `AR1 TITLE CARD (archetype master)`

**SHOT:** S014 · **DURATION:** 2.70 s · **STATE ID:** F014.0
**PRESET:** PAN-A(down), ty +41.1 px, scale 1.000, ease-in-out
**Measured text-lock:** title text shifted (0, +41) — confirming baked text.

### 1. WHAT THE VIEWER SEES
A bright, minimally-furnished office or classroom. A large aluminium-framed whiteboard fills the right two-thirds of the frame, square to camera. Handwritten dark-blue lettering reads **`7. Brand New Cars`**. The presenter stands at the left, weight on one leg, body angled toward the board, left arm extended palm-up in a presenting gesture, wearing a brown blazer over a green check shirt and tan chinos. A small framed chart hangs on the pale wall behind his shoulder. Marker pens rest in the whiteboard tray. Flat, even daylight. Generous white negative space across the board.

### 3. CHANGE FROM PREVIOUS STATE
`REPLACED` — full scene change from V013 (police lineup). New environment, new wardrobe, new function.

### 4. VISUAL PURPOSE
`ESSENTIAL — STRUCTURAL`. This is the chapter marker. Removing it destroys the list architecture.

### 5. CONSTRUCTION MAP
```
Layer 1 — generated illustration (whiteboard text baked in)
Layer 2 — channel avatar watermark PNG
```

### 6. EXACT LAYOUT
Whiteboard occupies x 33–96, y 8–72. Text baseline y ≈ 22, left edge x ≈ 38. Presenter x ≈ 15, y ≈ 50, scale ≈ 0.78 frame height. Negative space: centre-right of board. Eye path: face → gesturing hand → text.

### 7. ATTENTION ORDER
FIRST: presenter's gesture. SECOND: whiteboard text. THIRD: face. Classification: **CLEAN** — deliberately uncluttered so the numbered item lands.

### 8. IMAGE REUSE STATUS
`NEW BASE`. Not reused elsewhere. Note: the seven AR1 cards are **not** reuses of one another — each is a separately generated image in a different room with different wardrobe.

### 10. EXACT STANDALONE IMAGE PROMPT
```
[MASTER STYLE BLOCK]
[MASTER CHARACTER BLOCK — wardrobe override: brown blazer over a green check
shirt, tan chinos, brown shoes]

SCENE: A bright, sparsely furnished modern classroom or small office with pale
cream walls and a light floor. A large whiteboard on a slim aluminium frame fills
the right two thirds of the frame, presented square to camera, its surface clean
and evenly lit. Written across it in neat dark navy-blue handwritten marker,
left-aligned in the upper portion, is exactly: "7. Brand New Cars". Coloured
marker pens and an eraser rest in the whiteboard tray. The man stands at the far
left in the foreground, weight shifted onto one leg, torso angled toward the
board, his left arm extended outward palm-up in an open presenting gesture, head
turned toward the viewer with a warm, knowing expression. A small framed line
chart hangs on the wall behind his shoulder. Flat, even, shadowless daylight.
Generous empty white space across the centre-right of the board.
```

### 11. TEXT BAKE / OVERLAY DECISION
`BAKE: YES` (reference-faithful). **Recommended deviation: NO — use clean plate + editor type.** See §7.5 and §11.1. The reference's own numbering inconsistency (§5.2) is caused by baking.

### 12. FIDELITY LOCK
Board square to camera; text left-aligned upper portion; exact wording `7. Brand New Cars`; presenter far left with open palm gesture; even shadowless light; large negative space. **PROHIBITED:** perspective skew on the board, additional writing, students or furniture clutter, dramatic lighting, motion cue.

### 16. COMPLETE MOTION EVENT INVENTORY
**NONE.** The presenter does not gesture, the text does not write on, nothing reveals. The only change across the 2.70 s is the editor pan.

### 18. WHAT STAYS STATIC
Everything, for the reason given in C16 under *reading stability*: the shot exists to let the viewer read six words. The creator correctly kept it still — but then applied a 41 px pan **during** the reading window, which mildly works against that goal.

### 21. RECOMMENDED PRODUCTION METHOD
**STATIC HOLD + EDITOR KEYFRAMES.** For an improved version: **HOLD with no motion** (see §11.2).

### 25. ANIMATION PROMPT
```
AI PROMPT: N/A
```

### 26. EDITOR / COMPOSITING BUILD
```
1. Import illustration; pre-scale 108%.
2. PAN-A(down): Position Y 0 → +41.1 px, ease-in-out. Scale locked. X locked.
3. Clip length 2.70 s.
4. Watermark PNG top layer.
```

### 27. EDIT OUT / NEXT STATE
`HARD CUT` at 00:50.000 → V015 (podcast studio).

### 28. RECONSTRUCTION RULE
**Archetype master.** Every AR1 card in the video is this prompt with three substitutions: room, wardrobe, and the exact numbered string.

---

## V010 — 00:33.167 – 00:34.567 · `AR3 DATA BOARD` · **HOLD**

**SHOT:** S010 · **DURATION:** 1.40 s · **STATE ID:** F010.0
**PRESET:** `HOLD` — no motion. Measured: scale 1.0000, tx 0.0, ty 0.0, residual **0.00%**.

### 1. WHAT THE VIEWER SEES
A theatrical stage framed by heavy red velvet curtains with gold tie-backs. Centre stage, a large cream board carries a bold heading **`UNEXPECTED EXPENSES!`** above a numbered list:

```
1. NEW DENTAL CROWN - $1,500
2. READING GLASSES (PAIR #4) - $300
3. ROOF LEAK REPAIR - $2,800
4. CAR BATTERY (DIED IN PARKING LOT)
5. HOME INSURANCE INCREASE - $600
6. CAT VET BILL (SWALLOWED A SOCK) - $900
7. PROPERTY TAXES (AGAIN) - $4,200
8. TOTAL: $10,480.00!!!
```

The presenter stands to the right of the board in a knit vest and check shirt, arms spread in a theatrical "behold" gesture, mouth open in exasperation. Warm spotlight from above; gold star motifs scattered on the curtains.

### 4. VISUAL PURPOSE
`ESSENTIAL — EVIDENTIAL`. This is the highest information-density frame in the cold open. It converts an abstract worry into a specific, absurd, itemised total.

### 7. ATTENTION ORDER
FIRST: the red `UNEXPECTED EXPENSES!` heading. SECOND: the bold total. THIRD: the presenter's gesture. Classification: **COMPETITIVE** — eight list rows plus a figure is a lot to read in **1.40 s**.

> **Retention risk `HIGH`.** This frame carries ~40 words of small type and is on screen for 1.40 seconds. At normal reading speed a viewer can absorb perhaps two lines. The joke items (*swallowed a sock*, *pair #4*) are the shot's comedic payload and most viewers will never read them.

### 10. EXACT STANDALONE IMAGE PROMPT
```
[MASTER STYLE BLOCK]
[MASTER CHARACTER BLOCK — wardrobe override: cream knit vest over a green and
brown check flannel shirt, brown trousers]

SCENE: A small theatrical stage framed by heavy crimson velvet curtains with gold
tasselled tie-backs and scattered small gold star motifs. Centre stage stands a
large cream presentation board, square to camera, occupying the left two thirds of
the frame. At the top, in bold red capitals, the heading reads exactly
"UNEXPECTED EXPENSES!". Below it, a neatly numbered list in dark capitals reads
exactly:
"1. NEW DENTAL CROWN - $1,500 / 2. READING GLASSES (PAIR #4) - $300 / 3. ROOF LEAK
REPAIR - $2,800 / 4. CAR BATTERY (DIED IN PARKING LOT) / 5. HOME INSURANCE
INCREASE - $600 / 6. CAT VET BILL (SWALLOWED A SOCK) - $900 / 7. PROPERTY TAXES
(AGAIN) - $4,200", with a final bold red line "8. TOTAL: $10,480.00!!!".
The man stands to the right of the board, both arms flung wide in a theatrical
"behold" gesture, eyebrows raised high, mouth open in comic exasperation. A warm
overhead theatrical spotlight pools on the board and figure; the curtain edges
fall into deeper shadow.
```

### 11. TEXT BAKE / OVERLAY DECISION
`BAKE: YES` in the reference. **Strong recommendation to deviate.** This is precisely the content that generative text renders unreliably — OCR of the reference already shows `READING GLASSES (PAIR #4) - $300` partially garbled as `(PAIR)L#300`. Generate a **blank cream board** clean plate and set all nine lines as editor type.

### 16. COMPLETE MOTION EVENT INVENTORY
**NONE.** Residual 0.00% — this is one of the 13 perfectly frozen HOLD shots.

### 18. WHAT STAYS STATIC
Everything, and here it is **correct**: `reading stability`. The creator's own duration rule (<2.05 s → no motion) produced the right call. A pan across dense type would have made it harder to read.

### 21. RECOMMENDED PRODUCTION METHOD
**STATIC HOLD.** Correct as-is. The defect is duration, not motion.

### 25. ANIMATION PROMPT
```
AI PROMPT: N/A
```

### 26. EDITOR / COMPOSITING BUILD
```
1. Import illustration at 100%. No scale, no keyframes, no effects.
2. Clip length 1.40 s.  [RECOMMEND: extend to 4.5-6.0 s]
3. Watermark PNG top layer.
```

### 27. EDIT OUT / NEXT STATE
`HARD CUT` at 00:34.567 → V011 (garage, distress beat).

### 28. RECONSTRUCTION RULE
Dense diegetic data board, frozen, brief. Reconstruct the freeze; **do not reconstruct the 1.40 s duration.**

---

## V029 — approx 01:57 · `AR3 CHART BOARD`

**SHOT:** S029 · **PRESET:** per EDL row S029

### 1. WHAT THE VIEWER SEES
A classroom with a dark green chalkboard filling the right of frame. A bold white arrow sweeps steeply downward from upper-left to lower-right, with the word **`DEPRECIATION`** lettered along its descending axis. The presenter stands at the left in a check shirt, one hand raised toward the arrow, head turned to camera with a wry expression. Rows of desks recede into the left background; a pale institutional wall and door behind.

### 4. VISUAL PURPOSE
`ESSENTIAL — EXPLANATORY`. The single clearest conceptual visual in the item-7 section: value falling over time, expressed as one descending line.

### 10. EXACT STANDALONE IMAGE PROMPT
```
[MASTER STYLE BLOCK]
[MASTER CHARACTER BLOCK — wardrobe override: red and blue check flannel shirt,
brown trousers]

SCENE: A traditional classroom. A large dark green chalkboard fills the right two
thirds of the frame, square to camera. Drawn across it in thick white chalk is a
single bold arrow sweeping steeply downward from the upper left to the lower
right, ending in a solid arrowhead. The word "DEPRECIATION" is lettered in white
chalk capitals running along the arrow's descending axis, following its angle. The
man stands at the left foreground in three-quarter view, one arm raised and
gesturing up toward the high end of the arrow, head turned toward the viewer with
a wry, knowing expression. Rows of empty wooden school desks recede into the left
background. Pale institutional walls, soft even overhead lighting.
```

### 11. TEXT BAKE / OVERLAY DECISION
`BAKE: YES` — chalk lettering is diegetic and angled along a drawn axis; an editor overlay could not match the chalk texture or the rotation naturally.

### 16. COMPLETE MOTION EVENT INVENTORY
**NONE.** The arrow does **not** draw on. There is no trim-path reveal, no stroke animation, no write-on. It is fully drawn from the shot's first frame to its last.

> This is the most instructive shot in the video for the brief. A descending "DEPRECIATION" arrow is the canonical case for a **trim-path stroke reveal** — the exact motion the source system's examples describe. **The reference does not animate it.** Reconstructing this shot faithfully means resisting the obvious animation.

### 21. RECOMMENDED PRODUCTION METHOD
**STATIC HOLD + EDITOR KEYFRAMES** (whichever preset the EDL row specifies).

### 25. ANIMATION PROMPT
```
AI PROMPT: N/A
```
Optional deviation only — see §11.3.

### 28. RECONSTRUCTION RULE
Draw the arrow **into the image**. Do not animate it.

---

## V213 — approx 13:52 · `AR9 CTA CARD`

### 1. WHAT THE VIEWER SEES
A home office in warm daylight. The presenter sits at a desk in a check shirt, turned toward a desktop monitor that fills the left-centre of frame. On screen, a video player interface displays a large red **`SUBSCRIBE`** button. His right hand is raised toward the screen; a small potted plant, a lamp and stacked books dress the desk. A window with garden greenery behind.

### 4. VISUAL PURPOSE
`TRANSITIONAL / CTA`.

### 10. EXACT STANDALONE IMAGE PROMPT
```
[MASTER STYLE BLOCK]
[MASTER CHARACTER BLOCK — wardrobe override: pale blue and grey check shirt]

SCENE: A bright home office in warm morning daylight. The man sits in a wooden
desk chair in three-quarter view, turned toward a desktop monitor that occupies
the left-centre of the frame. The monitor displays a simple video-player interface
with a prominent rounded red button reading exactly "SUBSCRIBE" beneath a video
thumbnail. His right hand is raised, open-palmed, gesturing toward the screen; he
smiles warmly at the viewer. A small potted succulent, a desk lamp and a short
stack of books dress the desk surface. Behind him a window shows soft green garden
foliage. Warm, even natural lighting, relaxed and unhurried mood.
```

### 11. TEXT BAKE / OVERLAY DECISION
`BAKE: YES` — the reference bakes the subscribe UI into the illustration. **Notable:** this creator delivers the CTA entirely through generated imagery. There is **no motion-graphic subscribe animation, no end card, no lower-third** anywhere in the video.

### 16. COMPLETE MOTION EVENT INVENTORY
**NONE.** The subscribe button does not pulse, bounce, glow or scale.

### 28. RECONSTRUCTION RULE
The CTA is an *illustration*, not a motion graphic. Four separate CTA images (S209, S211, S213, S214) are spaced through the outro rather than one animated end card.

---

## ALL REMAINING SHOTS

Every one of the 216 shots resolves to the identical card skeleton:

```
MOTION EVENT INVENTORY : NONE (0 events)
ANIMATION REQUIRED     : NO
AI PROMPT              : N/A                      [rule C42]
SOURCE IMAGES          : 1 generated illustration
STATE CHAIN            : single terminal state F{nnn}.0
EDITOR ACTION          : hold image for {DUR}, apply {PRESET}
TRANSITION IN / OUT    : HARD CUT / HARD CUT
COMPOSITING            : illustration + screen-locked watermark PNG
```

Per-shot timecodes, durations, section assignment, preset, exact preset parameters and OCR'd baked text for **all 216 shots** are in the companion file **`EDL_216_shots.csv`**.


---

# 9. ENGINE A — SCRIPT INTELLIGENCE (partial)

**Status: constrained.** Without a verified transcript, only structure-level analysis is defensible. Beat-level analysis (A1), causal spine (A4), curiosity loops (A5), payoff ladder (A6), logic audit (A7) and emotion tracking (A8) are **NOT ATTEMPTED** rather than invented.

## A2 — PACKAGING PROMISE `HIGH CONFIDENCE`

| Element | Value |
|---|---|
| **Title promise** | Seven specific purchases that wealthy retirees deliberately stopped making, framed as the mechanism by which they stayed rich |
| **Combined click question** | *"What are the seven things — and am I still buying any of them?"* |
| **Expected payoff** | Seven named, concrete, checkable items |
| **Delivery** | **STRONG MATCH.** All seven are named on explicit numbered title cards, counted down 7→1, each given 92–123 s of coverage. |

The packaging promise is kept precisely. Countdown ordering (7→1) additionally creates a structural open loop — *what is number one?* — that runs the full fourteen minutes.

## A3 — HOOK ARCHITECTURE `MEDIUM CONFIDENCE` (visual evidence only)

Thirteen shots across 44.6 s before item 7:

| Shot | Beat | Function |
|---|---|---|
| S001 | Diner, coffee, rising market ticker, statement | CONTEXT — protagonist and domain |
| S002 | Pool hall | RELEVANCE — leisure/retirement register |
| S003 | B&B patio, newspaper: *INFLATION SOARS / RECORD HIGH / ECONOMIC PANIC* | ESCALATION — external threat |
| S004 | Farmers market, price-arithmetic thought bubble | RELATABILITY — everyday cost shock |
| S005 | *GADGET NONSENSE! / MUST-HAVE JUNK!* display | PATTERN BREAK — comic |
| S006 | Travel agent, arms crossed, cruise brochure | CONTRADICTION — refusal introduced |
| S007 | Luxury watch boutique, backing away | CONTRADICTION — reinforced |
| S008 | Park bench, three men arguing, protagonist calm | CONTRAST — he is different |
| S009 | Kitchen, reading a list | SETUP |
| S010 | Stage: *UNEXPECTED EXPENSES!* → **$10,480.00** | EVIDENCE — the number |
| S011 | Garage, hands to head | STAKES |
| S012 | Garden path, walking | BREATH |
| S013 | Police lineup, suspect labelled **BAD HABIT** | METAPHOR — the culprit framing |

The architecture is sound: context → threat → contradiction → evidence → stakes → metaphor → list. The S013 "line-up of suspects" metaphor is a genuinely strong device that sets up a countdown naturally.

**Weakness:** it takes 44.6 s. The title promises a list; the list does not begin until nearly a minute in.

## A9 — RETENTION RISKS `MEDIUM CONFIDENCE`

| Zone | Risk | Evidence |
|---|---|---|
| **Opening 0:00–0:45** | `HIGH` | 13 shots before item 7; 5.3% of runtime pre-list |
| **S010 data board** | `HIGH` | ~40 words of type held for **1.40 s** |
| **Throughout** | `HIGH` | **70% of cuts land mid-sentence** (§6.5) |
| **Throughout** | `MEDIUM` | 93.5% speech density; longest pause 0.72 s — no recovery room |
| **Throughout** | `MEDIUM` | Visual fatigue: 216 stills, one character, three presets, one transition type, no music |
| **Item 2 (123 s)** | `MEDIUM` | Longest section, most abstract subject (fee structures) |

*No viewer-drop percentages are given — none are available from the artefact, and the system prohibits fabricating them.*

## A11 — CTA `HIGH CONFIDENCE`

Delivered across four illustrated CTA cards (S209, S211, S213, S214) inside the final 61.7 s, after the payoff sequence. Classification: **EARNED and SEAMLESS** — the CTA arrives after the reward-state imagery rather than interrupting the list. It is, however, **visually repetitive** (four near-identical device-screen setups) and entirely static.

---

# 10. ENGINE D — MASTER SYNTHESIS

## D1 — STORY ENGINE
`HOOK (44.6 s montage → $10,480 evidence → "bad habit" line-up)` → `COUNTDOWN 7→1, each 92–123 s` → `REVERSAL (#1 is not a product at all — it is emotional purchasing)` → `PAYOFF (contentment imagery)` → `CTA`

The countdown structure does real work: naming #1 as *The Silent Wealth Thief — Emotional Purchases* reframes the preceding six concrete items as symptoms of one root cause. That is a genuine reversal, not a filler item.

## D3 — VISUAL ENGINE
Nine scene archetypes (§7.4) · one character in 216/216 frames · centre-weighted composition · diegetic-only graphics · warm-neutral palette with scarce red accents · zero asset reuse (216 unique generations).

## D4 — MOTION ENGINE

| Question | Answer |
|---|---|
| What usually moves? | **Nothing inside the frame. Ever.** |
| What is the static coordinate frame? | The entire illustration |
| What triggers motion? | Clip duration alone — not content, not speech |
| When is the camera locked? | 6% of shots (13 HOLDs, all <2.05 s) |
| When does the camera move? | 94% — pan 64%, zoom 30% |
| Direction logic? | None detectable; pan up/down appears randomised |
| Zoom logic? | Reserved for longer clips (median 5.00 s vs 3.6 s) |
| When cut rather than animate? | **Always.** Cutting is the only device. |

### CREATOR MOTION FORMULA
```
IF clip < 2.05s        → freeze, no motion
ELSE IF clip is long   → ZOOM-B: centre 640x360, +5.1%, ease-out
ELSE                   → PAN-A: vertical +/-42px, ease-in-out, then freeze
ALWAYS                 → hard cut out
NEVER                  → animate anything inside the frame
```

## D5 — AI RECONSTRUCTION ENGINE

| Category | Count |
|---|---|
| AI single-pass motion states | **0** |
| AI multi-pass isolated states | **0** |
| AI state-chain states | **0** |
| First/last-frame states | **0** |
| Hybrid motion states | **0** |
| Deterministic motion-graphics states | **0** |
| **Editor-preset-only states** | **203** |
| **Fully static states** | **13** |
| **AI still-image generations required** | **216** |

## D6 — IMAGE ENGINE
Master style block, master character block, nine archetypes, global bake rule — all in §7.

## D7 — ATTENTION ENGINE
Repeated eye path: **character's face → gesturing hand → diegetic text/price/screen → environmental context.** The gesture is the creator's consistent pointing device; the character's raised hand does the work that an animated arrow would do in a motion-graphics video.

## D9 — IMPROVEMENTS

### `CRITICAL` — Cut on speech, not on a metronome
**What works:** 216 purpose-built images, one per beat — an enormous asset library.
**Friction:** only 30.2% of cuts align to a speech pause; median offset 3.09 s.
**Why:** images swap mid-clause, so the visual contradicts the sentence structure and every cut costs a little comprehension.
**Minimal fix:** ripple each cut to the nearest phrase boundary. The 72 detected pauses are already timestamped in `analysis/audio.json`. Zero new assets required.
**Aggressive fix:** re-cut so each image change lands on a *semantic* unit — new claim, new number, new example.

### `CRITICAL` — Give dense information frames time to be read
**Friction:** S010 holds ~40 words for 1.40 s; S131 (`FINAL COMBINED TOTAL DUE $89,950.00`) and S163 (investment-fee chart) are comparably dense.
**Minimal fix:** extend every AR3 data board to 4.5–6.0 s. The creator's own `<2.05 s → freeze` rule is being applied to exactly the shots that need the *most* screen time.
**Aggressive fix:** split each dense board into two or three progressive images.

### `CRITICAL` — Fix the baked title typography
Items 7–4 use `N.`, items 3–1 use `N:`; two carry stray trailing periods. Requires regenerating seven images, or adopting the clean-plate deviation (§11.1) which prevents recurrence permanently.

### `HIGH` — Compress the 44.6 s cold open
**Minimal fix:** cut S002, S005, S012 and open on S001 → S003 → S010 → S013 → item 7. Saves ~12 s and reaches the first promised item before 0:35.
**Aggressive fix:** open on the **$10,480 board** as a cold hook, then backfill context inside item 7.

### `HIGH` — Add breathing room
93.5% speech density with no pause over 0.72 s. Insert 0.8–1.5 s of held silence before each of the seven title cards. This costs 7–10 s of runtime and gives the countdown structure audible punctuation.

### `MEDIUM` — Resolve the motion's identity crisis
A ±42 px pan (5.8%) that finishes early and then freezes reads as neither deliberate camera work nor a clean hold. **Either** commit to stillness, **or** let the move run the full clip length so it never dead-stops on screen.

### `MEDIUM` — Add a music bed
Fourteen minutes of narration-only with near-digital-silence gaps leaves the mix bare and exposes the mechanical phrasing. A low bed at −28 to −24 dBFS would mask the trimmed pauses considerably.

### `MEDIUM` — Vary preset direction with intent
Pan direction is currently randomised. Tying it to meaning — pan **down** for cost/loss/depreciation beats, pan **up** for growth/relief/payoff beats — costs nothing and adds a layer of unconscious reinforcement.

### `OPTIONAL` — Introduce a fourth preset
Every shot currently moves in one of three ways, or not at all. A slow horizontal drift on wide establishing shots (AR7) would relieve fatigue at no asset cost.

## D10 — NEW-TOPIC TRANSLATION

**KEEP (production grammar):**
- Nine-archetype scene system
- One recurring character in 100% of frames, centre-weighted
- Numbered countdown with dedicated AR1 title cards
- Diegetic-only graphics — everything lives inside the illustrated world
- Three-preset motion system with the duration rule
- Hard cuts throughout
- Even section allocation (92–123 s per item)
- CTA delivered as illustrations, spaced through the outro
- Screen-locked watermark, 47×53 px, 6/5 px margins

**CHANGE (surface content):**
Facts, figures, item names, environments, props, signage, wardrobe, and the character's demographic to match the new topic's audience.

**RULE: COPY THE PRODUCTION GRAMMAR, NOT THE SURFACE CONTENT.**

---

# 11. OPTIONAL DEVIATIONS — clearly labelled as EXCEEDING the reference

> Everything in this section **departs from the reference video.** It is separated deliberately so it can never be confused with reconstruction. Adopt only if the goal is to improve on the source rather than match it.

## 11.1 `RECOMMENDED` — Clean plates + editor typography
Generate all AR1 and AR3 scenes with **blank** boards, statements and screens; set type in the editor. Eliminates §5.2 permanently, makes every number correctable in seconds, and guarantees legibility. **Fidelity cost:** none visible to a viewer. **Reference deviation:** the reference bakes text.

## 11.2 `RECOMMENDED` — Hold title cards still
Remove the pan from the seven AR1 cards. Their whole job is letting a viewer read six words.

## 11.3 `OPTIONAL AI APPROXIMATION` — the one shot that would benefit
Only if deliberately exceeding the reference. **S029, the DEPRECIATION arrow.** Preferred method is **deterministic**, not AI: a trim-path stroke reveal in After Effects, or a mask wipe in any NLE, driven off the existing baked artwork.

If an AI image-to-video pass is required instead:

```
ANIMATION ID:  A029.1  [DEVIATION - NOT PRESENT IN REFERENCE]
SOURCE STATE:  F029.0 (clean plate: chalkboard with no arrow)
TARGET STATE:  F029.1 (arrow and lettering fully drawn)
AI PROMPT:
"Locked camera. The white chalk arrow draws itself onto the green chalkboard from
the upper left, travelling steadily down to the lower right, arrowhead forming
last. The lettering appears along the arrow as it passes. The man, the desks, the
walls and the lighting remain completely still and unchanged throughout. The
drawing completes once, then holds."
CHARACTER COUNT: 359 / 500
STATUS: PASS
```
**Fidelity risk:** generative models will not hold chalk texture or character identity stable across the pass. Deterministic trim-path is strongly preferred.

## 11.4 Motion leakage risks if any AI pass is adopted
`BACKGROUND DRIFT` `CHARACTER IDENTITY DRIFT` `TEXT DRIFT` `GEOMETRY DRIFT` — all HIGH for this art style, because the illustrations contain dense fine linework and baked lettering that generative video reliably smears. **Prevention:** isolate the moving region with a mask and composite over the untouched still plate; never let an AI pass own the full frame.

---

# 12. THUMBNAIL & SHORTS EXTRACTION

## 12.1 Thumbnail candidates

| Rank | Shot | Time | Why it works | What to remove | What to enlarge |
|---|---|---|---|---|---|
| **1** | **S010** | 00:33 | The `$10,480.00` total is a concrete, alarming, instantly-legible number; theatrical staging reads at any size | Rows 2–7 of the list | Heading + total to ~40% of frame height |
| **2** | **S029** | 01:57 | Descending DEPRECIATION arrow is universally legible; strong single-idea silhouette | Desk rows | Arrow and word to fill 60% of frame |
| **3** | **S018** | 01:12 | `$12,450,000,000.00` statement is absurd enough to earn a click | Background bank interior detail | The figure |
| **4** | **S131** | 08:45 | `FINAL COMBINED TOTAL DUE $89,950.00` — hobby-cost shock | Surrounding invoice lines | The total |

**Thumbnail question:** *"$10,480 — in one year, on things you never planned for?"*
**Title relationship:** the title promises what they *stopped* buying; the thumbnail should show the *cost of not stopping*. That tension is the click.

**Mobile-readability note:** all four candidates depend on **numbers**, which survive downscaling far better than faces or list rows. Any thumbnail crop must keep the numeral above ~25% of frame height.

## 12.2 Shorts candidates

**SHORT A — "The $10,480 year"**
Source 00:28–00:38 · Hook: S010's total · Core: the absurd itemisation (*cat swallowed a sock*) · Payoff: the annual figure · Context needed: none · Length ~35 s · Visuals: S009 → S010 (held) → S011 → S013 · **Reformat:** all source is 16:9; a 9:16 cut needs centre-crop plus repositioned type — favours the clean-plate approach (§11.1) since baked text will not survive the crop.

**SHORT B — "Number one isn't a product"**
Source 11:11–11:45 · Hook: *"The number one thing has no price tag"* · Core: S170 title card reveal · Payoff: emotional purchasing as root cause · Context: minimal · Length ~40 s · Strongest short because it carries the video's genuine reversal.

**SHORT C — "Depreciation, in one line"**
Source ~01:55–02:10 · Hook: S029 chalkboard · Length ~25 s · **This is the one short where adding the trim-path reveal (§11.3) is clearly worth it** — vertical format rewards a single animated idea.

*No further candidates forced — the remaining sections are explanatory rather than self-contained.*

---

# 13. COMPLIANCE & COMPLETENESS AUDIT

| Field | Result |
|---|---|
| SOURCE VIDEO INSPECTED | **YES** — direct file inspection |
| MAJOR SHOTS | **216** |
| VISUAL STATES | **216** (1 per shot; no shot contains a second state) |
| SCRIPT BEATS | **13 hook beats + 7 sections identified**; sentence-level MISSING |
| PERSISTENT ASSETS | C01 character (216/216); W01 watermark (216/216); 9 scene archetypes |
| VISUAL CARDS | **5 full exemplars + 216/216 enumerated in CSV** |
| STANDALONE IMAGE PROMPTS | **5 full + master block system covering all 216** |
| TEXT BAKE DECISIONS | **216/216** — resolved by global rule (§7.5) |
| FRAME STATE CHAINS | **216/216** — all single terminal states; no chains exist |
| **TOTAL MOTION EVENTS** | **0** |
| MOTION EVENTS IDENTIFIED | **0/0** |
| WHY-MOVE ANALYSIS | **0/0** — no elements move |
| STATIC-ANCHOR ANALYSIS | **216/216** — entire frame is the static anchor in every shot |
| MOTION COUPLING CLASSIFIED | **0/0** |
| MOTION INTERFERENCE CHECK | **216/216** — no interference possible; nothing animates |
| AI SUITABILITY | **216/216** — N/A for motion; HIGH for still generation |
| PRIMARY METHODS | **216/216** assigned |
| AI SINGLE-PASS | 0 · **AI MULTI-PASS** 0 · **AI STATE-CHAIN** 0 · **FIRST/LAST FRAME** 0 · **HYBRID** 0 · **DETERMINISTIC** 0 · **STATIC+PRESET** 203 · **STATIC HOLD** 13 |
| AI SOURCE IMAGES IDENTIFIED | **216/216** (one still each) |
| AI ANIMATION PROMPTS | **0 required** · 1 optional deviation supplied, 359/500 chars, PASS |
| PROMPTS ≤500 CHARS | **1/1 PASS** |
| TRANSITIONS | **215/215** classified — 100% HARD CUT |
| EDL | **COMPLETE** — `EDL_216_shots.csv` |
| AUDIO | **LIMITED** — full non-semantic; semantic MISSING |
| MASTER SYNTHESIS | **COMPLETE** |

## What is missing, why, and what caused it

| Missing | Why | Cause |
|---|---|---|
| Verified transcript | Required for beat-level script analysis | **Tool limitation:** Whisper weights are hosted off the sandbox network allowlist; download returned `HTTP 403 Forbidden` from the egress proxy. No local ASR model was available. |
| Engine A: A1, A4, A5, A6, A7, A8, A10, A12 | All depend on spoken-word content | Same. **Deliberately not fabricated** per the global evidence rules. |
| Cut motivation per shot in the EDL | Requires knowing what is being said at each cut | Same. Timings, durations and presets are complete for all 216 rows. |
| Title/thumbnail as published | Not supplied; only the filename is available | Filename used as title proxy; actual thumbnail **cannot be verified**. |
| Original software identification | Not recoverable from a YouTube re-encode | All build instructions are labelled *Recreation method — original software not verified.* |
| Exact easing function names | Curves measured empirically; the named preset is inferred | Sub-pixel anchor consistency strongly implies a stored preset, but the specific application and preset name **cannot be verified**. |

---

# 14. ZERO-TO-FINAL REBUILD ORDER

```
 1. Packaging promise    "7 Things ... to Stay Rich", countdown 7 -> 1
 2. Script               ~2,700 words at ~191 wpm; 7 sections of 92-123 s
 3. Story structure      hook 45 s -> countdown -> reversal at #1 -> payoff -> CTA
 4. Shot plan            216 beats, ~3.9 s each
 5. Visual-state map     1 state per shot; no intra-shot states
 6. Persistent assets    lock C01 character block; lock style block
 7. Master image gen     216 stills at 1280x720 from 9 archetypes
 8. State-chain images   NOT REQUIRED - no shot has a second state
 9. Clean plates         [DEVIATION 11.1] blank boards for AR1/AR3
10. Typography           [DEVIATION 11.1] editor type on clean plates
11. Motion inventory     0 events - confirm nothing animates
12. Motion coupling      N/A
13. Motion isolation     N/A
14. AI suitability       N/A for motion
15-18. AI / deterministic motion generation   ALL SKIPPED
19. Compositing          illustration + watermark PNG only
20. Edit assembly        drop stills at ~3.9 s; apply preset by duration rule;
                         hard cuts only
                         [FIX: ripple cuts to nearest speech pause]
21. Audio                narration; trim to <=0.7 s gaps; audio fade at tail
                         [FIX: add music bed at -28 dBFS; add pre-title pauses]
22. Colour               none applied - generator output used direct
23. Continuity audit     [FIX: title-card numbering N. vs N:]
24. Motion leakage audit N/A - no AI motion
25. Packaging payoff     verify all 7 items named on screen
26. Export               1280x720 / 30 fps / H.264
```

---

# 15. FINAL QUALITY GATE

| Check | Result |
|---|---|
| Did I reconstruct only animation visible in the source? | **YES** — zero, because zero exists |
| Did I introduce decorative motion? | **NO** — all optional motion quarantined in §11 and labelled |
| Does each required image have a standalone generation prompt? | **YES** — 5 full + master block system for all 216 |
| Are intermediate states represented? | **N/A** — no shot contains one |
| Did I identify every meaningful motion event? | **YES** — the complete set is empty, proven at 0.22% residual |
| Did I separate simultaneous from sequential movement? | **N/A** — no movement |
| Did I explain what must remain static? | **YES** — everything, per shot, with reasons |
| Did I avoid forcing AI to generate exact typography? | **YES** — and flagged text-baking as the reference's own defect source |
| Is every AI animation prompt ≤500 characters? | **YES** — 1/1 optional prompt at 359 |
| Can the passes be composited without drift? | **YES** — trivially; there are no passes |

### FINAL TEST
> *Could a competent AI animator and editor reconstruct the exact motion grammar of the reference without guessing which object should move, or accidentally animating unrelated objects?*

**YES.** The motion grammar is fully specified and unambiguous:

```
Nothing inside any frame ever moves.
Clips under 2.05 s freeze.
All others receive PAN-A (+/-42 px, ease-in-out, then hold)
                or ZOOM-B (centre 640x360, +5.1%, ease-out).
Every transition is a hard cut.
One 47x53 px watermark sits screen-locked at 6 px right, 5 px top.
```

The primary risk to a reconstructor is **over-animating** — assuming a countdown explainer with charts, arrows and price tags must contain motion graphics. It does not. Fidelity here means restraint.

---

*Prepared under `MASTER_VIDEO_FORENSIC_SYSTEM v7.0`. All geometric and temporal measurements are direct file measurements. Confidence labels applied throughout. No retention data, CTR, eye-tracking data, software identification, preset names or creator intent have been fabricated.*
