# Audio edit record v2 (S090 trim, owner-approved 2026-11-21)
Chain: original `audio/take2/v1_rent_take2.wav` (sha 3ef0297814e610d64f2ebc30e41bdac1df934edcbe437648c354930081c14b6e, 416.88 s, untouched) -> edited master v1 `audio/take2_edited/v1_rent_take2_edited_cut124-254.8.wav` (sha 9709ad340795a5b285657e31936121dc2e663e4e43f03b692fb634102dfa857c, 286.06 s, untouched, owner-approved cut 124.00-254.80 s) -> **master v2** `audio/take2_edited_v2/v1_rent_take2_edited_v2_s090trim.wav` (sha 0521dd42caadbcf70afc5bc4c8dc46aee3850f1cd72ef0f4e7e21e4f86b63e75, 282.74 s, PCM s16le 24 kHz mono). v2 is a byte copy of `candidates/CANDIDATE_S090_trim_cut250.95-254.25.wav`.

## The edit
- Removed v1-timeline 250.95-254.25 s: "It matches the market measure today within a fraction of a point," (the claim that is only true for September; see R8_INDEPENDENT_QA_REPORT P1-1). Both cut points sit in measured silence (about 31 dB noise floor vs 60-75 dB speech). 20 ms equal-power style crossfade consumes 20 ms, so total removed = 3.32 s (actual file difference 79,680 samples = 3.320 s, measured, not assumed).
- Result sentence (ASR check with whisper large-v3-turbo on the 244-260 s audition clip, all words present and in order): "The official rent number moves in six-month steps, and it cannot tell you the dollar price of renting." No synthesized speech, no new words. "and it" is original speech (energy at v1 254.40-254.6 s).
- Pause between "steps." and "and": about 0.34 s (0.19 s of silence kept before the seam plus 0.15 s after).

## Numeric verification (not a listening test)
- v2 equals v1 sample-for-sample for t < 250.93 s; for v2 t >= 250.95 s, v2[t] = v1[t + 3.32 s] sample-exact to the end of file.
- Seam max sample step 55 in a 31 dB (noise-floor) region, no click signature. Integrated loudness -19.5 LUFS, same as v1.
- Muxed R9 file: decoded audio cross-correlates with v2 at lag 0.0 ms at 10, 100, 200, 251, 270 s. Video 282.7333 s vs audio 282.7307 s (2.6 ms, below one AAC frame).
- Timings: `t2e2_words.json` (768 words), `t2e2_sentences_timed.tsv` (S089 merged with the S090 remainder; S091-S099 shifted -3.32 s; S099 ends 282.23 s). Word times inside "and it cannot tell you" are approximate (+/-0.2 s, ASR timestamps were unreliable there); on-screen pop uses 251.1 s.

## Human checks still PENDING (Claude cannot hear)
1. Seam at 124 s (v1 cut, unchanged in v2): audition `qa_r8/audition/AUDITION_118-132s_edited_seam_at_124s.wav` and `AUDITION_118-132s_video_with_audio.mp4` (R8 video; seam audio is identical in R9).
2. S090 seam: `candidates/AUDITION_S090_candidate_244-260s.wav` (v2 timeline 244-260 s; the join is at about 250.95 s, 7 s into the clip).
Not approved for publication until the owner has listened to both.
