# CapCut Production System

Supersedes `CAPCUT_RECONSTRUCTION_GUIDE.md`. That file's specific numeric
guidance (fade durations of 0.1–0.3s, font sizes in pt, "-500ms to word
onset" text timing, an "0.8x slow-motion exception," per-object color-coding
rules) was checked against the corpus and is **not supported by any
measured column** in `01_master_data/` — no fade transitions were observed
anywhere in the corpus (see below), no font-size or color data exists in any
schema, and the ms-offset text-timing rules matched no actual measured
distribution. Kept below is only what the data actually supports; everything
else from the old guide is dropped rather than carried forward unverified.

## 1. Transitions

- **Measured finding:** every transition instance found across `MASTER_SHOTS.TRANSITION_IN`/`TRANSITION_OUT` (200 shots) is either a hard-cut keyword (146 entries in, 60 out) or a named discrete motion/state-replacement action (50 in, 125 out). **Zero fade, cross-dissolve, wipe, or slide transitions appear anywhere in the corpus.**
- **Rule:** reconstruct with hard cuts as the default. Do not add fades — they would not match the reference material.

## 2. Camera

- 89.8% of states (522/581) report a LOCKED- or STATIC-family camera. Default to a locked camera; only pan/push-in where a specific state's `CAMERA_STATE` says so (all such cases in this corpus are in `worlds-largest-cities-what-if`).

## 3. Motion timing

- Use `03_reconstruction_system/DECISION_RULES.md` §3 (motion duration by `RELATIONSHIP` type) and §4 (motion-to-speech alignment) as the timing source. In summary: `STATE_REPLACEMENT` motions (53% of all 438) are fast (~1.6s avg); trigger motion starts on the nearest spoken word (99.5% of real motion starts land during/adjacent to speech), not on a fixed ms offset before or after narration.

## 4. Audio

- Original narration track must remain unmodified (this is a documentation/reference-fidelity requirement, not derived from a measured column, but is consistent with every per-video `AUDIO_MAP.md` treating the source track as ground truth).
- 15 measured non-speech regions exist across the corpus (8 SILENCE + 7 PAUSE, `MASTER_AUDIO_EVENTS.csv`) — preserve them; do not delete or shorten them.

## What is NOT supported by current data (dropped from the prior guide)

- Font sizes, point values, and text hierarchy — no typography data exists in any schema.
- Color-coding rules — no color data exists in any schema.
- Specific ms-offset text-appearance timing ("-500ms to word onset") — not derived from any measured column.
- Any fade/cross-dissolve duration guidance — the corpus contains no fades at all (see §1); guidance for a transition type that never occurs would be fabricated by definition.
- Slow-motion / speed-modification guidance — no speed-ramp data exists in any schema.
