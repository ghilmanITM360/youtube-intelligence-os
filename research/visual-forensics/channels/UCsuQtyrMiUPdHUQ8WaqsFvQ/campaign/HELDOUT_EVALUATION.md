# Held-out evaluation against HELDOUT_PROTOCOL_v1 (scored 2026-11-05T18:33:03Z)
Frozen inputs unchanged at scoring (shasum -c HELDOUT_PROTOCOL_v1.sha256 OK): manual v1 2c40ba8d, protocol 0e29af14, aggregate_dev_final 41476ff5. v1 was not edited; revisions are only in CHANNEL_PRODUCTION_MANUAL_v2.md. These 4 videos are now seen: they can never again be called unseen validation.
Sources: LONG xBJ6suQSt98, 6YHva7Me2ls; SHORT C_jSOXP_XWY, 5gSIU30yiVs; sha256 re-verified against evidence/source_sha256.txt. Metrics: campaign/aggregate_heldout.{json,csv}, videos/<id>/tables/{segments_v1.csv,palette_measured.json}, evidence/ffprobe_full.json. Reuse: campaign/reuse_all.json. Reviewer image reads audited by pe_imgaudit: 17/17, 21/21, 2/2, 4/4, each once.

## Summary
| Group | PASS | FAIL | UNVERIFIABLE sub-parts |
|---|---|---|---|
| Measured H1-H8 (32 checks) | 23 | 9 | 0 |
| LONG only (16) | 14 | 2 | 0 |
| SHORT only (16) | 9 | 7 | 0 |
| Observed O1-O4 (16 checks) | 14 | 2 | O2 audio CTA, O3 sync timing, O4 platform captions |
| Reuse R1-R3 (3 checks) | 3 | 0 | 0 |
No threshold is declared a channel-level pass (protocol rule). Each FAIL is a recorded counterexample.

## Measured
| Check (LONG / SHORT range) | xBJ6suQSt98 | 6YHva7Me2ls | C_jSOXP_XWY | 5gSIU30yiVs |
|---|---|---|---|---|
| H1 50 fps CFR, native size, no letterbox | PASS 50/1 1920x1080 | PASS 50/1 1920x1080 | PASS 50/1 1080x1920 | PASS 50/1 1080x1920 |
| H2 background #FAFAFA-#FFFFFF | PASS #FDFDFD | PASS #FDFDFD | PASS #FCFCFC | PASS #FDFDFD |
| H3 median hold s (0.50-1.57 / 0.89-1.34) | PASS 1.04 | PASS 1.22 | **FAIL 1.39** | **FAIL 1.72** |
| H4 single-frame share (>=0.833 / >=0.923) | PASS 0.963 (n=81) | PASS 0.916 (n=95) | PASS 1.000 (n=7) | PASS 1.000 (n=14) |
| H5 cuts/min (18.4-32.4 / 18.9-25.3) | PASS 26.11 | PASS 29.02 | **FAIL 25.33** | **FAIL 28.79** |
| H6 events/min (34.1-59.7 / 35.7-47.9) | PASS 49.2 | PASS 44.5 | **FAIL 35.5** | **FAIL 33.6** |
| H7 mean ink (0.071-0.104 / 0.079-0.129) | **FAIL 0.1055** | **FAIL 0.1319** | PASS 0.0868 | PASS 0.0871 |
| H8 yellow holds (0.24-0.62 / 0.43-0.75) | PASS 0.561 | PASS 0.594 | PASS 0.750 (6/8, at the limit) | **FAIL 0.400** (6/15) |
| Passed | 7/8 | 7/8 | 5/8 | 4/8 |

Uncertainty:
- H1 letterbox is judged from native crops and sheets, with no separate all-frame bar measure. The sheet label hides the bottom band (see limits).
- H2 tests frame 0 only. xBJ6suQSt98 still contains full-black holds G0103-G0105 (SHEET_10), so a black beat exists inside a PASS.
- H5 and H6 depend on reviewer event classes (one reviewer per video).
- C_jSOXP_XWY is 11.84 s with 7 activities, so one event moves H5/H6 a lot: 25.33 vs 25.3 and 35.5 vs 35.7 are narrow misses, still FAIL under the no-widening rule.
- H7 explanation (MEASURED, does not change the score): holds with ink >0.5 are G0005, G0019, G0103, G0105 in xBJ6suQSt98 and G0011-G0021 (odd) in 6YHva7Me2ls; excluding them the means are 0.0712 and 0.0744. Mean ink is sensitive to a few dark or photo holds.

## Observed
| Check | xBJ6suQSt98 | 6YHva7Me2ls | C_jSOXP_XWY | 5gSIU30yiVs |
|---|---|---|---|---|
| O1 bearded caveman, yellow spotted tunic | PASS NATIVE_004042 G0137 | PASS SHEET_09 G0098 | PASS SHEET_02 G0011 | PASS NATIVE_000219 G0003 |
| O2 no CTA / end card seen | PASS fade to white G0162-G0163 | PASS fade to white G0190-G0191 | PASS ends on ghost joke G0015 | PASS ends on caveman G0029 |
| O3 literalised narrated word (ASR_UNCERTIFIED) | PASS "not normal rock" -> glowing rock G0008 | PASS "do trade" -> handshake G0003 | PASS "spiritual hole" -> belly hole + ghost G0012-G0015 | PASS "Social media" -> Instagram logo G0001 |
| O4 text built on white, no captions track | PASS word-by-word CLICKY CLICKY FIRE NOW G0074-G0080 | PASS BUT ONE DAY G0022-G0026 | **FAIL** title present from frame 0, no build seen | **FAIL** header present from frame 0, no word build seen |

