# 01 Strategy gaps and conflicts

## G1. Folder identity
Requested `research/what-if-channel-strategy-2026-11-18` does not exist; the folder is `research/what-if-channel-strategy/` on branch `research/what-if-channel-strategy-2026-11-18` (and its origin copy). Absent from `origin/main` (0 files). Any future "is it on GitHub?" check must name the branch.

## G2. The strategy under-uses the existing xkcd visual campaign (largest gap)
The brief states that earlier research "explicitly excluded video visuals". That is true of the 83-script study only. A separate, large xkcd visual-forensics campaign already exists **on `origin/main`** (1,599 files):

- Path: `research/visual-forensics/channels/UC6IxnFzHofFJ5X2PycSMsww/` (campaign dated 2026-11-04 to 2026-11-06, checkpoints A to R).
- 44 videos with every frame measured (24 long + 20 Shorts) and a `quality_gate.json` per video; 20 more long videos with measurement tables only (population-6). All marked `VISUAL_ANALYSIS_PARTIAL`.
- Production manuals v0.1 to v0.7; held-out protocols/evaluations v1 to v6 (frozen before ingest); reconstruction tests RT1 to RT4 (RT4 = portrait Short); 331-edge knowledge-link table.
- Honest open items recorded there: **audio listening BLOCKED for all 91 videos**, no FULL_AV_SIGNOFF, no CT_SCAN_COMPLETE, same-model-family reviewers, 27 videos without source media (at that time).

`05_30_DAY_EXPERIMENTAL_CALENDAR.md` and `03` cite only the 14-video Brain (`CHANNEL_DNA.md`) for xkcd pacing. They do not cite the campaign's own measured ranges.

## G3. Conflicting pacing numbers (different definitions, not yet reconciled)

| Number | Definition | Source | n |
|---|---|---|---|
| 7.77 s | median **shot** duration | Brain v1.0.0 (CHANNEL_DNA) | 14 videos |
| 2.15 to 2.33 s (long), 1.44 to 2.84 s (Shorts) | median **hold** between visual events | campaign manual v0.7 | 4 long, 9 Shorts at aggregation; later held-outs 20/20 and 116/120 checks pass |
| 4.9 to 6.1 /min (long) | **hard cuts** per minute | campaign manual v0.7 | same |
| 4.1 s / 59 s | gap between ffmpeg scene-change **candidates** | strategy 04 (competitors) | 3 |

A hold of about 2 s and a hard-cut interval of about 10 to 12 s describe the same videos differently. Using 7.77 s as "xkcd's pacing" in production specs is not supported. This audit marks it SUPERSEDED as the sole pacing number, not false.

## G4. Wrong or stale statements
- 03 §1: "Long durations are 2:43–3:33" in 2026. Census: 2:42 to 4:38 (11 videos). CONTRADICTED.
- 01 §1: "92 public videos as of 2026-11-18". Census has 91 at 2026-11-04; the 92nd is Aony69nO5kI. A live RSS fetch on 2026-11-23 lists no upload newer than 2026-11-17 (RSS returns only the latest 15, so this is not a full recount).
- README "Scripts are not written yet" (line 8) conflicts with its own Status lines 6 and 7 (Day 1 approved, Day 3 drafted). Cosmetic.

## G5. Evidence not retained
- 02: 658 of 713 search rows not exported.
- 03 §4: 40 thumbnails judged in-browser, no images stored.
- 06: several sources "search-confirmed, not fetched". No domain expert.

## G6. Cross-source identity risk (from the campaign)
The campaign recorded that the 10 videos shared with the older Brain have **different media hashes** (different encodes). They are not one evidence set (AGENTS.md rule 9). Any statistic that mixes Brain rows with campaign rows double-counts videos.

## G7. Directive premises that differ from the repo
| Directive says | Repo shows |
|---|---|
| Two transcripts pending (9VG0yqq_PHM, X97DDWvxaqQ) | 8 of 91 have no catalog transcript (+1 newer upload). 9VG0yqq_PHM has a provisional local Whisper transcript; X97DDWvxaqQ has video but no ASR run. |
| Visual/motion/audio analysis not yet done | Visual measurement exists for 64 videos; audio listening is the open blocker. |
| 83 may not be the complete channel | Correct: 91 in census, 92 with the newest upload. 83 = videos with catalog transcripts. |

## What is genuinely missing (for the owner's goal)
1. A **reconciliation** of the three visual layers (Brain 14, campaign 64, Nov 17 deep pass of 8fADp43wJwU) into one evidence-tiered table with definitions aligned.
2. **Audio and narration alignment** (blocked in the campaign for lack of a listening capability; a deep audio pass exists for one video only).
3. **Science-visual layer** (Phase 7 of the brief): no existing study of how xkcd illustrates physics quantities. Not found anywhere in the repo.
4. **Asset-recipe layer** (Phase 8): the campaign has reconstruction blueprints, no original asset contracts.
5. Cross-video script synthesis (D4) and master script playbook (D5) of the 83-script study: confirmed not started.
6. 27 (now 4) videos without source media, 24 media-available videos with no visual analysis, 2 media-available videos with no transcript.

## Correction after Phase 6 (2026-11-23, later pass)
G3 above overstated the conflict. With one definition applied to both layers (`06_LAYER_RECONCILIATION.md`), the Brain's median **shot** of 7.77 s agrees with the campaign's long median shot of 8.44 s (n=24). The claim C17 is therefore **VERIFIED as a shot median but INCOMPLETE as a pacing rule**, not SUPERSEDED. What the strategy still lacks is the visual-event cadence (about 2.15 s gap, about 22 events per minute, about 10 events per 100 spoken words) and the hard-cut rate (about 5.3 per minute). Strategy files 03 and 05 cite only the 7.77 s figure.

Also from Phase 5 (`05_CROSS_VIDEO_SYNTHESIS.md` §3): the strategy's length-cutting rationale (match xkcd's median 680 words, 3:16) is not supported by performance data; within-year, longer long videos correlate with more views (rho +0.56 to +0.62, n 14 to 17, correlational only).


## Addendum 2026-11-23 (continuation): G3 corrected again, G-list status
- The earlier correction ("7.77 s and 8.44 s are the same quantity") is **withdrawn**: they are different units, samples and detectors (`06_PACING_CORRECTION.md`). C17 is PARTIAL: valid as a Brain shot median only.
- G1 (strategy scope) unchanged. G2 (visual campaign exists) unchanged. Transcript gap: 9 videos without catalog text = 5 with provisional ASR + 4 without media; X97DDWvxaqQ and alBQCm0QpJg now have provisional ASR. Live recount confirmed 92 videos.
- The strategy's "37 of 43 attributed openings" is superseded by 41 of 43 (manual audit plus V015 read by hand; `05_PHASE5_VERIFICATION.md`).
