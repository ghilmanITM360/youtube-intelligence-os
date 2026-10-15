# Running V2: caption verification

**Method.** Same as HIIT: teacher-forced Whisper base + small.en scoring (`tools/caption_score.py`; raw output in `V2_REVIEW/CAPTION_SCORE_RESULTS.txt`). Machine evidence only, not human listening.

**Audio.** Unchanged. The speech rate is 5.7 syl/s, so no pacing edit was needed.

| Src time | ASR (small.en / base) | Shown in V2 | Evidence (log-lik) | Status |
|---|---|---|---|---|
| 0.98 | "I'll give you 7" / "you a 7" | **I'll give you 7 out of 10.** | small.en −5.39 vs −7.49; base prefers "a 7" (−8.55 vs −9.78) | small.en reading |
| 9.3–10.4 | "the other muscular scuttle system" / "the others musculoskeletal system" | **the other musculoskeletal system.** | small.en −3.46 vs "scuttle" −5.93; base −8.51 vs −15.70. Both free decodes say "musculoskeletal". | **Corrected (R3 wording).** The broad joint claim still needs clinical review. |
| 15.4 | "3 times per week" | **3 times per week** | "three" −11.66 vs "two" −20.23 | Wording verified. R5 frequency claim → clinical review. |
| 17.5 | should / would | **should** | small.en −11.66 vs −13.59; base near tie (would −10.79 vs −11.04) | small.en reading |
| 25.2 | VO2 | **VO₂** | Standard notation; the subscript is drawn with the Arial Unicode fallback | Formatting |
| 27.5–28.1 | "of the other blood" (both) | **of the blood,** | Free decodes of the isolated clip give "of the blood" in **both** models. Forced: base −18.08 vs "other" −20.78; small.en −16.86 vs −21.29. | **Corrected (R7 wording).** The VO₂ / "maximum oxygen extraction" terminology itself → clinical review. |
| 20.5 | have got | **have got** | −15.06 / −16.21 vs "have" −17.31 / −17.30 | Verified |

Uncertainty is kept here and in the register. No amber marks, "?" or claim IDs appear in the frames.
