# 06 — Pilot visual analyses (4 videos, 4 previously untouched channels)

**Status of every pilot: `VISUAL_ANALYSIS_PARTIAL`. Audio is `AUDIO_REVIEW_PENDING`.**

What was done for every pilot:
- source hash re-verified;
- every frame decoded;
- a per-frame scene score computed;
- **every second of the timeline viewed** on 1 fps sheets;
- dense windows viewed where the 1 fps view was ambiguous.

What was **not** done:
- frame-accurate event authoring, so overlays shorter than 1 s between samples are not certified;
- certified transcripts: a local whisper.cpp `ggml-small.en` ASR (found at `~/.cache/hyperframes/whisper/models/`, no install) was run late in the session. It is **uncertified machine transcription**, used below only for alignment spot-checks;
- human playback with sound.

Timestamps below come from sheet position: `sheet_1fps_NN` tile k = (NN−1)·30 + k s, accurate to ±1 s. Dense-window timestamps are accurate to the window's sampling step. Evidence paths are relative to this run folder; hashes are in `08_…json`.

Why these four: Primate, Monke, Primitive and Barely Evolved had **zero** prior visual work. Casually Finance long-form belongs to Machine A's pipeline and writer (see 05).
- **Primate, Monke:** median-length long-form.
- **Primitive:** a median 30 s Short.
- **Barely Evolved:** the shortest of its 3 videos.

| | Primate Economics | MonkeBiznis ("monke") | Primitive Education | Barely Evolved |
|---|---|---|---|---|
| Video ID | `DZG89lilGr0` | `95UrFFVrwJU` | `HERcUJ6fIlw` | `uPQcyookL0Y` |
| Title (registry) | Stocks Explained with Bananas | Watch this if you're tired of procrastinating | A Caveman Explains Gen Z Slang - Part 2 | The Worst Time in History to Be Born as a Human |
| SHA-256 (verified = inventory) | `821a4f39…0ffc204` | `9c3f56db…` | `8b7e5730…` | `1416669f…` |
| Duration / frames | 238.89 s / 7,164 | 235.98 s / 5,662 | 29.93 s / 1,494 | 488.78 s / 14,647 |
| Video | 1920×1080, 30 fps, H.264 | 1920×1080, 24 fps, H.264 | 1080×1920 (9:16), 50 fps, H.264 | 1920×1080, 29.97 fps, H.264 |
| Audio | AAC; −18.1 LUFS, LRA 7.1 | AAC; −31.5 LUFS, LRA 4.4 | AAC; −17.0 LUFS, LRA 6.5 | AAC; −19.0 LUFS, LRA 5.9 |
| Scene-score ≥0.30 candidates | 88 (incl. one 8-frame stepped-zoom cluster) | 39 | 5 (undercount, see 04) | 72 (none before 27.93 s) |
| Coverage viewed | 239/239 s at 1 fps + 4 dense windows | 236/236 s at 1 fps | 30/30 s at 2 fps | 489/489 s at 1 fps |

---

## Pilot 1 — Primate Economics `DZG89lilGr0`

