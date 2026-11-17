# Video 003 `5umJ63d3rzQ` — Production DNA (checkpoint 10)

Basis: tables/integrated/* (reviewer-integrated), tables/dna/motion_ledger.csv, dna_stats.json, timing_resolution.csv. 30 fps CFR, 22,583 frames, 752.85 s.
Labels: [M]=MEASURED (frame tables), [R]=reviewer OBSERVED (A/B/C/D second pass), [I]=INFERRED by analyst, [U]=UNAVAILABLE.
LIMIT: this is a synthesis of existing tables. No new frame-by-frame viewing was done in checkpoint 10. Per-object direction/distance/easing was NOT measured [U]. Audio was NOT listened to.

## 1. Visual DNA
- 409 states merge into 254 composition groups (155 merge_with_prev=True, 7 UNCERTAIN kept separate) [R]. Readable text per state: states_final.csv.
- Mixed vocabulary: authored 2D character/diagram scenes (600 of 695 candidates) plus embedded third-party screenshots/footage/screen captures (95) [R,I]. Third-party material is playback, not authored animation.

## 2. Editing DNA
- Group duration median 2.15 s, mean 2.71 s, p90 4.43 s, max 62.6 s (G0115 f9239-11116: a 5+-state merged run, not one static frame) [M].
- Group starts per minute: 26,27,22,23,16,2,17,20,28,18,20,25,10 (min 5 is the G0115 run) [M]. Roughly 20 new compositions/min.
- State boundaries are hard cuts: 19 states have a measured cut spike at the corrected start (17 at -1 frame, plus S0079 f3283, S0248 f13439) [M]. 9 other offsets are zoom/pan/fade/in-state events, not applied (timing_resolution.csv).
- Candidate change mix: REPLACE_CUT 196, ENTRY_POP_IN 124, EMBEDDED_PLAYBACK 91, POSE/ELEMENT_SWAP 86, TEXT_CHANGE 47, DRAW_ON_REVEAL 38, POINTER/PROGRESS 22, OTHER 87 [R].

## 3. Motion DNA
- Dominant: instant additive pop-ins on a held base (ENTRY_POP_IN) and in-place pose swaps rather than tweened moves [R]. Example: EP0006 f93 red hand-drawn X pops over the bubbles, robot unchanged.
- Draw-on/reveal appears 38 times; zoom, fade-out and scale animations are rarer (CUT_PLUS_SCALE_ANIMATION, HARD_CUT_THEN_ZOOM_OUT, FADE_OUT, REMOVAL_ANIMATION: see ledger OTHER rows).
- 922 ledger rows (695 candidates + 227 of the 256 REAL_MOTION disputes that carry a cut_frame, start frame only). 293 rows fall inside unowned intervals (no owning state).
- Easing, direction vectors, pixel travel: [U], not measured; the ledger says so per row.

## 4-6. Storytelling, script-to-visual mapping, pacing
- Provisional ASR alignment (script_visual_alignment.csv): 147 sentences, median 1 group/sentence, ~20.2 groups/min [I]. Visual change roughly tracks sentence boundaries; one beat = one composition.
- 4 sentences map wholly into unowned intervals; ASR not human-verified. Treat the mapping as provisional.
- Pacing rhythm [I]: tight cuts (2-3 s) for claims, a long held run (G0115, 62.6 s) at the bond-market section, shorter groups at the end (10/min at minute 12).

## 7. Visual quality scorecard (analyst judgement [I], evidence-limited)
| Dimension | Score /5 | Basis |
|---|---|---|
| Cut consistency | 4 | 19 states with clean measured spikes; few ambiguous (timing_resolution.csv) |
| Motion variety | 3 | pop-in/cut dominant, few tweens (dna_stats.json) |
| Information clarity | 3 | readable text present in many states; 'NONE_VISIBLE' in others |
| Evidence confidence | 3 | 652/695 candidate agreements, but no independent re-audit of first-pass 'viewed' labels |
Not scored: audio, narration quality, thumbnail (UNAVAILABLE).

## 8. Original asset reconstruction blueprint
Per-group structural specs: tables/dna/reconstruction_specs_per_group.csv (254 rows): measured frame range, duration, inferred layers, animation order from the ledger, beat offsets in frames, embedded-playback flag.
Rules for an original build: use a new script; replace each beat with an original illustration (prompt slots are placeholders in the CSV); use own licensed captures for any embedded-playback slots; do not copy source characters, captures, narration or the exact sequence. Illustration prompts are slots, not per-scene art descriptions, because the tables do not record visual content beyond readable text [U].

## Audio status
AUDIO_NOT_VERIFIED. No human listening was performed in this session. ASR (SENTENCES.csv) is machine output. Audiovisual certification BLOCKED; CT_SCAN_COMPLETE NOT awarded.
