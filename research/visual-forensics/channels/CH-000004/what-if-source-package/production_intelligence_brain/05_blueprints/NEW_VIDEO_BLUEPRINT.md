# New Video Blueprint

## Purpose
Template and guidelines for creating a new video following the corpus production patterns.

## Pre-Production Checklist
- [ ] Script finalized (copy to TRANSCRIPT.md)
- [ ] Narration recorded and exported as WAV/MP3
- [ ] Shot list drafted with visual descriptions
- [ ] Target states identified (what visuals needed)
- [ ] Visual assets sourced or flagged for creation

## Audio Processing
- [ ] Import narration to Whisper for transcription
- [ ] Generate word-level timestamps (TRANSCRIPT_WORDS.csv)
- [ ] Extract sentence boundaries (TRANSCRIPT_SENTENCES.csv)
- [ ] Validate timing covers full narration
- [ ] Check for silence regions at end; document non-narration audio

## Visual Planning
- [ ] Create TIMELINE.csv with shot/state structure
- [ ] Define STATE_IDs for each visual change
- [ ] Link MOTION_IDs for animations
- [ ] Identify ASSET_IDs for visual elements
- [ ] Document transitions (hard CUT — the only transition type measured anywhere in this 14-video corpus; see DECISION_RULES.md §7)

## Synchronization
- [ ] Run audio-visual sync to populate AUDIO_VISUAL_SYNC.csv
- [ ] Verify word-to-visual mapping
- [ ] Check STATE_CHANGE offsets fall within 300ms of the anchor word (covers 95.7% of the corpus, n=581 — AUDIO_VISUAL_SYNC_DNA.md)
- [ ] Identify motion start/end points relative to narration

## Editing
- [ ] Build CapCut project following CAPCUT_PRODUCTION_SYSTEM.md
- [ ] Validate shot timing follows pacing rules
- [ ] Sync state transitions to narration boundaries
- [ ] Add animations per motion patterns

## Validation
- [ ] Export final MP4
- [ ] Verify audio matches original
- [ ] Check sync accuracy against the corpus's measured tolerance (STATE_CHANGE offsets: 95.7% within 300ms of the anchor word, not a tighter ±100ms — AUDIO_VISUAL_SYNC_DNA.md)
- [ ] Confirm no narration artifacts from editing

## Reference Data
- Use DNA documents (02_production_dna/) for timing patterns
- Check SHOT_PATTERNS.csv for typical shot durations
- Reference AUDIO_DNA.md for word pacing guidelines