**Timeline (observed):**
- 0–1.7 s: hand-lettered title card "WHAT ARE STOCKS?" on white, with yellow sparkle marks. Dense window: the sparkles shift between frames (boil/jitter) (`dense/w_000.0-005.0_6fps.jpg`).
- 1.7–3.3 s: gorilla with thought bubbles. The bubble first appears **empty** (≈2.2–2.3 s), then fills with the "MONKI'S BANANAS" stall (≈2.5 s). This is a two-step reveal.
- 3.4 s: hard cut to an extreme close-up of a crying face with sans-serif text "It's beautiful" (a joke beat).
- 4–60 s: banana-stand business story. Characters: gorilla (owner), top-hat/monocle investor, bank-suit gorilla. The banana labelled "STOCK" is the core metaphor (24–25 s). An ownership pie with portrait icons appears at 28–30 s.
- 23.5–24.6 s: **stepped push-in** on the handshake, scale jumping every ~4 frames (`dense/w_023.4-024.4_30fps.jpg`). This is not a set of cuts.
- Section title cards, hand-lettered with sparkles: "STOCKS vs SHARES" (51 s), "DIFFERENT TYPES OF STOCKS" (77 s), "The STOCK MARKET" (105 s), "STOCK FUNDS" (130 s), "HEDGE FUNDS" (165 s), "WHY DO STOCK PRICES CHANGE?" (181 s).
- Quoted-term cards: "DIVIDENDS" (45 s), "BLUE CHIP Stocks" (97 s), "PENNY Stocks" (103 s), "S&P 500" (138 s, with a yellow radial burst at 139–140 s), "BASICALLY." (120 s).
- 84–90 s: **live-action war-film footage fades in behind the cartoon two-shot**. Characters stay as a cutout layer over the footage while a slow push-in runs (`dense/w_083.0-089.0_5fps.jpg`). A meme b-roll insert.
- Charts: green zig-zag up-arrow with a bull (112–114 s, "weeeee!") and red down-arrow with a bear (115–119 s, "i hate everyone"). The S&P 500 is shown as a rainbow pie of icons (141–156 s), recoloured green/red for up/down markets (157–164 s). A yellow pie with warning triangles stands for risk (170–171 s).
- Third-party marks inserted as jokes: Philadelphia 76ers logo (58 s), Apple logo on a building (109–111 s), Amazon logo (148 s), a politician-like caricature (162–164 s). Realistic hyper-detailed ape face on black (187–188 s), a style break.
- Market mechanics, 189–208 s:
  - crowd-vs-supply demand gag (190–192 s);
  - island map with multiplying "Banana Inc." buildings (193–195 s);
  - news-anchor "CHANNEL 7 BREAKING NEWS!" (200 s);
  - scientists with a **background darkening white→grey over ~3 s** (205–208 s);
  - "BANANA 2" paper (208–209 s) (`dense/w_202.0-212.0_3fps.jpg`).
- 210–211 s: black. 212–218 s: gorilla outro poses.
- **219–238 s: static black end card**, white sans text thanking 100,000 subscribers. Audio continues: no silence detected after 217.5 s.

**Editing DNA (observed in this one video):**
- Flat white background throughout, except for meme inserts.
- Thick black outlines with flat fills.
- Two text registers:
  - hand-lettered capitals for titles, terms and labels;
  - small clean sans for joke captions.
- Motion is mostly pose swaps and cuts, plus stepped zooms and occasional slow pushes.
- Repeated scene templates: character + metaphor object; quoted-term card; section card with sparkles; pie chart.
- Ending: a ~20 s static thank-you card. No end-screen elements are visible in the frames.

**Hypotheses (not observed facts):**
- The frequent absurd inserts (logos, real footage, extreme close-ups) may serve as attention resets.
- No retention data exists to test this.

---

## Pilot 2 — MonkeBiznis `95UrFFVrwJU`

