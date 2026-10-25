# Reconstruction Checklist

Use this checklist when building or validating a video reconstruction.

## Data Preparation
- [ ] TRANSCRIPT_WORDS.csv complete with timestamps
- [ ] TRANSCRIPT_SENTENCES.csv with valid word references
- [ ] TIMELINE.csv created with shots, states, motions, assets
- [ ] AUDIO_VISUAL_SYNC.csv populated with visual event mappings
- [ ] All MOTION_IDs and ASSET_IDs resolve to valid entries

## Audio Validation
- [ ] Narration audio imported unmodified
- [ ] Word timestamps within source duration
- [ ] Sentence boundaries correctly linked
- [ ] Silence regions preserved (not deleted)
- [ ] No audio artifacts or pops

## Visual Alignment
- [ ] All visual states correspond to MASTER_STATES entries
- [ ] STATE_CHANGE visual onsets land near an active spoken word (mean offset 75.5ms, median 37ms, 95.7% within 300ms of the anchor word — AUDIO_VISUAL_SYNC_DNA.md); this is a word-boundary alignment, not a sentence-boundary one, and ±100ms is tighter than the corpus actually measures
- [ ] State transitions linked to narration timing
- [ ] Animation start points on the nearest word boundary (99.5% of real motion starts land during/adjacent to speech — see DECISION_RULES.md §4)
- [ ] Animation durations match the specific motion's relationship type (STATE_REPLACEMENT ~1.6s, SEQUENTIAL ~3.5s, SIMULTANEOUS ~4.3-4.5s, PERSISTENT_LOOP ~9.4s — DECISION_RULES.md §3), not a fixed range

## Editing Quality
- [ ] Text readable at video resolution
- [ ] Element scaling uniform (no jarring size changes)
- [ ] Transitions smooth (no abrupt changes)
- [ ] Animations follow motion patterns (smooth, not jerky)

## CapCut-Specific
- [ ] Narration track is original (uncut, unmodified)
- [ ] All visual layers in timeline
- [ ] Keyframe timing matches audio cues
- [ ] Hard cuts only — zero fade transitions exist anywhere in this corpus (CAPCUT_PRODUCTION_SYSTEM.md §1)
- [ ] No corpus-measured lead time exists for text appearance; do not assume a fixed ms lead
- [ ] No background music or narration enhancement

## Image-to-Video Sequences (if used)
- [ ] I2V prompts describe start and end states
- [ ] Motion aligns to narration segment duration
- [ ] Generated sequence matches source resolution
- [ ] Color/lighting consistent with adjacent frames
- [ ] No visible artifacts or morphing errors

## Final Export
- [ ] Resolution and aspect ratio match the specific source video — the corpus is mixed (8/14 portrait 9:16, 6/14 landscape 16:9; see IMAGE_TO_VIDEO_SYSTEM.md §1), not uniformly 1920×1080
- [ ] Framerate 24-30fps consistent
- [ ] Audio bitrate 128-192kbps minimum
- [ ] Video bitrate matches quality requirements
- [ ] Metadata (title, description) populated

## Reference Data
- DNA documents: 02_production_dna/
- Pattern tables: 04_patterns/
- Reconstruction guides: 03_reconstruction_system/
- Master data: 01_master_data/
