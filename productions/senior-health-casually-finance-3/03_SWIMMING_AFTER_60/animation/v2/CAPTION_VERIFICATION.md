# Swimming V2: caption verification

**Method.** Teacher-forced Whisper scoring (`tools/caption_score.py`; raw output in `V2_REVIEW/CAPTION_SCORE_RESULTS.txt`). Machine evidence only.

**Audio.** Unchanged (4.8 syl/s).

| Src time | ASR | Shown in V2 | Evidence | Status |
|---|---|---|---|---|
| all | small.en: lower-case, no punctuation, "9" + ".5" split | **Sentence case, punctuation, "9.5"** | base ASR has the same words with punctuation | Formatting only; no word changed |
| 0–5.4 | "Swimming, I'll give it 9.5 out of 10. It's also one of the best exercises for the heart" | Verbatim | base −3.74, small.en −3.46 (best candidates) | Verified |
| 5.9–11.4 | "best exercise for cardiovascular fitness, best exercise for endurance, it uses the whole body" | Verbatim | base −3.40, small.en −4.35 | Verified wording. The **"best exercise" ranking is unsupported**: it is shown only as the speaker's view. |
| 11.9–13.9 | "so without using the joints, you are using the joints." | **Verbatim** | Strongly confirmed: base −4.60 / small.en −5.24 vs "loading/straining/stressing/hurting the joints" ≤ −19.3 | **S5: the self-contradiction is in the speech, not an ASR error.** It is not corrected and not illustrated as fact. Clinical/owner decision required. |
