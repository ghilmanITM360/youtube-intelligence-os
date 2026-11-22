# Take 2 edited master (owner-approved cut, 2026-11-21)
- Source (untouched): audio/take2/v1_rent_take2.wav sha256 3ef0297814e610d64f2ebc30e41bdac1df934edcbe437648c354930081c14b6e (416.88 s)
- Edited: audio/take2_edited/v1_rent_take2_edited_cut124-254.8.wav sha256 9709ad340795a5b285657e31936121dc2e663e4e43f03b692fb634102dfa857c, 286.06 s, PCM s16le 24 kHz mono
- Cut: removed 124.00-254.80 s (S030-S060, 344 words); 20 ms cos^2/sin^2 crossfade inside silence (-74 dB both sides); overlap consumes 20 ms so total offset is 130.82 s (not 130.80).
- Verified (numeric): 0-123.98 s sample-identical to source; edited[t>=124.02] == source[t+130.82] sample-exact over 3,888,960 samples; seam max sample step 9 (no click); loudness -19.5 LUFS vs -19.2 source.
- Seam: "Two more details." ends 123.56; next speech S061 starts 124.32 (0.76 s pause).
- NOT verified: a human listening pass. Claude cannot hear audio; waveform/loudness/sample-identity checks only. Owner must audition 118-132 s.
- Timings: t2e_words.json (780 words), t2e_sentences_timed.tsv (68 sentences). Remap t_new = t - 130.82 for t >= 254.80.
4ba9b175533c3a0d7c90da9e98d5e874da650d93636e6f6ddc2594b47e2ccf66  audio/take2_edited/t2e_words.json
1f422f5258ab1035d0ed816de2344c00f96859d758d7fc7d99ba7fd5b6a8a053  audio/take2_edited/t2e_sentences_timed.tsv
