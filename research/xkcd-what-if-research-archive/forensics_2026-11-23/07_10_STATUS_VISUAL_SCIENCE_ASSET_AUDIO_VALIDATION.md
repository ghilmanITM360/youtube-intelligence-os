# 07 to 10 Status: science visuals, asset reconstruction, audio, validation

Honest status per phase. "Done" means a MEASURED output exists in this folder. "Existing" means it lives in the repo campaign and was not redone. "Not done" or "Unavailable" is stated with the reason. Everything is self-review.

| Phase | Directive item | Status | Evidence / reason |
|---|---|---|---|
| 6 | Real visual forensics across the channel | **Partly done.** Reviewed timing for 44 videos (campaign ledgers, `06_*`). **New (checkpoint 6):** machine-measured shot and event ledgers for the 20 long videos and 24 Shorts that had none (`ledgers_measured/`: 719 shots, 2,160 events), validated on 38 held-out videos (events P 0.95, R 0.96; shot boundaries P 0.70, R 0.86). **Sample viewed (60 of 719 shots, `review_sample/`): 50 true cuts, 8 progressive, 2 borderline; one coder.** The rest not viewed or interpreted, so tier MEASURED not VERIFIED_VISUAL; DEEP_VISUAL remains 0; 3 videos have no media |
| 6 | Visual event vocabulary (measured) | **Done from ledgers.** Long-form events (n=2,022): scene swap 19.7%, label pop-on 13.2%, object pop-on 12.6%, type write-on 4.4%, line write-on 3.3%, pose swap 2.6%, damage state swap 1.3%. Shorts (n=686): scene swap 21.1%, object 12.2%, label 11.8%, line write-on 4.5%, damage swap 2.3%, annotation circle 2.3%. No camera motion recorded in 615 of 718 shots (86%) | Prior self-review labels, not re-verified here |
| 7 | Science and physics visual layer | **Done as a targeted pass over all 44 media-available long videos and 38 of 44 media-available Shorts (checkpoints 3 to 5).** 125 still frames at quantity moments (47 + 40 long, 38 Shorts; scheme frozen, holdout replicated). Pooled: spoken quantity on screen in 53 of 105 quantity frames (50%); long 53%, Shorts 46%; numeral or unit label is the commonest device (46 of 125). Shorts reuse the long videos' art (about 15 of 38 by eye), so frames are not independent. One coder, stills only. 2 Shorts and 1 long video have no media. TARGETED_VISUAL, not DEEP_VISUAL |
| 8 | Asset reconstruction and recipes | **Existing, not redone.** 44 per-video `reconstruction_blueprint.md`, reconstruction tests RT1 to RT4 (RT4 portrait Short), manuals v0.1 to v0.7. No new original assets, characters or animation were produced, per the directive | Blueprints describe *recreating the observed style*; original asset contracts for a new channel remain a gap |
| 9 | Audio and narration | **Machine signals done, listening unavailable.** `09_AUDIO_LEVELS_88.csv`: integrated loudness, true peak, loudness range and digital silence for all 88 library files. ASR-based narration timing in `06_*` (24 long, 20 Shorts). **Listening and voice-visual sync sign-off: UNAVAILABLE**, no audio perception tool in this session or in the campaign | Unblock: a human listener or an owner-approved audio-capable tool (campaign's own `unblock` list). Stems and levels exist for 8fADp43wJwU only (Brain encode) |
| 10 | Validation and holdouts | **Partly done.** Campaign held-out protocols v1 to v6 (20/20 and 116/120 checks) exist and were not redone. **New in this audit:** one holdout for the Phase 7 scheme (frozen before viewing, 23 unseen frames, headline replicated). The Phase 5 and 6 playbook numbers have no holdout (corpus of about 45 families cannot supply one without cutting n). All reviewers are same-model-family; this audit is self-review. **Independent QA: UNAVAILABLE** | Unblock: a human or different-family second coder on the Phase 7 CSVs |

## Audio levels (MEASURED, machine only)

- Median integrated loudness **-16.5 LUFS** (long) and -16.45 (Short); **84 of 88 files within -17.5 to -15.5 LUFS**.
- Median loudness range 3.0 LU (long), 2.4 LU (Short): a compressed, steady mix.
- Digital silence below -50 dB for 0.35 s or more: median 1 event in long, 0 in Shorts; silence ratio at most 2% of runtime. No dead air.
- Outliers: `zJNmUWZXj2M` -25.0 LUFS (Short), `XvvXDEtMfhw` -20.7, `oMtAHGv-DU4` -19.6; true peaks near full scale in `WH4g1ptJ-70` (-0.4 dBTP) and `U4cONnQxgvo` (-0.2 dBTP). Cause unknown; I did not listen.
- Meaning: what a measurement shows about the mix; it says nothing about voice quality, music choice or sync.

## What genuinely blocks the rest

1. **Listening**: a human or approved audio-capable tool. Everything else about audio is partial until then.
2. **More visual perception** (viewing the 719 keyframes and 2,160 events of the measured ledgers to fill interpretation columns, DEEP_VISUAL tier): feasible, not free; needs a decision on scope and an independent second reviewer.
3. **Independent review**: none exists for any layer.
