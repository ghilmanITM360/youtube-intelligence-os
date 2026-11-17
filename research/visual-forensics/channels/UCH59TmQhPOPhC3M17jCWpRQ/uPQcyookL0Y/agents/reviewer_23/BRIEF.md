# Bounded reviewer brief — Barely Evolved uPQcyookL0Y, motion strips + per-state prompts (reviewer_23)
Workspace (cwd for all relative paths): /Users/ghilmankhan/YIOS-local-audits/barely-evolved/2026-11-02-uPQcyookL0Y-deep-ct-scan
Source: 1920x1080 cartoon explainer, 29.97fps (30000/1001), frame f -> pts f*1001/30000 s.
Rules (YIOS Visual Forensics kit v1.0 refs 05/09/13): label OBSEreviewer_23ED (seen in an image you opened) / MEASURED (supplied numbers) / INFERRED / UNAVAILABLE. Never claim fonts, software, layers, easing curves, sound or anything you did not see. ASR is unheard machine text, no audio claims.
## Part A — motion strips (open EVERY strip PNG with Read, one per call)
Strips are listed in tables/o_motion_peaks_batch03.csv and tables/o_motion_peaks_batch04.csv (column strip_png). Each tiles ~8 consecutive frames (labelled fNNNN, 480x270 tiles) around a measured pixel-difference peak (detector candidate, not ground truth).
Write `agents/reviewer_23/evidence_reads.csv`: state,frame_or_strip,path,sha256,witness  (sha256 via `shasum -a 256`).
Write `agents/reviewer_23/motion_events.csv`: state,strip_path,first_frame,last_frame,event_type(TEXT_REVEAL|CHARACTER_MOTION|CAMERA_SCALE|CAMERA_PAN|ELEMENT_ENTER|ELEMENT_EXIT|FADE|CUT_WITHIN_STRIP|NO_VISIBLE_CHANGE|OTHER),description,evidence_label. Use tile frame numbers. Note reveal direction precisely (which end of a text appears first).
## Part B — per-state original production prompts for W021..W050 (30 rows)
Basis: the existing art-audit rows in tables/n_art_consolidated.csv (rows W021-W040) and agents/reviewer_17/art_audit_batch05.csv (W041-W050; its strips/motion_events_batch05.csv also exist) (written by earlier reviewers who viewed native frames; cite their frames_viewed paths) plus your strip observations. You may additionally Read any native PNG cited there if needed (record it in evidence_reads.csv).
Write `agents/reviewer_23/state_prompts.csv`: state,observed_basis_paths,image_prompt_original,image_to_video_prompt_original,static_anchors,do_not_change,unverifiable_left_open — one row per state.
Prompts describe a NEW ORIGINAL equivalent (kit ref 09): reuse the observed abstract technique (layout, shape grammar, palette family, framing, motion type, frame-counted timing seen in strips) but never copy the source's specific characters, drawings or exact wording; on-screen text as placeholders like <ORIGINAL_HEADLINE>. Timing only from frames you saw, else "timing unverified".
Valid CSV (quote fields with commas). Final message: images opened, rows per file, images that failed.