UNVERIFIABLE sub-parts (the scores above cover only what could be seen):
- O2: a spoken CTA cannot be excluded by listening (BLOCKED). A keyword search of ASR found none, and ASR is not listening.
- O3: word-to-picture timing is ASR_UNCERTIFIED.
- O4: local files have no subtitle stream and no burned captions were seen; YouTube-side caption tracks were not checked.
- O4 reading: I scored "built" per manual A6 (word by word). Under a looser reading (any text on white) C_jSOXP_XWY and 5gSIU30yiVs would pass; the stricter result stands.
- C_jSOXP_XWY and 5gSIU30yiVs were spot-checked on one sheet each; the remaining rows rest on the reviewer.

## Reuse predictions
| ID | Prediction | Result | Note |
|---|---|---|---|
| R1 | C_jSOXP_XWY >=0.80 of 6YHva7Me2ls | PASS 0.957 (22/23 words) | 8 hold dHash candidates |
| R2 | 5gSIU30yiVs >=0.80 of 3AsDdMQr_nQ (LOW prior) | PASS 0.935 (43/46) | 9 hold dHash candidates; the low prior was wrong |
| R3 | xBJ6suQSt98 contains >=0.80 of IUur04eOd4A (LOW prior) | PASS 0.991 (110/111) | 22 hold dHash candidates; the low prior was wrong |
Overlap is ASR text; dHash matches are candidates, not pixel-verified.

## Independence
Short-to-long best ASR overlap, all 15 videos: IUur04eOd4A->xBJ6suQSt98 0.991; W8AVd7RhTME->RmTdnXHbI8s 0.959; C_jSOXP_XWY->6YHva7Me2ls 0.957; f1vIzsTFrp4->qB_EKkMyuUE 0.952; 5gSIU30yiVs->3AsDdMQr_nQ 0.935; uIG2U_1xynQ->KyBWJPaF1KI 0.849; Nv4xJ_NsFdo->KyBWJPaF1KI 0.083.
- 6 of 7 portrait videos are narration excerpts of a landscape video. Only Nv4xJ_NsFdo has no sibling.
- 5gSIU30yiVs shares narration with a DEV long, so it is not independent of the rule-development set. C_jSOXP_XWY and 6YHva7Me2ls are not independent of each other. xBJ6suQSt98 shares narration with DEV Short IUur04eOd4A.
- The most independent held-out long is 6YHva7Me2ls. No held-out Short is an independent production sample.
- Manual v1 A10 claim that portrait unique-production evidence rests mainly on IUur04eOd4A and Nv4xJ_NsFdo is now wrong for IUur04eOd4A.

## Rule results
Held up: 50 fps CFR format, near-white canvas at frame 0, single-frame replacement as default grammar (H4 4/4), caveman with yellow tunic, no end card, long-form rhythm ranges (H3-H6 8/8 on LONG).
Did not hold: Short rhythm ranges from n=5 (H3, H5, H6 failed on both Shorts); mean ink upper bound for LONG; word-by-word text as a universal rule; "flat fills" as a rule for all held states.
Not predicted by v1: photographs inside videos (5gSIU30yiVs 13 rows such as G0021, G0024 Linkind bulb, with gradient; also xBJ6suQSt98 G0004, 6YHva7Me2ls G0189; DEV 3AsDdMQr_nQ 26 rows); personified geometric subject (6YHva7Me2ls G0137); magenta tunic and colour drift on a character (5gSIU30yiVs G0027-G0029).

## Evidence limit found during this run
pe_sheets.py paints its 22 px label over the bottom of each tile, so every reviewer and spot-check sheet hid the bottom 8.1% of landscape and 4.6% of portrait frames. This applies to all 15 videos and is not corrected in any earlier review. Targeted reinspection: pe_band_audit.py measured all HOLD end frames; 166 holds with band content were opened in campaign/band_review/BAND_01-04.jpg. Those are drawing extremities and photo edges, with no CTA, caption or end-card element. One text item: RmTdnXHbI8s G0009 "pervy neighbour", in the hidden band (SHEET review row says all lines visible; not corrected, listed for a targeted row correction). ACTIVITY tiles were not audited, and portrait strips were cut at 44 of about 57 px. Sheets were not regenerated, to keep the reviewed evidence unchanged.

## Addendum, checkpoint J (scores above unchanged)
Corrects the note under "Evidence limit": the audit now covers ACTIVITY tiles and the cropped portrait slices, see HIDDEN_REGION_AUDIT.md. Hidden regions held no CTA, caption or end card in any of the 15 videos, so observed scores O1-O4 keep their values. RmTdnXHbI8s G0008/G0009 (DEV) text corrected; xBJ6suQSt98 G0092 (held-out) onset one frame earlier, no held-out criterion uses it.
Limits restated: v1 scores (23/32 measured, 14/16 observed, reuse 3/3) stand. The means excluding dark holds are post-hoc diagnostics and do not turn H7 into a pass. Narration siblings are not independent evidence.
Fresh test of manual v2: no contract item requires one (campaign brief section 2 asks for held-out examples "where feasible", done for v1; the protocol only says revisions become v2 with the original preserved). Exact gap: v2 is not validated on unseen data. Eligible unseen population: 0 landscape (all 8 selected) and 29 portrait, most of which may be narration excerpts, so a v2 test could not cover LONG at all. Not a completion blocker.
