# V14 final sync QA

**Verdict:** V14 is built on Hamza's recording, and every measurable sync check passes.

It is **not yet verified by a person.** Nobody has watched it in a real-time player or listened to it, because I had no way to do either (see below). Treat it as a review cut until the owner has watched and listened.

## 1. Files

| File | Picture | Audio | Decode errors | Frozen stretches (n 0.0008, ≥ 0.75 s) |
|---|---|---|---|---|
| `SKYDIVER_SLOWDOWN_V14_HUMAN_VOICE.mp4` | 1080×1920, 24 fps, 2641 frames, 110.042 s | AAC 192k, 110.042 s | 0 | 0 |
| `SKYDIVER_SLOWDOWN_V14_CAPTIONS.mp4` | 1080×1920, 2641 frames | same mix | 0 | not run (same picture, captions added) |

- **Mix:** −16.0 LUFS integrated, LRA 3.5 LU, true peak −1.5 dBFS.
- **Stems:**
  - voice −18.5 LUFS
  - wind/ambience −27.0 LUFS
  - every other stem below −42 LUFS

  The voice is the loudest element throughout, and all other stems duck under speech (ambience −7 dB, effects −4.5 dB).
- **Audio and video:** both streams start at 0 and end at 110.042 s. The MP4 audio is 3 ms off the voice stem (one frame is 41.7 ms).
- **First word:** voiced audio starts at 0.402 s. The opening shows the aircraft and the faller from frame 0.
- **Ending:** the last word ends at 108.56 s. Then there is a 1.48 s end card with a slow push and the wind fading to 0. Picture and sound end together.

## 2. Narration

See `HUMAN_VOICE_TRANSCRIPT.md` and `audio/voice_edit.csv`.

| Check | Result |
|---|---|
| Only the new human narration | Yes. The V13 narration is not in V14 (only its timing, as a reference in `history/v13/`). |
| Pre-roll removed | 0–10.14 s removed (setup talk + silence). The first script word in the raw file is at 10.24 s, found by transcription and waveform. |
| No clipped words | Cuts were made only inside digital silence (about −134 dB). All 202 words are present: the word diff against the V13 script shows only the 5 wording differences listed in the transcript. |
| No false starts or repeated takes | None found. One continuous reading. |
| Pauses | 8 pauses over 1.5 s were shortened to 1.5 s (3.56 s of silence removed). All other pauses were kept. |
| Speed or pitch change | None |

## 3. Timing method

- **How the picture is timed:**
  - Hamza's phrases are matched in order to the V13 narration's phrases (difflib on the word sequence).
  - Each phrase onset becomes an anchor, and a monotone cubic map runs from V14 time to V13 design time (`audio/warp.json`).
  - Every frame draws the V13 design at the mapped time.
- **No single speed factor.** Locally the picture runs at 0.26×–1.40× of V13's design speed (median 0.68×), set by Hamza's own phrasing.
- **Two reveals are pinned to words:**
  - The drag bar passes the weight line on "stronger".
  - The push-in on the net force holds through "Think about that".
- **Stretched beats keep moving.** Body bob and roll, air streaks, wisps, flow markers, the density drift and the propeller run on real film time.
  - The slowest stretch (0.26× at about 88 s) is the graph building during the pause after "That's the strange part". The curve keeps drawing and the background keeps moving.
- **Physics:** `tools/model.py` is unchanged. The self-check passes:
  - 2641 frames
  - warp monotone
  - all 25 shots appear
  - model time never runs backwards
  - speed ≥ 0
  - altitude never rises
  - the needle never rises after the crossing
  - lowest altitude shown: 445 m

  Every quantity on screen (altitude, density dots, speed, drag, weight, net force, needle, terrain) still reads one model state per frame. Only the film time at which each state is shown changed.

## 4. Narration to picture (brief's table)

`NARRATION_VISUAL_SYNC_MAP.csv` has 33 rows: the phrase, its key word time, the visual event and its exact V14 frame.

- **All 33 pass.** No event comes more than 0.30 s before its phrase starts, and none comes more than 1.0 s after its key word.
- **Fixed in V14 because they revealed too early:**
  - "starts at rest" (was 1.9 s before "rest")
  - the speed ×2 sweep (started before "the faster you fall")
  - the net-force bar (was on "can actually"; now on "stronger")
- **New beats:**
  - "this is a model" brings in the model graph in the MODEL frame
  - "body position stays fixed" shows "posture: fixed"

## 5. Captions

`SKYDIVER_SLOWDOWN_V14.srt` and the burned-in caption version.

