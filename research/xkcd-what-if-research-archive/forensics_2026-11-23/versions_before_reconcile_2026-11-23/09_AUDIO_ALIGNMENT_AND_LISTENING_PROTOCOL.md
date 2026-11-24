# 09 Narration and visual alignment: machine result and a listening protocol (continuation, 2026-11-23)

## What this session can and cannot do
No tool in this environment plays audio to a listener, so **no narration, music, effect or sync judgement was made by listening** (by the model or a human). Everything below is machine evidence: ASR timestamps (whisper small.en, provisional, never certified) against measured visual-event times, and measured loudness. The pack for a human listener is prepared; the listening itself is **BLOCKED**.

## Machine alignment (MEASURED, provisional ASR; `09_AV_ALIGNMENT_ALL88.csv`, `scripts/phase9_listening_pack.py`)
All 88 videos with media: 4,439 ASR segments, each compared with the nearest measured visual-event start (campaign ledgers for 44 videos, audit ledgers for the other 44; segment-level whisper timing, not word-level).

| Group (videos) | median per-video median distance to nearest event | segment starts with an event within 0.5 s | within 1 s |
|---|---|---|---|
| Long, campaign ledgers (24) | 0.27 s | 58% | 67% |
| Long, audit ledgers (20) | 0.41 s | 56% | 69% |
| Short, campaign ledgers (20) | 0.39 s | 54% | 69% |
| Short, audit ledgers (24) | 0.34 s | 56% | 69% |

**Chance baseline:** shifting every segment start by 3 to 11 s (or back by 4 to 9 s) gives 33% to 37% within 0.5 s (median over 88 videos), so the observed 56% is about **20 points above chance**. Reading: speech clause starts and visual events are associated, but 4 in 10 clause starts have no event within half a second, and **the direction of influence (voice leads or follows the picture) is not established**. The two ledger sources and the two formats agree within about 4 points.

Machine loudness (`09_AUDIO_LEVELS_88.csv`, ffmpeg loudnorm/silencedetect): median about -16.5 LUFS, 84 of 88 files between -17.5 and -15.5, loudness range about 3 LU, near-zero digital silence. Not music vs voice separation, not a listening result.

## Human listening protocol (to be run by a person)
Pack: `09_LISTENING_REVIEW_PACK.csv`, 4,439 rows (one per ASR segment) with `video_id`, segment start and end, ASR text, nearest event time and signed offset, shot at the segment start, cuts inside the segment, pause before, machine flags (1,547 rows flagged: `NEAREST_EVENT_GT_1S`, `PAUSE_GE_1S`, `MULTI_CUT_SEGMENT`) and blank `listener_verdict` / `listener_notes`.

Suggested order (smallest useful first):
1. Pilot `9VG0yqq_PHM` (all frames already viewed): all segments.
2. Eight high-value physics videos, flagged segments only: `-1-ldW4kpLM`, `fs28lEq9smw`, `e3uk7jU3RHo`, `gp5G1QG6cXc`, `Z_xJ40QXu7Q`, `UQgw50GQu1A`, `0L44GEJ5pLE`, `DiWFXv9N0Vs`.
3. One Short from each family seam (compare Short audio with its long parent): 38 derived Shorts, sample 8.
4. Any remaining flagged segment.
For each row the listener records one of `SYNC_OK`, `VOICE_EARLY`, `VOICE_LATE`, `ASR_WRONG_TIME`, `ASR_WRONG_WORDS`, `NO_VISUAL_CUE`, plus emphasis, humour cue, music or effect presence and where a sound effect lands on a movement (Phase 9 list). Music and sound effects are third-party material: describe placement and function, never copy files.

Until rows carry a human verdict, every timing claim stays "provisional ASR" and the playbook's relation between voice and picture stays UNVERIFIED.

## Addendum 2026-11-23 (third pass)
- **Still no listening.** No audio-review capability exists in this session; every audio statement is machine analysis. Nobody has heard any passage.
- **New machine measurement (not listening):** audio energy above -45 dB begins within 0.5 s in 88 of 88 videos (median 0.06 s, max 0.49 s; `11_LEADING_SILENCE_88.json`). The Whisper segment start of 0.00 s in 88 of 88 is a timing artefact, not evidence of when narration starts. The waveform cannot tell voice from music or effects.
- **Priority list for a human listener:** `09_LISTENING_PRIORITY_ITEMS.csv` lists the physics-critical lines whose verdict could change with one spoken word (petawatt versus terawatt, oil versus soil, 6 versus 10 petawatts, "a few hundred" versus "a thousand" mph, the lightning definition lines). The full 4,439-row pack remains `09_LISTENING_REVIEW_PACK.csv`.
