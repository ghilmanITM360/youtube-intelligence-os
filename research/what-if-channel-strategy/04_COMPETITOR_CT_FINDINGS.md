# 04 — Competitor video forensics: 3 outliers, one per leading format family

The owner approved downloading these 3 videos on 2026-11-18. Standard: `visual-ct-scan`.

**Achieved mode:** STRUCTURAL+, not a full CT_SCAN (see §4).

**Where the media and evidence are (outside Git):**
- Media: `$YIOS_MEDIA_ROOT/WhatIfCompetitors-MP4/` (Machine B: `/Users/ghilmanislam360/Documents/YIOS-Media-Library/`)
- Evidence: `/Users/ghilmanislam360/Documents/YIOS-local-audits/2026-11-18/WHATIF_COMPETITOR_CT/`, containing `source_manifest.json`, `coverage.json`, `quality_gate.json`, per-video `pass_summary.json`, contact sheets, `continuation_handoff.md`

| Video | Channel (subs) | Views / PI (03) | Family | Duration | SHA-256 (prefix) |
|---|---|---|---|---|---|
| nAWpLtG-kNs "How Long You'd Last in Every Prehistoric Era" | Fossil (58K) | 13M / 71× | L ladder | 16:10, 25 fps | f0d9cbcc |
| gpLC_ELulyg "What If You Sped Up and Couldn't Stop?" | Minute Zero (24K) | 2.4M / 49× | R runaway | 9:00, 30 fps | 2a9dc332 |
| 0iBYMwGDin0 "What If Asteroid Apophis Hit Earth? Scientists Mapped Where It Lands" | Tracer Project (3.5K) | 5.6M / 6,829× | T timeline | 13:28, 30 fps | 38d19e49 |

## 1. Measured (full-duration ffmpeg passes; candidates, not verified cuts)

| Metric | Fossil (L) | Minute Zero (R) | Tracer (T) |
|---|---|---|---|
| Scene-change candidates (score > 0.25) | 212 | 2 | 16 (dissolves under-counted) |
| Median interval between candidates | 4.1 s | effectively one continuous shot | 59 s |
| Frames held still (state-detector mean diff < 0.5) | 72% | 11% | 85% |
| Frames in gradual motion | 26% | 82% | 14% |
| Spoken words / words per minute | 2,728 / ~169 (Whisper ASR) | **0: no narration** (ASR finds only music) | 2,119 / ~157 (YouTube captions) |

## 2. Observed grammar per video (contact sheets at 1 frame per 5 s; reviewed sheets listed in `coverage.json`)

### Fossil — L ladder
- **Structure:**
  - Opening frame: time machine stuck → "which era could you survive? just you, no tools".
  - Then chronological rungs, Precambrian → Pliocene.
  - Each rung runs the **same checklist**: air/oxygen, temperature, water, food, predators, fire.
  - Each rung ends with a **verdict on a tier board** (Hours → Days → Weeks → Months → Most of a year → A year+) that is shown again after every rung.
  - The video ends with best and worst.
- **Visuals:** a compilation of third-party paleo-art and documentary footage and stills, with screen-captured tier-maker UI, era title cards with dates, a reaction-meme face, simple stick-figure line gags, and a search-result screenshot used as evidence.
- **Accuracy:** at least one factual slip heard. The ASR transcript says "the Pliocene, also known as the Ice Age"; the Ice Age is the Pleistocene. INTERPRETATION: being accurate is a real way to stand out.
- **Transferable:** a fixed per-rung checklist plus a persistent scoreboard.
- **Not transferable:** third-party footage (copyright; 01 §6).

### Minute Zero — R runaway
- **Structure:** one continuous first-person POV in low-poly 3D. The speed escalates from walking pace to 99.999…% of the speed of light.
- **On-screen elements:**
  - A permanent HUD: "YOUR SPEED", distance, next landmark, and a time-dilation counter ("AT HOME, IT IS THE YEAR …").
  - One serif-italic caption roughly every 5 s, e.g. "You can't slow down.", "An airliner, taking off. You pass it on foot.", "Ahead: the Moon.", "The Virgo cluster. Thirteen hundred galaxies."
  - Real-world landmarks act as rungs: traffic, airliner, fastest jet, orbital speed, Moon, Andromeda, Virgo cluster, the Great Wall of galaxies.
