# 05 Master script playbook (D5): what the xkcd What If? corpus shows, and how an original channel may use it

Status: **self-review draft v0.1**. Scope: *script* and its timing. Source: 83 transcripts and their audits, recomputed counts in `05_CROSS_VIDEO_SYNTHESIS.md`, timing in `06_LAYER_RECONCILIATION.md`. Not Casually Finance rules: nothing here borrows that channel's timing, hook or retention heuristics.

**Rule classes** (AGENTS.md): `OBSERVED` = seen in the transcripts, `MEASURED` = computed, `INFERRED` = my reading of why, `OWNER` = a choice, never a platform fact. **No rule here is a performance claim**: there is no retention, CTR or watch-time data for any xkcd video. **IP boundary:** describe structure, never reuse wording, jokes, drawings or scripts; the study is of mechanism, not material.

## A. Shape of a long script (MEASURED, n=43)

| Item | xkcd corpus | Use for an original script |
|---|---|---|
| Length | median 680 words, 3:16, range 569 to 1,414 words | A **reference point, not a target**. Higher-viewed 2024 videos ran about 850 words; within a year, longer correlates with views (rho +0.56 to +0.62, n 14 to 17). The performance case for cutting to the median is not supported. **OWNER decision.** |
| Speech rate | 3.6 words per second over the full runtime; 3.8 over speech | Budget about 3.6 w/s for runtime planning |
| Paragraph rhythm | median 25 paragraphs | Plan beats at roughly 25 to 30 words each |
| Question marks | median 2 | Not a driver (rho about 0 against views) |
| Numerals | 2.4 per 100 words | Moderate number density, units explained in homely terms |

## B. Opening (OBSERVED, 41/43 long videos)

1. **State the asker's question in one sentence, attributed to a person.** Then **reframe it in beat 2**: correct a misconception, give the answer first and withhold the *mechanism*, deflate, or show a flash-forward. 10/10 in the first audited batch, 41/43 overall.
2. Narration begins at 0.0 s in 44/44 measured videos; the first on-screen event lands at about 2 s (MEASURED). No cold silence, no logo-first.
3. Cold-open evidence from captions is limited; an intro sting cannot be established from text.

Exceptions to copy neither way: V019 (narrator asks, doubles as promo), V024 (meta hook about competing coverage).

## C. Spines (OBSERVED; keyword-tagged counts are approximate)

Ladder or escalation (about 13 of 43), frame or idiom (about 6), consequence cascade (about 5), feasibility audit (about 4), anticlimax or deflection first (about 4), elimination tournament (about 2). A spine is a **repeatable skeleton for the argument**, not for the jokes: pick the one the physics dictates (a scale question wants a ladder, a "what happens next" question wants a cascade).

**Seams.** 38 of 40 Shorts are contiguous excerpts or abridgements of a long script, cut at an act break, a direction pivot, or one obstacle. INFERRED: write each long script **with its Short seams marked** (self-contained 100 to 300 word segments with a complete mini-arc), and run a logic check on every cut. Cuts have broken logic (V037, V038, V041, V076).

## D. Comic and emotional register (OBSERVED)

Dry deadpan, absurd bureaucracy (committees, building codes), an imagined objection, a running gag. The comic frame is often *dropped* in the Short cut and the physics chain kept: the humour is a layer over a self-contained reasoning chain. Emotions run curiosity then amusement then mild unease; awe or dread appears late and rarely.

## E. Endings and CTA (OBSERVED)

No summary. The ending is a **button**: a reframe, deadpan advice, an aphorism, a callback, a P.S. that flips a premise. **No CTA in 38 of 43 long videos** and no subscribe, Patreon, sponsor or next-video wording in any of the 83 (one book promo, one playful real-world action). **Visual qualification (checkpoint 8):** the transcripts carry no CTA wording, but all 44 long videos checked by keyframe close on a red end card of about 10 s with credits, four book covers and a book URL (a visual book promo; not in the 24 Shorts checked). So the no-CTA finding is about spoken and captioned wording only. This is a style fact about one established channel with a large audience; it is **not evidence that a new channel should omit CTAs** (INFERRED confound: xkcd's audience already exists).

## F. Narration and visual timing to plan against (MEASURED, 44 videos; relation to voice UNVERIFIED)

| Parameter | Long | Short |
|---|---|---|
| Median shot (hard-cut span) | 8.4 s | 6.5 s |
| Visual event gap | about 2.2 s | about 2.0 s |
| Visual events per 100 spoken words | 10.0 | 9.8 |
| Pauses of 0.35 s or more | about 9.7 per minute | about 10.4 |
| Words per shot | about 39 | about 32 |

Plan the script as **narration beats with one visual change per roughly ten words**, a scene swap about every 40 words, and a short breath about every 6 seconds. Visual "change" in this corpus is mostly a label or object popping on (about 25%), a scene swap (about 20%) and writing on (about 9%) rather than camera movement (long-form event shares; the ledgers record no camera motion in 615 of 718 shots, 86%, with pans, zooms or drifts in the rest).

## F2. Putting a quantity on screen (OBSERVED, targeted pass, one coder; see `07_SCIENCE_VISUAL_PASS.md`)

In 125 frames at quantity moments (all 44 media-available long videos plus 38 Shorts, `07b_*` and `07c_*` extend it) the spoken number was on screen in 53 of 105 cases (Shorts 46%, long 53%). Shorts mostly reuse the long video's art recomposed vertically, so plan each Short's quantity visuals as a portrait recomposition with the same numerals. The commonest device is a numeral or unit label beside the drawing, often in a different representation from the narration (miles drawn as a metre axis, one sixteenth gravity drawn as 0.61 m/s2). Comparisons ride on layout: side-by-side panels, a scaled axis, a number line with landmarks. A tiny drawn person or a labelled bracket gives size. Huge or abstract numbers are often drawn as context, not as the number. **Use as a storyboard checklist: for each script quantity decide label, axis, side-by-side, scale reference, elapsed-time stamp or worked board calculation, and decide on purpose when the number is not shown.** Not a performance claim; stills only.

## G. Things the corpus does NOT support (do not write rules from these)

- Any claim that this structure causes retention, CTR or growth.
- A specific hook formula that "works": 41 of 43 videos use one hook family, so there is no contrast set within xkcd, and no evidence about alternatives.
- Voice timbre, music, mixing and sync judgments (listening blocked). Machine loudness only (`09_AUDIO_LEVELS_88.csv`): median -16.5 LUFS, 84 of 88 within -17.5 to -15.5, loudness range about 3 LU, practically no digital silence. This is a description of the mix, not of how it sounds.
- Anything about Machine A-only data (not checked).

## H. How an original channel should use this

1. Treat sections A to F as a **comparison baseline** for a draft's measured shape (words, beats, event density), not as a template.
2. Test the opening and ending choices as the owner's hypotheses (`OWNER` class) against the channel's own data when it exists.
3. Before delivery, every production script goes through `scripts/check_slop_risk.py` (AI-slop gate) and the reference-framework check from AGENTS.md; this playbook is not a substitute.
4. Re-run `scripts/phase5_corpus.py`, `scripts/phase6_timing.py` and `scripts/phase7_tally.py` after any new data and update this file; each rule above carries its recompute path.
