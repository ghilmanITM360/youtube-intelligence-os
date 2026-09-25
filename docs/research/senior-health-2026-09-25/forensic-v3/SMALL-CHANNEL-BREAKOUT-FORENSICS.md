# Small-Channel Breakout Forensics — Senior Health Niche (V3)

**Date:** 2026-09-25
**Status:** Supersedes `forensic-v2/SMALL-CHANNEL-BREAKOUTS.json` (5 cases, 1 with a chronology error — see Correction below). Does not delete or overwrite that file; this is the V3 continuation per repository convention.
**Method:** All internal figures independently recomputed from `data/catalog/youtube_channel_registry.db` (fresh SQL, not reused from any prior file). All external figures from live, read-only YouTube browsing (no sign-in, no scraping tools, no paid API) conducted 2026-09-25. Every number below is traceable to a specific video ID, channel handle, or SQL query — see the two source agent reports (`INTERNAL-BREAKOUT-INVENTORY` findings, folded in below, and `EXTERNAL-BREAKOUT-RESEARCH-RAW.md`) for full detail.

**Correction applied (NC-02):** `forensic-v2/SMALL-CHANNEL-BREAKOUTS.json`'s "SB-05" case (Dr. Aliza Wright) claimed a video was a post-breakout follow-up copy. The registry DB shows the opposite: that video was posted 3 days *before* the real breakout, and the channel had already had an earlier, unrelated hit. The corrected chronology is given in full under Case 6 below.

**Correction applied (NC-05, independent audit, 2026-09-25):** This document's original summary text stated the total as "29 breakout events (23 internal + 6 external)". A direct recount of the per-case figures given later in this same document sums to **23 internal + 5 external = 28**, not 29/6 — the external total was an arithmetic error (Amos Boone's 1 event + SeniorHood's 4 events = 5, not 6). The per-event row data in workbook sheet `39_V3_BREAKOUT_INVENTORY` was already correct (28 rows); only this prose summary was wrong. All 23 internal events have been independently re-verified against `data/catalog/youtube_channel_registry.db` with exact video-ID and view-count matches. The canonical, identity-keyed 28-event table (with canonical channel IDs and YouTube video IDs) is at `cross-channel/BREAKOUT-EVENT-CANONICAL-TABLE.json`. The corrected count (28 = 23 internal + 5 external) is used everywhere below and in every dependent document; the original "29 (23+6)" figure is preserved here, in this note and in `STAGE2-CORRECTION-LEDGER.md` (NC-05), as the audit record of the error — not restated as fact anywhere else.

---

## The core question this document answers

> How can a channel with only ~20–40 visible uploads attract hundreds of thousands or millions of views, and what separates the successful cases from their unsuccessful counterparts?

**Short answer, evidenced below:** In every single case investigated — 6 internal channels, 2 new external successes, 4 external failures, plus cross-references to 10 further external channels screened and excluded — a breakout is a **discrete, non-durable spike on top of an otherwise low, flat baseline**, not a gradual ramp. No channel in this entire investigation converted a breakout into a permanently higher floor. The differentiator between the successes and failures studied here is **not** visible production quality, title template, or topic choice — several failure channels used the *exact same script template, word-for-word*, on the *exact same topics* (neuropathy, leg circulation) as the two successful channels, and got 1–2% of the views. What's evidenced, not just template use, is explained in the Cross-Cutting Findings section — and what remains genuinely unexplained (the actual differentiator) is stated plainly rather than invented.

---

## Cross-case summary table

| # | Channel | Type | Uploads (visible) | Subs | # Breakouts | First breakout at upload# | In brief's 20–40 window? | Durable lift? |
|---|---|---|---|---|---|---|---|---|
| 1 | Dr. Ares Senior (internal) | Success | 35 | — | 1 | #8 | No (early) | No |
| 2 | Senior Health Hub (internal) | Success (franchise) | 122 | — | 13 | #2 | Partial (#32, #39) | No |
| 3 | Doctor Thomas (internal) | Success | 22 | — | 3 | #9 | No (early) | No |
| 4 | Dr. Okoro (internal) | Success | 66 | — | 3 | #26 (day 58) | Yes (#26, #37, #38) | No |
| 5 | Dr. Elias Senior Health (internal) | **Negative control** | 29 | — | **0** | — | N/A | N/A (never breaks out) |
| 6 | Dr. Aliza Wright (internal, corrected) | Success | 32 | — | 3 | #6 | No (early) | No |
| 7 | Amos Boone (external) | Success | 43 | 2.87K | 1 | **#29** | **Yes** | No |
| 8 | SeniorHood (external) | Success (repeatable) | 76 | 28.4K | 4 | #12, #16, #26, ~#73 | Partial (#12, #16, #26) | No |
| 9 | Senior Mobility (external) | Failure | 13 | 198 | 0 | — | No (too few uploads) | — |
| 10 | Health 365 (external) | Failure | 54 | 311 | 0 | — | Spans it, no breakout | — |
| 11 | Senior Strength Secrets (external) | Failure | 41 | 59 | 0 | — | Spans it, no breakout | — |
| 12 | Aging Senior Health (external) | Failure | 110 | 76 | 0 | — | Spans it, no breakout | — |

