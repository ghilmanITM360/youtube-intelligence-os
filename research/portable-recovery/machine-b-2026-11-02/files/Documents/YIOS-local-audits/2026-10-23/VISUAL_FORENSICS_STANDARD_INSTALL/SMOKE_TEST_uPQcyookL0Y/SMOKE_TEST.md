# Smoke test — `/visual-ct-scan` dry run on pilot `uPQcyookL0Y` (Barely Evolved)

- **Request:** "CT scan uPQcyookL0Y". Routing gives `CT_SCAN` (long-form, so adaptive).
- **Method:** read-only check of archived run evidence. No decoding, no new frames, no ledger edit.

## What the skill contract produced
1. **Source identity:**
   - SHA-256 `1416669f10d7231f8110eb27044986912984dcdbacbd7d9f6440726349a0c69d`. It was re-hashed now and equals ledger 03 and manifest 08.
   - 488.78 s, 14,647 frames, 30000/1001 fps, 1920×1080 H.264, AAC audio present.
2. **Evidence located:**
   - in `MULTI_CHANNEL_VISUAL_FORENSICS/evidence/BarelyEvolved/uPQcyookL0Y/`:
     - 17 × `sheet_1fps_*.jpg`;
     - `scene_scores.txt`;
     - `cuts_0.30.tsv` (72 candidates);
     - 2 cut sheets;
     - ffprobe, frame count, EBU R128, silence;
     - uncertified whisper.cpp ASR.
   - 28/28 derived-file hashes match 08.
   - No dense windows exist for this pilot.
3. **Gates:** see [quality_gate.json](quality_gate.json).

| Gate | Result |
|---|---|
| source_identity | PASS |
| full_temporal_overview | PASS |
| candidate_shots_verified | PARTIAL |
| motion_design_review | PARTIAL |
| creative_design_review | PARTIAL |
| visual_script_mapping | PARTIAL |
| meaningful_state_timing | BLOCKED |
| production_blueprint | BLOCKED |
| audio_human_listening | BLOCKED |
| final_av_signoff | BLOCKED |

4. **Status:** `VISUAL_ANALYSIS_PARTIAL` / `AUDIO_REVIEW_PENDING`, the same before and after. The 1 fps sheets satisfy the overview gate only. The skill did **not** treat the prior pilot as complete.
5. **Next step it named:**
   - the 04 C-2 state detector, then native-frame windows per candidate;
   - frame-accurate `shot_ledger.csv` and `visual_event_ledger.csv`;
   - then per-state reconstruction prompts and human listening.
   - All of this waits for the Finance handoff gate in 09.
6. **No invented metrics:** no retention, CTR or gaze values were produced.

**Verdict:** PASS. Routing, evidence discovery and gate logic behave as specified, and there was no false promotion.
