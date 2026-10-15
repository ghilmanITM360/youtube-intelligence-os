# V2 defect register: three senior-health Shorts

**Sources reviewed.** The V1 MP4s, decoded:
- 2 fps full-length grids
- 6–10 fps windows at the openings and transitions
- the SRTs, the ASR (base + small.en), and teacher-forced re-scoring of disputed words (`CAPTION_SCORE_RESULTS.txt`)

**Audio.** Inspected by measurement only: speech rate, silence dB, F0 and ASR. **No human listening has been done.**

Severity: **C** = critical (wrong medical wording, QA data in frame) · **H** = high · **M** = medium · **L** = low.

| VIDEO_ID | TIME (V1) | DEFECT | EVIDENCE | SEV | PROPOSED_FIX | VALIDATION |
|---|---|---|---|---|---|---|
| HIIT | 21.9–22.7 | Caption "avoided/awarded" (raw ASR guess) shown in amber | V1 frame 22.0; base vs small.en ASR disagree | C | Re-score the audio, show "avoided in" | Both models prefer "avoided in" (base Δ5.1, small.en Δ1.1); V2 22.55 s frame |
| HIIT | 19.4–20.9 | "mortality or mobility" may be "morbidity" | ASR both "mobility" | C | Do not substitute without audio support; keep it, register as unresolved | Both models prefer "mobility" by 3–4.5; human/clinician listening required |
| HIIT | 0–30.6 | Review strip, claim IDs ("! H4 13.4-16.2S…") and amber underline in frame | V1 frames 15.0, 20.25, 23.7 | C | QA marks only in QA files | V2 frames: none (`review_marks_in_frames=false`) |
| HIIT | 0–7.1 | Opening narration fast | 9.3 syl/s (0–1.18), 8.5 (5.82–7.12); clip average 7.2 | H | atempo 0.90/0.93 on those spans only, +0.12 s pause in a silence | ASR words identical, p 0.923→0.926, F0 Δ<1%; **listening pending** |
| HIIT | 0–30.6 | Captions flash: 34 cues, shortest 0.42 s ("It's a wonderful") | V1 SRT | H | Phrase cues, 2 lines, min ≈0.85 s | 20 cues, min 0.86 s, median 1.64 s |
| HIIT | 0–3.2 | Weak hook: tiny bars, static floating runner, no ground | V1 0.0–3.0 grid | H | Frame-0 bar contrast, run cycle on a path, bars build with the words | V2 0–4.5 s 6 fps window |
| HIIT | 7.72 | Heart jumps position/scale at scene rebuild | V1 7.5→8.0 frames | M | Global-timeline layer, no jump | V2 contact 7–9 s |
| HIIT | 13.4–16.2 | Plant overlaps Sam's leg; Nora's hand on the window | V1 15.63 frame | M | Plant removed, window moved | V2 15.6 s |
| HIIT | 1.5–3.2 | Badge attribution overflows the outline; 14 px "illustrative pattern" note | V1 2.5 frame | M | Attribution as a separate readable label | V2 2.6 s |
| HIIT | 21.3–24.3 | Headline "Not one rule for everyone" softens the speaker's "avoid" advice | V1 23.7 | H | "Heart disease? Avoid it" + "the speaker's view" | Message preserved; clinical review still required |
| HIIT | 10.24–11.78 | "caught" vs "got" | ASR | L | Keep "caught" (acoustically preferred); note it | Listening |
| HIIT | 3.4 / 27.3 | "motor exercise" / "formula exercise" (base ASR) | ASR diff | M | small.en reading "mode of" / "form of" | small.en Δ6.7 / Δ3.4 |