**Timeline (observed):**
- 0–4 s: dark charcoal scene; gorilla at laptop beside an "ESSAY" stack; handwritten "Fu*k" (1–2 s).
- 5–12 s: close-up at a retro monitor showing a parody video UI "MONKETube" → "Fix it" → "LAZY BOI". Facial expression changes per beat.
- 13–18 s: marionette strings on the gorilla, then a push-in to an exposed brain (puppet metaphor).
- 19–30 s: **pink scene**: grey rat character beside a caged gorilla. Green crocodile on dark (23–27 s). Hand-drawn dopamine molecule with label "Dopamine" (28–30 s).
- 31–53 s: rat with "FU*K THIS" handwriting; rat behind the gorilla at a computer (yellow screen → red play icon); return to the monitor close-up.
- 51–53 s: **radial pink glow fades in at the corner**, revealing the rat (also at 73–77 s and 176–184 s).
- 57–65 s: beach scene (rat under umbrella). 65–72 s: banana-on-a-stick bribe.
- Section cards on **cream background** in clean bold sans with four banana glyphs in the corners: "Monke's 3-Step Plan To Trick Rat." (78 s), "Monke's Deal" (126 s), "Monke's Cave" (151 s).
- Chapter header pair "Part 1 / Monke's Bet" at top corners (80–82 s).
- Solution steps in bold sans captions: "Essay" struck through → "Write for 5 mins" (95–96 s), "Just 5mins lil bro", "sus", "this i can do" with clock icon, "First 5mins is the hardest part.", "Lust is powerful", "Boring environment = Fun work", "Write 500 words. ····· Scroll".
- **134–141 s: phone mock-up with real app UI screenshots (habit tracker, YouTube) + QR-code card "Get monke's app by tapping the link in the description".** An in-video promotion of the creator's own app.
- 154–159 s: rat among Meta/Instagram/YouTube icons and bananas (social-media temptation).
- 168–175 s: prohibition sign over phone; monitor shows "404", then "40:59" timer.
- 190–225 s: rapid **callback montage** of earlier scenes (rat at computer, cage, poker table, "Just 5mins").
- 212–233 s: bearded elder gorilla mentor with rectangular speech boxes: "This won't stop you procrastinating…", "Will you take action?", "GET TO WORK!".
- 234–235 s: end card "STAY MONKE" with flexing gorilla.

**Editing DNA (observed):**
- **Background colour encodes narrative register:**
  - charcoal = problem / the gorilla's mind;
  - pink = rat / dopamine world;
  - cream = plan / solution.
- Two characters (gorilla + rat as a personified impulse).
- Clean bold sans for the didactic text, handwriting for in-world text.
- Section cards with fixed decoration. Repeated callbacks.

**Hypotheses (not observed facts):**
- The background-colour coding may act as a navigation aid.
- The own-app QR segment is a monetisation choice; its effect is unknown.

---

## Pilot 3 — Primitive Education `HERcUJ6fIlw` (Short)

**Timeline (observed at 0.5 s steps, `dense/w_000-015_2fps.jpg`, `dense/w_015-030_2fps.jpg`):**
- 0–5.5 s: persistent **yellow-highlighted title bar** "A CAVEMAN EXPLAINS GEN Z SLANG" (bold sans, top).
  - The term "W" appears in yellow quotes at 0 s.
  - The gloss "win" is added at ≈1.0 s.
  - A pose swap to two raised fingers brings in "L" (≈2.0 s), with "loss" added at ≈2.5 s.
- ≈3.5 s: head-scratch pose. The title bar is gone by 6.0 s.
- 6.0–7.0 s: rainbow alphabet graphic.
- 7.5–10 s: shrug pose, caption "N word?" from ≈8.5 s (letter-N pun; ASR resolves it to "nice").
- 10.5–11 s: "nice." alone on white.
- 11.5–13 s: term card "out of pocket".
- 13.5–14.5 s: inserted third-party cartoon character (not channel art).
- 15.0–15.5 s: **live-action meme photo** (costumed person holding a manga).
- 16–17.5 s: two-caveman dialogue, ending in a thumbs-up swap.
- 18–19.5 s: running pose carrying a pot, with a ground shadow.
- 20–21.5 s: throw toward a campfire, with motion lines.
- 22.5 s: shattered pot. 25–25.5 s: ghost rises.
- 26–26.5 s: caveman crying in a black cloak.
- 27–27.5 s: panicked trio. 28–29.5 s: trio on a cliff edge (wide).
- No end card in the last frame.

**Editing DNA (observed):**
- Black line art with **only yellow-leopard tunic colour** on white.
- Rapid pose-swap animation: about 15 distinct states in 30 s by visual count. The scene detector found only 5.
- Term → gloss word-build captions.
- Meme inserts from outside the channel's art style.

---

## Pilot 4 — Barely Evolved `uPQcyookL0Y`

