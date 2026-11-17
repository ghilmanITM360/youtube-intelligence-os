# VISUAL 01 — CAPCUT BUILD

Practical assembly. Eight layers, four operations, no effects.

## Project settings

```
Ratio:        9:16 vertical
Canvas:       2160 × 3840
Frame rate:   24 fps  (the 4-frame strike is specified at 24 fps —
              at another rate, keep the DURATION, not the frame count)
Audio:        import the narration first and LOCK it.
              Every operation is placed against a word onset in that waveform,
              never against a clock time
Background:   E01 flat off-white, spanning the WHOLE timeline, not just this
              visual. All five visuals sit on it
```

## Tracks, bottom to top

| Track | Asset | At first frame |
|---|---|---|
| 1 | E01 off-white field | ON |
| 2 | IMG01 base plate (mug + heart) | ON |
| 3 | G02a fork left half | off |
| 4 | T01 text `GOOD?` | off |
| 5 | G02b fork right half | off |
| 6 | T02 text `BAD?` | off |
| 7 | C01 Dr. Rehan | off |
| 8 | G03 red strike (+ wipe mask) | off |

Drop every overlay in at 100% scale, no transform, no position keyframes. The
PNGs are authored at full canvas size, so they land in the right place with no
repositioning. If you find yourself dragging an overlay into place, the file
was exported at the wrong size — fix the file, not the timeline.

## The four operations

| On word onset | Operation | Type |
|---|---|---|
| **"good"** (w3) | Tracks 3 and 4 become visible, same frame | one-frame switch |
| **"bad"** (w7) | Tracks 5 and 6 become visible, same frame | one-frame switch |
| **"Rehan"** (w11) | Track 7 becomes visible | one-frame switch |
| **"wrong"** (w16) | Track 8 becomes visible, and its linear wipe mask animates left → right across **4 frames only**, then holds | 4-frame reveal |

Everything then holds, unchanged, until the cut.

## How to build the one-frame switches

Trim the clip's in-point to the anchor frame. That is the whole technique — the
layer simply starts there. Do not use opacity keyframes, do not use an entrance
animation, do not use "appear" presets. A preset adds a scale or a slide over
several frames and breaks the one-frame rule.

**Track 3 and track 4 must start on the same frame.** Same for 5 and 6. Set one,
then snap the other to it and verify by stepping a single frame back — both
should be absent, then both present. A one-frame stagger between a plate and its
label is visible and reads as an error.

## How to build the 4-frame strike

1. Track 8 starts on the onset frame of **"wrong"**.
2. Apply a **linear mask** to the G03 clip, rotated to match the stroke angle
   (lower-left to upper-right), positioned just off the stroke's left end so the
   stroke is fully hidden.
3. Keyframe the mask position: frame 0 hidden → frame 4 fully past the stroke's
   right end. Four frames. Set the keyframe interpolation to **linear** — the
   default ease makes it slow in and out, which reads as a slide.
4. Nothing after frame 4. The stroke holds, complete, to the cut.

Step through it frame by frame. If it takes more than four frames, it is wrong.

## What does NOT happen in this visual

```
no camera motion       no zoom, pan, push, tilt, parallax or shake
no fades               nothing fades in, nothing fades out
no transitions         the shot ends on a hard butt cut
no element leaves      every element that appears holds to the cut
no colour grade        no filters, no LUTs, no vignette
```

## Nothing is removed here — so nothing needs splitting

In VISUAL 03 and VISUAL 05 a group disappears while Dr. Rehan stays on screen,
which is why those plates must be exported as base + removable group. **Visual
01 has no removal at all.** Every one of its four operations is an addition.
IMG01 stays a single flat plate and no split export is required.

The structural rule still applies to the additions: the fork, the labels, the
doctor and the strike must be their own layers, never baked into IMG01, because
each one is revealed on a different spoken word.

## Cut to Visual 02

```
HARD CUT on the onset of "People" (w18)
```

No transition effect. Butt the two clips together. Track 1 (E01) continues
across the cut unbroken — only the plate and overlays change.
