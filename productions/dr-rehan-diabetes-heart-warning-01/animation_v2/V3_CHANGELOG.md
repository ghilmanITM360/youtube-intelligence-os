# V3 changelog (from V2 `c099ad0`)
V1 and V2 files are unchanged. V3 is built by `v3.py`, a copy of `v2.py` with the edits below. It reuses all V2 art, layers, music and SFX.

**Owner-reported defects (fixed)**
1. The bottom band `V2 PREVIEW · NOT FOR PUBLICATION · AUDIO/CLINICAL APPROVAL PENDING` has been removed from the compositor. It was not moved or covered.
2. The doctor-intro notes `Illustrated presenter — not his likeness` and `Name/credit awaiting owner approval` have been removed.
   - The headline stays as **"Dr. Rehan"**, the name spoken in the audio.
   - "Dr. Rehan Omar" and "Consultant Cardiologist" are **not shown**. No owner-approved credential was found in the repo. These still need owner review.

**Other issues found and fixed (7)**
3. Removed "(simplified)" from the on-screen ACS explanation. It was an internal hedge.
4. The amber `[word?]` captions have been replaced:
   - "angina", "angina-like", "subsets" and "sudden" now follow the owner script (`KEYFRAME_HANDOFF.json` script_words) where ASR misheard ("China", "subsurface", "certain").
   - "acute coronation in their home" now has **no verbatim caption**. The ACS headline is shown as an explanatory label instead.
5. Removed the stray ASR "in" before "angina" (the script reads "significantly angina but angina-like").
6. Captions no longer bridge pauses. V2 held "be evaluated for if" for 2.8 s across the ACS gap.
   - "Dr. Rehan" and "type 2" are no longer split across caption lines.
7. Small labels enlarged for phone viewing:
   - S3 icons: 40 → 50 px
   - S5 example line: 40 → 48 px
   - ACS explanation: 44 → 52 px
   - Takeaway "exertion" line: 52 → 62 px
8. In S3, the "Jaw / arm / back" label was clipped at the right edge. The right-hand icon column moved 60–70 px inward.
9. The S12 cut produced a near-blank frame at 38.6 s because a fade-in started on an empty scene (frame std 2.6). The fade was removed, and the minimum frame std is now 17.2.
10. The ending was trimmed: the export ends at **43.0 s** with a 1.0 s audio fade. This leaves a 4.4 s takeaway hold after the last spoken word at 38.6 s.
    - The takeaway's second line now appears at 40.6 s instead of 41.2 s, so it is on screen for 2.4 s.
    - The source MP3 is unchanged (sha256 `8f9e39ab…daf5` re-verified).

Rebuild: `python3 art.py && python3 audio.py && python3 v3.py timeline && python3 v3.py render && python3 v3.py sheet && python3 thumb.py`
