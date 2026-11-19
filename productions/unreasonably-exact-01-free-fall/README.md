# Unreasonably Exact — Day 1 (Mon 2026-11-23): "Does a Higher Fall Always Hit Harder? 1 Metre to the Edge of Space"

**Status:** script **v3 APPROVED by the owner, 2026-11-19** (length cut of v2; the earlier 18 Nov approval was for v1.1). The v1.1 text (title "What If You Fell From Every Height — …") was approved on 2026-11-18, then critically reviewed. v2 replaces it and is not approved yet. Next: voice-over and animation.

| File | What |
|---|---|
| `SCRIPT.md` | Narration (v3, ~890 words, ~4–5.5 min), on-screen directions, evidence labels, Sources. Gated by `scripts/check_slop_risk.py` |
| `SCRIPT.md.slop-risk.json` | Gate report (PASS, no findings) |
| `FACT_CHECK.md` | Per-claim table D1-01..30 (05 §3.1 gate), including the model's stated limits and a v1.1 → v2 change list |
| `thumbnail_day01.svg/.png` | Thumbnail (1280×720): "1 KM: 204 km/h · 100 KM: 204 km/h · SAME LANDING?". Regenerate with `research/what-if-channel-strategy/branding/make_brand_assets.py` + `render.sh` |

## What the review found and what v2 does about it

| Review finding | v2 fix |
|---|---|
| Title had no stakes | New title is a question people assume the answer to; the script answers it on screen at 0:56 |
| Cold-open promise paid off by "we're not going to guess" | Landing-speed line is the running payoff: climbs, then goes flat |
| Dead zone: ground-rules block, low heights, Eustace | One-paragraph rules; heights 1–3 merged; Eustace one sentence |
| No stakes or survival | Three sourced anecdotes; no lethality thresholds (sources disagree) |
| Stapp "hardest ever" claim contested | Removed |
| Model uncertainty hidden | ±15% and the 36 s vs 30 s miss said on screen |
| v1 "95% after 220 m" misapplied | Replaced by landing speeds from 300 m and 1 km (D1-07) |
| Jargon | g, speed of sound and terminal velocity explained in plain words |

**Review 2 (2026-11-19):** cut the 60 km height, added three dry jokes ("Enjoy it. It's about to stop.", terminal velocity's name, space's border like a map's), moved the ISS twist to the end ("Same height. Same gravity. Only one of you is going sideways."), removed the edge-of-space contradiction, flagged the 20 g as shaky, and removed the unrelated 39 km marker from the thumbnail. Word count rose to ~1,230, so runtime is about 9 min with pauses, not shorter. Time stamps were recomputed from word counts.

**v3 length cut (2026-11-19):** the 83-script xkcd study measured their 43 long videos at a median 3:16 and 680 words (31 of 43 under 4 min). v2 was ~1,230 words (~9 min), so v3 cuts it to ~890 words (~4.1 min at xkcd's pace, ~5.4 min at a calmer pace). Cut: ground-rules block, 10 m height, 19 km pressure height, Eustace, Alkemade, Baumgartner spin and freefall-duration detail. Same spine and the same cap-then-flat landing line. Three original dry lines were then added (the air as free safety equipment, estimates as "educated guesses in a lab coat", "more time to reconsider"); they are our own, in the same deadpan register the study observed, not xkcd material. xkcd's structure is followed; their words, jokes, art and reader-mail device are not (08). Runtime is unmeasured until recording.

**Honest status:** these are fixes to problems the review found. They do not make the video a guaranteed success; retention and views remain unmeasured until Day 14 (05 §4).

## Pre-production gates (05 §3)

1. **Science table:** done (FACT_CHECK.md). Three claims are SECONDARY-sourced (D1-10 partly, D1-28, D1-29). No domain expert has reviewed it.
2. **Collision check:** done 2026-11-18. Re-check the xkcd RSS on upload day.
3. **AI-slop gate:** PASS, no findings (a proxy; it says nothing about quality). Manual checklist C1–C5 is for a human to confirm.
4. **Packaging:** the title question is answered on screen at 0:56 and 4:24. Thumbnail numbers are COMPUTED (D1-07, D1-19).

## Day 2 Short

Cut from the `[EXCERPT → Day 2 Short]` segment (Height 3 cap + Height 4, ~0:56–2:06, about 30 s of speech). Gets its own script and review later. Working title (needs a re-check against the v2 framing): "Why jumping from higher makes you slow down before landing".

## Still to do (owner)

- ~~Re-approve the v3 script~~ done 2026-11-19. Day 2 Short script is now unblocked but not written; it needs an explicit request.
- Record the voice-over.
- Produce the animation (original line art).
- Register the CH-id and replace `UNREGISTERED` in the script header.
- Production time: 4 days remain before Day 1 (risk flagged in 05).