- 47 cues taken from the word timings, with Hamza's actual wording.
- Each cue is 40 characters or less, wrapped to at most 2 lines of about 24 characters.
- **0 overlaps.** Every cue appears 0.05 s before its first word.
- Each cue stays until 0.25 s after its last word, or until the next cue starts if speech is continuous.
- **One fast cue:** "Slowing down doesn't mean" is on screen for 0.66 s. Hamza says it that quickly, and the next cue continues the sentence.
- **Placement:** bottom band (design y 544–584), clear of the character, the wrist instrument and the arrows. Checked in `qa/consecutive_frames_critical.png`.
- **Known overlap:** during the push-in on the bar tops (about 64.9–65.9 s) the caption sits over the lower part of the enlarged bars. The violet net-force excess at the top stays clear.

## 6. Sound

`SOUND_DESIGN_CUE_SHEET.csv` lists the voice, the ambience bed, the aircraft hum and 35 cues.

- **Every cue is placed on the frame of its picture event,** e.g.:
  - wrist ticks on the cuts to the instrument
  - needle ratchets while the needle falls
  - a reveal tone for each diagram reveal
  - whooshes on the tilts and the pull-back
  - a gust for "grow brakes?"
  - a rising swell that stops on the model reset
- **Rights-clear:** every effect is generated in `tools/mix_v14.py`. No library or third-party clips are used.
- **Level:** effects are quiet (peaks −24 to −35 dBFS before the mix gain), there are no repeated tick loops, and there are 4 whooshes in the film.

## 7. Playback verification: not done by a person

- **Claude in Chrome:** reported "not connected" (tried this session).
- **The built-in browser:** cannot open local files or local servers.
- **Uploading to get around this:** I did not upload anything.
- **I cannot hear audio.** No listening review has been done.

What I did instead:

- **Real-time-rate decode:** `ffmpeg -re` decoded both final MP4s at normal playback speed: 0 errors, 109.5 s of wall time for 110.04 s of film (`qa/realtime_decode.log`). This shows the files play in real time. It is not a human viewing.
- **Consecutive frames** (every 2nd frame) at 12 critical moments: `qa/consecutive_frames_critical.png`.
  - first word
  - cut to the closed pack
  - gravity
  - "Wait, what?"
  - airflow
  - model reset
  - denser air
  - "stronger", the push-in on the net force, and "Think about that"
  - net force up
  - speedometer
  - "this is a model"
  - ending

  Each was checked against the caption shown in the same frame.
- **Review stills** across the whole film: `qa/stills_sheet.png`.
- **Isolated rebuild:** see §9.

**Owner action:** watch both MP4s once in QuickTime or Chrome with headphones, checking:
- that the voice sits above the wind
- the effect levels
- "speeds start" vs "speed starts" in the transcript

## 8. Acceptance list

| Item | Status |
|---|---|
| Only the new human narration is used | Pass |
| Material before the script removed | Pass |
| No spoken words clipped | Pass (word diff; cuts only in digital silence). Not listened to. |
| No false starts or duplicate takes | Pass (none in the recording) |
| Animation follows the new narration | Pass (33/33 sync rows) |
| Captions match the spoken words | Pass (ASR, two decodes agree). One ambiguous word pair needs a listen. |
| No awkward gaps, early reveals or late animations | Pass by measurement. Not judged by a person in real time. |
| Scientific model correct | Pass (model unchanged, self-check) |
| Character and instrument continuity | Pass (V13 rig and instrument, same assets) |
| Opening engaging, subjects upper-middle | Kept from V13: aircraft upper-middle, figure below, no cloud wipe |
| Sound effects match the action | Pass by placement (cue sheet). Not listened to. |
| Narration clear throughout | Voice 8.5 LU above the bed before ducking. Not listened to. |
| No unexplained frozen frames | Pass (0 frozen stretches) |
| Video and audio end together | Pass (110.042 s each) |
| Original V13 untouched | Pass (6/6 V13 SHA-256 hashes OK) |
| V14 self-contained | Pass (no path outside `v14/`; isolated rebuild, §9) |

## 9. Isolated rebuild

See `qa/isolated_rebuild.txt`.

A copy of `v14/` was made in a scratch folder, without the outputs. In that copy I reran:
- the narration edit
- the alignment
- the self-check
- the mix

The results were compared byte for byte with `v14/`, and all six were **identical**:
- `HAMZA_VOICEOVER_CLEAN.wav`
- `SKYDIVER_SLOWDOWN_V14.srt`
- `WORD_LEVEL_TIMESTAMPS.json`
- `audio/warp.json`
- `audio/narration_v14.json`
- `audio/V14_mix.wav`

The self-check also passed in the copy. The picture was not re-rendered there (about 6 minutes). It draws only from the same files and code.