**Timeline (observed):**
- 0–27.9 s: **no scene-score cut at all**. One continuous timeline device:
  - stick figure at "2025" with "This is you." (1 s);
  - the timeline extends left and figures multiply (3–11 s), passing period markers (wig, chain-mail);
  - a "100,000 BC" label with progressive zoom-in (12–17 s);
  - a "Your ancestor" arrow (19 s);
  - close-ups with word reveals "no name / no shoes / no idea" (20–23 s);
  - a split screen of the ancestor vs a modern person on a couch with phone and iced coffee (24–29 s), interrupted by a black-background bloodshot-eye close-up (28 s).
  - The transition type into the close-ups at ≈20 s is UNRESOLVED (no cut candidate; likely a zoom).
- 30–31 s: script-font line "but here is the thing".
- 38–50 s: **painted, detailed landscape backgrounds** with a cut-out "puppet" character (detailed bearded head on a simple body). A recurring **teacher in a classroom** with a chalkboard and a "Barely Evolved Shool" sign (sic) appears at 69–72, 75–78, 97–101, 164–172 (projector), 224–227, 255–263, 281–284, 309–312, 324–325, 334–335 (plague-doctor costume), 349–351, 359–362, 431–438 and 477–487 s.
- **Countdown structure** with numbered chapter cards, each with a small "Survival chance X%" line: "5. Ice Age" 68 % (86 s), "4. The Dawn of Agriculture" 54 % (173 s), "3. The Mongol Invasions" 24 % (264 s), "2. The Black Death" 7 % (322 s), "1. The Toba Supervolcano Eruption" 0.5 % (387 s).
- 79–85 s: **animated bar chart** "Chance of survival (%)" vs "Historical Events" 5→1. Bars grow one by one, yellow→red: 68, 54, 24, 7, 0.5 %.
- Explanatory devices:
  - globe with ice cap growing and a "2 miles" scale bar (92–96 s);
  - thermometer red→blue with "10°F (6°C)" (102–106 s) and "27°F (15°C)" (414–418 s);
  - size-comparison scale bars, human "5 ft 3 in (160 cm) 132 lbs (60 kg)" vs mammoth "11 ft 2 in (340 cm) 13,200 lbs (6,000 kg)" (120–124 s);
  - species label "Panthera spelaea" (126–130 s);
  - "Before farming / After farming" split (211–215 s);
  - "FARMING PROBLEMS" book checklist ticking Drought → Starvation → Goat theft → Diseases (228–235 s);
  - red territory map of the Mongol empire (285–286 s);
  - globe with spreading markers and "Estimated deaths: 40 million" (313–321 s, Mongol chapter);
  - "1347" on the chalkboard (324–325 s); a "PLAGUE EXPRESS" box travelling across a Europe map (326–329, 336–339 s);
  - "Yersinia pestis" bacterium icon (340–343 s);
  - Europe map whose figure markers thin out (367–373 s);
  - ash cloud "670 cubic miles" (398–402 s);
  - population bar 200,000 → 3,000 shrinking green→red (439–444 s);
  - a 3,000-figure crowd cluster labelled "your cousin" (445–451 s).
- **Realistic imagery** shown on the classroom "projector": archaeological photos, a skull, cave paintings, historical paintings (164–172, 255–263, 309–312, 349–351, 359–362, 431–438 s).
- Text effects:
  - "Welcome to the Dawn of [black redaction box]" → "Agriculture" (208–210 s), a redaction wipe;
  - "death" **blur-to-sharp reveal** (363–365 s).
- Atmosphere changes: sun dims and haze builds over ~6 s (406–412 s); sky haze fades to black (460–465 s).
- 466–476 s: closing sequence on black and white: "and yet" → "somehow" → cave fire → "They didn't give up" → "when everything else" → "DID." (heavy display font).
- 477–487 s: "subscribe" on the chalkboard with teacher close-up and pointer.

