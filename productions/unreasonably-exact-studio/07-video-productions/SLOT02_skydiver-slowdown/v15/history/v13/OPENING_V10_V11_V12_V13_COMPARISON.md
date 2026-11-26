# Opening comparison: V10, V11, V12, V13

**Contact sheet:** `qa/OPENING_V10_V11_V12_V13.png`. Rows are V10, V11, V12, V13; columns are 0.0, 0.8, 1.6, 2.4, 3.0, 3.6, 4.4 and 5.0 s, taken from each version's MP4.

**Owner screenshots vs V13 at the same moment:** `qa/before_after/V12_vs_V13_0m00s.png`, `_0m01s.png`, `_0m03s.png`.

## Which version did what best (in the first 5 s)

| Quality | Best before V13 | Notes |
|---|---|---|
| Subject placement | **V11** (V10 close) | The aircraft sits upper-middle with the tiny figure just below it, against sky |
| Aircraft framing | **V11** | The aircraft stays in frame, then exits at the top as the camera follows the figure |
| Environmental depth | V12 (real parallax) and V10 (photographic haze) | V12's depth came at the cost of tiny subjects and a ground-heavy frame |
| Readability at phone size | **V11** | |
| Cloud scale | **V11** | The V12 near-cloud wipe filled the whole frame for about 0.5 s (owner's 0:03 screenshot) |
| Closed-pack reveal | V11 (rear pose, ring on the pack) | |
| Text | V12 | V10/V11 carried a brand label, a "10 km above the ground" banner and a "you" tag |

**The V12 regression (owner's screenshots at 0:00, 0:01 and 0:03):**
- The camera was low and far away, with the subjects drawn into a world-scale mesh. The aircraft and figure were about 15–20 px tall at 1080 width.
- Both subjects sat at the lower right, with the aircraft half out of frame at 0:01.
- About 55% of the frame was ground.
- At 2.75–3.3 s a giant foreground cloud and a white bloom covered everything.

## What V13 does

The base is the V11 composition and painted V11 landscape (`CODEX_V11_ART_REPAIR_PACKAGE/environment/landscape_reference.png`), rebuilt as layers.

| Stage | Time | Picture | Camera / parallax |
|---|---|---|---|
| **A Establish** | 0–1.2 s | Aircraft upper-middle (about y 176 of 640, 124 units wide ≈ 370 px). Figure just below (y 262, 50 units wide ≈ 150 px) against clear sky. Horizon at about 2/3 of the height, with a haze band. One brief ring on the figure (0.45–2.1 s), no label. | Slow lateral drift: far layer 8 u/s, near fields 14 u/s, mid clouds 22 u/s |
| **B Follow** | 1.1–2.4 s | The camera tilts down with the falling figure. The aircraft rises and leaves at the top on purpose, at about 2.4 s; it never leaves by the side. | Far layer moves 0.55× the tilt, fields 0.8×, clouds 0.8×, the aircraft about 1.05×, so the depth separates |
| **C Approach** | 2.15–3.3 s | Dolly in on the figure (×4.2). Mid clouds pass beneath it; none crosses in front of it. | Depth-weighted zoom: far ×1.06 per unit, fields ×1.12, clouds ×1.45, subject ×4.2 |
| **D Reveal** | 3.3–5.22 s | Direct cut behind the faller. Bare hands (Codex V13). Slow push in. A dashed ring and "parachute: closed" (3.75–5.2 s). | No cloud wipe |

**Removed from V10/V11:**
- the "UNREASONABLY EXACT" corner label
- the "10 km above the ground" banner (the narration says it)
- the "you" tag

**Removed from V12:**
- the full-frame cloud wipe and white bloom
- the low, far camera
- the ground-heavy framing

## Known limits

- **Style change at the cut (3.3 s).** The rear shot uses the procedural terrain from V11/V12, which is more map-like than the painted opening. V11 had the same cut.
- **Not to scale.** The aircraft and figure are illustrative framing, not true scale. Nothing shows how to jump.
- **The 0:03 "after" frame is the end of the approach.** The figure is large, mid-frame, with the pack visible and no cloud cover.
