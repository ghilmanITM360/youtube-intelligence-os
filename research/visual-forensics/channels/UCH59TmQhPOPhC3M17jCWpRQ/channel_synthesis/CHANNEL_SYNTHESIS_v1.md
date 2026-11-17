# Barely Evolved — channel-level visual synthesis v1 (3 videos)
Channel UCH59TmQhPOPhC3M17jCWpRQ. Videos: uPQcyookL0Y (checkpoint P de9c3b8a), mNLNb-Z4T0M (checkpoint C 10a7865f), GNaBxt_zIRA (checkpoint C 100fbd01).
Out of scope: 4X3xd3MDZro (MISSING_NOT_REGISTERED; OUT_OF_SCOPE_4X3xd3MDZro.json).

Status: CHANNEL_DNA **DRAFT, n=3**. Every per-video report is VISUAL_ANALYSIS_PARTIAL. Audio listening is BLOCKED_CAPABILITY for all three. Three videos are not enough to call any pattern channel-defining, so the claims below are "recurring in this sample".
Reviewers were Claude sonnet subagents and the orchestrator was claude-opus-5-5 (same vendor). No human reviewed this work.

## 1. Measured structure
| video | frames | duration s | states | mean s/state | strip motion events |
|---|---|---|---|---|---|
| uPQcyookL0Y | 14647 | 488.7 | 89 (v6 ledger) | 5.49 | 178 |
| mNLNb-Z4T0M | 16689 | 556.8 | 136 (states_v1) | 4.09 | 192 |
| GNaBxt_zIRA | 16319 | 544.5 | 113 (states_v1) | 4.82 | 173 |
Caveat: video 1's state ledger was built with an earlier procedure (v5/v6 boundaries). Videos 2 and 3 used the shared be_* pipeline (D1+D2+D3 union, boundary review). The state density difference is therefore only partly comparable. All three are 30000/1001 CFR at 1920x1080 (MEASURED).

## 2. Recurring grammar (observed in more than one video)
| pattern | v1 uPQ | v2 mNLNb | v3 GNaBxt | label |
|---|---|---|---|---|
| Single-frame pose/prop swaps (no interpolation) | M5: W040 f7229->7230 mouth swap | S003 f18-25 mouth/pupil changes tile to tile | S003 f299->300 bear pop-in, no intermediate | OBSERVED |
| Pop-in scale with overshoot then settle | M3: W034 f6284-6286 | not found in strip descriptions (0 keyword hits) | PC-001 S015 f2076-2080, primary-verified | OBSERVED (v1, v3); v2 counterexample/absent in sample |
| Short element enter/exit (slides, drops) of a few frames | M6: 3-4 frames | 51 events, median span 5 frames; e.g. S010 f530-535 bed drops from top | 41 events, median span 5 frames | OBSERVED (span strip-bounded) |
| Camera push/pull and pans on illustrated scenes | M7: 27 scale / 16 pan | 19 scale / 9 pan; S028 f2260-2267 pan | 13 scale / 20 pan | OBSERVED; continuity of moves only MEASURED for v2 PC-002 |
| White-card / white-background text and word swaps | M1 clip reveal, M2 trailing-end slide | hard word swaps S029 f2461, S052 f4871->4872 | 1 swap hit (S001 f28) | OBSERVED; most frequent in v2 |
| Short fades/dissolves | M4: 5-frame fades | 7 events (S020 day->night f1370-1377) | 4 events | OBSERVED |
| Narration illustrated literally | ASR segs 0-75 partial | LITERAL 70 / ILLUSTRATIVE 22 / MIXED 12 / JOKE 1 | LITERAL 64+ / ILLUSTRATIVE 35+ / UNCERTAIN 58 | INFERRED from ASR (not listened) |

## 3. Video-specific choices and counterexamples
- **D3 large-pixel-change clusters mean different things per video (primary probe, MEASURED+OBSERVED).**
  - In v2 they are dominated by white-card word swaps and label entries.
  - In v3 they are mostly fast character/animal motion on painted scenic backgrounds: sloth f1673-1682, eagle swoop f6201-6216, thrown object f9421-9423.
  - So a single detector threshold does not map to one event type across the channel.
- **Camera continuity (v2 PC-002).**
  - A reviewer claimed a "stepped" camera move. Per-frame measurement shows a continuous move that decelerates to rest (f8181-8194).
  - Strip-based judgments of camera rhythm are unreliable without per-frame measurement.
- **Pop-overshoot is not universal.**
  - It is present in v1 and v3 but was not found in v2's 192 strip events.
  - Absence in strips is not proof of absence, because strips cover measured peaks only.
- **v3 has many UNCERTAIN narration relations (58).**
  - This reflects sparse frames falling outside ASR segment windows. It is a sampling limit, not a content property.
- **Gag timing (v2 PC-001, primary-verified).** The bread drop and crack land on the same frame (f4936->f4937).

## 4. Tested specs
- **v1 RT-01:** PASS on timing and geometry for M1, M3 and M5. Style was FAIL_BY_OMISSION.
- **v2 and v3:** reconstruction tests NOT_RUN. Their specs (production_specs/specifications_v1.json) are DRAFT.
- **Cross-video candidate spec set (PROPOSAL):**
  - single-frame swaps;
  - pop-in with a 1-2 frame overshoot;
  - 3-6 frame enter/exit slides and drops;
  - 5-8 frame fades;
  - continuous camera push/pan.
- Easing, fonts, software and sound are UNAVAILABLE.

## 5. What this synthesis does not claim
- No CTR, retention or "breakout" cause.
- No audio sync, SFX or music conclusions.
- No claim that n=3 defines the channel.
- No CT_SCAN_COMPLETE for any video.
