# Bounded boundary reviewer — Barely Evolved VID (RV)
Workspace (cwd for relative paths): WS
Source: 1920x1080 cartoon explainer, 29.97 fps; frame f -> f*1001/30000 s.
Rules (YIOS Visual Forensics kit v1.0 ref 03/13): detector candidates are NOT ground truth. Shot boundaries != pose changes != camera moves != typographic events. Label only what you see in the tiles; say UNCERTAIN when tiles cannot decide.
## Input
`tables/boundary_candidates.csv`: cand, start, end, detectors (D1 = pixel-change run, D2 = PySceneDetect, D3 = high-contrast pixel change), tiles (frame numbers shown), montage (PNG path). Each montage PNG holds 6 candidate rows; each row = up to 6 tiles (320x180) labelled fNNNN with the candidate id + range printed bottom-left in yellow.
## Task
Open EVERY montage PNG listed in the montage column with the Read tool (one per call). For every candidate row write one line in `agents/RV/boundary_review.csv` with columns:
cand,classification,new_state_first_frame,before_description,after_description,note
classification ∈ HARD_CUT (whole picture replaced between two adjacent tiles) | FADE_OR_DISSOLVE (incl. via black/white) | SLIDE_WIPE_OR_MASK_TRANSITION | CAMERA_MOVE_SAME_SCENE (zoom/pan/push, same scene) | GRAPHIC_OR_TEXT_EVENT_SAME_SCENE (text/label/element appears, swaps or leaves on otherwise same scene) | CHARACTER_MOTION_SAME_SCENE | NO_VISIBLE_CHANGE | UNCERTAIN.
new_state_first_frame = the first tile frame showing the new scene for HARD_CUT/FADE/SLIDE (else blank). Keep descriptions short (<15 words).
Also write `agents/RV/evidence_reads.csv`: montage_path,sha256 (shasum -a 256),witness (one sentence).
Valid CSV, quote fields with commas. Final message: montages opened, rows written, counts per classification, any montage that failed to open.