- **Cold open:** the end state (99.999…%, galaxy streaks) comes before the title card.
- **Production:** no voice-over. Procedurally simple: a single scene, a camera on a path, numbers driven by one variable.
- **Transferable:** the HUD as progress tracker, landmark rungs, and an end-state cold open.

### Tracer Project — T timeline
- **Structure, in order:**
  1. Cold open on a specific place and time ("ISTANBUL · 13 APRIL 2029 · 00:45").
  2. A credibility card: "SIMULATION — nothing in it is made up".
  3. Real history (2004 discovery, 1-in-37 odds, then **"0.0% — 2029 impact: ruled out"**).
  4. "THE MATH" cards, including size vs Eiffel Tower / Empire State and the break-up criterion ρ·v² > Y with an on-screen citation (Collins, Melosh & Marcus 2005).
  5. The impact sequence with T-minus/T-plus clocks ("ZERO SECONDS", "HEAT ARRIVES AT THE SPEED OF LIGHT", "M 6.6").
  6. A **"HOW FAR AWAY ARE YOU?"** distance-ring ladder with an effects readout.
  7. The ending returns to reality: the real 2029 flyby, OSIRIS-APEX, RAMSES, DART, "look up".
- **Visuals:** photoreal 3D Earth and impact renders with slow camera moves and dissolves, plus flat dark-blue explainer cards. A corner tag labels each segment SIMULATION, REAL HISTORY or THE MATH.
- **Transferable:**
  - labelled evidence layers (a trust device)
  - honesty about the real-world answer up front
  - on-screen citations
  - a distance ladder inside a timeline
  - an echo ending that returns to the real date

## 3. Cross-video synthesis (INTERPRETATION; n = 3, so a starting point, not channel DNA)

1. **A persistent progress tracker in all three:**
   - Fossil: tier board
   - Minute Zero: speed/time HUD
   - Tracer: T-clock and distance rings

   The viewer always knows where they are on the ladder, and how far is left. → Adopted as a calendar constant (05 §1).
2. **The cold open shows the extreme end state, then states the question.** → Adopted.
3. **Real landmarks and comparisons make each rung concrete:** airliner, Eiffel Tower, Moon, named eras. → Adopted in the thumbnail and script concepts.
4. **Edit pace is not what they share.** Hard-change intervals range from about 4 s (Fossil) to one continuous shot (Minute Zero) to about 1-minute dissolves (Tracer). xkcd's own measured median shot length is 7.77 s (CH-000004 DNA). → No pace rule. Choose the pace per format.
5. **Narration is optional for runaway formats** (Minute Zero has none). → HYPOTHESIS worth one test later; it is not in month 1, because the voice is a calendar constant.
6. **Trust devices differ:**
   - Tracer labels its layers and cites sources on screen.
   - Fossil cites a search-result screenshot and makes at least one factual slip.

   → Our differentiator: labelled layers plus primary-source on-screen citations (05 §3 verification table).

## 4. Coverage and what remains for a full CT_SCAN (honest status)

**Done:**
- File identity and hashes (ffprobe).
- Full-duration per-frame state detector (the run-04 C-2 filter).
- Scene-score candidates.
- 1/5 fps contact sheets for every video.
- Visual review of 2 sheets per video (6 of 17 sheets).
- Transcripts: YouTube auto-captions for Tracer; local whisper.cpp for Fossil. Minute Zero has no speech.

**Not done:**
- native-frame dense windows
- a frame-accurate shot ledger and visual-event ledger
- object, motion and camera lifecycle
- audio listening (music, SFX, VO tone) and AV sync
- review of the remaining 11 sheets

Status: `ct_scan_complete=false` in `quality_gate.json`. Two YouTube caption requests got HTTP 429 and were not retried, per the repo rule.

These findings shape *original* production choices only. No frames, footage, captions or scripts from these videos are reused.
