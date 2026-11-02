# Visual forensics reviewer brief — video xtqbRt94TTw "To Save the Economy... We are About to Break It" (Casual Finance), FIRST PASS (shards 1-10; ROOT/evidence/<ID>.jpg exists for every candidate)

You LOOK at images and WRITE one JSON file. You change nothing else.
ROOT = /Users/ghilmankhan/YIOS-local-audits/2026-11-01--xtqbRt94TTw-deep-ct-scan
Shard folder: ROOT/agents/shard_N (N in your prompt). Write ONLY ROOT/agents/shard_N/OUT_shard_N.json (plus optional crops in ROOT/agents/shard_N/crops/). Do NOT modify the source MP4, any other file, the Git repo, other shards. No installs, no network. Use python3 -I only for JSON building; Read tool to view images.

## Video
827.58 s video stream, 19,862 frames, 1920x1080, 24 fps CFR (frame i has PTS (i+1)/24 s; first PTS 0.0417). Same channel family as prior videos but DO NOT assume style: describe what you actually see (canvas, characters, props, screenshots, charts). Everything given to you is AUTOMATED discovery: nothing is verified until you look.

## Your inputs (in your shard folder)
- candidates.csv: candidate episodes (id EPxxxx or SUBxxx, tier, machine cls, start/end frame, n frames, net_changed_frac, diff_bbox x;y;w;h, kind STATE_BOUNDARY | STATE_TRANSITION_MOTION | INTRA_STATE_MOTION | MICRO_EVENT, has_I (I-frame => possible codec artifact), evidence path relative to ROOT).
- ROOT/evidence/<ID>.jpg: for each candidate PRE and STABLE frames at 960x540, native-resolution crop of the changed bbox, a net-diff overlay, and for multi-frame candidates 4 mid-frame tiles. VIEW EVERY ONE.
- states.csv: machine DRAFT states (id, start,end,entry,exit,micro_events,motion_intervals, rep_image = ROOT-relative 960x540 stable frame). VIEW every rep_image.
- disputes.csv: scene-detection cuts (SDxxx) that do NOT coincide with a draft state boundary; ROOT/disputes/<id>.jpg shows 3 tiles (frame cut-2, cut, cut+2) at 480x270. VIEW every one and decide.
- Native extraction for tiny text (max 30 crops per shard): ffmpeg -v error -ss <(frame+1)/24> -i "/Users/ghilmankhan/Downloads/videos in mp3/CasuallyFinance/To Save the Economy... We’re About to Break It - Casual Finance (1080p, h264).mp4" -frames:v 1 -vf "crop=w:h:x:y" crops/<name>.png, then Read it.

## OUT_shard_N.json = {"shard":N,"candidates":[...],"states":[...],"disputes":[...]} — one object for EVERY row in your csvs, same order, ids exact.

### candidate object
{"id":"EP0123","verdict":"CONFIRMED|RECLASSIFIED|CODEC_ARTIFACT|UNVERIFIED|NOT_A_CHANGE",
 "type": FULL_REPLACE|PARTIAL_REPLACE|ADDITIVE_ENTRY|ELEMENT_EXIT|ELEMENT_SWAP|POSE_SWAP|EXPRESSION_CHANGE|TEXT_CHANGE|HIGHLIGHT_ADD|NUMBER_OR_LABEL_CHANGE|ZOOM_OR_SCALE|PAN_OR_SCROLL|CHARACTER_ANIMATION|OBJECT_MOTION|DRAW_ON_OR_REVEAL|WIPE_OR_FADE|PROGRESS_BAR_OR_COUNTER|CODEC_ARTIFACT|OTHER,
 "state_boundary":"YES|NO" (YES = the dominant on-screen composition/subject is replaced so a new visual state starts here; additive highlights, small text edits, cursor/blinks are NO),
 "desc":"<=35 words: what visibly changes, WHERE (left/centre/right, top/bottom) and WHAT objects. Specific.",
 "shot_boundary":"YES|NO|AMBIGUOUS" (INFERRED: whole scene replaced by an unrelated composition),
 "motion":null for 1-2 frame events; for n>=3 {"path":"...","easing":"linear|ease-in|ease-out|ease-in-out|stepped|overshoot|UNKNOWN","duration_note":"..."},
 "confidence":"HIGH|MEDIUM|LOW"}
CONFIRMED = real change of the measured class; RECLASSIFIED = real change, machine class wrong (type = truth, say so); CODEC_ARTIFACT = no content change, diffuse noise (esp. I-frames); NOT_A_CHANGE = sub-threshold noise with no visible content change; UNVERIFIED = cannot tell. Never CONFIRM what you cannot see. For micro events name the tiny element.

### dispute object
{"id":"SD001","verdict":"REAL_STATE_CHANGE|REAL_MOTION|WITHIN_STATE_CHANGE|NO_VISIBLE_CHANGE|UNVERIFIED","desc":"<=25 words what the cut tile shows changing","matches_candidate":"EPxxxx or SUBxxx or null (the candidate whose frames contain this cut frame, if you can tell from candidates.csv start/end)","confidence":"HIGH|MEDIUM|LOW"}

### state object (all fields required, plain strings)
{"id":"S0123","objects":"every visible object/figure/text block with approx position (x,y fractions of width/height) and scale","background":"canvas colour or cut-in screenshot","illustration":"line/fill style, character face/pose/expression (describe; no competitor names)","typography":"style class, relative size (% frame height), colour, alignment; 'none'","readable_text":"verbatim text ACTUALLY readable (quoted) else ''","unreadable_text":"text present but not confidently readable (kind) else ''","hierarchy":"focal order and why","camera_motion":"STATIC 2D|PAN|ZOOM|SCROLL.. as observed from episodes in/around the state","entry_exit":"how it begins/ends citing candidate ids","story_function":"INFERRED role","evidence":"OBSERVED vs INFERRED parts","confidence":"HIGH|MEDIUM|LOW","continuity":"which earlier/later states reuse assets/layout","recon":"ORIGINAL production instructions (2-4 sentences, NEW original assets: layers, placement, scale, timing, entry)","prompt":"ONE self-contained original image-gen prompt (30-70 words): flat hand-drawn whiteboard style with this state's specific objects/positions/colours; NO brand/person names, logos or quoted source text","family":"F1 character-only|F2 character+prop|F3 object/icon cluster|F4 full-bleed screenshot/document|F5 screenshot+character|F6 chart/graph|F7 text card|F8 dark-UI capture|F9 full-bleed drawn scene|F10 title/end card|F11 other composite|F12:<label>"}
If the state is short (1-3 frames) say it is an animation/flicker frame and what it shows. If one draft state visibly contains two different compositions (a missed boundary) say so in 'evidence' beginning with "SPLIT_NEEDED:" and give the approximate frame/time if known; if two adjacent draft states are really the same composition, begin 'evidence' with "MERGE_WITH_PREV:".

## Standards
Truth labels: describe only what you see; unreadable text goes in unreadable_text; never infer numbers. Be unique per state (name what differs from neighbours). Look at every image; accuracy first. Write the JSON in chunks via partial files if needed; valid JSON mandatory; verify counts equal csv rows. Reply with ONLY: shard number; counts candidates/states/disputes; counts of CODEC_ARTIFACT/RECLASSIFIED/UNVERIFIED/NOT_A_CHANGE; counts SPLIT_NEEDED/MERGE_WITH_PREV; structural problems. Do not paste the JSON.