**Editing DNA (observed):**
- Mixed media: simple stick/cut-out characters over painted, detailed environments, plus real historical imagery framed inside a diegetic projector.
- Numbered countdown chapters, each with a survival statistic.
- Heavy use of measurement graphics: scale bars, thermometers, charts, maps.
- Script-style and handwriting fonts for narration words.

**Visual-accuracy note (observation + ASR):**
- "10°F (6°C)" and "27°F (15°C)" are **not** equivalent absolute temperatures; they match as temperature *differences* (10 °F ≈ 5.6 °C; 27 °F = 15 °C).
- Uncertified ASR has the narration say "temperatures dropped by about 10 degrees Fahrenheit, 6 degrees Celsius" (98.6–110.3 s) and "crashed by up to 27 degrees Fahrenheit, 15 degrees Celsius" (411–424 s). So the audio supplies the "drop" meaning.
- The on-screen card alone (no minus sign) can mislead a muted viewer. This is a minor packaging risk, not a factual error.

---

## Content-to-visual alignment (uncertified ASR spot-checks; no listening)

ASR files: `evidence/<channel>/<id>/asr/whisper_small_en.{csv,json}` (whisper.cpp 1.9.5, model sha256 prefix `c6138d6d58ecc832`).

| Video | ASR (start–end s) | Visual at the same time | Alignment |
|---|---|---|---|
| Primate | 0.0–1.6 "What are stocks?" | Title card 0–1.7 s | Tight: the card mirrors the line |
| Primate | 11.1–12.7 "Monkey rob bank." | Gorilla hands banana to banker at BANK (11 s) | Visual softens the joke (a transaction, not a robbery) |
| Primate | 23.9–25.3 "This is called a stock." | Stepped push-in to banana labelled "STOCK" (23.5–25 s) | Tight: the zoom lands on the term as it is spoken |
| Primate | 84.2–91.8 "[Music]" | War-footage b-roll insert (84–90 s) | Music-only meme beat, no narration |
| Primate | 217.3–220.0 "This video is not financial advice. Please do not sue monkey." | Gorilla outro poses (212–218 s) | Disclaimer is **spoken only, not on screen** |
| Monke | 0.0–13.6 problem setup ("search YouTube to find video that will help") | "MONKETube" monitor (5–12 s) | Tight literal illustration |
| Monke | 126.4–128.0 "Step two, monkey's deal." | "Monke's Deal" card (126–127 s) | Tight; chapter card = spoken chapter |
| Monke | 134.1–141.8 reward "after two hours of studying" | Phone mock-up with real app UI + QR "Get monke's app…" (134–140 s) | **Visual-only promotion**: the narration does not mention the app in this span |
| Monke | 226.7–236.9 "Will you actually take action… Get to work and stay monkey." | Elder "Will you take action?" → "GET TO WORK!" → "STAY MONKE" | Tight; captions echo the narration |
| Primitive | 0.0–15.8 "If W mean win and L mean loss… what N word will be. We hope nice. Out of pocket mean too wild" | W/win, L/loss, alphabet, "N word?", "nice.", "out of pocket" (0–13 s) | Word-by-word caption build. "N word?" is a letter-N pun resolved by "nice." |
| Primitive | 15.8–29.8 elders'-ashes fire story → "bye bye cliff" | Pot thrown in fire, ghost, mourning, cliff (18–29.5 s) | Literal pose-by-pose illustration of the joke |
| Barely | 0.0–34.8 "This is you… powdered wigs, chain mail, mammoths… no name, no shoes, and no idea… snack addiction… caffeine" | Timeline with wig and chain-mail markers, no-name/no-shoes/no-idea cards, couch + iced coffee (0–29 s) | Tight; each listed noun gets an icon or card |

## Validation performed

- Source SHA-256 for each pilot equals the inventory hash (asserted in the 08 build script).
- Frame counts were decoded in full. Durations match ffprobe.
- First and last seconds were viewed for all four.
- Every claim above cites a timestamp from a sheet or dense window stored under `evidence/<channel>/<id>/`.
- No claim about real-time playback, listening, retention, CTR or editing software is made.
