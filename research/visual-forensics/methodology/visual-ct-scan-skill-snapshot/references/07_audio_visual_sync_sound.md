# 07 — Audio and visual synchronization / sound forensics

## Evidence hierarchy for sound

Human/audible source inspection > raw waveform/spectral attributes for measured levels > verified word-aligned transcript > ASR hypothesis > pure visual inference. ASR never = listening and volume normality never = music/SFX/signoff.

## What to analyze

Speech presence, sentence phrasing, stress (only from source sound), pauses, vocal shifts, music entry/exit, ambience, whooshes/impacts/clicks/chimes, sync to reveals and poses, silences, masking, clipping/loudness changes, sound bridges between shots, repetition of motifs, diegetic/non-diegetic where audible.

## Alignments

- Phrase word/group start/end with source PTS, confidence and human/manual validation if possible.
- Video event PTS start/end, lead/lag versus sound cue, estimated synchronization tolerance.
- If ASR is untimed/spot checked, report `ASR_ONLY_NOT_AUDIO_VERIFIED`, and don't invent 100ms speech word timing.
- Explicitly distinguish intended beat synchronization (inferred) versus directly audible time coincidence (observed).
- Sound absence in provided mute clip ≠ silent original unless verified audio track.

## Levels and metrics

ffmpeg `volumedetect` / `ebur128` can characterize levels, not emotional impact or exact words. Loudness, peaks and intelligibility are different properties. No musical key/BPM/tempo attribution without analysis; no sound origin/provider guesses.

## AV sign-off

`FULL_AV_SIGNOFF_COMPLETE` requires actual human/qualified full-source hearing/listening and visual review with integrity and time coverage, not merely ML transcription and contact sheets. Machine B historical report had no full listening; retain status pending. Escalate user review/listening for material claims and medical/regulated narratives where relevant.
