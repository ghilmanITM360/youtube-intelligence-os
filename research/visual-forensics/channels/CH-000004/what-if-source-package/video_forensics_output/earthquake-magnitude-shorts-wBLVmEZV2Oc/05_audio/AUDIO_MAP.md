# AUDIO MAP

## LIMITATION (read first)
This environment has no speech-to-text/ASR tool and no ability to listen to audio. The AAC stereo track's existence, format, and duration are OBSERVED (see SOURCE_MANIFEST.md). Its actual content — narration wording, music, sound effects — is UNKNOWN beyond what can be inferred from on-screen text and the genre.

## NARRATION — INFERRED ONLY
- LIKELY: a single voice-over narrator reads/paraphrases the on-screen title and caption text (T01/T02) roughly in sync with each state's IN time — this is the standard convention for this "infographic explainer Short" genre and matches the joke structure (e.g., the newspaper/phone/LIVE-box gag at F01.3-4 only lands if narrated as a punchline).
- UNKNOWN: exact wording of narration, whether it matches on-screen text verbatim or paraphrases it, voice characteristics (gender, tone, pacing).

## MUSIC — UNKNOWN
- POSSIBLE: a background music bed, common in this content genre, but not verified. No separated stems were available to confirm.

## SFX — UNKNOWN
- POSSIBLE: short whoosh/stinger sounds at the 11 hard-cut transitions (A03, A05, A13, A15, A18, A21, A22, etc. — see MOTION_EVENTS.csv), and a "record-scratch" or alarm-style sting at F01.9's red-scribble build-up (16.0-17.5s) before the Magnitude 9 reveal. This is a common genre convention but UNVERIFIED here.

## SYNC POINTS THAT CAN BE STATED WITH CONFIDENCE (visual-only)
Every visual state transition in TIMELINE.csv has a precise IN timestamp; whatever the narration/SFX turns out to be, it should be cut to align with those timestamps — that alignment is the reliable, reusable part of this map regardless of the audio's actual content.

## RECOMMENDATION FOR RECONSTRUCTION (both WAY 1 and WAY 2)
Since original narration cannot be extracted or verified, write new narration lines that match each on-screen text beat (see TIMELINE.csv LITERAL_FRAME_DESCRIPTION column for exact on-screen wording) and time each line's start to that state's IN timestamp.
