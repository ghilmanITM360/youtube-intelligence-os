# All 3,893 frames of 9VG0yqq_PHM viewed (spans 0-959, 960-1679, 1680-3892)

Status: **self-review, one coder.** Follows `span_960_1679/SPAN_REPORT.md` (middle 30 s). Now the whole video has been viewed frame by frame: 83 sheets of 48 frames at 192x108 (`span_0_959/` 20 sheets, `span_960_1679/` 15, `span_1680_3892/` 47), plus a full-resolution difference of every frame against the previous one (`fullres_changes.csv` in each span folder; frame 0 has no predecessor).

## Result
- **Every visible change I could see matched a ledger row**, with these exceptions found by the extra checks:
  1. **Small objects missed by the detector and by the sheets:** a pair of white eyes appears in the dark trees at frames 3236, 3240, 3244, 3248 and 3252 (one new pair every 4 frames, 6 per second, about 200 pixels each). Found from the full-resolution diff, confirmed on a 380 px crop (`span_1680_3892/lowerright_cadence.jpg`). Added to the ledger as X001 to X005. This is the one place the stepped animation (on fours) appears; everywhere else motion is on ones.
  2. **Two descriptions corrected** after viewing native frames 212 and 213, 235 and 236 (`span_0_959/toaster_hops.jpg`): E006 is a toast slice popping out of the toaster and E007 the slice lowering into it. The earlier text "small shelf item appears" was wrong.
- **The 192x108 sheets mislead on motion.** Reading consecutive cells I thought I saw figures, steam and the microphone shifting between frames (steam and smoke in the toaster scenes, the left figures in the fridge scene, figures in the ice-cream factory, the microphone and figures in the podcast scene). The full-resolution numbers say those frames are still: for example the smoke scene has 6 of 81 frames changing at all, by at most 1 pixel; between the figure pose swaps at frames 3100 to 3150 only 3 frames change, by at most 16 pixels. None of these impressions is recorded as an animation.
- **Residuals in HOLD frames (whole video, full resolution):** 1,900 of 3,892 transitions (48.8%) have no change above 2 grey levels. Of 3,606 HOLD frames, 706 (19.6%) have at least 15 pixels changed by more than 8 grey levels; 395 of them (56%) are within 8 frames of a detected event, the other 311 sit in 33 runs, almost all of at most 121 pixels (0.013% of the frame): longest runs frames 2680 to 2764 (85 frames, in the ice-cream scene), 2397, 2479, 2545 (about 38 frames each, in the appliance diagram). Amplified difference images at frames 2704 and 2750 show scattered speckle along line edges, not a drawn stroke: codec noise. The only far-from-event run above 121 pixels is the eyes (about 200 pixels).
- **Nothing else:** no unlisted cut, no unlisted label, no hidden idle animation was found.

## Corrections to earlier statements
- `visual_ct_scan_report.md` said 10.5% of frames were viewed and listed 42 unviewed change-span frames. Now all frames are viewed; the window sheets stay as the close-up evidence.
- The claim that animation inside a change is on ones now has one exception: the eyes (on fours).

## Limits
- 192x108 is too small for marks of a few pixels; the full-resolution diff covers that, but changes below 15 pixels (and below 8 grey levels) were not examined individually.
- One video, one coder, no audio, no second reviewer. Do not generalize the hold share (92.7% at the ledger threshold, 48.8% unchanged at the sensitive threshold) to the channel.
- Machine states (HOLD, EVENT, FAINT) were never changed; the X rows are an overlay.
