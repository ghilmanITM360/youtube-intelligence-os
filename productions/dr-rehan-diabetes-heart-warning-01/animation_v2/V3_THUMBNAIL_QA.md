# V3 thumbnail QA
All files are in `thumbnail/` and are 1080×1920 RGB PNGs, built by `thumb.py` from the existing V2/V3 vector-drawn assets (the worried patient, warning-sign icons, and the heart with its coronary overlay). There is no photograph, no doctor portrait and no watermark. The comparison is in `THUMBNAIL_COMPARISON.png` at 540, 180 and 120 px.

| | A: "DIABETES? / DON'T MISS THESE HEART SIGNS" | B: "HEART ATTACK / WARNING SIGNS / with diabetes" |
|---|---|---|
| Focal point | One large worried patient with the 4 symptom icons used in the video | Patient plus a large heart diagram (two competing objects) |
| 120 px read | "DIABETES?" is clearly readable; the second line is just readable | Headline is readable; "with diabetes" is lost |
| Accuracy | Matches the video: several less-obvious signs in people with diabetes. "THIS SIGN" (singular) was changed to "THESE SIGNS" | Accurate, but more generic |
| Safe area | Text sits at y 120–470, x ≤ 900; the bottom 420 px holds only the character's feet | Same |

**Selected: A**, saved as `Dr_Rehan_Heart_Warning_THUMBNAIL_FINAL.png`. It has a single focal point and a stronger hook at small size.
- I removed a red glow from A because its rectangular edge was visible.
- No CTR claim is made.
- It has not yet been checked in the real YouTube upload UI.
