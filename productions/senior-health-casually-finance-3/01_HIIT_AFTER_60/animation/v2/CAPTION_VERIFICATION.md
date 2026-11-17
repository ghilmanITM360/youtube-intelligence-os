# HIIT V2: caption verification

**Method.** Each disputed span was scored by teacher-forced log-likelihood under two local Whisper models, base and small.en (`tools/caption_score.py`; raw output in `V2_REVIEW/CAPTION_SCORE_RESULTS.txt`).
- This is machine evidence. It is not human listening.
- **Rule:** the captions show the highest-likelihood reading when both models agree. Where they disagree, they show the small.en reading and the word is flagged here.
- No word was replaced only because a medical term would fit better.
- On-screen headlines are labels, not subtitles.

| Src time | ASR (small.en / base) | Shown in V2 | Evidence (log-lik, higher = better) | Status |
|---|---|---|---|---|
| 0.00 | or / or | **…or** | Clip starts mid-sentence. The ellipsis marks the clipped source opening. | Verified |
| 0.18 | high intensity / high-intensity | **high-intensity** | Standard spelling. | Verified |
| 1.67 | seven | **7** | Same number; matches "7 out of 10" at the end. | Formatting only |
| 3.4 | mode of / motor | **mode of exercise** | small.en −1.56 vs −8.22; base tie (−4.23 / −4.23) | Verified (small.en) |
| 11.1 | caught / called | **caught** (kept) | Both models favour "caught": small.en −2.21 vs "got" −5.24; base −3.04 vs "got" −4.91. Elsewhere the speaker says "have got" twice. | **Listening check:** "caught" or "got"; the meaning is the same |
| 14.8 | expert cardiologist | **expert cardiologist** | small.en −0.86 vs "a cardiologist" −7.94 | Wording verified. H4 is an absolute *clinical* claim, so the headline attributes it ("the speaker's advice"). |
| 19.4 | mortality or mobility | **mortality or mobility** (kept) | Both models favour "mobility" over "morbidity": base −4.85 vs −7.75; small.en −3.60 vs −7.38; long context −6.46 vs −10.96. | **UNRESOLVED (H5).** "Morbidity" is the expected medical pair, but the audio scores do not support it, so it is not substituted. A human or clinician must listen. |
| 21.9 | awarded to / avoided in | **avoided in** | base −4.49 vs −9.55; small.en −4.50 vs −5.56. Both free decodes give "avoided". | **Corrected (H6).** The small.en margin is narrow, so a listening confirmation is recommended. |
| 24.4 | But for / For | **But for** | Both free decodes give "but"; near tie on scoring. | Verified |
| 27.3 | form of / formula | **form of exercise** | small.en −8.88 vs −12.25; base prefers "formula". | small.en reading; listening check is low priority |

**Not shown in frames:** amber marks, "?" brackets, claim IDs. All uncertainty stays in this file, in `qa/MEDICAL_CLAIMS.csv` and in `V2_REVIEW/DEFECT_REGISTER_V2.md`.
