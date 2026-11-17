> SUPERSEDED — NOT CANONICAL
>
> This file is retained only for project provenance.
> Use `03_reconstruction_system/IMAGE_TO_VIDEO_SYSTEM.md` for current production guidance.

# Image-to-Video Reconstruction Guide

## Overview
Using Image-to-Video (I2V) synthesis to generate animated sequences from static visual states,
guided by measured synchronization and semantic audio data.

## Core Principles

### 1. When to Use I2V

Optimal scenarios:
- **State progression:** Evolving visual (object growing, state changing)
- **Illustration reveal:** Hidden elements becoming visible
- **Spatial relationships:** Objects moving relative to each other
- **Emphasis:** Region brightening or focusing

Not recommended:
- Simple static states (no animation needed)
- Rapid transitions (narration too fast for 1–2s generation)
- Complex interactions requiring precise timing

### 2. Prompt Engineering for I2V

Structure:
```
[START_STATE]: Visual description of initial frame
[END_STATE]: Visual description of final frame
[NARRATION]: Corresponding spoken text
[DURATION]: 0.8–2.0 seconds
```

Example:
```
[START_STATE]: Earth in space, small blue sphere
[END_STATE]: Earth 2x larger, showing cloud formation
[NARRATION]: "If Earth grew 1 centimeter every second..."
[DURATION]: 1.2 seconds
```

Keys to effective prompts:
- Be specific about visual change (growth, movement, appearance)
- Reference narration content
- Specify desired motion path
- Mention objects, colors, textures precisely

### 3. Motion Characteristics

Natural motion:
- **Growth/scale change:** Smooth, uniform scaling from center
- **Object movement:** Linear or arc paths matching physics
- **Reveal:** Fade-in or slide revealing hidden elements
- **Rotation:** Smooth rotation around logical axis

Avoid:
- Jerky or uneven motion
- Motion that contradicts narration
- Overly complex multi-object interactions

### 4. Timing Constraints

Source anchor:
- I2V duration must match narration segment duration
- Start frame must align to state onset (word start)
- End frame must align to state end (word end or sentence boundary)

Examples:
- 3-word sentence (750ms narration): I2V duration 0.8s (hold 0.2s after narration ends)
- 5-word sentence (1250ms narration): I2V duration 1.3s
- 8-word sentence (2000ms narration): I2V duration 1.8–2.0s (hard ceiling)

### 5. Color and Lighting Consistency

Match source videos:
- Color palette from original video
- Lighting direction consistent with base state
- No sudden color shifts (use fade transition instead)

Semantic colors:
- Objects: Neutral (gray, blue, brown)
- Emphasis: Accent color (orange, red, yellow)
- Scales/rulers: Bright accent over gradient background

### 6. Resolution and Aspect Ratio

Standard output:
- 1920×1080 (1080p) or 3840×2160 (4K)
- 16:9 aspect ratio (matching source videos)
- 24–30 fps (standard video framerate)

Generated sequence constraints:
- Must match source video resolution
- Framerate interpolation if needed (I2V may generate at different fps)
- Export with lossless or high-quality compression

## Reconstruction Workflow

1. **Identify state sequence:** From AUDIO_VISUAL_SYNC.csv, find consecutive image changes
2. **Extract reference frames:** Get base state images from source or existing forensics
3. **Write I2V prompt:** Describe start state, end state, narration context
4. **Generate:** Run I2V model with timing constraints
5. **Quality check:** Verify motion smoothness and alignment
6. **Integrate:** Splice into timeline at correct temporal position
7. **Sync verification:** Check audio alignment to motion
8. **Export:** Render to video format matching source specs

## Decision Tree

```
Is this a visual state change?
├─ Pure cut/replace: Use image splice, no I2V
└─ Animated progression: Use I2V

Is the narration segment < 0.5s?
├─ YES: Use static image, no I2V (too short for generation)
└─ NO: I2V generation possible

Does the visual show motion/growth/reveal?
├─ YES: I2V appropriate; write motion-oriented prompt
└─ NO: Static state; use image + fade transition

Does the motion span multiple sentences?
├─ YES: Split into multiple I2V sequences (each 1–2s max)
└─ NO: Single I2V sequence matching sentence duration

```

## Prompt Guidelines

### Scale/Growth Sequences
```
START: Object at normal scale (diameter D)
END: Object at 2× scale (diameter 2D)
NARRATION: "...grows exponentially each second..."
MOTION: Smooth uniform scaling, centered
DURATION: 1.5s
```

### Reveal Sequences
```
START: Area obscured/hidden
END: Full object revealed/visible
NARRATION: "...suddenly appeared..."
MOTION: Fade-in or slide revealing from edge
DURATION: 0.8s
```

### Rotation/Perspective Sequences
```
START: Object viewed from angle A
END: Object rotated to show angle B
NARRATION: "...and this side shows..."
MOTION: Smooth rotation around vertical axis
DURATION: 1.2s
```

### Multi-object Movement
```
START: Objects at distance D apart
END: Objects closer (distance D/2)
NARRATION: "...as they approach..."
MOTION: Linear convergence toward center
DURATION: 1.5s
```

## Quality Criteria

Generated sequence should satisfy:
- [ ] Motion smooth without artifacts or popping
- [ ] Motion direction matches narrative intent
- [ ] Start and end frames visually match context
- [ ] Duration matches narration segment length ±100ms
- [ ] No visible color shifts mid-motion
- [ ] Objects remain visually coherent (no morphing)
- [ ] Motion speed perceptually matches narration speed

## Integration Checklist

- [ ] Generated sequence matches source resolution
- [ ] Framerate matches or interpolates correctly
- [ ] Audio remains unmodified
- [ ] Temporal alignment verified to word-level precision
- [ ] Transition into/out of sequence (fade 0.1–0.2s)
- [ ] No gaps or double-rendering at sequence boundaries
- [ ] Color/lighting consistent with adjacent frames
- [ ] Export verification (play through; check sync)

## Fallback Strategies

If I2V generation fails or produces poor quality:
1. Use fade transition between static frames (0.3s)
2. Generate simpler motion (single object movement)
3. Reduce prompt complexity (fewer objects/changes)
4. Fall back to manual CapCut animation (scale/rotate keyframes)
5. Use static image with shorter narration segment (re-record if needed)

