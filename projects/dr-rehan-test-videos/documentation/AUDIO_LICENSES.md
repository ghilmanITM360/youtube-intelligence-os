# Audio licences: Calf_Pain_PAD_FINAL_v2.mp4

**No third-party music or sound effects are used.** All audio other than the narration was synthesised for this project with `project/tools/make_audio.py` (NumPy + FFmpeg). No samples, loops or downloads went in, and the generator is deterministic (fixed seed 1012).

| Element | Source | Creator | Licence / rights | File | Attribution required |
|---|---|---|---|---|---|
| Narration | `/Users/ghilmankhan/Downloads/1012.mp3` (SHA-256 `b419bad2…be2bce2b`), copied unmodified to `project/public/narration.mp3` | Supplied by the project owner | Owner-supplied; usage rights rest with the owner | `project/public/narration.mp3` | Per owner |
| Music bed "Calf Pain Bed" (84 BPM, F major → D minor → F) | Original synthesis: soft pad, mallet arpeggio, sine bass, synthetic room reverb | Generated in this project (Claude Code for the project owner) | Original work made for this video; no third-party rights | `project/audio/music_bed.wav` | No |
| 10 SFX (accent, shimmer, pop, 2 × whoosh, bubble, tick, boom, thumps, chime) | Original synthesis (sine/noise generators) | Same as above | Same as above | `project/audio/sfx.wav`; cue list in `project/audio/cues.json` | No |
| Final mix | Narration + music (ducked under speech) + SFX | Same as above | Same as above | `project/audio/mix.wav` | No |

## Why there is no library track
- **YouTube Audio Library** (preferred) needs a signed-in YouTube Studio session. **Mixkit** would have meant downloading a third-party file, and that needs your explicit approval of the specific file. Neither was used.
- The brief's fallback was applied instead: "create an original subtle instrumental bed with available local tools". No paid service was used.
- To swap in a licensed track later:
  1. Approve a specific file.
  2. Replace the music generator's output with that file in `make_audio.py`.
  3. Record the track's name, creator, URL, licence and credit in this file.

## Mix facts (measured)
| Measure | Value |
|---|---|
| Music level (alone, before ducking) | −31.7 LUFS, which is **20 LU under the narration** (−11.7 LUFS) |
| Ducking | Up to −5 dB, keyed to the speech envelope (60 ms attack, 450 ms release) |
| Fades | 1.2 s fade-in; cosine fade-out ending with the last frame |

**Narration handling:** sample-identical, with no EQ, compression, pitch or speed change. The only change is one static gain of −1.88 dB on the *whole* mix, to keep peaks below −1.5 dBFS. The source MP3 itself peaks at +0.06 dBFS.
