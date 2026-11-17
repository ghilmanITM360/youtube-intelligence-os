> SUPERSEDED — NOT CANONICAL
>
> This file is retained only for project provenance.
> Use `03_reconstruction_system/CAPCUT_PRODUCTION_SYSTEM.md` for current production guidance.

# CapCut Reconstruction Guide

## Overview
Evidence-based guidelines for reconstructing videos in CapCut based on measured production patterns.

## Core Principles

### 1. Shot Duration and Pacing
- **Fast narration** (< 150ms/word): Use shorter shots (1–2s)
- **Medium narration** (150–250ms/word): Standard shot duration (2–4s)
- **Slow narration** (> 250ms/word): Hold shots longer (3–5s)

Reference:
- Mean word duration: 223.5ms
- Median: 200.0ms
- Range: 10.0–1400.0ms

### 2. Cut Points
Optimal cut placement:
- **Before complex concepts:** 0–100ms before narration begins
- **On key words:** Synchronized to word onset
- **At sentence boundaries:** 0–50ms after final word of previous sentence
- **Avoid:** Mid-word cuts (perceptually jarring)

### 3. Transition Selection
- **Default:** Hard cut (immediate transition)
- **Between related states:** Fade (0.2–0.3s)
- **State to animation:** Fade (0.1–0.2s)
- **Avoid:** Wipe, slide, or other dramatic transitions

### 4. Animation Timing

Duration guidelines:
- **Simple reveal:** 0.3–0.5s
- **Standard animation:** 0.8–1.2s
- **Complex sequence:** 1.5–2.5s
- **Hold after animation:** 0.5–1.0s

Start timing:
- On word onset for emphasis animations
- 0–100ms after word onset for supporting animations
- At sentence boundary for state transitions

### 5. Text Placement and Sizing

Hierarchy:
- **Titles/numbers (0–5s mark):** Large (40–60pt)
- **Main explanation text:** Medium (24–32pt)
- **Details/units:** Small (16–20pt)
- **Scale labels:** 14–18pt

Duration:
- Text appears: -500ms to word onset
- Text holds: Full sentence duration + 200ms
- Text exits: At next state change or sentence end

### 6. Audio Alignment

Critical constraints:
- Original narration track must remain unmodified
- Visual state changes lock to narration timing
- No audio enhancement that shortens/extends clips

Silence handling:
- Maintain natural pauses from original
- Do NOT remove silence regions (they serve cognitive function)
- Use silence for scene transition points

### 7. Color and Semantic Coding

Consistent application:
- Objects discussed: Use consistent color per object
- Measurements/scales: Highlight with accent color
- Emphasis/important concepts: Brighten or isolate
- State transitions: Use fade (not color change) for clarity

### 8. Speed and Slow-Motion

Avoid speed modifications:
- Do NOT speed up or slow down video sections
- Motion pacing already optimized for comprehension
- Narration speed is canonical

Exception:
- Very brief emphasis animations may benefit from slow-motion (0.8x speed, 0.3–0.5s duration)

## Reconstruction Workflow

1. **Import**: Load original MP4 with narration
2. **Segment**: Divide into scenes at major visual boundaries (sentence clusters)
3. **Layout**: Place visual states in sequence following narrative order
4. **Sync**: Align state transitions to narration using word-level timestamps
5. **Animate**: Add entry/exit animations (reveal, fade) following duration guidelines
6. **Text**: Add titles and labels synchronized to narration
7. **Polish**: Apply fade transitions between states; verify audio sync
8. **Export**: Generate MP4 at original resolution and framerate

## Decision Tree

```
Does this visual explain a concept?
├─ YES: Use persistent state + animation on key word
└─ NO: State change on sentence boundary

Is the narration fast (< 150ms/word)?
├─ YES: Short shots (1–2s), frequent cuts
└─ NO: Longer shots (3–5s), fewer cuts

Does the animation show motion/force/change?
├─ YES: Duration 0.8–2.0s, starts on word onset
└─ NO: Duration 0.3–0.5s, starts before narration

Is there silence > 1s in the audio?
├─ YES: Use for scene transition, not for deletion
└─ NO: Maintain continuous visual flow

```

## Common Mistakes to Avoid

- ❌ Cutting or re-timing narration
- ❌ Adding transitions not in original
- ❌ Extending shot duration beyond pacing guidelines
- ❌ Removing silence regions
- ❌ Adding background music (changes original audio)
- ❌ Syncing visuals to word end instead of word onset
- ❌ Over-animating (more animation ≠ better comprehension)

## Verification Checklist

- [ ] All audio synchronized without gaps or overlaps
- [ ] All shot cuts within 100ms of narration word onset
- [ ] All silence regions preserved
- [ ] Animation timing follows duration guidelines
- [ ] Text appears before narration explains it
- [ ] Color coding consistent per object/concept
- [ ] No modifications to narration audio
- [ ] Export matches original resolution

