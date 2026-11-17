# Reconstruction blueprint (ORIGINAL production guidance) — uPQcyookL0Y — PARTIAL

Everything below is original-production guidance derived from the observation tiers in visual_ct_scan_report.md; it is not the creator's project spec. Exact software, fonts, easing curves, asset origin and palette values are UNKNOWN (no palette/typography measurement was run; no project files).

## A. Observed edit grammar (counts are from the reviewed candidate tables, sparse/downscaled)
1. Shot-level state changes ~11 per minute (median 4.2 s); fastest chapter #2 Black Death 14.8/min, slowest #4 Agriculture 8.5/min (chapter_pacing_v4.csv). Narration 131-159 words/min; no chapter departs strongly from 130-160.
2. Dominant in-state motion = scale/camera move (46 of 113 bursts) then fade/wipe (23), object entry/exit (20). Hard cuts are the minority of intra-state events; true shot starts are listed in shot_ledger.csv.
3. Recurring white 'card' composition: figures/labels swap in place on a white field (X001, X068, X090, X097 and the bar-chart card around f13168). Counts as one state in this draft.
4. Board/classroom motif: a painting on a classroom board is replaced by a collapse-to-strip then grow-in (X059 f9353-9357; seq125 f12985-12989; seq129 f13100-13108).
5. Transition vocabulary seen: backdrop-only fade to black (X002, X092), fade-in from black (X095, 'and yet' f13993), fade via white with slide-in (X052), white->wood dissolve (X069), water-overlay wipe (X046), globe/zoom morph (X017, X080).
6. Character: same caveman asset reused across the hook (continuity of one head/bone-in-hair design confirmed across f600-f841); mouth/eye swaps are pose swaps (closed<->open mouth f7229/7230, f7298/7299).
7. Label behaviour: text swaps in place (e.g. 'no shoes' -> bold 'no idea' f701-705), labels can slide off with their carrier object (X088 f13347-13352).

## B. Narration-to-visual crosswalk (tables/narration_state_link_provisional.csv; ASR text, not heard)
Per-state ASR words and wpm are provided. Verified anchors only: '5. Ice Age' title card f2602-2663 vs ASR 'Number five, Ice Age' ~86 s; 'Yersinia pestis' card f10244-10326 vs ASR 341.9-344 s; label 'no name/no shoes/no idea' f663-705 (22.1-23.5 s) vs ASR 20.5-26.9 s. All other state<->phrase relations are NOT_ASSESSED.

## C. Original production template (recommendation, not observation)
- Chapter skeleton: hook (analogy of ancestry, ~85 s) -> ranked list countdown with a title card per rank -> each rank: title card, world-scale establishing zoom, 3-5 consequence visuals, one comic character beat, dry-voice summary stat.
- Pacing target to test (hypothesis): 9-15 shot-level states/min, with at least one in-state camera or swap event every 2-4 s; hold ceiling ~10 s except an opening card (the observed 28 s opener is an outlier).
- Build rules: one reusable original character kit (head, torso, limbs, 2 mouth states, 2 eye states); a white-card scene template with slots for 3-6 swapped figures; a 'board painting' template (collapse-to-strip 3-4 frames, grow-in 3-5 frames at 29.97 fps - taken from X059/seq129 timings, tolerance +-2 frames); fade-through-black helper 4-5 frames (X095 f14059-14063).
- Do NOT copy the creator's characters, jokes, script or layout; use only the grammar.

## D. Not yet produced (needs further work)
Per-state image prompts and image-to-video prompts for the 89 states (require a per-state art-direction audit on viewed frames first); design-token table with sampled palettes; typography estimate; audio-cue plan (needs listening); QA frame list at 1080p. Backlog: asr/LISTENING_BACKLOG.md.
