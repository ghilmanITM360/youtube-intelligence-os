# Senior Health Competitive Intelligence: Forensic Report V2

**Date:** 2026-09-25 · **Status:** see `FORENSIC-EXPANSION-STATUS-V2.md` (all gates pass; 4 disclosed caveats)
**Cohort:** 6 channels, 306 videos, 23.66M views at scrape. 305 transcripts are stored; 1 is absent.
**Deep population:** 149 videos.

**Evidence labels used in this report:**
- REPOSITORY_FACT
- ACTUAL_TRANSCRIPT_TEXT
- TRANSCRIPT_LEXICAL_HEURISTIC
- APPROXIMATED_FROM_WORD_POSITION
- LIVE_WEB_VISUAL
- LIVE_GOOGLE_TRENDS
- LIVE_WEB_SEARCH_RESULT
- WEB_RESEARCH
- ANALYTICAL_CONCLUSION

No first-party analytics exist, so every "why" below is a hypothesis backed by observable evidence, not a proven cause.

---

## 1. What changed from the first forensic pass

19 factual errors were corrected (`DATA-QUALITY-CORRECTIONS.json`). The ones that changed conclusions:

- **Dr. Okoro's chronology.** The channel joined 2026-03-19. The breakout was upload #26, on day 58. The pass-1 report said the channel launched around 2026-07. Pass-1 also said the channel "near-totally failed" after the breakout. In fact a second hit followed 18 days later (neuropathy, 100,852 views), and the channel decayed only after that.
- **Senior Health Hub's 3.09M clove video.** It was not a novel one-off. It was the channel's **24th clove upload out of 41**. Clove videos are 34% of the channel's uploads and 73% of its views, and 14 of the 41 reached ≥3x. The channel's baseline did **not** rise after the hit: the median was 9,539 before and 9,418 after. Its own exact repeats of the format returned to about 1x.
- **Title-feature multipliers.** The earlier "3.5x" figures were artefacts of mixing channels of very different sizes. Measured within each channel, every title feature shifts the median by less than 1x. The `has_age_marker` flag is a regex bug: it is identical to `has_number` on all 306 videos.
- **The 247x "audience narrowing" claim.** The actual numbers are 11,319 vs 45 (251x). The loser was posted 42 days later, into channel decay, and its stored transcript had 8 caption tracks concatenated together. A counterexample exists: a diabetes-gated eggs video reached 127,627.
- **Every "estimated" Google Trends value was withdrawn.** It was replaced by 32 live investigations.

## 2. Core findings (evidence-ranked)

1. **The same package on a different channel gives radically different results.**
   - "Dr. Aliza Wright Senior Health" (a separate channel with 22.9K subscribers) published "Taking Amlodipine, Losartan, or Lisinopril…" on 2026-05-31. It has **941,154** views.
   - Five days later the cohort channel with the same persona posted the **same title and the identical thumbnail, typo "LOSARTON" included**. It got **160**.
   - Across 37 same-title pairs between channels, results range from 2 views to 1.6M.
   - Scripts are *not* copied: the highest cross-channel transcript overlap (5-gram Jaccard) is 0.024. Packaging is copied; scripts are rewritten.
2. **Order does not decide who wins a copied title; the copying channel does.**
   - Second movers won 22 of 37 cross-channel same-title pairs.
   - When the copy came 29 or more days later, the second mover won 14 of 16. These are mostly stronger channels re-running weak channels' titles.
   - Inside the Ares↔Elias twin, re-runs posted 15 or more days after the sibling lost 4 of 6.
3. **Ares and Elias show same-operator signals.**
   - They share identical thumbnail text, including the same typos ("ONES OR TWICE").
   - They share the same mismatched thumbnail on a different title.
   - They have 15 shared titles, with rewritten scripts.
   - Ownership is UNVERIFIED.
   - Persona-name clones on other channels ("Dr. Ares Smith Senior Health!", "Wellness After 70 – Dr. Elias") get 1–122 views.
4. **Hits do not raise a channel's floor.**
   - Top video = 13–78% of channel views.
   - Okoro's recent-10 median is 75 after a 494K hit.
   - TopHealthTips (336K subscribers) decayed from 1–2M videos to 2–28K within about two months.
