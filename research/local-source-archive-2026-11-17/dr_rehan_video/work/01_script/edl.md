# Edit decision list v2 (Version A, 16:9)

In/out points come from **Whisper large-v3 word timings** (`00_intake/doctor_transcript_whisper.json`). Every cut sits at a sentence end; each will get a 2–4 frame audio crossfade, fine-tuned on the waveform in Phase 3. No sentence of his is reordered.

| # | Source | In | Out | Dur (s) | Starts at | Notes |
|---|---|---|---|---|---|---|
| 1 | H01 | — | — | 21 | 0:00.0 | Cold open over graphics only. Riser starts ~5 s in and lands on the I01 cut |
| 2 | I01 | — | — | 15 | 0:21.0 | L-cut: his first frame is revealed under the last 4 s along with the lower third |
| 3 | DR | 0:00.00 | 0:40.20 | 40.2 | 0:36.0 | Out in the breath after 'underlying hypertension' (ends 40.14), before 'However'. Jargon labels |
| 4 | J01 | — | — | 12 | 1:16.2 | Graphics card. Ends on 'there's a catch' → his 'However…' |
| 5 | DR | 0:40.20 | 0:59.64 | 19.44 | 1:28.2 | Out after 'fall down.' Label: orthostatic HYPOtension (he says 'hyper' at 0:51.4). ⚠️ Trim candidate T1 inside |
| 6 | J02 ⚠️ | — | — | 23 | 1:47.6 | Hyper→hypo card. The sitting/standing line can be dropped |
| 7 | DR | 0:59.64 | 1:39.16 | 39.52 | 2:10.6 | Out after 'millimeters of mercury' (99.16), before 'But recently'. Show systolic <150 only |
| 8 | B01 | — | — | 6 | 2:50.2 | Number-line card |
| 9 | DR | 1:39.16 | 1:56.32 | 17.16 | 2:56.2 | Out after 'always be treated' (116.32). 140/90 card |
| 10 | B02 | — | — | 17 | 3:13.3 | Balance-scale card. Opens loop L2 |
| 11 | DR | 1:56.32 | 2:36.20 | 39.88 | 3:30.3 | Out after 'ACE inhibitors or ARB' (156.20). Condition→medicine map, his pairs only |
| 12 | U01 ⚠️ | — | — | 27 | 4:10.2 | Light-3D target chart. Needs doctor approval |
| 13 | DR | 2:36.20 | 3:10.30 | 34.1 | 4:37.2 | 'So to cut the long story short…' → out after 'geriatric cardiologist' (190.30). Three-tick recap |
| 14 | O01 | — | — | 28 | 5:11.3 | Takeaway + disclaimer card. 0.5 s breath with no music before the last line |
| 15 | DR | 3:10.30 | 3:25.20 | 14.9 | 5:39.3 | Subscribe (kept). Ends 0.3 s after 'thank you' (204.92) |
| 16 | END | — | — | 4 | 5:54.2 | End card 'Decode Your Heart with Dr. Rehan' (+ optional O02) |

**Real runtime (draft v1, 2026-11-02): 6:45.0**, built from the real VO lengths by `04_edit/build.py` (scene starts in `04_edit/timeline.json`):
H01 0:00 · I01 0:26.3 · DR1 0:47.9 · J01 1:27.9 · DR2 1:44.6 · J02 2:02.7 · DR3 2:32.7 · B01 3:12.0 · DR4 3:19.6 · B02 3:36.6 · DR5 4:00.8 · U01 4:40.5 · DR6 5:19.7 · O01 5:53.6 · DR7 6:25.4 · END 6:40.5.
Without U01 (if not approved): ≈ 6:05.

## Trims to his recording (candidates, confirmed by ear in Phase 3)
| ID | Source | What | Action |
|---|---|---|---|
| T1 | **0:58.24–0:59.33 (applied in draft v1)** | Stumble: 'and they fall— out… fall down' | Cut set on the waveform (speech dip 58.25, 'fall' resumes 59.35). Keeps 'and they … fall down'. Masked with a cut-zoom to 1.08 |
| T2 | 1:29.6–1:32.4 | Garbled stretch (Whisper confidence ~0) around his first '150 by 90'. The supplied transcript has 'In the earlier clinical trials, the cutoff…' here | ⚠️ Listen first. Trim only if it is a clear repeat or false start; otherwise leave it |

## Not touched
- His audio is never edited for the 'hypertension' / 'hybrid' / '150 by 90' slips. The fixes are on-screen labels and narrator lines (J02, U01).

## VO trims (narrator files)
| File | Cut | Reason |
|---|---|---|
| J02.mp3 | **17.95–19.85 s (applied in draft v1)** | The words "Doctor check" (the ⚠️ marker read aloud). Whisper small: "faint." ends 17.48, "Doctor" 18.56–18.90, "check." 18.90–19.32, "That's" starts 20.08. Not needed if J02 is re-recorded. |
