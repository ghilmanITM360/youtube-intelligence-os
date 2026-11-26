# V15 audio mix QA

**Owner-reported V14 defect:** the background was too loud and competed with Hamza's narration.

**Owner decision (2026-11-25):** V15 approved as OWNER_APPROVED_FINAL. The rights-clear master `audio/V15_mix.wav` is the publication audio. The library-review mix is not for publication.

**Status at handover:** fixed by measurement. The mix is rebuilt so the voice dominates in every voiced moment. **I could not listen to it.** I have no audio output, so every statement below is a measurement, not a listening judgement. The owner's listening check (see the end of this file) is the remaining acceptance step.

## What changed

| | V14 | V15 |
|---|---|---|
| Wind bed level | −5 dB × envelope | −15 dB × envelope (**−10 dB**) |
| Aircraft engine | −6 dB | −14 dB |
| Wind bed EQ | 70 Hz–5.2 kHz, flat | 90 Hz HPF, 3.5 kHz LPF, −6 dB dip at 2.5 kHz (out of the consonant region) |
| Ducking under speech | ambience −7 dB, effects −4.5 dB, linear 0.18 s ramps | ambience **−12 dB**, effects **−9 dB**, raised-cosine ramps (0.22 s lead-in, 0.38 s release, so word endings are not clipped by a fast return) |
| Speech-band carve | none | every non-voice stem loses a further **−6 dB in 1–4.5 kHz** while Hamza speaks (the HyperFrames "voiceover carve" idea) |
| Voice processing | none | 70 Hz high-pass; 2:1 above −22 dBFS, 15 ms attack, 250 ms release (gentle levelling). No EQ, de-essing, pitch or speed change. |
| Reveal sounds | 11 plucks (almost every arrow) | 5 accents (weight, drag, net force, graph, ending) |
| Stems | VOICEOVER, WIND_AMB, FOLEY, TRANSITIONS, OTHER_SFX | VOICEOVER, AMBIENCE, FOLEY, SCIENCE_FX, TRANSITIONS (+ LIBRARY_REVIEW, review mix only) |

## Measurements (`tools/audio_qa.py`, results in `qa/audio_qa.json`)

**Method.** Every 0.4 s window (50 % overlap) inside Hamza's phrases where the voice is above −40 dBFS (303 windows). Voice stem level minus the summed background stems. Speech band = 300 Hz–4 kHz.

| Metric | V14 | V15 |
|---|---|---|
| Voice − background, broadband, **median** | 10.5 dB | **20.7 dB** |
| Same, 10th percentile | 5.2 dB | **17.1 dB** |
| Same, worst window | −6.8 dB | **+5.8 dB** |
| Voice − background, speech band, **median** | 14.1 dB | **24.8 dB** |
| Same, 10th percentile | 6.5 dB | **19.0 dB** |
| Integrated: voice stem − summed background | 8.6 LU | **15.4 LU** |
| Master integrated loudness | −16.0 LUFS | −16.0 LUFS |
| Master true peak | −1.5 dBFS | −1.5 dBFS |
| Master LRA | 3.5 LU | 3.4 LU |

**Stem loudness (pre-master, V15):**
- voice −24.3 LUFS (LRA 3.6)
- ambience −39.7
- transitions −48.7
- science FX −51.4
- foley −56.9
- library review −61.4

**Weakest speech-band windows: 93.1 s and 76.2 s (about 0 dB).** These sit inside a phrase but in a breath: the voice's speech-band level is −52 / −48 dBFS, and the ambience is just as quiet. No word is under the bed there. The weakest window that actually contains speech energy is +6.3 dB in the speech band at 62.8 s.

**Why −16 LUFS alone proves nothing:** V14 also measured −16 LUFS. Integrated loudness says how loud the whole mix is, not whether the voice wins. The separation numbers above are the evidence that changed.

## Library SFX

The SFX Library's own README says licensing and ownership were not established, so no library clip is in the publication master.

`audio/V15_mix_library_review.wav` and `qa/review/review_library_mix.mp4` add four clips for comparison only. All four are listed in `SFX_LICENCE_MANIFEST.csv`:

| Clip | Use |
|---|---|
| whoosh_air | cut behind the faller |
| wind_gust | air reverses |
| flag | fabric |
| gear_metal | dial |

Each is −30 to −38 dB peak and gets the same ducking and carve as the other effects. The review mix measures −16.0 LUFS, TP −1.5.

## Sync

The MP4 audio cross-correlates with the voice stem at **3 ms** offset, in both the clean and captioned versions (one frame is 41.7 ms). The audio and video streams both run 110.042 s.

## Listening check for the owner (not yet done)

On the review page (`qa/review/`):
1. Headphones, normal volume: every word clear, including "denser", "net force", "decrease".
2. Phone speaker at the **Low volume (20 %)** button: the voice is still understandable.
3. Compare **Clean** with **Library-SFX mix**. If the library version is preferred and its licence can be confirmed, it can become the master by switching `master()` in `tools/mix_v15.py`.
