# V3 audio QA
- **Source:** `~/Downloads/1015.mp3`, 45.49 s, sha256 `8f9e39ab409959d4e06f99052860cf4391d56a7ab6caa85f560217d35cc3daf5`, re-verified and unchanged.
- **Boundaries:** I measured RMS in 0.25 s windows.
  - Speech energy (-14 to -25 dB) ends at about 38.5 s. ASR places the last word, "mentioned.", ending at 38.59 s.
  - From 38.6 to 45.5 s the level is -30 to -46 dB, which is consistent with room tone or breath. No words appear in the ASR.
- **Edit:** the video export is cut at 43.0 s with `afade=t=out:st=42.0:d=1.0`. No speech or meaningful pause is cut. The full MP3 is kept separately and is never written to.
- **Mix:** reused from V2 (`audio.py`):
  - Original synthesised music sits about 20 dB under speech.
  - 17 soft SFX, the last at 39.6 s, all inside the cut.
  - Whole-mix gain is ×0.89.
- **Encoded:** max -1.0 dB (no clipping), mean -18.3 dB.
- **Not done:** I did not listen to the audio. Speech clarity, music balance, SFX restraint and sync were checked by measurement and timing only. The owner should listen on a phone and on headphones.

## Wording still unconfirmed (owner/clinician)
| Time | ASR heard | Owner script | V3 caption |
|---|---|---|---|
| ~13.2–16.3 s | "in China … in China like" | "angina … angina-like" | "angina … angina-like" (from the script) |
| ~19.4–20.3 s | "subsurface" | "subsets" | "subsets" (from the script) |
| ~33.9–34.9 s | "acute coronation in their home" | "acute chronic syndrome" | **no caption**. Headline label "Acute coronary syndrome (ACS)" (explanatory) |
| ~35.4 s | "certain onset" | "sudden onset" | "sudden" (from the script) |
