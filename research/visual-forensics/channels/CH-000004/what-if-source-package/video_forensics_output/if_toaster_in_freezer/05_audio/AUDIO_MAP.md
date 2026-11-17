# Audio map

| Timestamp | Audio type | Supported observation | Visual sync | Confidence |
|---|---|---|---|---|
| 00:00.000–162.261 | Source audio | AAC stereo stream exists continuously. Speech/music/SFX categories and exact words were not transcribed with available local tools. | Use extracted AU01 as timing master for every visual event in `TIMELINE.csv`. | High for stream; unknown for content |
| 00:01.000 | Unknown source cue | Timing aligns with question-banner reveal A01. | S01 text introduction | Medium |
| 00:25.250 | Unknown source cue | Timing aligns with bumper cut A08. | S03 title card | Medium |
| 00:42.000 | Unknown source cue | Timing aligns with scale cut A14. | S05 scale | Medium |
| 00:58.000 | Unknown source cue | Timing aligns with burner analogy cut A16. | S06 | Medium |
| 01:15.000 | Unknown source cue | Timing aligns with technical-diagram cut A22. | S08 | Medium |
| 01:45.000 | Unknown source cue | Timing aligns with ice-cream vignette cut A27. | S09 | Medium |
| 02:26.000 | Unknown source cue | Timing aligns with closing-panel cut A35. | S11 | Medium |
| 02:33.000 | Unknown source cue | Timing aligns with end-card cut A38. | S12 | Medium |

Limitation: no local ASR engine was available. Do not fabricate narration words, music track, or SFX names. For exact rebuild, extract AU01 from supplied source and preserve its waveform timing.