5. **Thumbnails (LIVE_WEB_VISUAL, 149 inspected), within-channel medians.**
   - Answer withheld: **1.90x** vs 0.63x. Answer revealed: 0.47x vs 1.76x, and none of the 14 answer-revealing thumbnails reached 3x.
   - Large number: 2.13x vs 0.80x.
   - Warning icon: 0.55x.
   - Cluttered infographic: 0.91x.
   - Each channel runs a fixed template: Thomas uses a doctor plus text, Aliza a female doctor persona, Ares/Elias a sketch-illustrated senior on black, Okoro a doctor plus a photo inset, SHH macro food plus 3D organ renders.
6. **Openings (actual first ~30 s of the transcript), within-channel medians.**
   - Direct command ("look at your feet right now"): 1.65x.
   - "What if…": 1.33x.
   - Warning-led: **0.32x**, with 14 of 22 below half the channel median.
   - Winners put the viewer inside a lived moment ("2:47 a.m.", pills on the nightstand) and set an open loop within about 100 s.
   - Winners withhold the core reveal for minutes (all times APPROXIMATED_FROM_WORD_POSITION):
     - Thomas's heel cue: ~242 s.
     - Elias's "kiwi": ~493 s.
     - Ares's bath answer: ~690 s.
7. **Search demand is context, not cause (LIVE_GOOGLE_TRENDS).**
   - **Trend-amplified:** Okoro's neuropathy video landed in the 5-year worldwide peak week (GT-24). SHH's clove franchise rode a ~10x five-year rise (GT-01). Garlic-at-night landed near the January peak (GT-22).
   - **Winners with no search tailwind:** bathing (0/100 before upload, GT-20), eyesight fruit (0 in the upload week, GT-21), Ares sleeping position (launched after the peak, into a dip).
   - **High interest that did not rescue a loser:** stroke in June 2026 (the spike was heat stroke, HX-05), and Okoro's sleeping-position video, launched into higher interest (GT-17).
8. **Replicated failure.**
   - "What a stroke looks like the day before it hits" failed on all 3 channels that ran it (2,078 / 1,890 / 1,186).
   - The Ares version had the highest fear density of any matched-pair video.
9. **Medical reality of the category's winners (24 checks).**
   - Several of the biggest winners rest on UNSUPPORTED claims: "10 minutes later" clove effects, "12 kg of waste", "fruit repairs cataracts overnight", "vegetable heals dead kidneys", "foot signs before any blood test".
   - Two claims are CONTRADICTED: "stop walking" and "never eat this fish" (salmon).
   - A new channel must separate the performance mechanics from the claims.
10. **Small channels can break out fast, usually on proven topics with new packaging.**
    - Okoro: 3.8K subscribers, day 58.
    - The Aliza persona channel.
    - Fit Lit Health: from 70–2,900 views to 11 uploads over 250K in five weeks. **Caveat:** its thumbnails are in Urdu, so it serves a South-Asian-language audience.

## 3. Strategic answers

- **Why did the biggest videos break out?** Four things together:
  - A lived-moment opening plus a withheld single answer.
  - A topic with multi-channel demand (falls, nocturia, sleep, medications, feet).
  - A readable single-idea thumbnail.
  - Channel- or network-level distribution we cannot observe.

  Trend alignment helped in a minority of cases.
- **Why did near-identical copies fail?** Titles, thumbnails and personas do not transfer between channels. The same title and thumbnail produced 941K and 160. Mill copies of a fresh hit (2–150 views) failed almost universally. Copies by stronger channels often won.
- **Why do some channels get millions from a few videos?** Distribution is extremely concentrated (the top 5 videos hold 51–98% of views), and follow-ups rarely hold the level. SHH is the exception: a 41-episode franchise with a 1-in-3 hit rate.

## 4. Final First 10 (built last; full 17-field specs are in `FIRST-10-FINAL.json` and sheet 26)

| # | Launch video | Key evidence | Medical |
|---|---|---|---|
| 1 | The walking habit physical therapists check first after 70 | Thomas 1.0M/596K/329K; Cochrane −23% falls; GT-28 plateau | SUPPORTED (reframed) |
| 2 | Seated exercises that can ease neuropathy symptoms | GT-24 5-year peak; TopHealthTips 1.3M; Okoro 101K | PARTIAL |
| 3 | Why you wake up to pee at night after 60 | Ares 404K; Rena Malik 1.2–1.3M; GT-10 | PARTIAL |
| 4 | Morning or night for BP pills? What the TIME trial found | GT-13 ~6.6x growth; TIME trial RCT | SUPPORTED |
| 5 | Amlodipine, losartan or lisinopril: 6 things to discuss with your pharmacist | 941K persona channel; Aliza 47K; GT-12 | PARTIAL, pharmacist review |
| 6 | Anesthesia and surgery after 70: questions to ask first | Ares 613–716K; Elias 556K; HX-07 | MEDIUM |
| 7 | How often should you really bathe after 65? | Ares 527K; Gentle 602K; GT-20 zero search | PARTIAL |
| 8 | Foot changes after years of high blood sugar, and the A1C test | Okoro 494K; GT-05; reframed per MV-01/02 | PARTIAL |
| 9 | Back-sleeping, sleep apnea and stroke risk | Ares 1.48M; GT-17 rising "to avoid stroke"; AHA | PARTIAL |
| 10 | What your creatinine number really means | GT-14 5-year high; external 1.1M; NKF/AKF | SUPPORTED |

