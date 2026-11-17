# Narration-to-Visual Blueprint

## Alignment Model

### Phase 1: Word-Level Sync
For every visual change, identify:
1. **Trigger word:** The word whose onset triggers visual change
2. **Offset:** Milliseconds between word onset and visual onset
3. **Relation:** BEFORE_WORD / ON_WORD / DURING_WORD / AFTER_WORD

Corpus patterns (from AUDIO_VISUAL_SYNC_DNA.md, STATE_CHANGE events, n=581):
- Mean offset: 75.5ms, median 37ms (visual follows word onset slightly, not exactly aligned)
- Range: −300–579ms; 95.7% fall within 300ms (a small negative tail exists for BETWEEN_WORDS-anchored events, where the visual precedes the next word it's anchored to)
- Motion events anchor differently: MOTION_START mean offset is −14.6ms (n=438), MOTION_END is +14.8ms (n=402) — see AUDIO_VISUAL_SYNC_DNA.md for the full per-event-type breakdown before assuming a single global offset rule

### Phase 2: Sentence-Level Context
For each visual state, determine:
1. **Active sentence:** Which sentence(s) explain this visual
2. **Sentence span:** Hold visual for full sentence + transition
3. **Pacing alignment:** Faster sentences → shorter shots, slower sentences → longer holds

Reference PACING_DNA.md for sentence duration patterns.

### Phase 3: Motion Timing
For animations:
1. **Start trigger:** nearest word boundary — 99.5% of real motion starts occur during/adjacent to speech (DECISION_RULES.md §4), not a fixed pre/post delay
2. **Duration:** varies by relationship type, not a single range — STATE_REPLACEMENT averages 1.6s, SEQUENTIAL 3.5s, SIMULTANEOUS_COUPLED/INDEPENDENT ~4.3-4.5s, PERSISTENT_LOOP ~9.4s (DECISION_RULES.md §3); use the specific motion's own DURATION_SEC when reconstructing a known motion
3. **End anchor:** Visual state revealed by motion end
4. **Hold:** no corpus-wide minimum hold duration is measured; do not assume one

### Phase 4: Silence Handling
Pauses and silence regions:
- Do NOT delete silence (serves cognitive function)
- Use silence for scene transitions
- Hold visual state during silence
- Resume new state on next narration word

## Decision Tree

```
Visual change needed?
├─ Is it a cut between states?
│  └─ Place cut on sentence boundary or key word onset
├─ Is it an animation/reveal?
│  └─ Start near the nearest word boundary (DECISION_RULES.md §4); duration by RELATIONSHIP type — STATE_REPLACEMENT ~1.6s, SEQUENTIAL ~3.5s, SIMULTANEOUS ~4.3–4.5s, PERSISTENT_LOOP ~9.4s (DECISION_RULES.md §3) — not a fixed range
└─ Is it a held state?
   └─ Hold for full active sentence(s)
```

## Verification
- [ ] Every visual sync maps to valid word or sentence
- [ ] STATE_CHANGE offsets within 300ms covers 95.7% of the corpus — flag outliers, don't force them
- [ ] Motion durations match the relationship-type averages in DECISION_RULES.md §3, or the specific motion's own measured duration
- [ ] No visuals during silence >1s (OK to hold state)
- [ ] Transitions are hard cuts — zero fade transitions exist anywhere in this corpus (CAPCUT_PRODUCTION_SYSTEM.md §1); do not add one
