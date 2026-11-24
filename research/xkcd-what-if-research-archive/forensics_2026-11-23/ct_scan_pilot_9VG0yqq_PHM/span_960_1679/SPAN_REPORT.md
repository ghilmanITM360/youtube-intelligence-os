# Span check: frames 960-1679 (40.0 s to 70.0 s) of 9VG0yqq_PHM, all 720 frames

Status: **self-review, one coder.** Question: do the frames the detector calls holds hide changes?

## Method
- **Viewed:** all 720 frames, 48 per sheet (8x6, 192x108), 15 sheets `sheet_01-15.jpg`, sheet k starts at frame 960+48(k-1), row-major.
- **Measured at full resolution:** every frame differenced against the previous one at the source resolution (`fullres_changes.csv`: pixels changed by more than 2, 8 and 24 grey levels, bounding box, machine state) (`scripts/ct_span.py`). The ledger detector works at 256x144 with area averaging, so it can smear small changes; this check does not.
- **Zoom on residuals:** previous frame, frame and the difference amplified 8 times for the 8 largest residuals (`diff/diff_*.jpg`, `scripts/ct_span_diff.py`).

## Result
- **Nothing visible was missed.** Every change I could see across the 720 frames is one the ledger already lists: object and label pop-ons, typed "600 C" (frames 1035 to 1040), the glow fade on the toaster, label pop-ons on the axis (room temperature, fridge, freezer), the typed bracket text (about frames 1270 to 1275), the cut at 1367, the speech bubble at 1412, the cut at 1518, plug and outlet pop-ons, the door closing at 1618, the red glow fade from 1663. No ledger row needed correcting in this span.
- **At full resolution, 480 of 720 frames (67%) have no change above 2 grey levels; the longest such run is 75 frames (3.1 s, frames 1110 to 1184).** Of the 685 frames labelled HOLD, 205 change by more than 2 grey levels somewhere, 184 by more than 8, **54 (in 18 runs) by at least 15 pixels** (the largest residual 225 pixels of 921,600).
- **These residuals are codec settling, not animation.** All 54 sit 1 to 8 frames from a machine-detected event, except one at 21 frames; the amplified difference images show scattered speckle, not a drawn stroke; there are no I-frames among them (29 B, 25 P frames). A single-pixel flicker at a fixed spot (right of centre, near 72% across and 72% down) repeats every third frame during holds in the toaster scene: also an encoder pattern.
- **The steam and smoke do not wobble.** In the smoke scene (frames 1420 to 1500) 6 of 81 frames change at all, by at most 1 pixel. I thought I saw the steam and smoke lines vary between frames on the 192x108 sheets; the pixel data show they do not, so that impression was wrong and is not recorded as a finding.

## Limits
- 192x108 per frame is too small for fine marks; the full-resolution numbers carry the proof for holds.
- One span (30 s of 162 s, the middle), one video, one coder.
- A change smaller than 15 pixels at full resolution would not appear as a drawn change in these checks.