**First 50 re-evaluation:** 26 KEEP, 18 MODIFY, 6 DROP. The drops are the ingredient-water/7-day templates, generic silent-heart-attack signs and generic stress. 17 new concepts come from rising Trends, external breakouts and whitespace: GLP-1 brand shift, creatine, BP-timing trial, mini-stroke in women, supplement interactions, and others.

## 5. Knowledge corpora, traceably applied

- **DS-000011** (13 knowledge units, sheet 34). Supported: one-big-idea/withheld packaging, contrarian-if-accurate, pain-point openings. Not predictive alone: title formulas. Not testable publicly: "first 10 s are packaging".
- **DS-000018** (19 creator claims vs platform facts, sheet 35). Personalization and watch history are SUPPORTED, and internal evidence is consistent with them (non-search winners). The templated-repetition policy is SUPPORTED, and the copy/persona-clone results are consistent with it. "Shorts and long-form must never share a channel" is CONTRADICTED. AEO script structure is not supported.
- **DS-000031** (11 frameworks, sheet 36). Each has an internal example, an internal counterexample, an external example, a limitation and an implication. The strongest are Outlier → Demand Signal, validated when the same topic outperforms on 2 or more unrelated channels, and Hit → Follow-up → Cluster, where follow-ups must land within about 3 weeks and must change substance, not just form.

## 6. File index (forensic-v2/)

| File | Content |
|---|---|
| `VERIFIED-FACTS.json` | Re-queried facts, 306 videos / 6 channels |
| `DATA-QUALITY-CORRECTIONS.json` | 19 corrections |
| `TRANSCRIPT-FORENSICS.json` | All 305 transcripts (149 flagged deep); opening segments, cues, timings, densities |
| `MATCHED-PAIRS-SCRIPT-FORENSICS.json` | 29 script-vs-script + thumbnail comparisons |
| `THUMBNAIL-MATRIX.json`, `thumbnail_obs_raw.jsonl`, `thumbnail_order.json` | 149 LIVE_WEB_VISUAL observations + feature performance |
| `trends/TRENDS-LIVE.jsonl`, `TRENDS-REGISTER.json` | 32 live Trends investigations + withdrawn estimates |
| `external/*.txt`, `EXTERNAL-BENCHMARKS.json`, `SMALL-CHANNEL-BREAKOUTS.json` | 13 clusters, 172 videos, channel and watch pages, 5 breakouts |
| `DUPLICATE-NETWORK.json`, `DUPLICATE-NETWORK-SUMMARY.json` | Duplicate / content-mill network |
| `HISTORICAL-CONTEXT.json`, `MEDICAL-VALIDATION.json` | 10 events, 24 fact-checks |
| `DS-000011-TRACE-MATRIX.json`, `DS-000018-CLAIM-MATRIX.json`, `DS-000031-FRAMEWORK-MATRIX.json` | Corpus traceability |
| `ARCHETYPE-PERFORMANCE.json`, `MAJOR-CONCLUSIONS.json` | Hook/script/topic/title tables, 18 conclusions |
| `FIRST-50-REEVALUATED.json`, `FIRST-10-FINAL.json` | Re-evaluated plan + final launch 10 |
| `EVIDENCE-REGISTER-V2.json` | 650 granular evidence records |
| `SENIOR-HEALTH-FORENSIC-WORKBOOK-V2.xlsx` | 38 sheets, 20 charts with commentary |
| `SENIOR-HEALTH-CASE-STUDIES-V2.md` | 11 case studies from actual evidence |
| `scripts/` | Reproducible builders (read-only against canonical data) |

To rebuild, run the following from `forensic-v2/scripts/`:
1. `build_verified_facts.py`
2. `transcript_forensics.py`
3. `thumbnail_matrix.py`
4. `matched_pairs_script.py`
5. `build_outputs.py`
