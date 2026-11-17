# Barely Evolved — channel-level visual synthesis v1.2 (3 videos)

v1.2 (non-audio completion, 2026-11-05) adds four things:
- the dense interval review;
- the asset crosswalk;
- the camera-ease retest;
- the style and full-scene reconstruction tests and production manual v1.2.

v1.1 is preserved unchanged, and so is v1. Sections 1–3 below are carried over from v1.1 without change. Section 4 is replaced, and section 6 is new.

v1.1 (final audit 2026-11-04): corrections FC-01..FC-03 from final_audit/FINAL_CORRECTIONS.csv; v1 preserved unchanged as CHANNEL_SYNTHESIS_v1.md. Evidence: final_audit/FINAL_VISUAL_CHECK.csv.
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
| Single-frame pose/prop swaps (no interpolation) | M5: W040 f7229->7230 mouth swap | PC-001 S053 f4936->4937 bread lands + crack appears same frame (primary-verified; S003 citation withdrawn, VC-13) | S003 f299->300 bear pop-in, no intermediate | OBSERVED |
| Pop-in scale with overshoot then settle | M3: W034 f6284-6286 | NOT_OBSERVED in 4 MEASURED squash-expand swaps (S062/S069/S094/S122, VC-12); absence across v2 NOT_ESTABLISHED | PC-001 S015 f2076-2080, now MEASURED +5.5% vertical (VC-11) | OBSERVED (v1, v3); v2 unresolved |
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
- **Pop-overshoot recurrence is unresolved in this sample.**
  - It is present in v1 (W034) and v3 (S015). In v2 it was not found in 192 strip events, and the same squash-expand mechanism measured in 4 events had no overshoot.
  - Absence in strips is not proof of absence, because strips cover measured peaks only.
- **v3 has many UNCERTAIN narration relations (58).**
  - This reflects sparse frames falling outside ASR segment windows. It is a sampling limit, not a content property.
- **Gag timing (v2 PC-001, primary-verified).** The bread drop and crack land on the same frame (f4936->f4937).

## 4. Tested specs (`final_audit/RECONSTRUCTION_TESTS_v2.csv`)

- **Timing modules:**
  - v1 RT-01: PASS.
  - v2 RT-V2-01: squash PASS; camera FAIL, kept as pre-registered.
  - v2 RT-V2-02: camera pan PASS.
  - v3 RT-V3-01: PASS.
- **Punch-in:** v1 RT-V1-P01 PASS (incremental scale 2.139 about (627, 818); criterion v1 failed on the source and is kept).
- **Style and full scene:**
  - v1 W021: RT-V1-S01 PASS.
  - v2 S067: S01–S03 FAIL (kept); S04 PASS.
  - v3 S057: S01 and S02 FAIL (kept; spec errors); S03 PASS.
- **Not tested:** easing source, fonts, software and sound are UNAVAILABLE.

## 6. Production manual v1.2 (scoped to these three videos; all assets must be new and original)

| Module | Parameters | Source | Tested |
|---|---|---|---|
| White-card clip reveal | 3–6 frames, left to right, hard edge | v1 M1 | RT-01 PASS |
| Pop-in with overshoot | peak within 2 frames, settles smaller (v3 about +5%) | v1 M3, v3 S015 | RT-01, RT-V3-01 PASS |
| Single-frame pose/prop swap or pop-in | 1 frame, no in-between | v1 M5, v3 S003, v2 PC-001 | RT-01, RT-V3-01 PASS |
| Squash-expand picture swap | collapse 2, band 2, expand 2 frames; band about 22% height; no overshoot | v2 (4 events) | RT-V2-01 PASS |
| Camera pan | horizontal, about 16 frames, ease-in-out, scale constant (S080: tx 0→137.8 px) | v2 PC-002/S080 | RT-V2-02 PASS (RT-V2-01 FAIL kept) |
| Single-frame punch-in reframe | 1-frame jump, same artwork, about 2.1× about a lower-left fixed point, then held | v1 UBC-002/003, f2835/f5429 | RT-V1-P01 PASS |
| Slow zoom (v3) | pure zoom about a top-centre fixed point (about 960, 50), no pan, eased tails | v3 S057 | RT-V3-S03 PASS |
| Screen-anchored character layer | presenter/teacher stays fixed on screen while the background zooms | v3 S057 (ESTIMATED from tiles) | RT-V3-S03 PASS |
| Style scene modules | palette fractions, line weight and layout per the PASSing specs | v1 W021, v2 S067, v3 S057 | RT-V1-S01, RT-V2-S04, RT-V3-S03 PASS |

**Asset reuse.** Recurring characters, sets and props across the three videos are listed in `nonaudio_completion/crosswalk/ASSET_CROSSWALK_v1.csv`:
- 86 canonical assets;
- 473 SAME, 209 VARIANT and 51 UNCERTAIN appearances.

For example, the classroom teacher BE-CHR-003 appears in all three videos. New productions should use their own original recurring cast and should not copy these assets.

## 5. What this synthesis does not claim
- No CTR, retention or "breakout" cause.
- No audio sync, SFX or music conclusions.
- No claim that n=3 defines the channel.
- No CT_SCAN_COMPLETE for any video.