**Total qualifying breakout events across all cases: 28** (23 internal + 5 external instances — corrected from an earlier "29 (23+6)" arithmetic error, NC-05), plus 1 explicit zero-breakout internal channel and 4 explicit zero-breakout external channels as negative controls — a materially larger and more balanced evidence base than V2's original 5 cases (2 internal, 3 external with unknown script openings).

---

## Internal cases (registry DB, full detail)

### Case 1: Dr. Ares Senior — isolated spike, no repeat

35 observed uploads (2026-08-06 → 2026-09-19), whole-channel median 45,512 views (this channel already runs "hot," so its breakout multiple is smaller than the others).

- **Breakout:** Upload #8 (2026-08-19), "Cardiologist Warns: This Sleeping Position Increases STROKE Risk Overnight" — 1,475,129 views (32.4x median).
- **Before:** uploads #3–7 ordinary mixed performance (4,384–140,448), no ramp signal.
- **After:** one near-miss follow-on (#11, 11.1x) then reversion; three later near-misses (12.9x–14.2x) on the same fear/cardio-warning formula show a repeatable *near*-hit pattern that rarely crosses into true breakout territory.
- **Matched failure:** Upload #14 (6 days later), "What a Stroke Looks Like the Day Before It Hits" — 1,890 views (0.04x) — same topic, same fear framing, near-zero result.

### Case 2: Senior Health Hub — the clove franchise, now fully inventoried

122 observed uploads (2025-09-15 → 2026-09-20), whole-channel median 9,540 views.

**13 breakout-magnitude videos found** (≥15x median) across a 13-month span — not the 4 V2 had sampled:

| Upload# | Date | Views | Multiple |
|---|---|---|---|
| #2 | 2025-09-17 | 1,090,015 | 114.3x |
| #9 | 2025-10-05 | 432,821 | 45.4x |
| #32 | 2025-12-08 | 143,862 | 15.1x |
| #39 | 2025-12-31 | 168,985 | 17.7x |
| #49 | 2026-01-31 | 1,055,564 | 110.7x |
| #51 | 2026-02-06 | 353,637 | 37.1x |
| #53 | 2026-02-12 | 554,619 | 58.1x |
| #65 | 2026-03-22 | 245,337 | 25.7x |
| #66 | 2026-03-25 | 290,424 | 30.4x |
| #68 | 2026-04-01 | 501,622 | 52.6x |
| #75 | 2026-04-22 | 325,737 | 34.1x |
| #77 | 2026-04-28 | **3,088,021** | 323.7x (channel peak) |
| #112 | 2026-08-14 | 173,273 | 18.2x |

Every single hit follows the same before/after pattern: 3–5 ordinary sub-baseline videos before, immediate reversion after (channel-median lift confirmed at **zero** across the full inventory, not just V2's 4-video sample: pre/post medians ~9,539 vs ~9,418).

**Matched failure:** Upload #58, "ONE Clove Under Your Tongue... Blood Sugar & Heart" — 5,894 views (0.6x) — essentially the same mechanic as the later #112 breakout ("I Put a Clove Under My Tongue," 173,273 views), released 5.5 months earlier, 29x fewer views for near-identical content.

### Case 3: Doctor Thomas — early two-hit cluster, source of a duplication network

22 observed uploads (2026-06-04 → 2026-07-27), whole-channel median 8,234.

- **Breakouts:** #9 (596,346, 72.4x), #14 (1,004,391, 122.0x, channel peak), #16 (328,707, 39.9x) — all before observed upload #20, i.e. an *early* breakout comparison case.
- **Duplication-network finding:** #14 and #16's exact titles were reused, in the opposite pairing order, by Dr. Aliza Wright 2–7 days later (see Case 6) — direct evidence Doctor Thomas is the likely first-mover source, not a coincidence of shared template.
- **Matched failure:** #13, "Why Your Ankles Are Making You Fall After 70" — 3,738 views (0.5x) — same "prevent falls + X-minute fix" hook as the #9 breakout, posted the day before #14 ignited, flopped anyway.

### Case 4: Dr. Okoro — the V2-confirmed case, now shown to be a 3-hit cluster

66 observed uploads (2026-03-20 → 2026-07-20), whole-channel median 199 (near-zero baseline outside hits).

- **Breakout #1** (previously the only one V2 documented): #26 (2026-05-16, day 58 since channel join 2026-03-19), "Cardiologist Warns: 9 Foot Signs of Hidden Diabetes After 60" — 494,473 views (2,484.8x). **The brief's own "30th-40th upload" framing for this case is unsupported by any file and is discarded — the real, independently-confirmed number is upload #26.**
- **Breakout #2**: #37 (2026-06-03), neuropathy-exercises video — 100,852 views (506.8x).
- **Breakout #3**: #38 (2026-06-05, 2 days later), kidney/creatinine video — 11,319 views (56.9x).
- After #38, all 28 remaining uploads (#39–66) regress to double/triple digits — no further breakout.
- **Matched failure (cleanest pair in the entire cohort):** #55 (7 weeks after #26), "Cardiologist Warns: 9 Skin Signs of Hidden Diabetes After 60" — 205 views (1.0x) — a near-verbatim title-formula clone of the #26 breakout (foot→skin swap, same disease framing), same channel, same creator, 2,400x worse result. **Correction (NC-07, 2026-09-25):** both videos' real transcripts were directly diffed for this pass — they are 0.4% textually similar (different opening hooks, different body content, sharing only the medical-disclaimer boilerplate and the "N signs" list structure). This is *title-formula* cloning, not script cloning — the earlier framing implied a closer copy than the evidence supports, and the corrected finding is if anything stronger: near-zero script overlap still produced a 2,400x gap on the same title.

### Case 5: Dr. Elias Senior Health — the negative control

29 observed uploads (2026-08-06 → 2026-09-09), whole-channel median 87,120. **Zero videos reach even 15x median** (channel high is 6.5x). This channel runs a uniformly elevated, low-variance baseline — several of its titles are verbatim duplicates of other cohort channels' breakout titles (e.g. "How Often Should Seniors Take a Bath," "NEVER Agree to This: 5 Deadly Surgeries" also appear on Dr. Ares Senior) — yet never produces a true outlier. This is valuable precisely because it shows a channel can look healthy on raw averages while having no discrete breakout event to analyze at all.

### Case 6: Dr. Aliza Wright — corrected chronology (replaces V2's SB-05)

32 observed uploads (2026-06-05 → 2026-07-25), whole-channel median 217.

**What V2 got wrong:** claimed video `rpArUoI6Qbg` ("Walk Straight") was a post-breakout copy made *after* the real breakout.

**What the registry DB actually shows:**

| Upload# | Date | Title | Views | Multiple | Role |
|---|---|---|---|---|---|
| #6 | 2026-06-12 | "If You Take Losartan, Amlodipine, or Metoprolol After 60..." | 47,032 | 216.7x | **True Hit #1** (unrelated medication topic) |
| #14 | 2026-06-23 | "Why You Can't Walk Straight Anymore After 70..." (`rpArUoI6Qbg`) | 20,701 | 95.4x | **Hit #2** — a topic-experiment, 3 days *before* Hit #3, not a copy of it |
| #15 | 2026-06-26 | "One SIMPLE Change to How You Walk...After 70" (`r_ja_nYHCHE`) | 219,009 | 1,009.3x | **Hit #3** — the channel's biggest hit, 3 days *after* #14 |

The corrected reading: this channel tested a walking-related angle at #14, got a strong-but-not-explosive signal (95x), then re-packaged the same theme with a sharper hook 3 days later and it exploded to 1,009x — a genuine two-step natural experiment, not a copy-after-success story. Both titles are near-verbatim matches of Doctor Thomas's #14/#16 (Case 3), posted in the opposite order — a real duplication-network link, distinct from the separately-documented 941K-vs-160 persona-clone case elsewhere in the corpus. This channel had **3** breakouts, not 1, and the walking breakout was its **second and third** hits, not its first.

**Matched failure:** #18 (18 days after Hit #1), reusing the exact medication-safety template — 173 views (0.8x). This template was run 6 times on the channel; only #6 broke out.

---

## External cases (live YouTube research, 2026-09-25)

### Case 7: Amos Boone (`@Amossboone`) — SUCCESS at exactly the target window

2.87K subscribers, 43 visible videos. Note: channel "joined" 2019 per its info panel but visible uploads only span ~6 months — this is explicitly an **observed/visible** upload sequence, not necessarily the channel's true history (older content may be deleted/private, or the channel was dormant).

- **Breakout: upload #29 of 43** — "The ONLY 7 Exercises YOU Need to Relieve Neuropathy in Feet & Legs" (`Jljlizl2G0E`) — 207,000 views, vs. a surrounding baseline of double/triple digits.
- **Immediately after (#30):** the exact same "ONLY N Exercises...to Improve Leg Circulation" template — 592 views. No lift transferred.
- **Packaging:** live closed-captions (readable without sign-in during playback, not the blocked transcript panel) show the video opens with a **pathophysiology/medical-explainer hook** ("...is not a malfunction in the usual sense. It is a nerve that has..."), not a curiosity-gap hook.
- **No video description was present** — unusual for this niche, suggesting a lower-effort operation than Case 8.

### Case 8: SeniorHood (`@SeniorHood`) — SUCCESS, repeatable, both early and late breakouts

28.4K subscribers, 76 visible videos, runs a paid membership tier and an external funnel site — a more mature monetization operation.

- **Breakout #1:** #12, "Surgeon REVEALS: 5 Wall Exercises...Outperform Walking After 60" — 199,000 views.
- **Breakout #2 (channel peak):** #16, "Surgeon REVEALS: Do THIS 1 Exercise for Poor Leg Circulation After 60" — **1,046,812 views** (exact count).
- **Breakout #3:** #26, "Surgeon WARNS: Neuropathy Is Getting Worse After 60!" — 471,000 views.
- **Breakout #4 (late, for early/late comparison):** ~#73, "Jack LaLanne (89): The Only 4 Chair Exercises..." — 178,000 views, immediately preceded a week earlier by a near-identical "Jack LaLanne" video at 90,000 — the channel tested the same persona-hook twice back-to-back and both cleared six figures; a third repetition dropped to 6.3K (diminishing returns confirmed directly).
- **Packaging:** live captions show a **curiosity-gap ("What if I told you...")** opening on both large hits — a different hook style from Amos Boone's medical-explainer approach, despite similar "authority" title framing.
- **This channel's title template — "Surgeon REVEALS/WARNS: Do THIS 1 Exercise for [ailment] After 60" — is used nearly verbatim by at least 10+ other small channels found in this same research pass, nearly all of which get double/triple-digit views on the identical title wording.** (Corrected, NC-07: this is verified title-level identity only — full scripts were never compared for these external channels, since only titles and brief caption snippets were observed. Where full-script comparison *is* possible, on internal cohort data, it shows title-template cloning does not imply script cloning — see Case 4's corrected foot/skin diff below.) SeniorHood is the rare case where the template actually, repeatedly worked.

### Failure comparisons (same template/topic, zero breakout)

All four found via the same searches that surfaced SeniorHood — a real "content-mill ecosystem" of near-identical small channels:

- **Senior Mobility** (198 subs, 13 videos, abandoned after 1 month) — best video 5K views. Never reached the 20–40-upload range at all — evidence that simply not persisting long enough may itself be disqualifying, separate from packaging quality.
- **Health 365** (311 subs, 54 videos) — best video 241 views. Has videos on the **exact same topics that produced both successful channels' breakouts** (neuropathy, leg circulation) using the same "Surgeon Reveals" phrasing — 42–56 views. The single cleanest same-topic/same-format/zero-lift control case found in this research.
- **Senior Strength Secrets** (59 subs, 41 videos) — best video 2.2K, itself barely above its own catalog's 20–130 view norm, not a genuine breakout. The identical title template got 10–168 views on five *other* sibling channels found in search results.
- **Aging Senior Health** (76 subs, 110 videos, nutrition-focused) — best video 1.9K. 110 uploads, well past the 20–40 window, never broke out — persistence and volume alone were not sufficient here.

**Channels screened and excluded as too large to qualify as "small":** 10 further channels (Dr. Yonatan Whitten 150K subs/387 videos, Her Health 60+ 120K/139, SENIOR FOOD BLOG 148K/79, Senior Vital Health 104K/195, Healthy Aging-Senior Health Tips 15.4K subs but only 5 already-viral videos [likely a rebrand/spinoff], Senior BeWell 22.6K/243, Seniors Circle 141K/114, Gentle Health 29.4K/273, Dr Todd Sullivan 52.5K/476) — several of these show the same breakout-shaped outliers, reinforcing that the pattern generalizes beyond the 6 primary cases, but they don't fit the "breakout from a small/new channel" definition. One lead (`Imperial Fitness Hub`, a 128K-view result that may sit on a small channel) was not opened due to research time budget and is flagged for a future pass, not claimed as verified.

---

## Cross-cutting findings

**1. Every breakout is a spike, never a step-change.** Across all 28 breakout instances (23 internal + 5 external) in this document, not one channel's post-breakout baseline durably exceeded its pre-breakout baseline. The very next upload, in nearly every case, reverts to the channel's ordinary range. Senior Health Hub is the strongest counter-test (13 independent breakouts over 13 months on one channel) and even there, the whole-channel median is statistically unchanged before vs. after each hit.

**2. Template alone does not explain outcomes — this is directly falsifiable and was falsified.** The "Surgeon REVEALS/WARNS: Do THIS 1 Exercise" template is used, in some cases with identical wording, by SeniorHood (4 breakouts, up to 1.05M views) and by at least 10+ sibling channels (documented: Health 365, Senior Strength Secrets, plus 5 more named in search results) that get double/triple-digit views on the same words applied to the same ailments. Topic choice is similarly falsified: Health 365 has videos on neuropathy and leg circulation — the exact topics behind both Amos Boone's and two of SeniorHood's breakouts — and gets 42–56 views on them.

**3. A minimum-uploads threshold appears necessary but is not sufficient.** Senior Mobility never reached 20 uploads and never broke out — consistent with needing a longer runway. But Aging Senior Health posted 110 uploads and Health 365 posted 54, both spanning well past the 20–40-upload window, and neither ever broke out — so persistence alone does not cause a breakout either.

**4. What this evidence base cannot determine — stated plainly, not guessed at.** None of the internal or external data sources available here include first-party analytics (impressions, click-through rate, average view duration, traffic source). The actual mechanism connecting a specific title/thumbnail/hook combination to the YouTube recommendation system's decision to surface a video broadly is **not observable** from public view counts alone. Every "packaging" observation in this document (hook style, title formula, authority framing) is a correlational description of the winning videos, not a demonstrated cause — and the failure cases prove that surface-level template/topic matching is not the determining factor, without identifying what is. This gap should be stated in any downstream strategy document, not papered over.

**5. Cross-channel duplication is common and its success is not guaranteed by being either first or by copying a proven winner.** Doctor Thomas's titles were duplicated (in reordered form) by Dr. Aliza Wright 2–7 days later, with mixed results relative to the original. This is consistent with the separately-documented duplication-network finding elsewhere in the corpus (22 second-movers won vs. 15 lost on cross-channel copies) — copying is not a low-risk strategy, it inherits the same unpredictability as original content.

---

## Limitations and what remains unknown

- Internal upload-index numbers are **observed** upload counts from the registry DB, not necessarily true lifetime upload numbers (deleted/private uploads are invisible).
- External upload-index numbers are similarly **visible-catalog** positions as rendered by YouTube's own "oldest first" sort at research time; Amos Boone's "joined 2019" vs. "6 months of visible content" mismatch is a concrete example of this caveat mattering.
- Script-opening/hook data for external videos came from live auto-playing closed captions (a handful of lines each), not full transcripts — the dedicated transcript panel remained inaccessible without sign-in, consistent with V2's prior finding. This was not worked around.
- No first-party analytics (CTR, retention, traffic source, exact upload timestamp-to-view-accumulation curve) exist for any case — every performance number is a single point-in-time public view count, so nothing here demonstrates *causation*, only correlation and timing.
- The external search (11 queries, 16 channels opened in full, ~20 more screened from search snippets) is a real, disclosed, audit-able sample — but it is a sample of a much larger content-mill ecosystem in this niche, not an exhaustive census. `Imperial Fitness Hub` is an explicitly flagged, unchecked lead.
