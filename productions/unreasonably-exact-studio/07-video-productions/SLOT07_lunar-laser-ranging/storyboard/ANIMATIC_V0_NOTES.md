# Animatic V0 and composition boards: what they are and what they showed

Generated 2026-11-26 by `tools/animatic.py` + `tools/boards.py` from the beat map (times are the recording's: phrase edges measured ±0.02 s, word anchors estimated ±0.12 s).

| File | What it is |
|---|---|
| `storyboard/animatic/ANIMATIC_V0_540x960_15fps.mp4` | 540x960, 15 fps, the master recording as audio, geometric placeholders, provisional captions (the spoken words, placed in the provisional band) |
| `storyboard/panels/S01..S10_*.png` | one sheet per scene: per beat three panels (start / development / payoff), annotated with the provisional safe box (yellow), caption band (magenta), motion arrows (green), plus layers, camera, action, model class, assets |
| `storyboard/panels/beats/<id>_<start|dev|payoff>.png` | the same panels at 540x960, unannotated for the caption but with overlays |

Regenerate: `python3 tools/animatic.py boards` and `python3 tools/animatic.py video` (about 1 minute).

## Honest status
- **Placeholders only.** Ellipses for continents, a capsule astronaut, a rectangle dome. They prove timing, placement, reveal order and layout; they say nothing about final art.
- **Not watched by a human.** I rendered and inspected stills (contact sheets of 60+ frames, and full-size crops of B19-B21); I have not played it through. Treat any statement about pacing as UNVERIFIED until someone watches it.
- Compositions follow `tools/storyboard_data.py`; they are *not yet* adjusted to the saved reference photographs (that revision comes with the reference-informed pass).
- The caption band (y 1480-1730) and safe box (y 150-1440) are PROVISIONAL numbers, chosen so key subjects clear a typical bottom UI strip. They are not verified against any platform overlay (G5).

## Things the animatic exposed (decisions or changes)
1. **Stopwatch and pulse are slowed together** (factor about 1.8x over B06-B07, 1.2-1.3x at B10/B11). Recorded in `SCIENTIFIC_VISUAL_DESIGN.md` and the MG_001 / OPT_001 rows. The earlier "real time" wording was wrong for this narration.
2. **B20 is the hardest 2.2 s.** Three rays at once read as a tangle. The V0 plays the rays one after another (about 0.6 s each), earlier rays dimmed, and the footprint inset enters at 45.55 s ("tiny fraction"). Still to verify by a human at the animatic: fallback is moving the inset to B21.
3. **Formula fold (B34-B35):** the out-and-back path is 2d, which cannot fit in a vertical frame next to the real path. V0 uses a separate horizontal bar that folds in half at the midpoint, then B36 fills the ruler along the real path. The visual link between the folded bar and the path is not solved: needs a design pass (idea: the bar rides the path up and the return leg down, then the second half rotates over the first).
4. **Earth limb enters the caption band.** Allowed (background, not a key subject); everything else is above y 1440.
5. **Orbit scene needs real numbers only at the ends**: the ruler readout uses rounded 357,000-407,000 km mapped to 2.38-2.71 s (C03/C04). The 384,400 km figure at B36 is labelled "mean distance" and is sourced (C03).
6. No new assets were required by the animatic: ghost mirror, brackets, crossed ring and question mark are already in MG_005/MG_007 and OPT_004; the fold bar is MG_003.
