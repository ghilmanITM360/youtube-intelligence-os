# V13 sound design QA

**Source:** `tools/mix_v13.py`. Cue sheet: `SOUND_DESIGN_CUE_SHEET.csv`. Stems: `audio/stems/`. Mixes:
- `audio/V13_mix.wav`
- `audio/V13_mix_rights_clear.wav`: voiceover plus the synthesised wind and aircraft, no library clips

**I cannot hear audio. No listening review has been done.** Everything below comes from the mix script, envelopes and measurements, which do not verify how it sounds.

## What changed from V12 and why

| Area | V12 | V13 |
|---|---|---|
| **Opening** | The aircraft hum faded out by 3.0 s. A wind gust was used under the cloud-wipe bloom. | The aircraft hum is unchanged (fades by 3.0 s, as the aircraft leaves the top of frame at about 2.4 s). A short whoosh at 1.25 s goes on the tilt that follows the figure. The gust at 2.55 s goes on the approach and carries over the cut behind the faller. There is no wipe any more. |
| **Wind bed** | Dropped by about 6 dB within 0.25–0.4 s whenever the lens, trail or graph appeared. These were ambience changes caused only by a foreground graphic. | It follows the fall. Every change takes at least 0.7 s and is at most about 3 dB. The bed eases down slightly under the bar push-in, the trail and the graph, so the narration and reveal cues stay clear. **The one deliberate drop** is the model reset at 20.9–21.3 s ("starting from rest"). |
| **Airflow** | A gust as the streamlines drew on (17.3 s) | Gust at 17.9 s, when the camera locks on the faller and the air starts streaming up past them. A soft paper tick at 19.35 s as the drag arrow draws on. |
| **Density** | — | One soft tick when the denser box fills (29.2 s) |
| **Forces** | Paper ticks when the ×30 lens opened (41.4 s, 67.1 s) | Ticks when the bars appear (40.35 s), when the drag bar passes the weight line (43.75 s), and on the recap bars (66.2 s) |
| **Character and wrist** | Sleeve rustles at 8.38 s and 54.33 s; ticks on the cuts to the dial at 9.72 s and 55.40 s | Unchanged |
| **Rights-clear mix** | Present | Present: voiceover plus synthesised wind and aircraft only |

The wind is an illustrative soundscape. Its level is not a measurement of speed. During the slowdown it stays high: you are still falling fast.

Narration stays dominant: non-voiceover stems duck to about 45% while a phrase is being spoken (60% for the aircraft hum). The voiceover itself is the unaltered owner recording.

## Measurements (final `SKYDIVER_SLOWDOWN_V13.mp4`)

| Measure | Value |
|---|---|
| Integrated loudness | −16.4 LUFS |
| Loudness range (LRA) | 4.4 LU |
| True peak | −1.1 dBFS |
| Audio | AAC, 192 kbps, 78.2 s |
| Library cue placements | 18, from `SFX Library/` |

## Library licensing

`SFX Library/README.txt` says: "Licensing/ownership was not established by this extraction." **None of the 18 library placements is licence-cleared.** Use `audio/V13_mix_rights_clear.wav` for any version that has to be rights-clean.

## A person still needs to check (on headphones)

1. Wind continuity across every cut, especially:
   - 3.30 s (the cut behind the faller)
   - 16.8 s (into the airflow shot)
   - 20.9 s (the model reset)
   - 47.7 s (the trail)
   - 55.35 s (first person)
2. Whether the paper ticks (19.35, 29.2, 40.35, 43.75, 47.66, 66.2 s) feel restrained, or too frequent.
3. Narration clarity over the 14.3 s and 17.9 s gusts.
4. Whether the sleeve rustles read as clothing.
